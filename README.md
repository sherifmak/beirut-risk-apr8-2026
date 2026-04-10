# beirut-risk-apr8-2026

A reproducible statistical estimate of the probability that an **average
Beirut resident** would have been killed on **8 April 2026**, the day Israel
launched its largest wave of strikes on Lebanon of the war — ~100 targets in
~10 minutes, including central Beirut without warning.

**This is a methodology exercise, not a body count, not a political
statement, and not personal guidance.** The number is a per-capita daily
average that hides huge block-level variance. Read the caveats before the
numbers.

---

## ⚠️ Read this first

1. **"Average Beirut resident" is a statistical fiction.** It's the right
   denominator for understanding scale across a city. It is the wrong number
   for judging any individual person's risk. Residents of blocks that were
   directly hit faced risks **orders of magnitude higher** than the average
   (perhaps 100–1,000×). Someone in an untargeted neighborhood faced close
   to a normal day.

2. **These are preliminary figures.** The Lebanese Ministry of Public
   Health says its 300+ killed / ~1,150 wounded totals are not final and
   are expected to rise. The Monte Carlo in Estimator D (in the notebook)
   propagates this uncertainty.

3. **This is a numerical comparison, not a moral one.** When the numbers
   below show that Apr 8 in Beirut produced per-capita daily-risk values
   comparable to 9/11 in New York on a consistent denominator basis, that
   is a statement about arithmetic, not a claim of moral equivalence. These
   events have different causes, contexts, and ethical status; the
   statistics say nothing about any of that.

4. **The numbers can be weaponized in either direction.** A rigorous
   methodology, full disclosure of assumptions, and explicit uncertainty
   bounds are the main defense. If you want to disagree with any
   assumption, the repo is open — clone it, change the input, and see
   where the numbers go.

---

## The answer

Central estimates from the Monte Carlo (Estimator D, N=200,000 samples)
with **90% credible intervals**. All inputs from Lebanese Ministry of
Public Health (Apr 9) and Civil Defense (Apr 8, preliminary).

| Area | Median µM | 90% CI | 1 in X (median) | vs normal day |
|---|---:|---:|---:|---:|
| **Greater Beirut metro** (2.2M) | **~80** | **[69, 97]** | ~1 in 12,500 | ~3× |
| Beirut governorate (city proper, 361k–433k) | ~266 | [228, 327] | ~1 in 3,800 | ~11× |
| Dahiyeh (southern suburbs, 333k–400k) | ~191 | [163, 235] | ~1 in 5,200 | ~8× |

*A normal-day background mortality risk for a healthy 30-year-old is
~25 µM. 1 µM = 1 in 1,000,000 chance of death.*

**Reading the metro-vs-metro central estimate:** the daily risk of death
for an average Greater Beirut resident on Apr 8 was roughly **80 µM
(~1 in 12,500)**, or about **3× a normal day**. On a consistent
metro-area basis, that's about **55% of what the average New Yorker faced
on 9/11** (~145 µM on the 19M metro population basis).

**At the city-proper level**, the central estimate for a Beirut-governorate
resident (~266 µM) is within 23% of the NYC-city-basis 9/11 figure
(~344 µM). The 90% credible interval on the Beirut governorate number is
[228, 327] — the upper end of that range is within 5% of the 9/11 NYC city
number.

## Methodology in one paragraph

Four complementary estimators, all in
[micromorts](https://en.wikipedia.org/wiki/Micromort):

1. **Empirical base rate** — `deaths ÷ population`, matched scope-to-scope.
2. **Strike density + lethal footprint** — physics-based naive upper bound
   with uniform-exposure assumption.
3. **Back-solved per-strike footprint** — reveals how far the uniform
   assumption is from reality.
4. **Monte Carlo** — propagates uncertainty from scaling assumption,
   population denominator choice, and preliminary-data revision into 90%
   credible intervals.

Uncertainty sweeps over source choice, scope, denominator, strike count,
and lethal radius are all in the notebook.

---

## Data sources

**Primary (Lebanese authorities):**
- **Lebanese Ministry of Public Health** — authoritative nationwide total
  (300+ killed, ~1,150 wounded as of Apr 9, preliminary).
- **Lebanese General Directorate of Civil Defense** — preliminary Apr 8
  district-level breakdown (Beirut governorate: 92 killed / 742 wounded;
  Dahiyeh: 61 killed / 200 wounded). Used to decompose the Health Ministry
  nationwide total by district share.

**Press (for cross-reference, all Apr 9 2026):**
- [AP wire — "Lebanon digs for survivors after Israeli attack kills over 300"](https://www.wsls.com/news/world/2026/04/09/lebanon-digs-for-survivors-after-deadliest-day-of-renewed-war-between-israel-and-hezbollah/)
- [UN News — "Hundreds feared dead in Lebanon strikes"](https://news.un.org/en/story/2026/04/1167268)
- [BBC live feed](https://www.bbc.com/news/live/clyeg3224d9t)
- [Wikipedia — 8 April 2026 Lebanon attacks](https://en.wikipedia.org/wiki/8_April_2026_Lebanon_attacks)

**Population figures (with source audit):**
- Beirut governorate: **361k** (World Population Review) or **433k**
  (citypopulation.de / Wikipedia, end-2017 estimate). Both cited; Monte
  Carlo samples uniformly over the range.
- Dahiyeh: **333k–400k** (Statistics Lebanon via L'Orient-Le Jour).
- Greater Beirut metro: **~2.2M**.
- Lebanon nationwide: **5.8M** (World Bank 2024).
- NYC city 2001: ~8M; NYC metro 2001: ~19M (US Census 2000).

**9/11 numerator:** **2,753** NYC-specific victims (excludes 184 at the
Pentagon and 40 on Flight 93 near Shanksville). Earlier drafts of this
analysis used 2,977 (total across all three sites), which was a scope
mismatch when dividing by NYC-only denominators. Correction documented in
the notebook.

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

> Use `python3` (not `python`) for the `venv` step — macOS ships without a
> `python` alias. Once the venv is activated, `python`, `pip`, and
> `jupyter` all work.

Run all cells (`Kernel → Restart Kernel and Run All Cells`). The notebook
is pre-seeded with the Apr 9 dataset and works offline. Live fetchers
(OCHA, ACLED) are optional and fail gracefully.

For a no-install view: open `risk_estimate.html` in a browser, or view the
notebook directly on GitHub — it renders inline.

---

## Repository layout

```
beirut-risk-apr8-2026/
├── risk_estimate.ipynb     # the analysis
├── risk_estimate.html      # static export
├── README.md               # this file
├── BLOG_POST.md            # the accompanying writeup
├── assets/                 # charts, pull quotes, TL;DRs
│   ├── generate_assets.py  # run to regenerate all charts
│   ├── charts/             # PNG charts + social media cards
│   ├── pull_quotes.md
│   ├── tldr.md
│   └── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Full caveats

1. **Totals still rising.** Ministry of Public Health says the 300+ figure
   is preliminary. Rescue teams are still pulling bodies from rubble as
   this is being written. The Monte Carlo allows for further upward
   revision in its `hm_uplift` prior.

2. **Non-uniform targeting.** Strikes cluster in specific neighborhoods.
   The citywide average hides orders-of-magnitude variance between blocks.
   **This is the single most important caveat.** The number below is a
   citywide mean; it is not the number for any specific person.

3. **Non-uniform exposure.** People shelter, flee, or crowd. The
   uniform-distribution assumption in Estimator B is wrong in both
   directions; Estimator C quantifies the gap.

4. **Scaling assumption.** The `health_ministry_scaled` point estimates
   apply the Civil Defense preliminary per-district *share* to the Health
   Ministry nationwide total. If the late-reported bodies are concentrated
   outside Beirut (e.g., delayed reporting from southern Lebanon), the
   true Beirut count could be as low as the CD observation (92 deaths in
   Beirut governorate, 255 µM unscaled). If concentrated in Beirut, it
   could be higher. The Monte Carlo in Estimator D propagates this. The
   "~9/11-scale per capita" claim survives the full scaling range.

5. **Direct blast only.** Ignores hospital-overload deaths, loss of
   services, displacement, longer-term health effects, and psychological
   harm.

6. **One-day window.** Single-day estimates are high-variance. This is
   *this specific day*, not a war-average.

7. **Dual-use risk.** This analysis can be used honestly to understand
   scale, or dishonestly to minimize or inflate harm. I've tried to
   structure it so it's hard to cherry-pick: four estimators, full
   uncertainty bounds, full source list, reproducible code. The numerical
   comparison to 9/11 is a statement about arithmetic, not moral
   equivalence.

---

## FAQ / expected objections

**Q: Why compare city-proper Beirut to city-proper NYC? Most 9/11 deaths
were in Lower Manhattan (~1.5 km²).**

Because city-proper-to-city-proper is the consistent denominator choice
available without pinning Lower Manhattan / the 5-neighborhood Beirut
strike zone against each other (both of which would push both numbers
upward by similar factors). The blog post leads with the
**metro-vs-metro** comparison precisely because it's the safest consistent
pairing; the city-proper number is shown as a secondary, more aggressive
comparison. If you spread both events to the actually-affected footprint,
both get much larger and the ratio is similar.

**Q: Why scale the Civil Defense share by the Health Ministry ratio
instead of using the CD number directly?**

Because the Health Ministry is the authoritative source for the total,
and we don't have a direct HM district breakdown. Proportional scaling is
the least-bad assumption. **The Monte Carlo allows the Beirut share of
the uplift to be anywhere from 0% (pure CD observation) to 60%** — the
central claim survives that full range.

**Q: Why use 361k for Beirut governorate when some sources say 433k?**

Both are cited; the discrepancy reflects whether refugees are counted.
Lebanon has had no census since 1932. The Monte Carlo samples uniformly
over both. At 433k the point estimate drops from ~302 to ~252 µM, but the
Monte Carlo median is robust because it samples over both.

**Q: Why a single-day window? Single-day micromorts are noisy.**

Because the question is about *this specific day*, not a war-average. A
war-averaged daily micromort rate would be much lower, and it would be a
different question with a different answer.

**Q: Isn't the "average resident" number misleading?**

Yes, and caveat #2 leads with that explicitly. It's the right number for
scale, the wrong one for individual risk.

**Q: Why not a full Bayesian model with priors on the true death count?**

The Monte Carlo is a simplified Bayesian treatment with uniform priors
over the uncertain inputs. A full hierarchical Bayesian model (e.g. with
Gamma prior on true death rate) would give similar intervals and is left
as an exercise.

**Q: Your Estimator B spans three orders of magnitude. Is it actually
informative?**

Not as a point estimate. It's informative because Estimator C inverts it
and quantifies the gap between the uniform-exposure assumption and
reality. The range of B shows that the assumption is under-constrained;
the fact that C back-solves a much smaller effective footprint shows the
direction and magnitude of the mismatch.

**Q: Why not compare to a day from Gaza, Mariupol, or Syria?**

Good-faith question. I chose Western-legible reference events so a Western
audience has familiar anchors. Adding a day from Gaza 2023–2024 or
Mariupol 2022 would very plausibly yield µM values comparable to or
exceeding Apr 8 Beirut — which is a fact, but which also makes the post
about a different question (comparative war statistics) than the one I'm
answering (what was the per-capita risk on this specific day). If you
want those comparisons, the code is open.

**Q: Is this propaganda?**

No. The code is open, the assumptions are explicit, the uncertainty is
quantified, and the caveats lead. If you disagree with any input, clone
the repo and change it.

## The accompanying essay

See [BLOG_POST.md](BLOG_POST.md) or the published version at
[sheriff.substack.com](https://sheriff.substack.com).

## License

MIT — see [LICENSE](LICENSE). You are free to reuse the code and
methodology. If you publish derivative numbers, please link back and
include the caveats.
