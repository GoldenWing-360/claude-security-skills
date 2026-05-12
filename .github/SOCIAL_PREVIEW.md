# Social Preview — Design Spec

GitHub uses the **social preview image** as the card shown when the repo is shared on Twitter / X, LinkedIn, Slack, Discord, Mastodon, etc. A custom one significantly increases click-through compared to the default avatar-on-grey card.

Upload via: **Settings → General → Social preview → Upload an image**.

## Spec

- **Dimensions**: 1280 × 640 px (2:1 ratio; GitHub displays as ~640×320, but uploading 2× retina is the sweet spot)
- **Format**: PNG (preferred) or JPG. < 1 MB.
- **Safe area**: leave 80 px margin on all sides — Twitter/LinkedIn crop slightly differently
- **Text**: must be readable at 640 px wide and at thumbnail size (~300 px)

## Suggested layout (option A — text-forward, recommended)

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   🛡️  CLAUDE CODE SECURITY SKILLS                                │
│                                                                  │
│   25 defensive security skills for Claude Code                   │
│   AI agents · WordPress · VPS · Cloudflare · Next.js · GDPR     │
│                                                                  │
│   github.com/GoldenWing-360/claude-security-skills               │
│                                                                  │
│                                          made by goldenwing.at   │
└──────────────────────────────────────────────────────────────────┘
```

- Background: dark (`#0d1117` matches GitHub dark mode) with subtle gradient or grid
- Title: bold sans-serif (Inter, IBM Plex Sans, JetBrains Sans), ~80 px
- Tagline: regular weight, ~36 px, muted color (`#8b949e`)
- Categories: same font, ~28 px, accent color
- URL and brand: ~22 px, bottom corners
- Optional: subtle 🛡️ or lock-shaped graphic on the left, do not overwhelm the text

## Suggested layout (option B — graphic-forward)

If you have a designer:

- Hero visual on the left (abstract shield / lock / network mesh)
- Title + tagline on the right
- "25 skills" badge prominent
- GoldenWing brand mark bottom-right

## Color palette suggestion

To match the existing badges and the dark-tech aesthetic:

| Use | Hex |
|---|---|
| Background | `#0d1117` |
| Text primary | `#f0f6fc` |
| Text secondary | `#8b949e` |
| Accent (links, badges) | `#58a6ff` |
| GoldenWing orange | `#f97316` |

## Quick paths to creation

- **Figma / Canva** template — search "GitHub social preview 1280x640"
- **Carbon** (carbon.now.sh) for a code-themed render
- **Designer commission** — quick gig on Fiverr/Behance, ~€50–100
- **AI image gen** — most current image models can produce a clean GitHub-style card given the spec above; iterate until the text is sharp (text-in-images is still imperfect in some models)

## Don't

- Don't use a busy photo background — thumbnails lose all detail
- Don't put the full skill list on the card — readers scan, not read
- Don't trademark-borrow Anthropic / Claude logos beyond fair-use mention
- Don't pack the card so dense that it looks like a slide deck

## After upload

Test the preview:

- [https://twitter.com/share?url=https://github.com/GoldenWing-360/claude-security-skills](https://twitter.com/share?url=https://github.com/GoldenWing-360/claude-security-skills)
- [https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/GoldenWing-360/claude-security-skills](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/GoldenWing-360/claude-security-skills)
- [https://cards-dev.twitter.com/validator](https://cards-dev.twitter.com/validator)

Cache busting: Twitter/LinkedIn cache aggressively. After updating the social preview, the new image may take 24h+ to propagate. Use the validator endpoints above to force a refresh.
