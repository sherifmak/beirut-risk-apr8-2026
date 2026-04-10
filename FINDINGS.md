# What was the risk of dying in Beirut on April 8, 2026?

On April 8, 2026, Israel launched its largest wave of airstrikes on
Lebanon of the current war — about 100 targets in 10 minutes, including
central Beirut without warning. More than 300 people were killed and
over 1,000 wounded.

This project estimates the **per-capita daily risk of death** for an
average Beirut resident that day, and compares it to other days the
world remembers.

---

## The short answer

| Where you lived | Your risk that day | Odds | How many normal days of risk |
|---|---:|---:|---:|
| Greater Beirut (metro, 2.2M people) | ~80 µM | ~1 in 12,500 | ~3× |
| Dahiyeh (southern suburbs, ~400k) | ~191 µM | ~1 in 5,200 | ~8× |
| Beirut city proper (~361k) | ~266 µM | ~1 in 3,800 | ~11× |

*A "µM" (micromort) is a 1-in-1,000,000 chance of death. A healthy
30-year-old faces about 25 µM on a normal day just from background
causes. So "3× normal" means Tuesday was about three normal days of
risk compressed into one.*

---

## How does this compare to other events?

All numbers computed the same way: deaths ÷ population ÷ 1,000,000.

| Event | Risk per resident |
|---|---:|
| London 7/7 bombings (2005) | ~7 µM |
| Paris attacks, Nov 13 (2015) | ~11 µM |
| Peak COVID day in NYC (Apr 7, 2020) | ~75 µM |
| **Beirut, Apr 8, 2026 (metro average)** | **~80 µM** |
| Beirut port explosion (Aug 4, 2020) | ~100 µM |
| 9/11, NYC metro basis | ~145 µM |
| **Beirut, Apr 8, 2026 (city proper)** | **~266 µM** |
| 9/11, NYC city basis | ~344 µM |

**Key takeaway:** On a per-capita basis, Tuesday in Beirut was in the
same numerical neighborhood as 9/11 in New York — about half on a
metro-vs-metro basis, about three-quarters on a city-proper basis.

This is a numerical comparison, not a moral one. These events have
different causes and contexts. The only thing being compared is one
number: the chance a randomly chosen resident would die that day.

---

## How we computed this

**Data.** Lebanese Ministry of Public Health (300+ killed nationwide,
updated Apr 9, preliminary) and Civil Defense district-level breakdown
(92 killed in Beirut city proper, 61 in the southern suburbs of
Dahiyeh).

**Method.** Four independent approaches:

1. **Simple division** — deaths ÷ population for each area.
2. **Physics model** — how many strikes × how large a lethal zone ÷ how
   large the city. A rough upper bound.
3. **Calibration check** — given the observed deaths, how concentrated
   was the targeting? (Answer: very — the strikes hit specific buildings,
   not random ground.)
4. **Monte Carlo simulation** (200,000 runs) — varies every uncertain
   input (which source to trust, how to define "Beirut," how to allocate
   updated nationwide totals to districts) and reports the range of
   answers. The numbers in the table above are the central values from
   this simulation.

The full analysis is in `risk_estimate.ipynb` (viewable directly on
GitHub). You can also open `risk_estimate.html` in any browser without
installing anything.

---

## What this number does NOT tell you

1. **It's an average across a whole city.** A resident of a block that was
   directly hit faced a risk perhaps 100–1,000× higher than these numbers.
   A resident of a quiet neighborhood faced close to a normal day. The
   average hides that enormous range.

2. **The totals are still rising.** The Health Ministry says 300+ is
   preliminary. These numbers are a lower bound.

3. **It only counts direct blast deaths.** It doesn't include hospital
   overload, displacement, lost services, long-term health effects, or
   psychological harm.

4. **It's one day, not the whole war.** The daily risk during a single
   spike is much higher than a war-average daily risk.

---

## Sources

- Lebanese Ministry of Public Health (via AP wire, Apr 9, 2026)
- Lebanese General Directorate of Civil Defense (district map, Apr 8, 2026)
- BBC, UN News, Wikipedia
- 9/11 figures: 2,753 NYC-specific victims
  ([source](https://en.wikipedia.org/wiki/Casualties_of_the_September_11_attacks))
- Full source list and methodology in the
  [notebook](risk_estimate.ipynb)

---

## Want to check the math?

Everything is open. Clone this repo, change any assumption, and re-run:

```bash
git clone https://github.com/sherifmak/beirut-risk-apr8-2026.git
cd beirut-risk-apr8-2026
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook risk_estimate.ipynb
```
