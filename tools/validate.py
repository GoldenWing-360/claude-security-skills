#!/usr/bin/env python3
"""Repository integrity validator for claude-security-skills.

Checks:
  1. Every <slug>/SKILL.md has YAML frontmatter with `name:` (matching slug)
     and a `description:` of reasonable length.
  2. index.json matches the SKILL.md files actually on disk.
  3. README skill-count claims match reality.
  4. Intra-repo markdown links resolve to existing files.

Exits 0 on success, 1 on any finding. Run from any working directory.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIN_DESCRIPTION_LEN = 80

findings: list[str] = []


def fail(msg: str) -> None:
    findings.append(msg)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Extract simple key: value YAML frontmatter (no nesting / lists)."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        end = text.find("\n---", 4)
        if end == -1:
            return None
    body = text[4:end]
    fm: dict[str, str] = {}
    for line in body.split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip()
    return fm


# 1. Walk skill directories
skill_dirs = sorted(
    d for d in ROOT.iterdir()
    if d.is_dir()
    and (d / "SKILL.md").exists()
    and not d.name.startswith(".")
)
slugs_on_disk = sorted(d.name for d in skill_dirs)

for skill_dir in skill_dirs:
    slug = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    content = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    if fm is None:
        fail(f"{slug}/SKILL.md: missing or malformed YAML frontmatter")
        continue
    if "name" not in fm:
        fail(f"{slug}/SKILL.md: frontmatter missing 'name:'")
    elif fm["name"] != slug:
        fail(
            f"{slug}/SKILL.md: frontmatter 'name: {fm['name']}' "
            f"does not match directory slug '{slug}'"
        )
    if "description" not in fm:
        fail(f"{slug}/SKILL.md: frontmatter missing 'description:'")
    elif len(fm["description"]) < MIN_DESCRIPTION_LEN:
        fail(
            f"{slug}/SKILL.md: description suspiciously short "
            f"({len(fm['description'])} chars, expected ≥ {MIN_DESCRIPTION_LEN})"
        )

# 2. index.json sync
index_path = ROOT / "index.json"
if not index_path.exists():
    fail("index.json: missing at repo root")
else:
    try:
        index = json.loads(index_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"index.json: not valid JSON ({exc})")
        index = {}

    if "skills" not in index:
        fail("index.json: missing 'skills' key")
    else:
        index_slugs = sorted(s["slug"] for s in index["skills"])
        missing = sorted(set(slugs_on_disk) - set(index_slugs))
        extra = sorted(set(index_slugs) - set(slugs_on_disk))
        if missing:
            fail(f"index.json: missing skills present on disk: {missing}")
        if extra:
            fail(f"index.json: lists skills not present on disk: {extra}")

        # Per-skill: name + description match SKILL.md frontmatter
        for entry in index["skills"]:
            slug = entry.get("slug")
            if not slug or slug not in slugs_on_disk:
                continue
            sm = parse_frontmatter((ROOT / slug / "SKILL.md").read_text(encoding="utf-8")) or {}
            if entry.get("name") != sm.get("name"):
                fail(f"index.json: '{slug}' name mismatch ({entry.get('name')!r} vs SKILL.md {sm.get('name')!r})")
            if entry.get("description") != sm.get("description"):
                fail(f"index.json: '{slug}' description differs from SKILL.md frontmatter")

    if index.get("skill_count") not in (None, len(slugs_on_disk)):
        fail(
            f"index.json: skill_count={index['skill_count']} but "
            f"{len(slugs_on_disk)} skills found on disk"
        )

# 3. README skill-count assertion
readme = (ROOT / "README.md").read_text(encoding="utf-8")
expected = len(slugs_on_disk)
# Patterns we authoritatively maintain:
#   "skills-NN-..." in shields badge
#   "**NN production-tested skills** ..." stat line
#   "Repository structure / NN skills + repo metadata"
authoritative = [
    rf"skills-{expected}-",                          # shields badge
    rf"\*\*{expected} production-tested skills\b",    # hero stat
    rf"<summary>{expected} skills",                   # repo-structure tree summary
    rf"### \w+ {expected} skills",                    # alternative section heading
]
# Any digit pattern that does NOT match expected and looks like an all-skills count
# We accept "5 skills", "6 skills" etc. as per-category counts in the inside table.
# Only flag claims of the totalskill_count specifically.
totals_phrases = re.findall(r"(\d+)\s+production-tested\s+skills?\b", readme, re.IGNORECASE)
for n in totals_phrases:
    if int(n) != expected:
        fail(f"README.md: claims '{n} production-tested skills' but {expected} exist")

# Shields badge skills-NN-...
badge_match = re.search(r"skills-(\d+)-", readme)
if badge_match and int(badge_match.group(1)) != expected:
    fail(f"README.md: shields badge claims {badge_match.group(1)} skills but {expected} exist")

# 4. Intra-repo link resolution
link_pattern = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
files_to_check: list[Path] = [
    ROOT / "README.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    ROOT / "CODE_OF_CONDUCT.md",
]
files_to_check += list((ROOT / "docs").glob("*.md")) if (ROOT / "docs").exists() else []
files_to_check += [d / "SKILL.md" for d in skill_dirs]

def strip_code_blocks(text: str) -> str:
    """Remove fenced code blocks and inline code so we don't lint example links."""
    # Fenced blocks (``` ... ``` or ~~~ ... ~~~)
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"~~~.*?~~~", "", text, flags=re.DOTALL)
    # Inline code spans (single backticks)
    text = re.sub(r"`[^`\n]+`", "", text)
    return text


for f in files_to_check:
    if not f.exists():
        continue
    content = strip_code_blocks(f.read_text(encoding="utf-8"))
    for m in link_pattern.finditer(content):
        url = m.group(2).strip()
        # External / non-file links: skip
        if url.startswith(("http://", "https://", "#", "mailto:", "tel:", "data:")):
            continue
        # Strip anchor
        url_path = url.split("#", 1)[0].split("?", 1)[0]
        if not url_path:
            continue
        try:
            target = (f.parent / url_path).resolve()
        except (OSError, ValueError):
            fail(f"{f.relative_to(ROOT)}: unresolvable link {url!r}")
            continue
        # Allow root references and the repo itself
        if not target.exists():
            fail(f"{f.relative_to(ROOT)}: broken link {url!r} → {target.relative_to(ROOT) if target.is_relative_to(ROOT) else target}")

# Report
if findings:
    print(f"❌ {len(findings)} finding(s):\n")
    for f in findings:
        print(f"  - {f}")
    sys.exit(1)

print(f"✅ Repository integrity OK")
print(f"   skills        : {len(slugs_on_disk)}")
print(f"   index.json    : in sync with filesystem")
print(f"   README counts : consistent")
print(f"   markdown links: all intra-repo links resolve")
sys.exit(0)
