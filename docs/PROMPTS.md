# Prompt Library — Claude Code Security Skills

Ready-to-use prompts that reliably trigger each skill in Claude Code (and any compatible agent). Phrased the way you would naturally describe the situation — not as keywords.

Copy a prompt, paste it into your agent, and the matching `SKILL.md` will load automatically because its YAML `description` matches the trigger surface.

Prompts work in any language the model speaks. English versions below; German variants follow the same shape — agents match on semantics, not exact wording.

---

## 🤖 AI & LLM security

### `mcp-security`
- "I'm about to install a new MCP server that talks to Stripe. Walk me through what to check before granting it write access."
- "Audit my Claude Code MCP configuration — what's risky, what should I rotate, what should I remove?"
- "A contractor is leaving the team. Which MCP tokens should I revoke and how?"

### `ai-agent-guardrails`
- "I'm building an agent that can deploy to production. What guardrails do I need before giving it write access?"
- "My Claude Code agent just made bulk edits across 30 WordPress sites and broke them all. How do I prevent this next time?"
- "Design an approval-gate pattern for an agent that issues refunds in Stripe."

### `prompt-injection-defense`
- "I'm building a customer-support agent that reads inbound emails and can reply. How do I prevent injection attacks?"
- "My RAG system summarizes user-uploaded documents. What should I worry about, and how do I contain it?"
- "Review this LLM-app design for prompt-injection risk: agent fetches a URL, summarizes it, then can send email."

### `llm-app-security`
- "We're about to launch an AI chat feature to public traffic. What operational controls do I need?"
- "A user is complaining that our AI gave them legally wrong advice. Walk me through the AI-incident response."
- "I want to implement the OWASP LLM Top 10 in our app. Where do I start?"

### `llm-coding-failure-modes`
- "Review this PR — it was mostly written by Claude. What recurring LLM mistakes should I look for?"
- "We had an incident where the agent disabled CSRF 'temporarily' and it stayed off for months. What pattern is this and how do I prevent it?"
- "Onboard our team to vibe-coding safely. What's the antipattern catalog?"

### `rag-security`
- "Our RAG chatbot indexes the whole company wiki. Users are seeing content from documents they don't have access to. Fix the design."
- "We let customers upload documents into a shared knowledge base for our AI assistant. What can go wrong and how do I contain it?"
- "Review our vector-database setup for tenant isolation — one Pinecone index, all customers, metadata filter per query."

---

## 🌐 Web application

### `wordpress-hardening`
- "My customer's WordPress site has weird `.php` files in `wp-content/uploads/`. Help me figure out what to do."
- "I just took over hosting for a client with 12 WordPress sites on shared hosting. Walk me through hardening them."
- "There's a `wp-info.php` file in the docroot I don't recognize. What is it and how should I respond?"

### `nextjs-security`
- "I'm upgrading from Next.js 14 to 15. What security-relevant changes should I review?"
- "Audit my Next.js app for the middleware-bypass class of vulnerability."
- "I'm adding Server Actions for the first time. What do I need to validate beyond the function arguments?"

### `payload-cms-security`
- "I'm shipping a Payload CMS app to production. Walk me through the access-control review."
- "Help me design multi-tenant isolation in Payload — one instance, many customer organizations."
- "Audit the file-upload flow in this Payload collection — is it safe to accept PDFs from end users?"

### `api-security`
- "Review my REST API for BOLA — every endpoint that takes an ID."
- "We're building a public GraphQL API. What rate-limiting and query-complexity controls do I need?"
- "A user reports they can see another user's invoices by changing the ID in the URL. Triage."

### `file-upload-security`
- "I'm adding image uploads to my Next.js app. How do I do this safely without becoming a malware-hosting platform?"
- "Audit our file-upload endpoint — magic-byte validation, virus scanning, storage, serving. The works."
- "We accept user-uploaded PDFs and SVGs. What's the threat model and how do I defang them?"

### `stripe-webhook-security`
- "Wire a new Stripe webhook handler. Cover signature verification, idempotency, and the edge cases."
- "We had a customer get double-charged after a webhook retry. What went wrong and how do I prevent it?"
- "Help me add a new event type (`charge.dispute.created`) to our existing webhook handler without breaking it."

### `site-server-audit`
- "I'm onboarding a new client site to our Cloudflare. Run a non-intrusive audit first."
- "Audit this public site: TLS, security headers, exposed paths, DNS hygiene."
- "Pre-launch checklist for the marketing site we're about to push live."

---

## 🏗️ Server & infrastructure

### `vps-hardening`
- "I just provisioned a new Ubuntu VPS. Walk me through the 30-minute baseline hardening."
- "I inherited a Debian server from a contractor with no documentation. Audit what's there before I add anything."
- "Set up fail2ban with a `wp-login` jail and tune unattended-upgrades."

### `cloudflare-hardening`
- "We're putting goldenwing.at behind Cloudflare for the first time. What should I configure beyond the orange cloud?"
- "Our origin IP just leaked via a misconfigured DNS record. How do I rotate it and prevent the next leak?"
- "Set up Authenticated Origin Pulls plus a Cloudflare-only firewall on the origin."

### `postgres-hardening`
- "I'm provisioning a new managed Postgres for a multi-tenant SaaS. What do I configure?"
- "Audit my `pg_hba.conf` — is it too permissive?"
- "Help me add row-level security to the `invoices` table so tenant A can't see tenant B's rows."

### `docker-container-security`
- "Review this Dockerfile for production readiness — non-root user, capabilities, image size."
- "Why is my container reachable from the internet even though UFW blocks the port? (it's the Docker UFW-bypass trap)"
- "Set up image scanning in our CI before any image gets pushed to the registry."

### `kubernetes-security`
- "I inherited a Kubernetes cluster. Audit it for the common findings."
- "Roll out Pod Security Standards `restricted` mode across all app namespaces. What breaks?"
- "Set up NetworkPolicy default-deny in our production namespace."

### `dns-domain-security`
- "We decommissioned a bunch of services last year. Audit our DNS zone for dangling records before someone takes over a subdomain."
- "Lock down our domain portfolio — registrar security, transfer locks, CAA, expiry monitoring. What's the checklist?"
- "A certificate showed up in CT logs for one of our subdomains that we never issued. What happened and what do I do?"

### `object-storage-security`
- "Audit our S3 buckets — I want to know nothing is public that shouldn't be and our IAM policies aren't over-scoped."
- "We serve user uploads straight from our R2 bucket. Design presigned upload and download flows that don't leak the whole bucket."
- "Make our backups bucket ransomware-resistant — versioning, object lock, separate credentials."

---

## 🛰 Distributed systems

### `distributed-system-audit`
- "I'm doing security due-diligence on a SaaS we might acquire. They have a fleet of customer-installed agents talking to a central server. Where do I start?"
- "Audit our multi-region microservices architecture. Focus on what happens at trust boundaries."
- "We had a heartbeat-collision incident across agents. What's the audit pattern that would have caught this?"

### `agent-client-security`
- "I'm shipping a monitoring agent that runs on customer Macs. What should I do for installer signing, updates, and credentials?"
- "Audit our RMM client — installer, OTA channel, mTLS, anti-tampering. Where are the gaps?"
- "Design the bootstrap-token + cert-rotation flow for a new fleet of native agents."

### `message-bus-security`
- "We just added NATS to our stack. Walk me through the JWT-account-subject setup for multi-tenancy."
- "Audit our RabbitMQ — vhost isolation, user permissions, TLS. Look for anything broad."
- "Set up replay protection and consumer-side idempotency for our command bus."

---

## 🎯 Architecture & reliability

### `backend-architecture`
- "Why do user uploads disappear every time we redeploy?"
- "I want to scale from one server to two. What breaks?"
- "Walk me through productionizing this Claude-generated prototype before our pilot customer goes live next week."

### `backup-disaster-recovery`
- "We have backups, but I'm not sure anyone has ever restored them. Audit the strategy."
- "Set up encrypted, off-provider, ransomware-resistant backups for our Postgres."
- "Design a quarterly restore-drill that I can actually run without a full day's effort."

---

## 🔎 Audit & review

### `codebase-audit`
- "A new client is paying me to audit their codebase. I have one week. Walk me through the methodology."
- "I just joined a company. The codebase is huge and undocumented. Help me build a mental model in the first 30 minutes."
- "Review this AI-generated codebase before we ship it to production. What's the systematic approach?"

---

## 🔐 Identity & access

### `auth-hardening`
- "We're seeing a credential-stuffing wave. What's the right response — lockout? CAPTCHA? Both?"
- "Help me design the password-reset flow correctly. Single-use token, invalidation on use, etc."
- "Plan the MFA rollout for our SaaS — staff first, then customers. What factors and how do I avoid SMS?"

### `secret-hygiene`
- "I just committed `.env` to a public repo. What do I do now, in what order?"
- "A contractor is offboarding. Walk me through every credential they could have seen and the rotation order."
- "Set up pre-commit hooks across our dev team so this doesn't happen again."

---

## 📦 Supply chain & CI/CD

### `dependency-supply-chain`
- "There's an npm typosquat advisory affecting `colours-js`. Was our project affected, and what's the cleanup?"
- "Review the new dependency we want to add. Single maintainer, sketchy package name. Is it safe?"
- "Set up socket.dev in our PR workflow so new dependencies get behavior-level scanned."

### `github-actions-security`
- "Audit our GitHub Actions workflows — pinned actions, scoped tokens, OIDC. Where are the gaps?"
- "Migrate from long-lived AWS keys in secrets to OIDC. Walk me through the IAM-role setup."
- "We added `pull_request_target` to a workflow and now I'm worried. Should I be?"

---

## 📋 Compliance (EU / DACH)

### `gdpr-technical-controls`
- "Help me build the data-inventory for our GDPR documentation."
- "Implement the SAR endpoint — programmatic, time-limited download, authenticated."
- "We had a personal-data breach yesterday afternoon. What's the 72-hour timeline and who do I notify?"

### `dach-compliance`
- "We're launching a site for an Austrian customer. What pages do I need beyond Impressum?"
- "Review our Datenschutzerklärung against what the site actually does — what's missing or stale?"
- "Our cookie banner sets analytics cookies before consent. Help me fix the flow."

---

## 🔍 Detection & monitoring

### `log-strategy`
- "We just started logging and our cost ballooned. Help me design retention tiers and what to drop."
- "Investigation revealed we don't log who exported the customer database. Design the audit-log schema."
- "Help me set up centralized logging without leaking PII into Datadog."

### `honeypot-tarpits`
- "I want to detect scanners hitting our site, but I don't want to pay for a SIEM. What's the minimum viable setup?"
- "Set up fake admin paths plus a canary `.env` file plus fail2ban that bans on hit."
- "We're worried someone scraped our JS bundle. Help me plant a canary API key so we'd find out."

---

## 🛡️ Incident response

### `incident-response`
- "A customer just reported their WordPress site is redirecting to a casino. Walk me through the runbook."
- "We found a webshell on one of our servers. What's the order of operations — and what do I NOT do first?"
- "Write a post-mortem for the credential-leak incident we resolved yesterday."

---

## 📨 Email security

### `email-deliverability-security`
- "Our transactional emails are landing in spam. Help me diagnose and fix SPF / DKIM / DMARC."
- "Set up DMARC for a new sending domain. Plan the migration from `p=none` to `p=reject`."
- "Domains under our brand are being spoofed in phishing emails to our customers. What can we do at the DNS layer?"

---

## 📱 Mobile security

### `ios-security`
- "I'm shipping an iOS app that stores OAuth refresh tokens. What's the right Keychain configuration?"
- "Pre-App-Store-submission security review for our app — Keychain, ATS, third-party SDKs, privacy strings."
- "Add certificate pinning to our app. What are the tradeoffs and how do I avoid bricking on cert rotation?"

### `android-security`
- "I'm shipping an Android app that stores OAuth refresh tokens. Keystore, EncryptedSharedPreferences, or what?"
- "Pre-Play-Store security review for our app — exported components, backup rules, WebView settings, third-party SDKs."
- "Our Android app has a WebView with a JavaScript bridge. Harden it."

---

## Multi-skill scenarios

Some situations naturally cross several skills. The agent will load multiple SKILL.md files when the prompt warrants it:

- **WordPress site compromised on shared hosting** → invokes [`incident-response`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/incident-response/SKILL.md) + [`wordpress-hardening`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/wordpress-hardening/SKILL.md) + [`secret-hygiene`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/secret-hygiene/SKILL.md). Try: *"I think one of my customer's WordPress sites was compromised — there are unfamiliar admin accounts. Walk me through the full response and cleanup."*

- **Launching an LLM-powered feature to public traffic** → [`prompt-injection-defense`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/prompt-injection-defense/SKILL.md) + [`llm-app-security`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/llm-app-security/SKILL.md) + [`ai-agent-guardrails`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/ai-agent-guardrails/SKILL.md). Try: *"We're shipping a customer-support AI chatbot next week. Walk me through the full security review — injection defense, operational controls, agent design."*

- **Auditing a distributed-agent product** → [`distributed-system-audit`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/distributed-system-audit/SKILL.md) + [`agent-client-security`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/agent-client-security/SKILL.md) + [`message-bus-security`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/message-bus-security/SKILL.md) + [`kubernetes-security`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/kubernetes-security/SKILL.md) (if applicable) + [`codebase-audit`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/codebase-audit/SKILL.md). Try: *"I'm auditing a SaaS with a Kubernetes control plane, NATS message bus, and native agents on customer machines. Where do I start?"*

---

Maintained by [GoldenWing](https://goldenwing.at) — defensive-security audits and incident response for small teams. · [Main repository](https://github.com/GoldenWing-360/claude-security-skills) · [FAQ](./FAQ.md) · [Glossary](./GLOSSARY.md)
