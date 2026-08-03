---
name: object-storage-security
description: Secure object storage buckets on S3, Cloudflare R2, GCS, and MinIO against public exposure and credential abuse. Covers public access audit, bucket policy vs ACL vs IAM, presigned URLs with scoped credentials, CORS for direct browser upload, encryption choices, versioning and object lock, and access logging. Invoke when creating a new bucket, auditing inherited buckets for exposure, or wiring an app to storage with presigned uploads.
---

# Object Storage Security

Public-bucket leaks remain one of the top breach causes a decade after S3 launched — not because the controls are missing, but because the defaults were permissive for years and every provider's mental model (bucket policy, ACL, IAM, signed URL, public binding) overlaps just enough to confuse. One `public-read` flag or one over-broad access key turns a dumb byte store into a data breach.

This skill is the baseline for any S3-compatible store: AWS S3, Cloudflare R2, Google Cloud Storage, self-hosted MinIO. The threat model is the same everywhere — accidental public exposure, over-scoped credentials, exfiltration you never notice, and uploads that come back to bite the app that serves them. For validating the file *contents*, see [`file-upload-security`](../file-upload-security/SKILL.md).

## When to invoke

- Creating a new bucket for an app (uploads, backups, static assets)
- Auditing buckets you inherited and did not provision
- Wiring presigned upload/download URLs into an application
- A credential that had storage access leaked or may have leaked
- Moving from local-disk storage to object storage
- Reviewing ransomware / mass-deletion resilience of stored data

## Step 1 — Public access audit

Start by answering one question per bucket: *can an unauthenticated stranger read it?*

```bash
# S3: Block Public Access must be on at BOTH levels
aws s3api get-public-access-block --bucket example-app-uploads
aws s3control get-public-access-block --account-id 123456789012

# Turn it on (account level covers future buckets too)
aws s3control put-public-access-block --account-id 123456789012 \
  --public-access-block-configuration \
  BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true

# Is the policy public per AWS's own analysis?
aws s3api get-bucket-policy-status --bucket example-app-uploads

# Empirical test — should return 403, never a listing
curl -s https://example-app-uploads.s3.amazonaws.com/
```

Historical traps to check on old buckets:

- **`authenticated-users` ACL grant** — the classic misreading. It means *any AWS account holder on Earth*, not "my authenticated users". Anyone with a free AWS account could list/read. Audit: `aws s3api get-bucket-acl --bucket example-app-uploads` and look for the `AuthenticatedUsers` group URI.
- **`public-read` on individual objects** — Block Public Access with `IgnorePublicAcls=true` neutralizes these without you having to find each one.
- **R2**: buckets are private by default, but check for a public development URL (`r2.dev` — never for production) and custom-domain public bindings in the dashboard. A Worker binding is fine (the Worker is the gatekeeper); a public bucket URL means every object is world-readable.
- **GCS**: look for `allUsers` or `allAuthenticatedUsers` in IAM bindings (`gcloud storage buckets get-iam-policy gs://example-app-uploads`), and enable Public Access Prevention.
- **MinIO**: `mc anonymous get myminio/example-app-uploads` — anything but `none` on a private bucket is a finding.

If a bucket must serve public content (static site assets), that is a deliberate, documented exception — one dedicated bucket, nothing else in it.

## Step 2 — One access-control model: policies + IAM, not ACLs

S3 grew three overlapping mechanisms. Pick the modern pair and disable the legacy one.

| Mechanism | Granularity | Who it attaches to | Verdict |
|---|---|---|---|
| ACLs | Per-object, coarse grants | Object/bucket | Legacy — disable via Object Ownership `BucketOwnerEnforced` |
| Bucket policy | Bucket + prefix + conditions | The bucket | Use — resource-side rules (deny non-TLS, scope prefixes) |
| IAM policy | Bucket + prefix + conditions | The principal (app, user, role) | Use — per-app allow rules |

```bash
# Disable ACLs entirely — bucket owner owns everything, ACL grants are ignored
aws s3api put-bucket-ownership-controls --bucket example-app-uploads \
  --ownership-controls 'Rules=[{ObjectOwnership=BucketOwnerEnforced}]'
```

Baseline bucket policy — deny plaintext transport, regardless of what IAM allows:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "DenyInsecureTransport",
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": [
      "arn:aws:s3:::example-app-uploads",
      "arn:aws:s3:::example-app-uploads/*"
    ],
    "Condition": { "Bool": { "aws:SecureTransport": "false" } }
  }]
}
```

Per-app IAM policy — the app touches its own prefix and nothing else:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
      "Resource": "arn:aws:s3:::example-app-uploads/uploads/*"
    },
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::example-app-uploads",
      "Condition": { "StringLike": { "s3:prefix": "uploads/*" } }
    }
  ]
}
```

Note what is absent: `s3:*`, `s3:PutBucketPolicy`, `s3:PutBucketAcl`, `s3:DeleteBucket`. The app moves objects; it does not reconfigure its own container.

## Step 3 — Credential scoping

The blast radius of a leaked key is exactly what the key can do. Shrink it before it leaks.

- **One credential per app per bucket.** A key like `AKIAIOSFODNN7EXAMPLE` shared across three services means one leak compromises all three, and rotation breaks all three at once.
- **R2**: create API tokens scoped to a *specific bucket* with the minimum permission (`Object Read only` / `Object Read & Write`) — never the account-level token with `Admin Read & Write` in an app's env.
- **Prefer STS temporary credentials over long-lived keys** wherever the runtime supports it: EC2/ECS/Lambda roles, EKS IRSA, GitHub Actions OIDC. Credentials that expire in an hour cannot be harvested from an old `.env` in a git history six months later.
- **MinIO**: per-app users with attached policies (`mc admin user add` + `mc admin policy attach`), never the root credentials in application config.
- Rotate anything long-lived on a schedule, and immediately on any suspicion — a storage key that touched a leaked repo, a compromised laptop, or a pasted log is burned.

## Step 4 — Presigned URLs done right

Presigned URLs delegate *your* credential's authority for one operation on one key. Three rules:

1. **Short expiry.** Minutes, not days. 5 min for downloads, 10-15 min for uploads. A presigned URL in a log file, referrer header, or chat message is a bearer token.
2. **Sign with a scoped key, never admin credentials.** The URL can do whatever the signing credential can do *for that operation* — and the signing key's lifetime caps nothing if the key itself is over-scoped. Sign with the per-app key from Step 3.
3. **Constrain uploads.** An unconstrained presigned PUT lets the holder upload anything of any size. Pin content type and length.

```js
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

// Client constructed with the app-scoped key — not an admin key
const url = await getSignedUrl(s3, new PutObjectCommand({
  Bucket: 'example-app-uploads',
  Key: `uploads/${userId}/${crypto.randomUUID()}`,   // server-generated key, never client filename
  ContentType: 'image/jpeg',        // signed — a PUT with another type fails
  ContentLength: validatedSize,     // signed — a different size fails
}), { expiresIn: 600 });
```

For browser form uploads, presigned POST supports explicit policy conditions (`content-length-range`, exact `Content-Type`) — use it when you need a hard server-enforced size window. Either way: validate the request *before* signing (auth, quota, type allowlist) and verify the object *after* upload (magic bytes, re-encoding — see [`file-upload-security`](../file-upload-security/SKILL.md)).

## Step 5 — CORS: minimal, exact origins

CORS on a bucket exists for exactly one reason: direct browser upload/download. Everything else needs none.

- **Never `AllowedOrigins: ["*"]` on a private bucket.** Combined with credentials or presigned URLs it lets any website a user visits script requests against your bucket in their browser context. Wildcard origin is only defensible for a truly public, read-only asset bucket.
- List exact origins, exact methods, and keep `MaxAgeSeconds` modest:

```json
{
  "CORSRules": [{
    "AllowedOrigins": ["https://app.example.com"],
    "AllowedMethods": ["PUT"],
    "AllowedHeaders": ["Content-Type"],
    "MaxAgeSeconds": 3600
  }]
}
```

CORS is not access control — it gates *browsers*, not `curl`. It complements presigning; it never replaces it.

## Step 6 — Encryption

| Option | Keys managed by | Protects against | Cost/complexity |
|---|---|---|---|
| SSE-S3 (AES-256) | Provider, transparent | Stolen disks at the provider | Free, default — baseline |
| SSE-KMS | Your KMS key | Adds an audit trail + a second gate: reader needs object access AND `kms:Decrypt` | Per-request KMS cost, key policy to maintain |
| Client-side | You, before upload | The provider itself, subpoena of provider, any bucket misconfiguration | Highest — key loss = data loss |

Verdict: SSE-S3 (or the provider's default at-rest encryption — R2 and GCS encrypt everything) is table stakes and does **not** protect against your own misconfiguration — a public object is served decrypted. SSE-KMS earns its cost when you want CloudTrail on every decrypt or per-tenant key revocation. Client-side encryption (e.g. `age` before upload) is the right call for backups and anything where the bucket must never be a single point of disclosure — see the backup pattern in [`postgres-hardening`](../postgres-hardening/SKILL.md).

## Step 7 — Versioning + object lock: ransomware resilience

An attacker with write credentials can overwrite or delete everything. Make destruction recoverable:

```bash
aws s3api put-bucket-versioning --bucket example-app-uploads \
  --versioning-configuration Status=Enabled
```

- **Versioning** turns overwrites and deletes into recoverable events (a delete just adds a delete marker). It is the single cheapest resilience control.
- **MFA Delete** requires the root account's MFA token to permanently delete versions or disable versioning — operationally clunky, strong for small high-value buckets.
- **Object Lock (compliance mode)** makes versions immutable for a retention period — *nobody*, including root, can delete early. This is the real ransomware answer for backup buckets. Must be enabled at bucket creation on S3; MinIO supports it; R2 and GCS have equivalent retention/bucket-lock features.
- Pair with lifecycle rules (Step 9) to expire old noncurrent versions, or versioning silently multiplies your storage bill.

## Step 8 — Logging and detection

You cannot detect exfiltration you never recorded. Two complementary mechanisms on AWS:

- **Server access logs** — free, delivered to a *different* bucket, best-effort, hours of delay. Fine baseline for forensics.
- **CloudTrail data events** — per-object API records (`GetObject`, `PutObject`, `DeleteObject`), near-real-time, paid per event. Enable for sensitive buckets; wire to alerting.

R2: enable Cloudflare Logpush for R2 event logs. GCS: Data Access audit logs. MinIO: audit webhook to your log pipeline. Always log to a destination the storage credentials cannot delete — an attacker who can wipe the trail will.

Detections worth alerting on:

- Mass download — `GetObject` count per principal per hour far above baseline (exfiltration looks like a loop, not a user)
- `ListBucket`/`ListObjects` from an unfamiliar principal or IP range (recon precedes bulk download)
- Any `PutBucketPolicy`, `PutBucketAcl`, `PutPublicAccessBlock`, or versioning/logging change — configuration changes should be rare and expected
- Access denied spikes — someone probing what a stolen credential can reach

## Step 9 — Lifecycle rules: limit the blast radius of stale data

Data you no longer need is pure liability — it cannot help you, and it can still leak. Expire it mechanically:

```json
{
  "Rules": [
    { "ID": "expire-temp-exports", "Status": "Enabled",
      "Filter": { "Prefix": "exports/" },
      "Expiration": { "Days": 7 } },
    { "ID": "trim-old-versions", "Status": "Enabled",
      "Filter": { "Prefix": "" },
      "NoncurrentVersionExpiration": { "NoncurrentDays": 90 } },
    { "ID": "abort-stuck-multipart", "Status": "Enabled",
      "Filter": { "Prefix": "" },
      "AbortIncompleteMultipartUpload": { "DaysAfterInitiation": 3 } }
  ]
}
```

Temp exports, report downloads, and processing scratch space get days, not forever. Incomplete multipart uploads are invisible in normal listings and accumulate silently — abort them. Retention beyond need is the difference between "we leaked last week's exports" and "we leaked seven years of exports".

## The uploads-served-from-app-origin trap

The bucket can be perfectly locked down and still hand an attacker stored XSS. If user uploads are served from `app.example.com` — via a proxy route or a CDN mapping — an uploaded `payload.html` (or SVG) renders as HTML *on your app's origin*, with your users' cookies and localStorage in scope.

- Serve user content from a **separate registrable domain or dedicated subdomain** (`usercontent-example.com`, `cdn.example.com`) that carries no session cookies
- `Content-Disposition: attachment` and `X-Content-Type-Options: nosniff` for anything not on a strict inline allowlist
- Never let the bucket's website-hosting mode serve user uploads under the app's domain

Full serving pattern (CSP, SVG handling, re-encoding) lives in [`file-upload-security`](../file-upload-security/SKILL.md) — this skill's job is to make sure the storage architecture never puts user bytes on the app origin in the first place.

## Quick checklist

- [ ] Block Public Access on at account level and every bucket (or provider equivalent)
- [ ] No `authenticated-users` / `allUsers` / `allAuthenticatedUsers` grants anywhere
- [ ] ACLs disabled via `BucketOwnerEnforced`; access via bucket policy + IAM only
- [ ] Bucket policy denies non-TLS transport
- [ ] Per-app credentials scoped to one bucket and prefix; no `s3:*`, no bucket-config actions
- [ ] STS/OIDC temporary credentials where the runtime supports them
- [ ] Presigned URLs: minutes-long expiry, scoped signing key, type + length pinned on upload
- [ ] CORS lists exact origins and methods — no `*` on private buckets
- [ ] Encryption at rest confirmed; SSE-KMS or client-side where the threat model demands it
- [ ] Versioning enabled; object lock on backup buckets
- [ ] Access logging to a bucket the app credentials cannot touch; mass-download alerting
- [ ] Lifecycle rules: temp data expires, noncurrent versions trimmed, multipart uploads aborted
- [ ] User uploads served from a separate origin, never `app.example.com`
- [ ] R2 `r2.dev` development URLs disabled on production buckets

## What this skill will not do

- Help enumerate, access, or exfiltrate buckets you do not own
- Recommend public ACLs, wildcard-origin CORS on private data, or account-admin keys in application config as a convenience
- Replace provider-specific compliance guidance (HIPAA/PCI BAAs, data-residency law) — this is the engineering baseline underneath those
