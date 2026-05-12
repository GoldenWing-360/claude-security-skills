<!--
Thanks for the contribution. Before merging, please confirm the checklist below.
For first-time contributors: read CONTRIBUTING.md once — it covers what fits and what doesn't.
-->

## What this PR changes

<!-- One or two sentences. New skill / edit to existing skill / fix / etc. -->

## Type of change

- [ ] New skill (adds a `<name>/SKILL.md` directory)
- [ ] Update to existing skill (content correction or addition)
- [ ] Documentation / README / contributing-process
- [ ] Translation
- [ ] Fix (typo, broken link, etc.)

## Related issue

<!-- "Closes #NN" or "Refs #NN". For new skills, link to the proposal issue. -->

## Checklist

**For all PRs:**

- [ ] I read [CONTRIBUTING.md](../CONTRIBUTING.md)
- [ ] No real credentials, IPs, customer-identifying data, or provider-shaped strings (e.g. `sk_live_<24chars>`, `AKIA<16chars>`) in the diff
- [ ] Defensive content only — no offensive tradecraft, no exploitation steps
- [ ] If I used an LLM to draft this, I have personally reviewed and edited every paragraph

**For a new skill:**

- [ ] YAML frontmatter has `name` and `description`; description reads as triggers, not marketing
- [ ] "When to invoke" section present
- [ ] "What this skill will not do" section present at the end
- [ ] Length ≥ 4KB (substantive) and ≤ ~12KB (readable)
- [ ] Added to `README.md` in the appropriate category table
- [ ] Added to "Common scenarios" Q&A in README if applicable
- [ ] Cross-links to related skills with `[name](../other-skill/SKILL.md)` where natural

**Sanity check** (run before pushing):

```bash
! grep -rEn '(sk_live_[A-Za-z0-9]{24,}|sk_test_[A-Za-z0-9]{24,}|AKIA[A-Z0-9]{16}|ghp_[A-Za-z0-9]{36})' . && echo OK
```

## Anything reviewers should know

<!-- Tradeoffs, open questions, places where you want a second opinion -->
