# assets/

Shareable visual material for the project. Everything here is generated
from the same numbers in the main notebook — if you update the data,
re-run `generate_assets.py` and all charts regenerate.

## Contents

```
assets/
├── generate_assets.py          # Python script that produces all PNGs
├── charts/
│   ├── social_card_twitter.png    # 1200×675 — hero image for social sharing
│   ├── social_card_instagram.png  # 1080×1080 — square social card
│   ├── beirut_vs_911.png          # Head-to-head: Beirut vs NYC 9/11
│   ├── event_comparison_log.png   # Full log-scale event comparison
│   ├── beirut_by_scope.png        # Three Beirut scopes with CIs
│   └── comparison_sheet.png       # Text-heavy summary table, screenshot-ready
├── pull_quotes.md            # Short quotes for callouts and social media
└── tldr.md                   # One-sentence, one-paragraph, elevator-pitch summaries
```

## Suggested use

**Hero image** (social sharing): `charts/social_card_twitter.png` —
1200×675, pre-sized for Twitter/X cards and link previews.

**In-context charts** (embedded in articles or posts):
- `event_comparison_log.png` — the full event comparison
- `beirut_vs_911.png` — embed right after the 80-vs-145 / 266-vs-344 comparison
- `beirut_by_scope.png` — the three Beirut sub-populations with error bars
- `comparison_sheet.png` — screenshot-ready text table

**Pull quotes:** Short, shareable lines from `pull_quotes.md`.

**Summaries:** One-sentence, one-paragraph, and elevator-pitch versions
in `tldr.md` for social, email, or conversation.

## Regenerating

If the underlying numbers change:

```bash
source .venv/bin/activate
python assets/generate_assets.py
```

All PNGs in `charts/` will be overwritten in place.

## Style notes

- Dark red (`#8b0000`) is the Beirut highlight color
- Gray (`#7a7a7a`) is every other event
- Sans-serif, clean typography, white background
- Source attribution in small print on every chart
