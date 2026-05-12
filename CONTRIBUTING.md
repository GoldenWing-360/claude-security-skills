# Contributing

Thanks for considering a contribution. This repo grows by people sharing what they actually learned from real defensive work. Drive-by additions of generic content do not help.

## What kind of contribution fits

Welcome:

- **A new SKILL.md** that covers a defensive area not yet here (see [open ideas](#ideas-on-the-roadmap))
- **A refinement to an existing skill** — new detection patterns observed in the wild, updated rotation procedures as providers change APIs, corrections of inaccuracies, sharper examples
- **Translations** — the original is English; German translations are particularly welcome
- **Issue reports** — broken commands, outdated advice, wrong product behavior

Out of scope:

- Offensive tradecraft, exploit code, payloads
- "AI wrote me this skill, please merge" — anything you submit must be reviewed and edited by you
- Generic copy-paste from OWASP / NIST without local synthesis or distinctive examples
- Affiliate / promotional content disguised as advice

## The bar for a new skill

Every existing skill follows roughly this shape. Match it for new submissions:

1. **YAML frontmatter** with `name` and `description`. The description is the matcher Claude Code uses to auto-invoke the skill — write it as a comma-delimited paragraph of trigger conditions, not as marketing copy.
2. **"When to invoke"** — bullet list of concrete situations
3. **The body** — adaptive per skill, but typically: detection / steps / patterns / common gotchas / quick checklist
4. **"What this skill will not do"** — explicit non-goals; defensive-only stance

Length: aim for 4–10KB. Long enough to be substantive, short enough to read through. If you have less than 4KB you probably do not have a full skill — submit it as an addition to an existing one.

## Style rules

- **Defensive only.** No offensive payloads, no exploitation steps, no detection-evasion advice. Same authorization assumption as the rest of the repo — the user has explicit permission for the systems they work on.
- **No real credentials, IPs, or customer data.** This repo is public. Anonymize indicators of compromise; describe patterns, not specific incidents. Watch out for provider-shaped strings (e.g. `sk_live_<24chars>`, `AKIA<16chars>`) — GitHub Push Protection will block them, and they may match active keys by accident.
- **No proprietary screenshots or trademarked names** without permission.
- **Code blocks are executable or near-executable.** Pseudo-code is fine; mixed real/pseudo without a label is not.
- **Cross-link** to other skills with `[name](../other-skill/SKILL.md)` where natural — the value of the repo is the network of skills, not isolated documents.
- **Tone:** opinionated, concrete, terse. Direct verbs, no marketing voice.

## How to submit

1. **Open an issue first** for a new skill — gives you a chance to confirm fit and avoid duplicate effort
2. **Branch from `main`**, create your skill in `your-skill-name/SKILL.md`
3. **Update `README.md`** — add the skill to the appropriate category table and at least one "Common scenarios" Q&A if applicable
4. **Run the sanity check** before pushing:

   ```bash
   # From repo root — should print "OK"
   ! grep -rEn '(sk_live_[A-Za-z0-9]{24,}|sk_test_[A-Za-z0-9]{24,}|AKIA[A-Z0-9]{16}|ghp_[A-Za-z0-9]{36})' . && echo OK
   ```

5. **Open a PR** referencing the issue. Fill in the PR template.

## Ideas on the roadmap

Areas where a contribution is currently most welcome:

- `kubernetes-security` — pod security standards, RBAC, network policies, secrets management
- `react-native-security` / `flutter-security` — the cross-platform mobile gap
- `terraform-security` / `iac-security` — drift, state secrets, plan-vs-apply approval
- `windows-server-hardening` — Linux gets the love; Windows still runs a lot of small business
- `mariadb-mysql-hardening` — sibling to `postgres-hardening`
- `redis-hardening` — common attack surface that gets default-config'd
- `cdn-security` (beyond Cloudflare) — Fastly, Bunny, KeyCDN
- `slack-bot-security` / `discord-bot-security` — bot scopes, message-content access, webhook protection
- `webhook-signing-patterns` (generalized from `stripe-webhook-security`) — for any provider, not just Stripe
- Translations of the existing English skills to German

If you want to take one of these, open an issue.

## Reviewing

Maintainer reviews focus on:

- Accuracy (is the advice actually correct in 2026?)
- Scope (defensive only, no IOCs)
- Fit (does this belong in this repo's category model?)
- Readability (would a tired developer at 5pm understand this?)

Reasonable PRs land within a week. We may suggest restructuring rather than nitpicking line-by-line — the goal is a coherent skill, not the original draft.

## Recognition

Contributors are listed in the repo's GitHub contributors view; significant skill authors are credited in the skill's frontmatter as a `maintainers` field where applicable.

## Questions

Open a discussion or issue, or reach the maintainers via [goldenwing.at](https://goldenwing.at).
