---
name: secret-hygiene
description: Find, rotate, and prevent leaked credentials across repositories and disk. Covers leak detection with gitleaks and trufflehog, rotation order (the leaked secret first, then outward), git history purge with git-filter-repo, and prevention via pre-commit scanning. Invoke when a secret was committed to git, when a private repo went public, or as periodic audit.
---

# Secret Hygiene

A practical workflow for credential management: detecting leaks, rotating cleanly, and preventing recurrence.

## When to invoke

- A secret was committed to git, or a private repo went public
- A contributor leaves the project, or access scope changes
- A credential turned up in a public dump, paste, or leak feed
- Periodic audit (quarterly is reasonable)
- Onboarding a repo, hosting account, or VPS you inherited

## Step 1 — Inventory what you have

You cannot rotate secrets you cannot enumerate. Build a list, even a rough one.

```
- Hosting panel: <provider>     creds in: 1Password vault X
- DB user: <name>               creds in: server .env, 1Password
- API keys:
    - Stripe live + test        creds in: backend .env, Stripe dashboard
    - Mailgun                   creds in: backend .env
    - GitHub PAT                creds in: ~/.gitconfig (BAD — move to keychain)
- SSH keys: ~/.ssh/id_*         on machines: workstation, CI, VPS
- CI secrets: GitHub Actions    visible at: repo/settings/secrets
```

Keep this in a password manager or a private repo — never in plaintext on disk.

## Step 2 — Scan for leaks (local + repos)

### Local filesystem

```bash
# Files commonly containing secrets
find ~/Code -maxdepth 4 -type f \( -name '.env*' -o -name 'credentials*' -o -name 'secrets*' \) -not -path '*/node_modules/*' 2>/dev/null

# Permissions check — .env should be 600
find ~/Code -name '.env*' -not -path '*/node_modules/*' -exec stat -f '%Lp %N' {} \; 2>/dev/null

# Did you commit a .env by accident?
cd ~/Code/<repo>
git log --all --full-history -- '.env*' 2>/dev/null
```

### Git history

```bash
# Quick grep across all history for high-signal patterns
git log -p --all -S 'AKIA'        # AWS access key
git log -p --all -S 'sk-'         # OpenAI / many SaaS
git log -p --all -S 'ghp_'        # GitHub PAT
git log -p --all -S 'xoxb-'       # Slack bot token
git log -p --all -S 'BEGIN RSA PRIVATE KEY'
git log -p --all -S 'BEGIN OPENSSH PRIVATE KEY'

# Better: dedicated scanners
gitleaks detect --source . --report-format json --report-path gitleaks.json
trufflehog git file://. --json
```

### Hosted (GitHub)

GitHub runs secret scanning for public repos automatically. For private repos with paid tiers, enable it. Push protection blocks future leaks at `git push` time — turn it on.

## Step 3 — Rotation order

When a secret leaks, rotate **outward from the access it grants**. Common order:

1. **The leaked secret itself** — invalidate first.
2. **Anything that secret could have been used to read** (e.g. a leaked DB password → audit recent DB queries, then rotate DB user).
3. **Anything that secret could have been used to write** (e.g. a leaked API key with write scope → check for unauthorized writes, then rotate).
4. **Adjacent secrets stored in the same place** — if a `.env` leaked, assume *every* value in that `.env` leaked.
5. **Inbound credentials** that depend on the rotated outbound credential (downstream services, webhooks).

For each rotation, log: **what, when, by whom, who was notified**.

## Step 4 — Purging git history (last resort)

Rewriting history is disruptive — every collaborator must re-clone, and tags/CI references may break. Do it only if a high-value secret is in history and rotating is genuinely insufficient (rare; usually rotation is enough).

### Modern tool: `git-filter-repo`

```bash
# Install once: brew install git-filter-repo

# Backup first
git clone --mirror git@github.com:owner/repo.git repo-backup.git

# Remove a specific file from all history
cd repo-clone
git filter-repo --invert-paths --path .env
git filter-repo --invert-paths --path config/secrets.yml

# Or replace a literal string everywhere
echo 'AKIAIOSFODNN7EXAMPLE==>REDACTED' > replace.txt
git filter-repo --replace-text replace.txt

# Force-push (coordinate with the team — everyone re-clones after this)
git push --force --all
git push --force --tags
```

After force-push:

- Every collaborator must `git clone` fresh; rebasing existing forks is fragile
- Any CI/CD that pinned a commit SHA may break
- GitHub may still serve the old commit by SHA for a while — open a support ticket if cleanup is critical
- **Rotate the secret anyway** — assume it was already harvested before the purge

## Step 5 — Prevention

### Pre-commit scanning

Install once per workstation:

```bash
# Option A: gitleaks pre-commit hook
brew install gitleaks
gitleaks protect --staged --no-banner
```

Or via `pre-commit` framework — example `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

### `.gitignore` baseline

```
# Never commit these
.env
.env.*
!.env.example
*.pem
*.key
*.p12
id_rsa
id_ed25519
credentials.json
config/secrets.yml
```

### `.env.example` convention

Commit a placeholder file with the **keys but not the values**:

```
# .env.example
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
STRIPE_SECRET_KEY=sk_test_REPLACE_ME
GITHUB_TOKEN=ghp_REPLACE_ME
```

### Server-side secrets

- `.env` permissions: `chmod 600 .env`, owned by the app user
- Never bake secrets into Docker images (use runtime env, mounted files, or a secret store)
- For CI: use the platform's secret store (GitHub Actions secrets, GitLab CI variables) — never echo them into build logs

### Token scope minimization

- GitHub PATs: prefer fine-grained tokens, scoped to a single repo/org with the minimum scopes
- Database users: separate read-only and read-write users for separate processes
- Cloud IAM: avoid root keys; use scoped service accounts with explicit, minimal IAM

## Quick reference — common token prefixes

Useful for grep-based scans:

| Prefix | Provider |
|---|---|
| `AKIA`, `ASIA` | AWS access key |
| `ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_` | GitHub tokens |
| `xoxb-`, `xoxp-`, `xoxa-` | Slack tokens |
| `sk_live_`, `sk_test_` | Stripe |
| `key-` (Mailgun), `re_` (Resend) | Mail providers |
| `sk-`, `sk-proj-` | OpenAI / Anthropic-style |
| `glpat-` | GitLab PAT |
| `dckr_pat_` | Docker Hub PAT |
| `npm_` | npm tokens |
| `-----BEGIN OPENSSH PRIVATE KEY-----` | SSH private key |

## What this skill will not do

- Help retrieve or use credentials that are not yours.
- Scan repositories you do not have authorization to scan.
- Recommend storing secrets in source control "just for now" — there is no "just for now" with secrets.
