# What is the risk of dying in Beirut right now?

*A back-of-envelope answer to a question I wish I didn't have to ask.*

---

Yesterday, Israel launched the largest wave of airstrikes on Lebanon of the
current war. Fifty fighter jets. About a hundred and sixty munitions. A
hundred targets in ten minutes. Central Beirut — without warning — across at
least five neighborhoods. More than three hundred people killed. More than a
thousand six hundred wounded. Totals still rising.

I have family and friends in Beirut.

That's the whole reason I wrote this. I wanted a number I could reason
about. Not a headline. Not a body count. A number I could compare to things
I already understood — traffic, a bad disease year, a day I remember.

Because when you can't compare a risk to anything, it collapses into an
undifferentiated *bad*. And a hard feeling you can't size is a hard feeling
you can't carry.

## The unit nobody teaches you

There's a unit for this: the **micromort**. One micromort is a one-in-a-million
chance of death. A Stanford decision analyst invented it in the 1970s to
stop people from rounding small probabilities to zero. Some anchors:

- Driving 100 km on a highway — **0.4 µM**
- One skydive — **8 µM**
- A normal day of being alive, healthy 30-year-old — **25 µM**
- A normal day of being alive, healthy 60-year-old — **~300 µM**

You can turn any risk — traffic, war, disease — into micromorts and put
them side by side. That's the whole point.

## What I did

I pulled the Lebanese Ministry of Public Health nationwide total (300+
killed, 1,600+ wounded as of Thursday — preliminary), and a Civil Defense
district breakdown showing 92 killed in the Beirut governorate and 61 in
the southern suburbs of Dahiyeh. Then I computed the risk of death three
ways — a simple base-rate divide, a physics-based strike-density model, and
a back-solve that reveals how concentrated the targeting was. All three,
with uncertainty bounds, in [a Jupyter notebook on GitHub](https://github.com/sherifmak/beirut-risk-apr8-2026).

## The answer

For an average resident of Greater Beirut, on Tuesday April 8, 2026:

**~82 micromorts.** About 1 in 12,000. Roughly **3.3 times** a normal day
for a healthy 30-year-old.

The range by how you slice "Beirut":

| Area | Risk | vs normal day |
|---|---:|---:|
| Beirut governorate (city proper) | ~302 µM | **~12×** |
| Dahiyeh (southern suburbs) | ~120 µM | ~4.8× |
| Greater Beirut (metro average) | ~82 µM | ~3.3× |

## How to feel that number

Numbers without reference points are just pixels. Here's what April 8 looked
like next to other days the world remembers — same math, events computed
against the population most exposed:

| Event | Pop. denominator | Risk (µM) |
|---|---:|---:|
| London 7/7 bombings (2005) | London, 7.5M | ~7 |
| Paris Nov 13 attacks (2015) | Paris metro, 12M | ~11 |
| Peak COVID day in NYC (Apr 7 2020) | NYC, 8M | ~100 |
| **Beirut port explosion (Aug 4 2020)** | **Greater Beirut, 2.2M** | **~99** |
| **Beirut strikes (Apr 8 2026) — metro** | **Greater Beirut, 2.2M** | **~82** |
| 9/11 attacks (2001) | NYC metro, 19M | ~157 |
| **Beirut strikes (Apr 8 2026) — city proper** | **Beirut gov., 361k** | **~302** |
| 9/11 attacks (2001) | NYC city, 8M | ~372 |
| Hiroshima atomic bomb (Aug 6 1945) | Hiroshima, 340k | ~200,000 |

The comparison that stopped me short: **April 8 2026, for the average
Greater Beirut resident, was statistically about the same day of risk as
August 4 2020 — the port explosion.** Same city, same denominator, within a
rounding error.

Beirutis don't need anyone to explain what the port explosion was. We all
know exactly where we were at 6:07 PM that day, exactly what the sound was,
exactly which windows blew in and which held. The shape of the grief from
that day is still inside the city six years later, like a bruise that
doesn't fade.

Tuesday was, in the most literal statistical sense I know how to compute, a
day of that shape.

For a Beirut-governorate resident specifically — someone inside the
municipality proper, not the broader metro — the risk (~302 µM) was in the
same league as **9/11 for the average New Yorker**. One day. In a city of
361,000.

## Why the average is not the real number

Here I have to be careful, because the number above is the kind of thing
that can be decontextualized into either "see, it's not that bad" or "see,
it's a massacre," and both readings would be wrong.

The 82-micromort answer is a **mean across 2.2 million people**. It is the
number you get when you pretend the risk was spread evenly, when it
absolutely was not. The strikes hit specific buildings. A resident of a
block that took a direct hit faced a risk probably a hundred to a thousand
times higher than the average. A resident of a quiet neighborhood faced a
risk close to a normal day. The average collapses both realities into a
number that belongs to neither person.

Citywide averages are useful for scale. They are useless for personal
decision-making. If you want to know how bad April 8 was *for a city*, the
number is 82 micromorts — and I would not trust anyone whose instinct is to
round that down. If you want to know how bad it was for your cousin whose
building is two blocks from where a bomb landed, the statistics have
nothing to offer, and the number you want does not exist.

## What it doesn't capture

Hospital overload deaths that haven't happened yet. Displacement. Water,
electricity, healthcare. What it does to a child to hear a sonic boom at
2:30 PM on a Tuesday and not know if the next minute is the news. Grief
that will propagate through families for a generation. The war before this
day, the war after.

It is a single thin statistical sliver of a single day.

I computed it because the alternative was to sit with an undifferentiated
*bad* I couldn't reason about. The honest thing to do with a hard feeling
is to try to put bounds around it — not to make it smaller, but to make it
*the right size*. The right size of this feeling turned out to be: **a day
the shape of August 4 2020**.

I didn't feel better afterward. But I understood what I was afraid of with
a little more precision. That was what I came for.

---

**The full analysis**, with all three estimators, uncertainty sweeps,
sensitivity charts, and sources, is on GitHub:
**[github.com/sherifmak/beirut-risk-apr8-2026](https://github.com/sherifmak/beirut-risk-apr8-2026)**.
If you disagree with my assumptions, clone it and change them.

**Sources.** Lebanese Ministry of Public Health (via AP, Apr 9 2026).
Lebanese Civil Defense district map, Apr 8 2026. UN News. BBC. Full list in
the repo.

**Last caveat.** This is a citywide average. It is the wrong number for any
individual person's safety — including anyone you love. For that, the
statistics have nothing. For understanding the scale of a day on which
hundreds of people were killed in a city my family lives in, they were the
only tool I had.
