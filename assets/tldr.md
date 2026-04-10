# TL;DR summaries

Different lengths for different uses.

---

## One sentence

> On a per-capita daily-risk basis, Tuesday in Beirut was roughly
> comparable to what the average New Yorker faced on September 11, 2001.

---

## One paragraph

> On April 8, 2026, Israel launched its largest wave of airstrikes on
> Lebanon of the war — 100 targets in 10 minutes, central Beirut without
> warning, 300+ killed, ~1,150 wounded. Computing the per-capita daily
> risk of death in micromorts gives **~80 µM** for the average Greater
> Beirut resident (90% credible interval [69, 97]) — about **55% of what
> the average New Yorker faced on 9/11** on a consistent metro-area
> basis. At the city-proper level the comparison tightens to ~77% of
> 9/11. Full four-estimator analysis with Monte Carlo uncertainty bounds
> and sources on GitHub. **This is a numerical comparison, not a moral one.**

---

## Elevator pitch (~30 seconds)

> On Tuesday, Israel did the largest airstrikes on Lebanon of the war.
> I built a Jupyter notebook with four methods — including a Monte Carlo
> — to estimate the per-capita daily risk of death for an average Beirut
> resident. On a consistent metro-vs-metro basis, the risk was about 55%
> of what the average New Yorker faced on 9/11. On a city-proper basis,
> about 77%. Both are in 9/11's neighborhood. The methodology, all the
> assumptions, and the uncertainty bounds are on GitHub.

---

## Technical abstract

> Estimates per-capita daily risk of death for an average Beirut
> resident during the April 8 2026 Israeli strikes on Lebanon using
> four complementary methods: empirical base rate, strike-density
> physics model, back-solved per-strike footprint, and Monte Carlo
> uncertainty propagation (N=200k). Data from the Lebanese Ministry of
> Public Health (authoritative nationwide total, Apr 9 preliminary)
> decomposed by Civil Defense district shares. Central estimate for
> Greater Beirut metro: 80 µM (90% CI [69, 97]) — approximately 55% of
> NYC 9/11 metro-basis figure (~145 µM, from 2,753 NYC-specific victims
> divided by 19M NYC metro population). City-proper basis: 266 µM (90% CI
> [228, 327]), ~77% of NYC 9/11 city basis. The comparison is robust to
> denominator choice. Reproducible notebook in the repository.
