# Security Glossary — Claude Code Security Skills

Definitions for terms used across the skills. Brief — for depth see the relevant `SKILL.md`.

## A

- **agentskills.io** — Emerging open standard for the YAML-frontmatter convention used by `SKILL.md` files. Compatible with Claude Code and several other LLM coding agents.
- **Argon2id** — Modern password hashing algorithm. Memory-hard and side-channel resistant. The preferred default for new systems; bcrypt at cost ≥ 12 is acceptable. See [`auth-hardening`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/auth-hardening/SKILL.md).
- **ATS** — App Transport Security. Apple's iOS / macOS requirement that network calls go over HTTPS with modern TLS.
- **AVV** — Auftragsverarbeitungsvertrag (German). Equivalent to DPA. Required contract between data controller and data processor under GDPR Art. 28.

## B

- **BIMI** — Brand Indicators for Message Identification. DNS-published logo shown in supporting mail clients (Gmail, Apple Mail). Requires DMARC at `quarantine` or `reject` plus a Verified Mark Certificate.
- **BOLA** — Broken Object-Level Authorization. An endpoint that serves a resource without checking the requester owns it. The single most common API vulnerability.

## C

- **CAA record** — DNS record restricting which certificate authorities may issue certificates for a domain.
- **Certificate Transparency (CT) logs** — Public append-only logs every CA must write issued certificates to. Monitoring them reveals unexpected issuance for your domains — an early takeover or phishing signal.
- **CIS Benchmark** — Configuration baseline published by the Center for Internet Security, per OS or product. More detailed than this repo's hardening skills.
- **CNI** — Container Network Interface. The plugin system that gives Kubernetes pods their network. `NetworkPolicy` enforcement requires a CNI that supports it (Calico, Cilium, Weave, Antrea).
- **cosign / sigstore** — Modern open-source signing tooling for container images and artifacts.
- **CSP** — Content Security Policy. HTTP header that restricts script and style sources, mitigating XSS.

## D

- **DKIM** — DomainKeys Identified Mail. Cryptographically signs outbound email; receivers verify via a DNS-published public key.
- **DMARC** — Domain-based Message Authentication, Reporting & Conformance. Builds on SPF + DKIM and tells receivers what to do on failure (`none` → `quarantine` → `reject`).
- **DPA** — Data Processing Agreement. English term for AVV. See `auth-hardening` / `gdpr-technical-controls`.
- **DPAPI** — Data Protection API. Windows mechanism for encrypting per-user data using OS-managed keys.

## E

- **EdDSA / Ed25519** — Modern signature scheme. Preferred for new SSH keys, JWT signing, and similar.

## F

- **Fail-closed** — A control that denies on uncertainty. The opposite of fail-open. Auth checks should fail-closed.

## I

- **Idempotency** — Property of an operation where executing it N times has the same effect as executing once. Required for safe retries and replay-resistant webhook handlers.

## J

- **JetStream** — NATS's persistence layer. Adds streams, durable consumers, and exactly-once semantics on top of core NATS.

## K

- **Keychain (Apple)** — System-managed secure storage on iOS / macOS. Accessed via the Security framework with accessibility tiers (`WhenUnlockedThisDeviceOnly`, etc.).
- **Keystore (Android)** — Android's hardware-backed key storage. Keys are generated and used inside secure hardware and never exported; StrongBox is the dedicated-secure-element tier.
- **Kyverno / Gatekeeper (OPA)** — Kubernetes admission controllers. Enforce policy-as-code on resource submission.

## L

- **LOTL** — Living-off-the-land. Attackers using legitimate built-in tools (PowerShell, `curl`, `cron`) instead of dropping malware. Harder to detect.

## M

- **mTLS** — Mutual TLS. Both client and server present certificates and validate each other. Used for service-to-service auth and agent ↔ control-plane channels.
- **MITRE ATT&CK** — Catalog of adversary tactics and techniques.
- **MITRE ATLAS** — Adversary tactics and techniques against AI/ML systems.

## N

- **NATS** — Lightweight message bus. Used in `message-bus-security`. Account / subject permission model.
- **NIST 800-63B** — NIST's digital identity guidelines. Source for modern password policy (no rotation theatre, length over composition).
- **NIST CSF** — Cybersecurity Framework. High-level functions: Identify, Protect, Detect, Respond, Recover.

## O

- **Object Lock** — S3 / R2 write-once-read-many (WORM) mode. Objects cannot be deleted or overwritten for a retention period, even by the account owner — the backbone of ransomware-resistant backups.
- **OIDC** — OpenID Connect. Used in GitHub Actions to federate identity to AWS / GCP / Cloudflare without long-lived secrets.
- **OWASP API Top 10** — Catalog of the 10 most common API security failures. See `api-security`.
- **OWASP LLM Top 10** — Catalog of LLM-application-specific security risks. See `llm-app-security`.

## P

- **PICERL** — Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned. Standard incident-response phase model.
- **Pinning** — Hardcoding the expected public key or certificate of a remote service into the client. Defeats CA-level MITM but introduces operational fragility.
- **Play Integrity** — Google's attestation API reporting whether an app runs unmodified on a certified Android device. A risk signal, not a security boundary.
- **Pod Security Standards (PSS)** — Kubernetes built-in policy levels (Privileged / Baseline / Restricted).
- **Presigned URL** — Time-limited signed URL granting a single storage operation (upload / download) without sharing credentials. Inherits the permissions of the signing identity — sign with a scoped key.

## R

- **RAG** — Retrieval-Augmented Generation. LLM answers grounded in documents fetched from an index at query time. Security-relevant because retrieval crosses authorization boundaries the LLM cannot enforce.
- **RBAC** — Role-Based Access Control. The Kubernetes mechanism for "who can do what."
- **RLS** — Row-Level Security (Postgres). Per-row policy enforced by the database, useful for multi-tenant isolation.
- **RPO / RTO** — Recovery Point Objective (acceptable data loss, in time) / Recovery Time Objective (acceptable downtime during recovery). See `backup-disaster-recovery`.

## S

- **SAR** — Subject Access Request. GDPR right of a user to obtain a copy of their personal data.
- **SBOM** — Software Bill of Materials. Inventory of components / dependencies in a build.
- **SCRAM** — Salted Challenge Response Authentication Mechanism. Modern Postgres password auth method.
- **Slopsquatting** — Typosquatting that targets LLM-hallucinated package names. The attacker registers names LLMs invent so that the next `npm install <hallucinated-name>` lands on attacker code.
- **SPF** — Sender Policy Framework. DNS-published list of servers allowed to send mail for a domain.
- **SSRF** — Server-Side Request Forgery. App fetches a URL controlled by the user; attacker uses it to hit internal services or cloud metadata.
- **Subdomain takeover** — A DNS record (usually a CNAME) still points at a deprovisioned service whose name anyone can claim. The claimant then serves content under your domain.

## T

- **TOM** — Technical and Organizational Measures. Required by GDPR Art. 32 — the technical and procedural controls protecting personal data.
- **TLS-RPT** — TLS Reporting. DNS-published address to receive reports of TLS failures from sending MTAs.
- **TTDSG** — Telekommunikation-Telemedien-Datenschutz-Gesetz (Germany). Source of the cookie-consent requirement.

## U

- **UFW** — Uncomplicated Firewall. Front-end to iptables on Debian / Ubuntu. Caveat: Docker bypasses UFW by default.

## V

- **Verified Mark Certificate (VMC)** — Certificate issued by a specialized CA verifying a trademark, used to display a brand logo via BIMI.

---

Maintained by [GoldenWing](https://goldenwing.at) — defensive-security audits and incident response for small teams. · [Main repository](https://github.com/GoldenWing-360/claude-security-skills) · [FAQ](./FAQ.md) · [Prompt Library](./PROMPTS.md)
