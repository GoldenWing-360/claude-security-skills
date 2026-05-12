# Claude Code Security Skills

> Production-tested defensive security skills for [Claude Code](https://claude.com/claude-code) — checklists, playbooks, and hardening guides for WordPress, VPS servers, Cloudflare, Next.js, AI agents, MCP servers, and incident response. Battle-tested on real compromises, generalized for everyone.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-25-blue.svg)](#skills-by-category)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-purple.svg)](https://claude.com/claude-code)
[![Made by GoldenWing](https://img.shields.io/badge/made%20by-goldenwing.at-orange.svg)](https://goldenwing.at)

**25 self-contained `SKILL.md` files** covering everything from "how do I detect a webshell on WordPress" to "how do I harden an AI agent that can write to production". Each skill is a single Markdown file with YAML frontmatter — Claude Code auto-triggers them on relevant requests, but they are equally usable as plain runbooks for humans.

## Table of contents

- [Who this is for](#who-this-is-for)
- [Quick start](#quick-start)
- [Skills by category](#skills-by-category)
  - [AI & LLM security](#-ai--llm-security-the-2026-attack-surface)
  - [Web application security](#-web-application-security)
  - [Server & infrastructure](#-server--infrastructure)
  - [Identity & access](#-identity--access)
  - [Supply chain & CI/CD](#-supply-chain--cicd)
  - [Compliance (EU / DACH)](#-compliance-eu--dach)
  - [Detection & monitoring](#-detection--monitoring)
  - [Incident response](#-incident-response--secret-hygiene)
  - [Mobile security](#-mobile-security)
- [Common scenarios — find the right skill fast](#common-scenarios--find-the-right-skill-fast)
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
| [`payload-cms-security`](./payload-cms-security/SKILL.md) | Shipping Payload CMS to production, opening admin to non-developers, after a Payload version upgrade. Covers collection/field-level access control, hook safety, file uploads, GraphQL/REST surface, multi-tenant isolation. |
| [`site-server-audit`](./site-server-audit/SKILL.md) | Onboarding a new client site, before launch, after infra changes, periodic re-audit. Read-only checklist: DNS, TLS/HSTS, security headers, exposed paths (`.git`, `.env`, backups), cookies, software fingerprint. |

### 🏗️ Server & infrastructure

| Skill | Use when |
|---|---|
| [`vps-hardening`](./vps-hardening/SKILL.md) | Provisioning a new Debian/Ubuntu VPS, inheriting an existing one, before exposing a service to the public internet. 30-minute baseline: SSH key-only, UFW, fail2ban, unattended-upgrades, kernel sysctls, journalctl. Includes monthly audit script. |
| [`cloudflare-hardening`](./cloudflare-hardening/SKILL.md) | Onboarding a domain to Cloudflare, when origin IP may be exposed, after an attack. Covers account hardening, Authenticated Origin Pulls, WAF Managed Rules, Bot Fight, Rate Limiting, Transform Rules for headers, Zero Trust Access for admin paths, R2 / Pages security. |
| [`postgres-hardening`](./postgres-hardening/SKILL.md) | Provisioning a new PostgreSQL deployment, before opening it to a new app, after an advisory, or reviewing a multi-tenant schema. Covers `pg_hba.conf`, role separation, row-level security, backup encryption, pg_audit, version upgrades. |
| [`docker-container-security`](./docker-container-security/SKILL.md) | Adding Docker to a VPS with UFW (and hitting the bypass surprise), writing a new Dockerfile, pushing to a public registry, periodic audit. Covers non-root users, read-only FS, dropped capabilities, secret mounts, trivy scanning, distroless bases. |

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

## Common scenarios — find the right skill fast

These are written as the questions people actually type into a search bar.

### "Help, my WordPress site got hacked"
→ Start with [`incident-response`](./incident-response/SKILL.md) for the runbook, then [`wordpress-hardening`](./wordpress-hardening/SKILL.md) for WordPress-specific detection (webshells, malicious mu-plugins, injected admins). If multiple sites are on the same shared host, assume lateral movement and audit every sub.

### "How do I detect a webshell on WordPress?"
→ [`wordpress-hardening`](./wordpress-hardening/SKILL.md) — includes detection commands for the Sid Gifari, WSO, FilesMan, b374k, and c99 webshell families, plus file-system and database indicators.

### "I committed a `.env` to a public repo, what now?"
→ [`secret-hygiene`](./secret-hygiene/SKILL.md) — covers rotation order (rotate first, purge second), `git-filter-repo` to scrub history, and prevention via pre-commit scanning.

### "How do I prevent prompt injection in my LLM app?"
→ [`prompt-injection-defense`](./prompt-injection-defense/SKILL.md) — the "untrusted-since-confirm" pattern is the single highest-leverage defense for agent systems.

### "What are the most common security mistakes Claude / GPT / Copilot make in code?"
→ [`llm-coding-failure-modes`](./llm-coding-failure-modes/SKILL.md) — the antipattern catalog. Top 10 plus 5 honorable mentions, with detection patterns for code reviewers and mitigations for agent designers.

### "How do I review LLM-generated code for security issues?"
→ [`llm-coding-failure-modes`](./llm-coding-failure-modes/SKILL.md) — walks the recurring failure modes (slopsquatting, hallucinated APIs, bypassed safety guards, silent error swallowing, sycophancy) with what to look for in the diff.

### "How do I safely give an AI agent write access to production?"
→ [`ai-agent-guardrails`](./ai-agent-guardrails/SKILL.md) — blast-radius classification, dry-run-first, out-of-band approval gates, kill switches. Pairs with [`mcp-security`](./mcp-security/SKILL.md) for the MCP-server side.

### "How do I harden a new Ubuntu VPS in 30 minutes?"
→ [`vps-hardening`](./vps-hardening/SKILL.md) — step-by-step from "I just SSH'd in as root" to "SSH is key-only, UFW is up, fail2ban running, unattended-upgrades on".

### "My Cloudflare site got attacked, how do I lock it down?"
→ [`cloudflare-hardening`](./cloudflare-hardening/SKILL.md) — WAF rules, Bot Fight, Rate Limiting, Authenticated Origin Pulls so attackers cannot bypass the proxy by hitting your origin IP directly.

### "How do I hide my origin IP behind Cloudflare?"
→ [`cloudflare-hardening`](./cloudflare-hardening/SKILL.md) — common leak vectors (MX, leftover A records, SPF IP literals) plus origin-IP rotation and Cloudflare-IPs-only firewall rule.

### "How do I secure a Stripe webhook?"
→ [`stripe-webhook-security`](./stripe-webhook-security/SKILL.md) — signature verification, idempotency, replay protection, the double-charge traps.

### "What's the OWASP LLM Top 10 and how do I implement it?"
→ [`llm-app-security`](./llm-app-security/SKILL.md) — each item mapped to a practical control.

### "How do I scope a GitHub PAT / move from long-lived cloud secrets to OIDC?"
→ [`github-actions-security`](./github-actions-security/SKILL.md) — SHA-pinned actions, scoped `GITHUB_TOKEN`, OIDC for AWS / GCP / Cloudflare.

### "Do I really need a German Impressum and what's a TOM?"
→ [`dach-compliance`](./dach-compliance/SKILL.md) — Impressum content per TMG/MStV/ECG, AVV, technical-organizational measures, cookie consent that matches German + Austrian + Swiss law.

### "How do I block brute force on `/wp-login.php`?"
→ Combine [`wordpress-hardening`](./wordpress-hardening/SKILL.md) (mu-plugin defense), [`vps-hardening`](./vps-hardening/SKILL.md) (fail2ban with a `wp-login` jail), and [`cloudflare-hardening`](./cloudflare-hardening/SKILL.md) (Rate Limiting + Zero Trust Access in front of `/wp-admin`).

### "How do I write a post-mortem after a breach?"
→ [`incident-response`](./incident-response/SKILL.md) — includes a post-mortem template (timeline, impact, root cause, contributing factors, action items, IOCs).

### "How do I configure SPF / DKIM / DMARC properly?"
→ [`email-deliverability-security`](./email-deliverability-security/SKILL.md) — and the `p=none` → `p=quarantine` → `p=reject` migration path that doesn't break legitimate mail.

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

[MIT](./LICENSE) — use freely in your own projects, agencies, and trainings.

## Background

Built and maintained by [**GoldenWing**](https://goldenwing.at) ([GitHub: GoldenWing-360](https://github.com/GoldenWing-360)) — a Vienna-based studio working at the intersection of web engineering, AI integration, and infrastructure security. The patterns here are distilled from real cleanup, hardening, and incident-response work — particularly across small-business WordPress sites on shared hosting, Cloudflare-fronted VPS infrastructure, and LLM-powered applications. Specific incident details and indicators of compromise have been generalized so the guidance is portable.

Need help applying any of this to your own systems? → [goldenwing.at](https://goldenwing.at)

If a skill saved you time or helped during an incident, a GitHub star helps others find this. Issues and PRs welcome.

---

**Keywords**: Claude Code skills, Claude Code security, defensive security, AI security, LLM security, MCP server security, prompt injection defense, OWASP LLM Top 10, LLM coding antipatterns, vibe coding security, slopsquatting, AI agent guardrails, WordPress security checklist, webshell detection, VPS hardening guide, Cloudflare WAF setup, Next.js security, Stripe webhook security, Postgres hardening, Docker security, secret rotation, git history purge, incident response playbook, GDPR technical controls, DACH Impressum, GitHub Actions OIDC, SPF DKIM DMARC, iOS Keychain.
