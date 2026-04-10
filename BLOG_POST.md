# Beirut just had a 9/11-scale day, per capita

*I did the math because the news couldn't tell me what I needed to know.*

---

On Tuesday, April 8 2026, Israel launched the largest wave of airstrikes on
Lebanon of the current war. Fifty fighter jets. A hundred and sixty
munitions. A hundred targets in ten minutes. Central Beirut, without
warning, across at least five neighborhoods. Southern suburbs. The Bekaa
Valley. A funeral procession.

More than three hundred people killed. More than a thousand wounded. Totals
still rising.

I have family and friends in Beirut. I wanted to know what Tuesday actually
*meant* for them — not as a headline, but as a number I could compare to
something I already understood. Something in my bones.

I computed the answer four different ways, including a Monte Carlo that
propagates every uncertainty I could name into honest 90% credible
intervals. All four agreed on the scale.

**On a consistent per-capita basis, Tuesday in Beirut produced a daily risk
of death roughly comparable to what the average New Yorker faced on
September 11, 2001.** The exact number depends on which denominator you
use, but the comparison holds across every reasonable choice.

Before I defend that claim, I need to say something clearly:

> **This is a numerical comparison, not a moral one.** Two events can
> produce similar per-capita daily-risk numbers and still be categorically
> different in their causes, contexts, and ethical status. What follows is
> a statement about arithmetic, not a claim about equivalence. I am
> comparing one number — the per-capita chance of death in a single day —
> because that's the question the news didn't answer and I couldn't stop
> thinking about. Readers who want to judge anything else need a different
> set of tools.

And one more thing, because it is the single most important caveat and it
has to come before the numbers:

> **The "average resident" figure hides huge variance.** It is a citywide
> mean across millions of people. A resident of a block that took a direct
> hit faced risk 100 to 1,000 times higher than the average. A resident of
> a quiet neighborhood faced close to a normal day. The number I'm about
> to give you is the right number for understanding the *scale* of a day.
> It is the wrong number for any individual person's safety — including
> yours, including anyone you love.

Now the math.

## The unit

There's a unit for this kind of comparison. It's called a **micromort** —
one chance in a million of death. A Stanford decision analyst invented it
in the 1970s because human brains are bad at tiny probabilities: we round
rare to never and common to always. Micromorts fix this by turning small
probabilities into whole numbers. Some anchors:

- Driving 100 km on a highway — **0.4 µM**
- One skydive — **8 µM**
- A normal day at age 30 — **~25 µM**
- Peak COVID day in NYC (Apr 7 2020) — **~75 µM**
- A normal day at age 60 — **~300 µM**

You can compute a micromort for any day, any event — traffic, war,
disease — and put them side by side. That's the whole point.

## What I did

I pulled the Lebanese Ministry of Public Health nationwide total (300+
killed, ~1,150 wounded as of Thursday — preliminary), and a Civil Defense
district breakdown published Wednesday showing 92 killed in the Beirut
governorate and 61 in the southern suburbs of Dahiyeh. Then I computed
the daily risk of death four ways:

1. **Empirical base rate** — deaths divided by population, scope-matched.
2. **Strike density + lethal footprint** — a physics-based upper bound
   assuming uniform exposure. (Spoiler: it overshoots because the
   assumption is wrong.)
3. **Back-solved effective footprint** — given the observed deaths, how
   non-uniform was the actual exposure? (Quantifies how far estimator #2
   is off.)
4. **Monte Carlo** — propagates every uncertainty I could name (scaling
   assumption, population denominator, preliminary-data revision) into
   honest 90% credible intervals.

All four are in [a Jupyter notebook on GitHub](https://github.com/sherifmak/beirut-risk-apr8-2026).
You can clone it and change any assumption.

## The answer

**Monte Carlo central estimates with 90% credible intervals** (from
200,000 simulations):

| Area | Median µM | 90% CI | ≈ 1 in X | vs normal day |
|---|---:|---:|---:|---:|
| **Greater Beirut metro (2.2M)** | **~80** | **[71, 95]** | **~1 in 12,500** | **~3.2×** |
| Dahiyeh (southern suburbs) | ~191 | [163, 235] | ~1 in 5,200 | ~7.6× |
| Beirut governorate (city proper) | ~266 | [228, 327] | ~1 in 3,800 | ~10.6× |

The three rows answer three different versions of "who counts as a Beirut
resident." I lead with the metro-area number because it uses the most
consistent denominator for comparing across events — but all three are
defensible, and the ratio to 9/11 (below) is actually *stronger* at the
city-proper level.

## How Tuesday compares to 9/11

Start with 9/11. 2,753 people were killed in New York City on September 11,
2001 (the total across all three sites was 2,977, but 184 died at the
Pentagon and 40 on Flight 93 — dividing 2,977 by an NYC-only denominator
would be a scope mismatch). New York City had ~8 million residents in 2001;
the NYC metropolitan area had ~19 million. That gives you:

```
NYC city proper: 2,753 / 8,000,000  × 1,000,000 = ~344 µM
NYC metro area:  2,753 / 19,000,000 × 1,000,000 = ~145 µM
```

And Tuesday in Beirut:

```
Greater Beirut metro (Monte Carlo median):  ~80 µM
Beirut governorate (Monte Carlo median):   ~266 µM
```

Lining them up **on the same denominator basis**:

- **Metro vs metro:** Beirut Apr 8 2026 was **~55%** of NYC 9/11
  (80 µM vs 145 µM). About **half a 9/11**, per capita.
- **City proper vs city proper:** Beirut Apr 8 2026 was **~77%** of NYC
  9/11 (266 µM vs 344 µM). The **upper end of the 90% credible interval**
  (327 µM) overlaps the NYC figure within ~5%.

Either way, Tuesday in Beirut and 9/11 in New York sit in the **same
numerical neighborhood** on a per-capita daily-risk basis — within a factor
of about two. On a log-scale chart of days the world remembers, they sit
on top of each other.

## Why the comparison holds on either denominator (and the choice I didn't make)

A careful reader will ask: why those denominators? Why not Lower Manhattan
(where most 9/11 deaths happened, ~50k residents) against the five
neighborhoods of Beirut that were actually hit?

If you did that, 9/11 becomes somewhere north of 50,000 µM and Beirut Apr 8
becomes 1,000+ µM in the affected neighborhoods — and their ratio is still
in the same league. **The robust claim isn't the absolute micromort number;
it's the ratio.** I report two consistent denominator pairs (metro-vs-metro
and city-vs-city) because they bracket the range, and the ratio is stable
across the bracket. If I chose Lower-Manhattan-vs-five-Beirut-neighborhoods,
both numbers would shoot up by a factor of ~20 but the ratio would still
put Tuesday in 9/11's neighborhood.

What I'm *deliberately not doing* is picking one side's most-concentrated
denominator and the other side's most-dispersed one. That would be a
cherry-pick. The comparison in this post is robust to the denominator
choice, or it isn't worth making.

## The full picture

Here's April 8 next to other days the world remembers, all computed the
same way — deaths ÷ population most exposed × 1,000,000:

| Event | Pop. denominator | Risk (µM) |
|---|---:|---:|
| London 7/7 bombings (2005) | London, 7.5M | ~7 |
| Paris Nov 13 attacks (2015) | Paris IdF, 12M | ~11 |
| Peak COVID day, NYC (Apr 7 2020) | NYC, 8M | ~75 |
| **Beirut Apr 8 2026 — Greater Beirut metro** | **2.2M** | **~80** |
| Beirut port explosion (Aug 4 2020) | Greater Beirut, 2.2M | ~100 |
| 9/11 attacks — NYC metro basis | 19M | ~145 |
| **Beirut Apr 8 2026 — Dahiyeh** | **~400k** | **~191** |
| **Beirut Apr 8 2026 — Beirut governorate** | **361k** | **~266** |
| 9/11 attacks — NYC city basis | 8M | ~344 |
| Hiroshima atomic bomb (1945) | 340k | ~200,000 |

Three things fall out of this table.

**First**, Apr 8 in Beirut sits in the same cluster as the Beirut port
explosion, peak COVID NYC, and 9/11 on both NYC bases. Within that cluster,
Beirut Apr 8 metro and NYC 9/11 metro are within a factor of about 2.
Neither one is an outlier; neither can be dismissed without dismissing the
other. That's the claim.

**Second**, for the average Greater Beirut resident, Apr 8 was within
about 20% of the Beirut port explosion on the same metro-area basis.
Beirutis do not need anyone to explain what the port explosion was. We
all know exactly where we were at 6:07 PM that day. Tuesday was, in the
most literal statistical sense I know how to compute, a day of that
shape.

**Third**, even the governorate number (266 µM central, 327 µM upper CI)
is roughly a thousand times smaller than Hiroshima. That is worth saying
out loud, not because it minimizes anything, but because the unit only
works if you respect its full range. Days of war span an enormous
dynamic range. Apr 8 was a very bad day. It was not every bad day.

## The full caveat, restated

The 80-µM metro number is a mean across 2.2 million people. The 266-µM
governorate number is a mean across 361,000. **Both hide orders-of-magnitude
variance.** The strikes hit specific buildings. A resident of a block that
took a direct hit faced a risk probably 100–1,000× higher than either of
these numbers. A resident of a quiet neighborhood faced something close to
a normal day. The averages collapse both realities into single numbers that
belong to neither person.

Citywide averages are useful for scale. They are useless for personal
decision-making. If you want to know how dangerous Tuesday was *for a
city*, the number is roughly half of 9/11 on a metro basis, roughly
three-quarters on a city-proper basis. If you want to know how dangerous
Tuesday was for your cousin whose building is two streets from where a
bomb landed, this post has nothing to offer, and the number you want does
not exist.

## What it doesn't capture

Hospital-overload deaths that haven't happened yet. Displacement. Water,
electricity, healthcare. What it does to a child to hear a sonic boom at
2:30 PM on a Tuesday and not know if the next minute is the news. Grief
that will propagate through families for a generation. The war before this
day, the war after.

This is a single thin statistical sliver of a single day.

I computed it because the alternative was to sit with an undifferentiated
*bad* I couldn't reason about. The honest thing to do with a hard feeling
is to try to put bounds around it — not to make it smaller, but to make it
*the right size*. The right size of this one turned out to be **about half
of 9/11 on a metro-vs-metro basis**, **roughly 9/11-scale at city-proper**,
and **within 20% of August 4, 2020 in Beirut** — all at once, all on the
same log-scale chart.

I didn't feel better afterward. But I understood what I was afraid of with
a little more precision. That was what I came for.

## What would change my mind

The central claim depends on two load-bearing inputs. If either turns out
to be wrong, I will update:

1. **If the Health Ministry publishes a direct Beirut-governorate death
   count that is materially different from ~109.** My number is derived
   from the CD preliminary (92 observed) scaled by the HM uplift ratio.
   The Monte Carlo already allows the Beirut share of the uplift to be
   anywhere from 0% (pure CD observation) to 60% of the total uplift, and
   the comparison survives. But if HM says the real Beirut number is
   significantly below 92 or above 150, the comparison changes.
2. **If the NYC denominator convention turns out to be something I didn't
   consider.** I used both NYC city (8M) and NYC metro (19M) for 9/11; if
   someone has a more defensible pair, I'll recompute.

Both are easy updates — change the input in the notebook and re-run.

---

**The full analysis**, with all four estimators, the Monte Carlo, full
uncertainty sweeps, and sources, is on GitHub:
**[github.com/sherifmak/beirut-risk-apr8-2026](https://github.com/sherifmak/beirut-risk-apr8-2026)**.
If you disagree with any of my assumptions — which source to trust, how to
define "Beirut," which NYC denominator is fair — clone it and change them.

**Sources.** Lebanese Ministry of Public Health (via AP wire, Apr 9 2026).
Lebanese Civil Defense district map, Apr 8 2026. BBC live feed, UN News.
Full list in the repo. 9/11 figures from the [9/11 Memorial Museum casualty
database](https://en.wikipedia.org/wiki/Casualties_of_the_September_11_attacks)
(2,753 NYC-only victims). Beirut population figures from World Population
Review and citypopulation.de (both are cited; the Monte Carlo samples over
the range).

**Last caveat, restated again.** This is a citywide average. It is the
wrong number for any individual person's safety — including anyone you
love. For that, the statistics have nothing. For understanding the scale
of a day on which hundreds of people were killed in a city my family
lives in, they were the only tool I had.
