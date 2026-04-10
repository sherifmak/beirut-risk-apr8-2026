# assets/

Shareable material for the blog post. Everything here is generated from the
same numbers in the main notebook — if you update the data, re-run
`generate_assets.py` and all charts regenerate.

## Contents

```
assets/
├── generate_assets.py        # Python script that produces all PNGs
├── charts/
│   ├── social_card_twitter.png    # 1200×675 — hero image for Twitter/X + Substack
│   ├── social_card_instagram.png  # 1080×1080 — square social card
│   ├── beirut_vs_911.png          # Head-to-head: Beirut vs NYC 9/11
│   ├── event_comparison_log.png   # Full log-scale event comparison
│   ├── beirut_by_scope.png        # Three Beirut scopes (city / Dahiyeh / metro)
│   └── comparison_sheet.png       # Text-heavy summary table, screenshot-ready
├── pull_quotes.md            # Short quotes for callouts and social media
└── tldr.md                   # One-sentence, one-paragraph, elevator-pitch summaries
```

## How to use these in the Substack post

**Hero image** (the big image at the top of the post):
`charts/social_card_twitter.png` — 1200×675, already sized for social-media
cards. Upload once to Substack and it'll be used as both the in-post hero
and the OG/Twitter preview.

**In-post charts** (embedded where each section discusses them):
- `event_comparison_log.png` — embed right after the "How to feel that number"
  section
- `beirut_vs_911.png` — embed right after the central 80-vs-145 / 266-vs-344 comparison
- `beirut_by_scope.png` — embed next to the Beirut scope table
- `comparison_sheet.png` — optional "at a glance" summary image to put near
  the end or the top

**Pull quotes:** Substack supports pull-quote blockquote styling. Pick 2–3
from `pull_quotes.md` and scatter them through the post at natural breaks.
The headline-claim quote should go in the first third; the closing-line
quote at the bottom.

**Previews / sharing:** `tldr.md` has one-sentence, one-paragraph, and
elevator-pitch versions for Substack's "email preview," LinkedIn,
Twitter/X, and DMs.

## Regenerating

If the underlying numbers change (Health Ministry revises upward, new
strikes happen, etc.), update the `events` list in `generate_assets.py`
and re-run:

```bash
source .venv/bin/activate
python assets/generate_assets.py
```

All PNGs in `charts/` will be overwritten in place.

## Style notes

- Dark red (`#8b0000`) is the Beirut highlight color
- Gray (`#7a7a7a`) is every other event
- Sans-serif, clean typography, white background — deliberately restrained
  visual style for a sensitive topic
- Source attribution in small print on every chart
