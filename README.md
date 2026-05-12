# Claude Code Security Skills

Defensive security skills for [Claude Code](https://claude.com/claude-code). Each skill is a single Markdown file with YAML frontmatter — Claude Code can auto-trigger them, and they read equally well as plain runbooks for humans.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-555.svg)](https://claude.com/claude-code)

Coverage: WordPress, VPS / Cloudflare / Next.js / API hardening, Kubernetes, distributed-system audit, agent / client / message-bus security, backend architecture, AI agent guardrails and MCP security, prompt injection defense, OWASP LLM Top 10, file upload safety, codebase audit methodology, incident response, backups, GDPR / DACH compliance — 34 skills total.

## Table of contents

- [Who this is for](#who-this-is-for)
- [Quick start](#quick-start)
- [Repository structure](#repository-structure)
- [Skills by category](#skills-by-category)
  - [AI & LLM security](#-ai--llm-security-the-2026-attack-surface)
  - [Web application security](#-web-application-security)
  - [Server & infrastructure](#-server--infrastructure)
  - [Distributed systems](#-distributed-systems)
  - [Architecture & reliability](#-architecture--reliability)
  - [Audit & review](#-audit--review)
  - [Identity & access](#-identity--access)
  - [Supply chain & CI/CD](#-supply-chain--cicd)
  - [Compliance (EU / DACH)](#-compliance-eu--dach)
  - [Detection & monitoring](#-detection--monitoring)
  - [Incident response](#-incident-response--secret-hygiene)
  - [Mobile security](#-mobile-security)
- [Find the right skill](#find-the-right-skill)
- [Using with Claude Code](#using-with-claude-code)
- [Contributing](#contributing)
- [License](#license)

## Who this is for

- **Developers shipping with LLM assistance ("vibe coders")** who need a security checklist that actually fits how they work — agent loops, MCP servers, fast iterations, small teams
- **Solo operators and small agencies** running 5–50 WordPress sites, a few VPS servers, and Cloudflare — without a dedicated security team
- **Engineers building LLM-powered features** (chat, RAG, agents, MCPs) who need a defensive baseline against prompt injection, exfiltration, and runaway costs
- **Anyone inheriting an undocumented production system** who wants a fast, structured way to audit it

Each skill is **defensive only**. No exploitation, no offensive tradecraft. Authorization for the systems you work on is assumed.

## Quick start

```bash
git clone https://github.com/GoldenWing-360/claude-security-skills.git
```

Use any skill in three ways:

1. **As a Claude Code skill** — Claude auto-triggers the right one based on the conversation. The YAML `description` field is matched against your request.
2. **As a runbook for yourself** — open `<skill-name>/SKILL.md` and follow the steps.
3. **As a checklist for review** — paste the skill into a PR or audit doc and walk through it.

## Repository structure

<details>
<summary>34 skills + repo metadata — click to expand</summary>

```
claude-security-skills/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug-report.md
│   │   ├── config.yml
│   │   └── skill-request.md
│   ├── FUNDING.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── SOCIAL_PREVIEW.md
│
├── agent-client-security/SKILL.md
├── ai-agent-guardrails/SKILL.md
├── api-security/SKILL.md
├── auth-hardening/SKILL.md
├── backend-architecture/SKILL.md
├── backup-disaster-recovery/SKILL.md
├── cloudflare-hardening/SKILL.md
├── codebase-audit/SKILL.md
├── dach-compliance/SKILL.md
├── dependency-supply-chain/SKILL.md
├── distributed-system-audit/SKILL.md
├── docker-container-security/SKILL.md
├── email-deliverability-security/SKILL.md
├── file-upload-security/SKILL.md
├── gdpr-technical-controls/SKILL.md
├── github-actions-security/SKILL.md
├── honeypot-tarpits/SKILL.md
├── incident-response/SKILL.md
├── ios-security/SKILL.md
├── kubernetes-security/SKILL.md
├── llm-app-security/SKILL.md
├── llm-coding-failure-modes/SKILL.md
├── log-strategy/SKILL.md
├── mcp-security/SKILL.md
├── message-bus-security/SKILL.md
├── nextjs-security/SKILL.md
├── payload-cms-security/SKILL.md
├── postgres-hardening/SKILL.md
├── prompt-injection-defense/SKILL.md
├── secret-hygiene/SKILL.md
├── site-server-audit/SKILL.md
├── stripe-webhook-security/SKILL.md
├── vps-hardening/SKILL.md
├── wordpress-hardening/SKILL.md
│
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

Every skill is a self-contained `SKILL.md` with YAML frontmatter (`name`, `description`) plus a body that follows roughly: *when to invoke → detection / steps / patterns → checklist → what this skill will not do*.

</details>

## Skills by category

### 🤖 AI & LLM security (the 2026 attack surface)

The class of risks that classical security tooling does not yet handle well — and the area most teams shipping with LLM assistance get wrong.

| Skill | Use when |
|---|---|
| [`mcp-security`](./mcp-security/SKILL.md) | Adding a new MCP server, before granting one write access to production, after a malicious-MCP advisory, periodic MCP audit. Covers inventory, risk-tiering (🟢 read-only → ⚫ spends-money), secret-in-config detection, tool-poisoning indicators, lifecycle. |
| [`ai-agent-guardrails`](./ai-agent-guardrails/SKILL.md) | Designing an autonomous agent, granting an LLM write access to production, after an agent makes an unexpected change. Covers blast-radius classification, dry-run-first, out-of-band approval gates, scope locking, idempotency, kill switches, rollback. |
| [`prompt-injection-defense`](./prompt-injection-defense/SKILL.md) | Building any app where untrusted text reaches an LLM (chat, RAG, summarize-this-URL), or where the LLM has tools that act on real systems. Covers source-of-trust tagging, tool-use confirmation after untrusted input, output validation, markdown-image exfiltration prevention. |
| [`llm-app-security`](./llm-app-security/SKILL.md) | Shipping an LLM feature to production, handling an abuse complaint, after a model-provider advisory. Walks the OWASP LLM Top 10, covers rate limits, cost caps, PII scrubbing, audit logging, model-version pinning, AI-incident playbook. |
| [`llm-coding-failure-modes`](./llm-coding-failure-modes/SKILL.md) | Reviewing LLM-written code, designing a coding agent's guardrails, onboarding a team to "vibe coding", investigating an LLM-driven incident. The antipattern catalog: bulk-ops without review, safety-guard bypass as friction, indirect injection acted on, secrets in logs, slopsquat-bait packages, outdated training patterns, sycophancy on insecure proposals, and more. |

### 🌐 Web application security

| Skill | Use when |
|---|---|
| [`wordpress-hardening`](./wordpress-hardening/SKILL.md) | A WordPress site shows unexpected files, suspicious admin accounts, defaced pages, or hardening a fresh install. Covers Sid Gifari / WSO / FilesMan webshell detection, mu-plugin defense pack, shared-hosting pivot defense, integrity monitoring. |
| [`nextjs-security`](./nextjs-security/SKILL.md) | Reviewing a Next.js app before launch, after a major version upgrade (13 → 14 → 15 → 16), or when adding Server Actions. Covers middleware-bypass class, `NEXT_PUBLIC_` env leakage, RSC over-fetch, CSP, open redirects, `next/image` SSRF. |
| [`api-security`](./api-security/SKILL.md) | Designing a new REST/GraphQL API, reviewing one before scaling, after abuse (scraping, account takeover via API). Walks the OWASP API Top 10: BOLA, broken auth, mass assignment, excessive data exposure, resource consumption, broken function-level auth, SSRF, misconfig, inventory, unsafe third-party consumption. |
| [`payload-cms-security`](./payload-cms-security/SKILL.md) | Shipping Payload CMS to production, opening admin to non-developers, after a Payload version upgrade. Covers collection/field-level access control, hook safety, file uploads, GraphQL/REST surface, multi-tenant isolation. |
| [`file-upload-security`](./file-upload-security/SKILL.md) | Adding upload to a new endpoint, after an upload-caused incident, migrating from local-disk to object storage, reviewing an inherited upload feature. Covers magic-byte validation, image re-encoding to defang polyglots, EXIF stripping, virus scanning, path-safe storage keys, separate-origin serving with `Content-Disposition`, signed URLs, presigned-PUT for large files. |
| [`site-server-audit`](./site-server-audit/SKILL.md) | Onboarding a new client site, before launch, after infra changes, periodic re-audit. Read-only checklist: DNS, TLS/HSTS, security headers, exposed paths (`.git`, `.env`, backups), cookies, software fingerprint. |

### 🏗️ Server & infrastructure

| Skill | Use when |
|---|---|
| [`vps-hardening`](./vps-hardening/SKILL.md) | Provisioning a new Debian/Ubuntu VPS, inheriting an existing one, before exposing a service to the public internet. 30-minute baseline: SSH key-only, UFW, fail2ban, unattended-upgrades, kernel sysctls, journalctl. Includes monthly audit script. |
| [`cloudflare-hardening`](./cloudflare-hardening/SKILL.md) | Onboarding a domain to Cloudflare, when origin IP may be exposed, after an attack. Covers account hardening, Authenticated Origin Pulls, WAF Managed Rules, Bot Fight, Rate Limiting, Transform Rules for headers, Zero Trust Access for admin paths, R2 / Pages security. |
| [`postgres-hardening`](./postgres-hardening/SKILL.md) | Provisioning a new PostgreSQL deployment, before opening it to a new app, after an advisory, or reviewing a multi-tenant schema. Covers `pg_hba.conf`, role separation, row-level security, backup encryption, pg_audit, version upgrades. |
| [`docker-container-security`](./docker-container-security/SKILL.md) | Adding Docker to a VPS with UFW (and hitting the bypass surprise), writing a new Dockerfile, pushing to a public registry, periodic audit. Covers non-root users, read-only FS, dropped capabilities, secret mounts, trivy scanning, distroless bases. |
| [`kubernetes-security`](./kubernetes-security/SKILL.md) | Provisioning a new cluster, inheriting one, before opening a cluster to a new tenant, after a K8s CVE. Covers Pod Security Standards (Restricted / Baseline / Privileged), RBAC with least privilege, NetworkPolicy default-deny, secrets without env vars (SealedSecrets / External Secrets / SOPS), admission controllers (Kyverno / OPA), image scanning, audit logging, common findings on inherited clusters. |

### 🛰 Distributed systems

| Skill | Use when |
|---|---|
| [`distributed-system-audit`](./distributed-system-audit/SKILL.md) | Auditing a client/server product, microservices, IoT or fleet-management backend, multi-tenant SaaS with workers, acquisition due-diligence on a distributed product. Map first, judge later: per-component trust analysis, protocol audit (replay / ordering / forgery), threat-modeling-lite, failure-mode audit, forensic accountability, multi-tenant isolation. |
| [`agent-client-security`](./agent-client-security/SKILL.md) | Shipping a native agent / endpoint client (monitoring, RMM, deployment, CI runner, IoT controller), designing the installer / updater, auditing one before adoption. Covers installer integrity and code signing per platform, OTA update channel with rollback and kill-switch, mTLS with per-agent identity, local secret storage (Keychain / DPAPI / libsecret), anti-tampering signals, telemetry hygiene. |
| [`message-bus-security`](./message-bus-security/SKILL.md) | Introducing NATS / RabbitMQ / Kafka / MQTT to an architecture, adding multi-tenancy to an existing bus, after cross-tenant message leakage, auditing a system that uses a bus. Covers account / vhost / topic-prefix tenancy, deny-default permissions, mTLS / NKEYs / SASL auth, replay protection + idempotency at consumer, encryption in-transit and at-rest, cross-cluster trust. |

### 🎯 Architecture & reliability

| Skill | Use when |
|---|---|
| [`backend-architecture`](./backend-architecture/SKILL.md) | "User uploads disappear after redeploy", scaling from one server to two, moving from prototype to production, handing off to a team that has to run it. The Solutions-Architect baseline: stateless apps + state in the right places (object storage / managed DB / Redis), immutable artifacts, health checks, graceful shutdown, migrations that don't lock the world, background jobs without `setTimeout`, twelve-factor patterns. |
| [`backup-disaster-recovery`](./backup-disaster-recovery/SKILL.md) | "We have backups but nobody has ever restored them", new system holding production data, after a near-miss, before a major migration. Covers RPO/RTO, the 3-2-1 rule, encryption before leaving the host, ransomware-resistant immutable storage, restore drills (a backup you have not restored is a wish), the things-that-aren't-the-database backup list, retention split (operational vs legal). |

### 🔎 Audit & review

| Skill | Use when |
|---|---|
| [`codebase-audit`](./codebase-audit/SKILL.md) | Inheriting a codebase (new job, client takeover, acquisition), accepting an "audit my app" engagement, reviewing AI-generated code before shipping, periodic re-audit. The methodology: scope discipline, 30-minute Day-0 triage, SAST/SCA tool recipes (semgrep, CodeQL, gitleaks, trivy), OWASP Top 10 mapped to grep patterns, auth-surface walkthrough, dependency-and-infra review, writing the report (severity classes, reproduction, remediation), anti-patterns junior auditors fall into. |

### 🔐 Identity & access

| Skill | Use when |
|---|---|
| [`auth-hardening`](./auth-hardening/SKILL.md) | Building auth from scratch, reviewing an existing system, handling a credential-stuffing wave, planning MFA rollout. Covers NIST 800-63B passphrase policy (no rotation theatre), MFA enforcement, session vs JWT, OAuth scope minimization, account lockout. |
| [`secret-hygiene`](./secret-hygiene/SKILL.md) | A secret was committed to git, a private repo went public, a contributor leaves, periodic audit. Covers leak detection (gitleaks/trufflehog), rotation order, `git-filter-repo` history purge, pre-commit prevention. |

### 📦 Supply chain & CI/CD

| Skill | Use when |
|---|---|
| [`dependency-supply-chain`](./dependency-supply-chain/SKILL.md) | Adding a new dependency, after a supply-chain incident (npm typosquat, package takeover), periodic audit. Covers lockfile hygiene, npm/pnpm audit and its limits, socket.dev, postinstall script review, package pinning, minimum-permission CI. |
| [`github-actions-security`](./github-actions-security/SKILL.md) | Adding a workflow, introducing a third-party action, after a workflow leaked a secret, migrating from long-lived cloud keys to OIDC. Covers SHA pinning vs tags, scoped `GITHUB_TOKEN`, OIDC, `pull_request_target` traps, environment protections. |

### 📋 Compliance (EU / DACH)

| Skill | Use when |
|---|---|
| [`gdpr-technical-controls`](./gdpr-technical-controls/SKILL.md) | Building a product handling EU resident data, responding to a SAR (Subject Access Request), preparing for a Datenschutz audit. Covers data inventory, deletion/portability endpoints, anonymization, log scrubbing, 72h breach notification, DPA implications. |
| [`dach-compliance`](./dach-compliance/SKILL.md) | Launching a site for Germany / Austria / Switzerland, adding third-party services to a DACH site, reviewing an inherited DACH site. Covers Impressum (TMG/MStV/ECG), Datenschutzerklärung, AGB basics, AVV / DPA, TOMs, consent banners. |

### 🔍 Detection & monitoring

| Skill | Use when |
|---|---|
| [`log-strategy`](./log-strategy/SKILL.md) | Starting a new service, investigation revealed missing log fields, log volume becoming expensive. Covers what to log / never log (PII, secrets), structured logging, retention tiers, centralization, alert routing. |
| [`honeypot-tarpits`](./honeypot-tarpits/SKILL.md) | Public services see constant automated probing, want detection without a SIEM, complementing fail2ban + WAF. Covers fake admin paths, decoy `.env` files, canary tokens, fake API keys in JS bundles, scanner tarpits. |

### 🛡️ Incident response

| Skill | Use when |
|---|---|
| [`incident-response`](./incident-response/SKILL.md) | A site is defaced or redirecting, webshell found, admin appeared without consent, abuse notice from a provider. SANS PICERL-style runbook: Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned. Includes post-mortem template. |

### 📨 Email security

| Skill | Use when |
|---|---|
| [`email-deliverability-security`](./email-deliverability-security/SKILL.md) | Launching a new sending domain, domains being spoofed, transactional mail in spam, consolidating to a single ESP. Covers SPF, DKIM, DMARC, BIMI, ARC, MTA-STS, TLS-RPT, and the `p=none` → `p=reject` migration. |

### 📱 Mobile security

| Skill | Use when |
|---|---|
| [`ios-security`](./ios-security/SKILL.md) | Shipping a native iOS / macOS app that holds credentials or sensitive data, before App Store submission, after a mobile advisory. Covers Keychain, App Transport Security, certificate pinning tradeoffs, jailbreak detection limits, biometric auth, OTA update integrity. |

## Find the right skill

| Scenario | Where to start |
|---|---|
| Site hacked / webshell found | [`incident-response`](./incident-response/SKILL.md) → [`wordpress-hardening`](./wordpress-hardening/SKILL.md) |
| Detect a webshell on WordPress | [`wordpress-hardening`](./wordpress-hardening/SKILL.md) |
| Committed a `.env` to a public repo | [`secret-hygiene`](./secret-hygiene/SKILL.md) |
| Preventing prompt injection in an LLM app | [`prompt-injection-defense`](./prompt-injection-defense/SKILL.md) |
| Reviewing LLM-generated code | [`llm-coding-failure-modes`](./llm-coding-failure-modes/SKILL.md) |
| Giving an AI agent write access to production | [`ai-agent-guardrails`](./ai-agent-guardrails/SKILL.md) |
| Hardening a new Ubuntu VPS | [`vps-hardening`](./vps-hardening/SKILL.md) |
| Hardening a Kubernetes cluster | [`kubernetes-security`](./kubernetes-security/SKILL.md) |
| User uploads disappear on redeploy | [`backend-architecture`](./backend-architecture/SKILL.md) |
| Architecting a backend that scales | [`backend-architecture`](./backend-architecture/SKILL.md) |
| Zero-downtime deploys | [`backend-architecture`](./backend-architecture/SKILL.md) |
| Inherited a codebase, where to start | [`codebase-audit`](./codebase-audit/SKILL.md) |
| Auditing a distributed / agent system | [`distributed-system-audit`](./distributed-system-audit/SKILL.md) |
| Fleet of native agents on customer machines | [`agent-client-security`](./agent-client-security/SKILL.md) |
| Multi-tenant NATS / RabbitMQ / Kafka | [`message-bus-security`](./message-bus-security/SKILL.md) |
| Backups exist but have never been restored | [`backup-disaster-recovery`](./backup-disaster-recovery/SKILL.md) |
| Broken access control / BOLA in an API | [`api-security`](./api-security/SKILL.md) |
| Accepting user file uploads safely | [`file-upload-security`](./file-upload-security/SKILL.md) |
| Cloudflare WAF / origin-IP protection | [`cloudflare-hardening`](./cloudflare-hardening/SKILL.md) |
| Securing a Stripe webhook | [`stripe-webhook-security`](./stripe-webhook-security/SKILL.md) |
| Implementing OWASP LLM Top 10 | [`llm-app-security`](./llm-app-security/SKILL.md) |
| GitHub Actions OIDC + scoped tokens | [`github-actions-security`](./github-actions-security/SKILL.md) |
| DACH Impressum / Datenschutz / AGB | [`dach-compliance`](./dach-compliance/SKILL.md) |
| Blocking brute force on `/wp-login.php` | [`wordpress-hardening`](./wordpress-hardening/SKILL.md) + [`vps-hardening`](./vps-hardening/SKILL.md) + [`cloudflare-hardening`](./cloudflare-hardening/SKILL.md) |
| Writing a post-mortem after a breach | [`incident-response`](./incident-response/SKILL.md) |
| Configuring SPF / DKIM / DMARC | [`email-deliverability-security`](./email-deliverability-security/SKILL.md) |

## Using with Claude Code

Each `SKILL.md` has YAML frontmatter (`name`, `description`) that Claude Code matches against your request. Drop the directory in a path Claude Code scans for skills, or reference the skills directly. Claude will pick up the right one when a conversation matches its description.

If you prefer to work without auto-triggering, just `cat` the relevant `SKILL.md` and follow it manually.

## Contributing

Contributions welcome, especially:

- Additional detection patterns observed in the wild (with IOCs anonymized)
- Updated rotation procedures as providers change their APIs
- Translations (the original is English; the maintainer also operates in German)
- New skills for under-covered areas

Please keep contributions defensive in spirit. No exploitation tradecraft, no recommendations to weaken existing protections.

## License

[MIT](./LICENSE).

## Maintainers

Maintained by [GoldenWing](https://goldenwing.at). Patterns here are distilled from real cleanup, hardening, and incident-response work. Specific indicators of compromise and customer details have been generalized so the guidance is portable.
