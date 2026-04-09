# beirut-risk-apr8-2026

A statistical estimate of the probability an average Beirut resident would have
been killed on **8 April 2026**, the day Israel launched its largest wave of
strikes on Lebanon of the war — ~100 targets in ~10 minutes, including central
Beirut without warning.

**This is a reproducible methodology exercise, not a body count, not a political
statement, and not personal guidance.** Read the caveats before the numbers.

---

## ⚠️ Read this first

1. **"Average Beirut resident" is a statistical fiction.** It's the right
   denominator for understanding scale across a city. It is absolutely the
   wrong number for judging any individual person's risk. Residents of the
   blocks that were actually hit faced risks **orders of magnitude higher**
   than the average. Someone in a northeastern neighborhood that wasn't
   targeted faced close to a normal day. The "average" hides that variance.

2. **These numbers are lower bounds.** The Lebanese Ministry of Public Health
   says its 300+ killed / 1,600+ wounded totals are preliminary and expected to
   rise. This notebook will be stale by the time you read it.

3. **This is not a comment on what the right number "should" be.** A rigorous
   estimate of Apr 8 citywide-average risk doesn't capture hospital-overload
   deaths, displacement, infrastructure loss, or psychological harm. It
   doesn't capture the war that preceded this day or the days that will follow.
   It's one narrow question: *if we distribute the reported deaths across
   Beirut's population, what probability of death does that imply?*

4. **The numbers can be weaponized in either direction.** "1 in 12,000" reads
   as either "that's not that bad" or "that's insane for one day." Both
   readings miss the point. The number is a unit of scale, not a verdict.

---

## The answer

Central estimate, based on Lebanese Ministry of Public Health figures (Apr 9):

| Area | Deaths (est.) | Population | Risk (µM) | 1 in X | vs normal day |
|---|---:|---:|---:|---:|---:|
| **Greater Beirut** (central) | **181** | 2,200,000 | **82.3** | **1 in 12,155** | **3.3×** |
| Beirut governorate (city proper) | 109 | 361,000 | 301.9 | 1 in 3,312 | 12.1× |
| Dahiyeh (southern suburbs) | 72 | 600,000 | 120.0 | 1 in 8,333 | 4.8× |

*A normal-day background mortality risk for a healthy 30-year-old is ~25
micromorts (µM).*

**Reading the central estimate:** the daily risk of death for an average
Greater Beirut resident on Apr 8 was roughly **82 µM (~1 in 12,000)**, or about
**3.3× a normal day**. A day of being alive in Beirut was, on average, roughly
equivalent to the daily risk for a healthy 60-year-old anywhere in the world.

**Reading the range:** depending on which "Beirut" you live in, the risk spans
roughly **3× to 12× a normal day**. Depending on which block, it spans
*much* more than that — see caveat #1.

---

## Methodology in one paragraph

Three complementary estimators, all in [micromorts](https://en.wikipedia.org/wiki/Micromort)
(1 µM = 1-in-1,000,000 chance of death):

1. **Empirical base rate** — `deaths ÷ population`, matched scope-to-scope
   (Beirut deaths ÷ Beirut population).
2. **Strike density + lethal footprint** — physics-based cross-check assuming
   each strike produces a ~30 m lethal radius and uniform exposure. A rough
   upper bound that ignores shelter and targeting.
3. **Back-solved effective lethality** — given observed deaths, what per-strike
   lethal radius would match? Reveals how far Estimator B overshoots because
   strikes hit buildings, not random ground.

Results in all three are reported with uncertainty bounds swept over source
choice, denominator choice, strike count, and lethal radius.

---

## Data sources

**Primary:**
- **Lebanese Ministry of Public Health** — authoritative nationwide total
  (300+ killed, ~1,600 wounded as of Apr 9, preliminary).
- **Lebanese General Directorate of Civil Defense** — preliminary Apr 8
  district-level breakdown (Beirut governorate: 92 killed / 742 wounded;
  Dahiyeh: 61 killed / 200 wounded). Used to decompose the Health Ministry
  nationwide total by district share.

**Press (for cross-reference):**
- [AP wire via WSLS — "Lebanon digs for survivors after Israeli attack kills over 300", Apr 9](https://www.wsls.com/news/world/2026/04/09/lebanon-digs-for-survivors-after-deadliest-day-of-renewed-war-between-israel-and-hezbollah/)
- [UN News — "Hundreds feared dead in Lebanon strikes"](https://news.un.org/en/story/2026/04/1167268)
- [BBC live feed](https://www.bbc.com/news/live/clyeg3224d9t)
- [Wikipedia — 8 April 2026 Lebanon attacks](https://en.wikipedia.org/wiki/8_April_2026_Lebanon_attacks)

**Optional live data (in the notebook):**
- [ReliefWeb (OCHA)](https://reliefweb.int/help/api) — no API key needed
- [ACLED](https://acleddata.com/) — free key required

---

## How to run

Requirements: Python 3.9+.

```bash
git clone https://github.com/sherifmak/beirut-risk-apr8-2026.git
cd beirut-risk-apr8-2026
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook risk_estimate.ipynb
```

Run all cells (`Kernel → Restart Kernel and Run All Cells`). The notebook is
pre-seeded with the Apr 9 dataset and works offline. Live fetchers (OCHA,
ACLED) are optional and fail gracefully.

For a no-install view: open `risk_estimate.html` in a browser, or view the
notebook directly on GitHub — it renders inline.

---

## Repository layout

```
beirut-risk-apr8-2026/
├── risk_estimate.ipynb     # the analysis
├── risk_estimate.html      # static export (no Python needed)
├── README.md               # this file
├── BLOG_POST.md            # the accompanying writeup
├── assets/                 # charts, pull quotes, TL;DRs for the blog post
│   ├── generate_assets.py  # run to regenerate all charts
│   ├── charts/             # PNG charts + social media cards
│   ├── pull_quotes.md      # shareable quotes
│   ├── tldr.md             # one-sentence / one-paragraph summaries
│   └── README.md           # index of assets
├── requirements.txt
├── LICENSE                 # MIT
└── .gitignore
```

---

## Full caveats

1. **Totals still rising.** Ministry of Public Health says the 300+ figure is
   preliminary. Rescue teams were still pulling bodies from rubble as this was
   written.
2. **Non-uniform targeting.** Strikes cluster in specific neighborhoods. The
   citywide average hides orders-of-magnitude variance between blocks.
3. **Non-uniform exposure.** People shelter, flee, or crowd into areas they
   perceive as safer. The uniform-distribution assumption in Estimator B is
   wrong; Estimator C quantifies that gap.
4. **District shares assumed stable.** The `health_ministry_scaled` rows apply
   the Civil Defense preliminary per-district *share* to the Health Ministry
   nationwide total. If the Health Ministry later publishes a direct district
   breakdown that differs, those rows should be replaced.
5. **Direct blast only.** Ignores hospital-overload deaths, loss of services,
   displacement, longer-term health effects, and psychological harm — all of
   which are real harms from a bombing campaign.
6. **One-day window.** Single-day estimates are high-variance. This is *this
   specific day*, not a war-average.
7. **Dual-use risk.** This kind of analysis can be used honestly to understand
   scale, or dishonestly to minimize or inflate harm. I've tried to structure
   it so it's hard to cherry-pick: all three estimators, full uncertainty
   bounds, full source list, reproducible code.

## The accompanying essay

See [BLOG_POST.md](BLOG_POST.md), or the published version at
[sheriff.substack.com](https://sheriff.substack.com).

## License

MIT — see [LICENSE](LICENSE). You are free to reuse the code and methodology.
If you publish derivative numbers, please link back and include the caveats.
