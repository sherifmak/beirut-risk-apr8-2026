# What is the risk of dying in Beirut right now?

*A back-of-envelope answer to a question I wish I didn't have to ask.*

---

Yesterday, Israel launched the largest wave of airstrikes on Lebanon of the
current war. Fifty fighter jets. About a hundred and sixty munitions. A
hundred targets in ten minutes. Central Beirut — without warning — across at
least five neighborhoods. Southern Beirut. The Bekaa Valley. A funeral
procession in a village I had never heard of.

I have family and friends in Beirut.

That's the whole reason I wrote this. It's the reason I spent a Thursday
evening building a Python notebook I wish didn't need to exist. I wanted to
know what their risk was. Not a body count. Not a headline. Not "hundreds
dead" or "deadliest day of the war." Those phrases are true, and they are
also too large to carry in your head.

I wanted a number I could reason about. A number I could compare to something
I already understood. Is this like a bad day driving a motorcycle? Is it like
skydiving? Is it like a normal day of being alive at sixty instead of thirty?

Because when you can't compare a risk to anything, it collapses into an
undifferentiated *bad*. And when you can compare it, sometimes you find out
the reality is worse than the feeling. Sometimes the reverse. Either way, you
learn something.

## The unit nobody teaches you in school

There's a unit for this kind of thinking. It's called a **micromort** — a
one-in-a-million chance of death. It was invented by a Stanford decision
analyst named Ronald Howard in the 1970s specifically because human brains
are bad at tiny probabilities. We confuse *rare* with *never*, we confuse
*common* with *always*, and we refuse to do arithmetic on fractions smaller
than about 1 in 100.

Micromorts fix this by turning small probabilities into whole numbers. Some
examples:

- Driving 100 km on a highway: **about 0.4 micromorts**
- One skydive jump: **about 8 micromorts**
- A normal day of being alive if you're a healthy 30-year-old: **about 25
  micromorts**
- Climbing Mount Everest: **about 40,000 micromorts** (yes, really)

You can take the annual risk of anything and chop it into daily micromorts.
You can turn any activity into micromorts per hour. You can add them up. You
can compare them across totally different categories — traffic, disease,
adventure sports, wars. That's the whole point.

So my question became: on Tuesday, what was Beirut in micromorts?

## What I actually did

I pulled the reported casualty figures from the Lebanese Ministry of Public
Health (the authoritative source, more than 300 killed and 1,600 wounded as
of Thursday afternoon — still rising) and the Civil Defense district-level
breakdown from Wednesday (a map a friend sent me that listed Beirut at 92
killed and the southern suburbs of Dahiyeh at 61). I cross-referenced both.

Then I computed the risk of death three different ways, because a single
number here is a lie. Any honest estimate has to carry its uncertainty with
it.

**Method 1: the obvious one.** Take the number of people killed in Greater
Beirut. Divide by the population of Greater Beirut. Multiply by a million.
That's your micromorts.

**Method 2: the physics check.** Treat each strike as having a lethal zone
roughly the size of a city block. Assume people are scattered evenly across
the city. How many strikes × how much lethal area ÷ how much city area = the
probability that any given person would find themselves in a lethal zone.
This is a deliberately naive upper bound. It ignores that strikes hit
buildings on purpose and that people are inside buildings on purpose. It
would be the right answer if the bombs fell on random coordinates and
everyone was standing outside.

**Method 3: the reality check.** Invert Method 2. Given the deaths we
actually observed, how large would the "effective" lethal zone per strike
have to be? If the answer is way bigger than a bomb's real lethal radius, it
means the strikes are hitting dense clusters of people (bad). If it's way
smaller, it means most strikes are missing civilians (less bad). This turns
Method 2's broken assumption into useful information.

I put all of this into a Jupyter notebook. I swept the numbers across every
reasonable choice of which source to trust, how to define "Beirut," how many
strikes to assume, and how lethal each strike was. Then I ran it.

## The answer

For an average resident of Greater Beirut, on Tuesday April 8, 2026, the risk
of being killed that day was roughly:

**82 micromorts.**

That's about 1 in 12,000. About **3.3 times** a normal day's risk of death
for a healthy thirty-year-old. Roughly the same daily risk of death that a
healthy sixty-year-old carries around everywhere, every day, without thinking
about it.

But the range matters more than the point estimate. Depending on which slice
of Beirut you live in:

| Area | Risk | Vs normal day |
|---|---:|---:|
| Beirut governorate (city proper) | ~302 µM | **~12×** |
| Dahiyeh (southern suburbs) | ~120 µM | ~4.8× |
| Greater Beirut (metro average) | ~82 µM | ~3.3× |

Twelve times a normal day. For a whole city, for a single day, distributed
evenly across everyone who lives there. That's the honest citywide floor.

## Why the honest citywide floor is not the real number

Here is where I have to be very careful, because the number above is the
kind of thing that can be decontextualized into either "see, it's not that
bad" or "see, it's a massacre," and both readings would be wrong.

The 82-micromort answer is a **mean across 2.2 million people**. It is the
number you get when you pretend the risk was spread out evenly, when it
absolutely was not.

The strikes hit specific buildings. They didn't land randomly across the
metropolitan area. A resident of a block that took a direct hit faced a risk
probably a hundred to a thousand times higher than the average. A resident
of a quiet neighborhood that wasn't targeted faced a risk close to a normal
day. The "average" collapses these two realities into one number that
belongs to neither person.

This is actually a general rule about casualty statistics. Citywide averages
are useful for scale. They are useless for personal decision-making. If you
want to know "how bad was April 8th for a city?" the number is 82
micromorts. If you want to know "how bad was it for *my brother, who lives
on this specific street?*" then 82 micromorts is the wrong question — and
the right question has an answer the numbers can't give you.

## What the number does tell you

So if the citywide average can't tell you about your brother, what is it
good for?

It tells you about **the scale of a day**. On a normal Tuesday in Beirut,
the entire population's collective risk of death is the background rate —
unremarkable, unaccounted, invisible. On this Tuesday, that rate multiplied
by somewhere between three and twelve, depending on where you draw the
boundary of "Beirut." For a whole city. For a single day of bombing, *after*
a ceasefire had been announced for an adjacent conflict.

It tells you that the average resident of the municipality of Beirut faced,
on Tuesday, the equivalent of **thirty years of normal-day risk compressed
into twenty-four hours**. (Twelve times a normal day, for one day, = twelve
days of risk; across the ~three hundred sixty-five days of a year that's not
thirty years, but you see what I mean. The compression is enormous.) And
that number is a lower bound, because the Health Ministry says the total is
still rising.

It tells you that this isn't an abstract thing to be debated in the
comments section of a news article. It is, statistically, something that
happened to a lot of real people at once, over a very small number of hours,
in a city where my cousins live.

## What the number doesn't tell you, and what nothing can

This number doesn't capture hospital-overload deaths that haven't happened
yet. It doesn't capture the people displaced from their homes, or the ones
whose homes won't be livable for months. It doesn't capture the damage to
water, electricity, the healthcare system. It doesn't capture what it does
to a child to hear a sonic boom at 2:30 PM on a Tuesday and not know if this
is the minute her school turns into the news. It doesn't capture the grief
that will propagate through families for a generation. It doesn't capture
the war before this day or the war after.

It is a single thin statistical sliver of a single day.

I computed it because the alternative was to sit with an undifferentiated
*bad* I couldn't reason about. And because I think the honest thing to do
with a hard feeling is to try to put bounds around it — not to make it
smaller, but to make it *the right size*. The right size of this feeling
turned out to be about twelve times a normal day.

I didn't feel better afterward. But I understood what I was afraid of with
slightly more precision. That was what I came for.

## The code

The whole analysis is on GitHub: **[github.com/sherifmak/beirut-risk-apr8-2026](https://github.com/sherifmak/beirut-risk-apr8-2026)**.
It's a single Jupyter notebook with three estimators, uncertainty sweeps,
and a comparison chart. If you disagree with my assumptions — about which
source to trust, how to define "Beirut," what counts as a strike — you can
clone it, change the inputs, and see what the numbers do. That's the whole
point of publishing the code and not just the answer.

If you found this useful, painful, or both, that's the appropriate response.

---

**Sources.** Lebanese Ministry of Public Health (via AP wire, Apr 9 2026).
Lebanese Civil Defense district map, Apr 8 2026. UN News. BBC. The full list
lives in the repo.

**Caveat I feel obligated to repeat once more at the end.** This is a
citywide statistical average. It is the wrong number to reason about any
individual person's safety, including yours, including anyone you love. For
individual-level decisions, the statistics have nothing to offer. For
understanding the scale of a day on which hundreds of people were killed in
a city my family lives in, they were the only tool I had.
