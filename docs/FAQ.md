# Frequently Asked Questions — Claude Code Security Skills

Common questions about installing, using, and contributing to the [Claude Code Security Skills](https://github.com/GoldenWing-360/claude-security-skills) library. Click any question to expand.

<details>
<summary><strong>How do I install these skills in Claude Code?</strong></summary>

Drop the repo into a path Claude Code scans for skills:

```bash
git clone https://github.com/GoldenWing-360/claude-security-skills.git ~/.claude/skills/security-skills
```

Or, in a project: clone the repo as a sibling and reference its skills directly. Claude Code matches the YAML `description` of each `SKILL.md` against your conversation and loads the relevant one.

</details>

<details>
<summary><strong>Do I need Claude Code specifically, or do other agents work?</strong></summary>

No, you don't need Claude Code specifically. The skills are plain Markdown with YAML frontmatter (`name`, `description`). They work with any LLM coding agent that supports the same convention — **Cursor**, **GitHub Copilot**, **OpenAI Codex CLI**, **Cline**, **Continue.dev**, **Gemini CLI**, and others.

You can also read any `SKILL.md` as a runbook without any agent involvement — they're written to be useful for humans too.

</details>

<details>
<summary><strong>How do the trigger words / skill discovery work?</strong></summary>

Each `SKILL.md` has a YAML `description` field that doubles as the agent's discovery surface. When your conversation matches the description semantically, the agent loads that skill into context.

The descriptions in this repo follow a deliberate 3-sentence pattern:

1. **What** the skill does
2. **Covers** — the topics inside
3. **Invoke when** — concrete triggering situations

The "Invoke when" sentence is where most of the discoverability lives. See the [Prompt Library](./PROMPTS.md) for examples that reliably trigger each of the 34 skills.

</details>

<details>
<summary><strong>Why is the repo named "Claude Code Security Skills" if it works with other agents?</strong></summary>

Pragmatic discovery. Claude Code is the largest LLM coding agent right now, and the `SKILL.md` YAML-frontmatter convention originates in Claude Code's design. The skills happen to also work elsewhere, but most users find them via the Claude Code naming.

The repo is explicitly **not affiliated with Anthropic PBC** — see the disclaimer in the [main README](https://github.com/GoldenWing-360/claude-security-skills).

</details>

<details>
<summary><strong>Why is there no offensive / red-team content?</strong></summary>

Defensive-only is an intentional positioning. Offensive tooling is well-served by other libraries. This repo focuses on the developer / agency / solo-operator who wants to *not get hacked* and *respond cleanly when they do*.

The patterns are distilled from real cleanup, hardening, and incident-response engagements — see the [maintainer's site at goldenwing.at](https://goldenwing.at) for the engagement side of that work. Every skill assumes the user has explicit authorization for the systems they work on.

</details>

<details>
<summary><strong>Why 34 skills and not 754?</strong></summary>

Different positioning. Larger libraries optimize for breadth — every Volatility3 plugin, every Sigma rule. This repo optimizes for **depth per skill**, distilled from real incident-response and hardening work. Each `SKILL.md` is 4–12KB of practitioner content, not a thin framework mapping.

If you need breadth, look at [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills). If you need a small set of well-tested defensive playbooks tuned for the vibe-coder era and small-team realities, this is it.

</details>

<details>
<summary><strong>Can I use these in commercial work?</strong></summary>

Yes. **MIT license.** Use in client engagements, training material, internal documentation, products. Attribution is appreciated — a link back from your own docs or a star on the repo helps others find this.

If you'd like hands-on help applying these patterns to your own systems, [GoldenWing](https://goldenwing.at) does that work directly.

</details>

<details>
<summary><strong>How do I contribute a new skill?</strong></summary>

Open an issue first (use the "New skill proposal" template) to confirm fit, then submit a PR. See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the format and style rules.

The roadmap of currently-wanted skills is listed in `CONTRIBUTING.md`. Translations to other languages are welcome, especially German.

</details>

<details>
<summary><strong>How do I report a security issue with the repo itself?</strong></summary>

`office@goldenwing.at` or via [private vulnerability reporting](https://github.com/GoldenWing-360/claude-security-skills/security/advisories/new). See [`SECURITY.md`](../SECURITY.md) for what counts.

The most common issue class is "a skill recommends an outdated or unsafe pattern" — those are valid and welcome security reports.

</details>

<details>
<summary><strong>The skill descriptions used to be longer. Why are they shorter now?</strong></summary>

Earlier descriptions were keyword-stuffed walls optimized purely for agent-discovery matching. They worked, but read poorly. The current 3-sentence pattern (what / covers / invoke when) reads naturally as prose, still triggers correctly in agents, and looks professional in the README's per-category tables.

If you find a description that fails to trigger a skill you expect, open an issue — better trigger surfaces are an ongoing improvement.

</details>

<details>
<summary><strong>Does this work in German, French, or other languages?</strong></summary>

The skills are written in English but agents are multilingual — German, French, Spanish, etc. prompts work fine. The agent matches semantics, not exact wording.

The maintainer also operates in German, and DACH-specific content is covered by the [`dach-compliance`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/dach-compliance/SKILL.md) and [`gdpr-technical-controls`](https://github.com/GoldenWing-360/claude-security-skills/blob/main/gdpr-technical-controls/SKILL.md) skills. Translations of the skill content itself are welcome contributions.

</details>

<details>
<summary><strong>What's the difference between <code>index.json</code> and the README's skill tables?</strong></summary>

- **README tables**: human-readable, organized by domain, with one-line summaries.
- **`index.json`**: programmatic — for agents, search UIs, or skill-discovery tooling. Contains slug, name, full description, domain, and path for each skill.

Use whichever fits your interface.

</details>

<details>
<summary><strong>Are there plans for an MCP server, CLI, or npm package?</strong></summary>

Possibly, depending on demand. For now the skills are static Markdown — drop them in, use them. If a CLI (`skills add ...` à la npm) or MCP server would solve a real problem for you, [open a discussion](https://github.com/GoldenWing-360/claude-security-skills/discussions).

</details>

<details>
<summary><strong>Who maintains this and where can I learn more about the engagements behind the patterns?</strong></summary>

Maintained by [**GoldenWing**](https://goldenwing.at) — a Vienna-based studio working on web engineering, AI integration, and infrastructure security. The skills here are distilled from real cleanup, hardening, and incident-response work across small-business WordPress sites on shared hosting, Cloudflare-fronted VPS infrastructure, and LLM-powered applications.

Specific incident details and indicators of compromise have been generalized so the guidance is portable.

</details>

---

Maintained by [GoldenWing](https://goldenwing.at) · [Main repository](https://github.com/GoldenWing-360/claude-security-skills) · [Prompt Library](./PROMPTS.md) · [Glossary](./GLOSSARY.md)
