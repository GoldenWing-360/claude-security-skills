<p align="center">
  <img src="./assets/banner.png" alt="Claude Code Security Skills" width="100%">
</p>

<div align="center">

# Claude Code Security Skills

### Defensive security playbooks for LLM coding agents and the developers using them

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-34-brightgreen.svg?style=flat-square)](#skills-by-category)
[![Domains](https://img.shields.io/badge/domains-13-9cf.svg?style=flat-square)](#whats-inside--13-security-domains)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-555.svg?style=flat-square)](https://claude.com/claude-code)
[![Stars](https://img.shields.io/github/stars/GoldenWing-360/claude-security-skills?style=flat-square)](https://github.com/GoldenWing-360/claude-security-skills/stargazers)
[![Forks](https://img.shields.io/github/forks/GoldenWing-360/claude-security-skills?style=flat-square)](https://github.com/GoldenWing-360/claude-security-skills/network/members)
[![Last commit](https://img.shields.io/github/last-commit/GoldenWing-360/claude-security-skills?style=flat-square)](https://github.com/GoldenWing-360/claude-security-skills/commits/main)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![Featured on dev.to](https://img.shields.io/badge/Featured%20on-dev.to-black.svg?style=flat-square&logo=devdotto)](https://dev.to/goldenwing360/10-security-mistakes-claude-code-and-copilot-make-in-production-584l)

**34 production-tested skills · 13 security domains · defensive-only · MIT-licensed**

[Get started](#quick-start) · [What's inside](#whats-inside--13-security-domains) · [Find a skill](#find-the-right-skill) · [Read on dev.to](https://dev.to/goldenwing360/10-security-mistakes-claude-code-and-copilot-make-in-production-584l) · [Contributing](./CONTRIBUTING.md)

</div>

---

> ⚠️ **Independent project** — Not affiliated with Anthropic PBC. The skills are plain Markdown with YAML frontmatter and work with any LLM coding agent that supports the same convention.

## Give any LLM coding agent the instincts of a senior engineer

A senior engineer knows when a `--no-verify` flag is hiding a real bug, when an empty `catch {}` is silently swallowing an auth check, what to do when a customer's WordPress site starts redirecting to a casino, and how to harden a fresh VPS in thirty minutes. **Your AI coding agent doesn't — unless you give it these skills.**

This repo contains **34 production-tested defensive security skills**, each a self-contained Markdown file with YAML frontmatter so Claude Code (or any compatible agent) can auto-trigger the right one. Every skill comes from real incident-response, hardening, and audit work — generalized so the patterns travel beyond the original engagement. Clone it, point your agent at it, and your next deploy, audit, or 3am alert gets expert-level guidance in seconds.

## What's inside — 13 security domains

| Domain | Skills | What it covers |
|---|---|---|
| 🤖 AI & LLM security | 5 | MCP security · agent guardrails · prompt injection defense · OWASP LLM Top 10 · coding-agent failure modes |
| 🌐 Web application | 6 | WordPress · Next.js · Payload CMS · API (OWASP API Top 10) · Stripe webhooks · file upload safety |
| 🏗️ Server & infrastructure | 5 | VPS · Cloudflare · Postgres · Docker · Kubernetes |
| 🛰 Distributed systems | 3 | Distributed-system audit · native-agent / client security · message bus (NATS / RabbitMQ / Kafka) |
| 🎯 Architecture & reliability | 2 | Backend architecture (twelve-factor, stateless deploys) · backups & disaster recovery |
| 🔎 Audit & review | 2 | Codebase audit methodology · site / server audit checklist |
| 🔐 Identity & access | 2 | Auth hardening (NIST 800-63B, MFA tiers) · secret hygiene & rotation |
| 📦 Supply chain & CI/CD | 2 | npm / pnpm / typosquat defense · GitHub Actions (OIDC, SHA pinning) |
| 📋 Compliance (EU / DACH) | 2 | GDPR technical controls · DACH Impressum / Datenschutz / AGB |
| 🔍 Detection & monitoring | 2 | Log strategy (operational / access / audit) · honeypots & tarpits |
| 🛡️ Incident response | 1 | SANS PICERL runbook with post-mortem template |
| 📨 Email security | 1 | SPF / DKIM / DMARC (with the p=none → p=reject migration path) |
| 📱 Mobile security | 1 | iOS / macOS — Keychain, ATS, certificate pinning, jailbreak signal |

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

## Skill anatomy

Every `SKILL.md` follows a consistent structure that doubles as a discovery contract and a self-contained runbook:

```markdown
---
name: <kebab-case-slug>
description: <three-sentence summary — what / covers / invoke when>
---

# <Skill title>

<one-paragraph framing>

## When to invoke
- <concrete situation>

## <Body — adaptive per skill>
detection · steps · patterns · common gotchas

## Quick checklist
- [ ] ...

## What this skill will not do
- <explicit non-goals — defensive-only stance>
```

A companion [`index.json`](./index.json) at the repo root indexes every skill's slug, name, description, and domain for programmatic use (skill discovery, agent loading, search UIs).

## Documentation

Reference material that complements the skills:

- 📝 **[Prompt Library](./docs/PROMPTS.md)** — ready-to-use prompts that reliably trigger each of the 34 skills
- 📖 **[Security Glossary](./docs/GLOSSARY.md)** — definitions of terms used across the skills (BOLA, mTLS, RPO/RTO, slopsquatting, ...)
- ❓ **[FAQ](./docs/FAQ.md)** — installation, compatibility, contribution flow, commercial use

## Compatibility

Skills use plain Markdown with YAML frontmatter (`name`, `description`). Tested target is **Claude Code**; the same files work with any LLM coding agent that supports the convention — including Cursor, GitHub Copilot, Codex CLI, Cline, Continue.dev, and Gemini CLI. Nothing in the body is platform-specific.

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
├── docs/
│   ├── README.md
│   ├── PROMPTS.md
│   ├── GLOSSARY.md
│   └── FAQ.md
│
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── index.json
├── LICENSE
├── README.md
└── SECURITY.md
```

Every skill is a self-contained `SKILL.md` with YAML frontmatter (`name`, `description`) plus a body that follows roughly: *when to invoke → detection / steps / patterns → checklist → what this skill will not do*.

</details>

## Skills by category

Each link goes to the full `SKILL.md` with detection commands, step-by-step procedures, and checklists.

### 🤖 AI & LLM security

| Skill | Summary |
|---|---|
| [`mcp-security`](./mcp-security/SKILL.md) | Audit MCP configurations, risk-tier capabilities, detect malicious servers, apply least-privilege scoping. |
| [`ai-agent-guardrails`](./ai-agent-guardrails/SKILL.md) | Blast-radius classification, dry-run-first, out-of-band approval gates, kill switches. |
| [`prompt-injection-defense`](./prompt-injection-defense/SKILL.md) | Source-of-trust tagging, tool-use confirmation after untrusted input, exfiltration prevention. |
| [`llm-app-security`](./llm-app-security/SKILL.md) | OWASP LLM Top 10 mapped to practical controls — rate limits, cost caps, PII scrubbing, audit logging. |
| [`llm-coding-failure-modes`](./llm-coding-failure-modes/SKILL.md) | Antipattern catalog for LLM coding agents — bulk ops, bypassed guards, slopsquatting, sycophancy. |

### 🌐 Web application

| Skill | Summary |
|---|---|
| [`wordpress-hardening`](./wordpress-hardening/SKILL.md) | Detect WordPress webshells and harden against re-compromise on shared hosting. |
| [`nextjs-security`](./nextjs-security/SKILL.md) | Next.js-specific issues — middleware bypass, RSC over-fetch, `NEXT_PUBLIC_` traps, CSP, `next/image` SSRF. |
| [`payload-cms-security`](./payload-cms-security/SKILL.md) | Access control, file uploads, GraphQL surface, and multi-tenant isolation in Payload CMS. |
| [`api-security`](./api-security/SKILL.md) | OWASP API Top 10 — BOLA, mass assignment, excessive data exposure, GraphQL depth limits. |
| [`file-upload-security`](./file-upload-security/SKILL.md) | Accept uploads safely — magic-byte validation, polyglot defense, separate-origin serving with `Content-Disposition`. |
| [`stripe-webhook-security`](./stripe-webhook-security/SKILL.md) | Raw-body signature verification, idempotency, replay protection, currency-mismatch traps. |
| [`site-server-audit`](./site-server-audit/SKILL.md) | Non-intrusive checklist for DNS, TLS, security headers, exposed paths, and cookies. |

### 🏗️ Server & infrastructure

| Skill | Summary |
|---|---|
| [`vps-hardening`](./vps-hardening/SKILL.md) | 30-minute Debian / Ubuntu baseline — SSH key-only, UFW, fail2ban, unattended-upgrades. |
| [`cloudflare-hardening`](./cloudflare-hardening/SKILL.md) | Origin-IP protection, WAF, Rate Limiting, Zero Trust Access, Transform Rules for headers. |
| [`postgres-hardening`](./postgres-hardening/SKILL.md) | `pg_hba`, role separation, row-level security, TLS, encrypted backups, `pg_audit`. |
| [`docker-container-security`](./docker-container-security/SKILL.md) | Non-root users, read-only filesystems, dropped capabilities, image scanning, the UFW-bypass trap. |
| [`kubernetes-security`](./kubernetes-security/SKILL.md) | Pod Security Standards, RBAC least-privilege, NetworkPolicy default-deny, admission controllers. |

### 🛰 Distributed systems

| Skill | Summary |
|---|---|
| [`distributed-system-audit`](./distributed-system-audit/SKILL.md) | Map first, judge later — trust boundaries, protocol audit (replay / ordering / forgery), failure-mode walk. |
| [`agent-client-security`](./agent-client-security/SKILL.md) | Native agents on customer machines — installer signing, OTA with rollback, mTLS, anti-tampering signals. |
| [`message-bus-security`](./message-bus-security/SKILL.md) | NATS / RabbitMQ / Kafka — tenant isolation, deny-default permissions, replay protection, consumer idempotency. |

### 🎯 Architecture & reliability

| Skill | Summary |
|---|---|
| [`backend-architecture`](./backend-architecture/SKILL.md) | Stateless apps, state in the right places, twelve-factor — survive redeploys, scaling, server reboots. |
| [`backup-disaster-recovery`](./backup-disaster-recovery/SKILL.md) | RPO / RTO, 3-2-1, encrypted off-host backups, ransomware-resistant immutable storage, restore drills. |

### 🔎 Audit & review

| Skill | Summary |
|---|---|
| [`codebase-audit`](./codebase-audit/SKILL.md) | Methodology for inherited codebases — triage, SAST / SCA recipes, OWASP grep patterns, severity-classed report. |

### 🔐 Identity & access

| Skill | Summary |
|---|---|
| [`auth-hardening`](./auth-hardening/SKILL.md) | NIST 800-63B passphrases, Argon2id, MFA tiers, no-enumeration lockout, password reset done right. |
| [`secret-hygiene`](./secret-hygiene/SKILL.md) | Find leaked secrets, rotate in the right order, optionally purge git history with `git-filter-repo`. |

### 📦 Supply chain & CI/CD

| Skill | Summary |
|---|---|
| [`dependency-supply-chain`](./dependency-supply-chain/SKILL.md) | Lockfile hygiene, behavior-level scanning, postinstall review, typosquat and slopsquat defense. |
| [`github-actions-security`](./github-actions-security/SKILL.md) | SHA-pinned actions, scoped `GITHUB_TOKEN`, OIDC in place of long-lived cloud secrets. |

### 📋 Compliance (EU / DACH)

| Skill | Summary |
|---|---|
| [`gdpr-technical-controls`](./gdpr-technical-controls/SKILL.md) | Data inventory, SAR and deletion endpoints, log scrubbing, 72-hour breach notification. |
| [`dach-compliance`](./dach-compliance/SKILL.md) | Impressum, Datenschutzerklärung, AGB, AVV / DPA, TOMs, cookie consent for Germany / Austria / Switzerland. |

### 🔍 Detection & monitoring

| Skill | Summary |
|---|---|
| [`log-strategy`](./log-strategy/SKILL.md) | What to log and what never to log — operational vs access vs audit, retention tiers, alert routing. |
| [`honeypot-tarpits`](./honeypot-tarpits/SKILL.md) | Fake admin paths, canary tokens, decoy `.env` files — high-signal detection without a SIEM. |

### 🛡️ Incident response

| Skill | Summary |
|---|---|
| [`incident-response`](./incident-response/SKILL.md) | SANS PICERL runbook for small teams, with a post-mortem template. |

### 📨 Email security

| Skill | Summary |
|---|---|
| [`email-deliverability-security`](./email-deliverability-security/SKILL.md) | SPF / DKIM / DMARC with the `p=none → p=quarantine → p=reject` migration path. |

### 📱 Mobile security

| Skill | Summary |
|---|---|
| [`ios-security`](./ios-security/SKILL.md) | Keychain accessibility tiers, ATS, certificate pinning, file protection, jailbreak detection as signal. |

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

Drop the directory in a path Claude Code scans for skills, or reference the skills directly. Claude matches the YAML `description` against your request and loads the matching `SKILL.md`. If you prefer to work without auto-triggering, just `cat` the relevant `SKILL.md` and follow it manually.

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
