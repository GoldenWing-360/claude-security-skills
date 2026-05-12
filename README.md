# claude-security-skills

A collection of **defensive-security skills** for [Claude Code](https://claude.com/claude-code), built from real incident-response and hardening work on small-team / shared-hosting environments.

Each skill is a single `SKILL.md` with YAML frontmatter (`name`, `description`) so Claude Code can auto-trigger them on relevant requests. The content is plain Markdown — you can also read them as runbooks without any tooling.

## What's in here

### 🌐 Web & hosting
| Skill | What it does |
|---|---|
| [`wordpress-hardening`](./wordpress-hardening/SKILL.md) | Detect webshells (Sid Gifari / WSO / FilesMan family) and backdoors, then harden WordPress against re-compromise. Tuned for shared-hosting environments where one dirty sub can pivot across the whole account. |
| [`site-server-audit`](./site-server-audit/SKILL.md) | Read-only, non-intrusive checklist for a public-facing site: DNS, TLS/HSTS, security headers, exposed paths (`.git`, `.env`, backups), cookies, software fingerprint, file-side hygiene. |
| [`nextjs-security`](./nextjs-security/SKILL.md) | Next.js-specific issues: middleware-bypass class, Server Actions hygiene, `NEXT_PUBLIC_` env leakage, RSC over-fetch, CSP, open redirects, `next/image` SSRF, runtime selection. |

### 🏗️ Infrastructure
| Skill | What it does |
|---|---|
| [`vps-hardening`](./vps-hardening/SKILL.md) | 30-minute baseline for Debian/Ubuntu VPS: SSH key-only, UFW, fail2ban, unattended-upgrades, sysctls, journalctl retention, sudo policy. Includes a monthly audit script. |
| [`cloudflare-hardening`](./cloudflare-hardening/SKILL.md) | Cloudflare account + zone hardening: API token scoping, origin-IP protection, Authenticated Origin Pulls, WAF/Bot/Rate-Limit baselines, Transform Rules for headers, Zero Trust for admin paths, R2 and Pages security. |

### 🛡️ Incident & hygiene
| Skill | What it does |
|---|---|
| [`incident-response`](./incident-response/SKILL.md) | SANS PICERL-style runbook: Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned. Designed for small teams and solo operators who do not have a dedicated IR firm on retainer. |
| [`secret-hygiene`](./secret-hygiene/SKILL.md) | Find leaked credentials in repos and on disk, rotate in the right order, optionally purge git history with `git-filter-repo`, and prevent recurrence with pre-commit scanning. |

### 🤖 AI-era security
| Skill | What it does |
|---|---|
| [`mcp-security`](./mcp-security/SKILL.md) | Audit and harden Model Context Protocol servers: inventory, risk-tiering (read-only → spend-money), secret-in-config detection, malicious-MCP indicators, least-privilege scoping, lifecycle. |
| [`ai-agent-guardrails`](./ai-agent-guardrails/SKILL.md) | Safety controls for LLM agents acting on real systems: blast-radius classification, dry-run-first, out-of-band approval gates, scope locking, idempotency, kill switches, rollback. |
| [`prompt-injection-defense`](./prompt-injection-defense/SKILL.md) | Containment patterns for direct and indirect injection: source-of-trust tagging, tool-use confirmation after untrusted input, output validation, exfiltration prevention (markdown image side-channel), context-window hygiene. |
| [`llm-app-security`](./llm-app-security/SKILL.md) | Operational controls for LLM-powered features: OWASP-LLM Top-10 mapping, rate limits + cost caps, PII scrubbing, audit logging, response moderation, model version pinning, AI-incident playbook. |

## Scope and intent

These skills are **defensive only**. They assume you have explicit authorization for the systems you are working on. They do not:

- Provide exploitation, post-exploitation, evasion, or "hack back" guidance
- Cover offensive red-team tradecraft, C2 frameworks, or malware development
- Help bypass authentication, security controls, or rate limits on systems you do not own

If you are doing authorized red-team or pentest work, these skills will help you on the *blue* side of that engagement — write the post-engagement hardening report, harden the systems you tested, run the post-incident remediation.

## Using with Claude Code

Drop the directory next to your project, or add it to a path Claude Code scans for skills. Once available, Claude will invoke the relevant skill when a request matches its `description` — for example:

- "Audit this site for misconfigurations" → `site-server-audit`
- "I found a strange `wp-info.php` file" → `wordpress-hardening`
- "We were just breached, what now" → `incident-response`
- "I committed a `.env` to a public repo" → `secret-hygiene`

You can also `cat` any `SKILL.md` and follow it manually.

## Contributing

Pull requests welcome, especially:

- Additional detection patterns you have seen in the wild
- Updated rotation procedures as providers change their APIs
- Translations (the original is English; the maintainer also operates in German)

Please keep contributions defensive in spirit and within the scope above.

## License

MIT — see [LICENSE](./LICENSE).

## Background

Built and maintained by [GoldenWing-360](https://github.com/GoldenWing-360). The patterns here are distilled from real cleanup and hardening work, particularly across small-business WordPress sites on shared hosting. Specific incident details and IOCs have been generalized so the guidance is portable.
