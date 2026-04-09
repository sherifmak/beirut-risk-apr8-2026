# TL;DR summaries

Different lengths for different uses — email previews, social platforms,
conversation.

---

## One sentence (Substack email subject-line supporting text)

> For the average resident of Beirut city proper, April 8, 2026 carried
> roughly the same daily risk of death that the average New Yorker carried
> on September 11, 2001.

---

## One paragraph (Substack preview, LinkedIn, Facebook)

> On April 8, 2026, Israel launched its largest wave of airstrikes on
> Lebanon of the war — 100 targets in 10 minutes, central Beirut without
> warning, 300+ killed, 1,600+ wounded. I wanted a number I could reason
> about, not a headline I could only feel. Computing the daily risk of
> death in micromorts gives roughly **302 µM** for the average Beirut
> city-proper resident — within a rounding error of the **~372 µM** that
> the average New Yorker faced on 9/11. Same math, same unit, same order
> of magnitude. The full three-method analysis, with uncertainty bounds
> and sources, is on GitHub.

---

## Elevator pitch (verbal, ~30 seconds)

> On Tuesday, Israel did the largest set of airstrikes on Lebanon of the
> war. I have family there and I wanted to know what the actual risk of
> dying was for an average Beirut resident that day — in a unit I could
> compare to other things. So I built a Jupyter notebook with three
> different ways to compute it. All three agreed: for a resident of
> Beirut city proper, the daily risk that day was roughly the same as
> 9/11 was for the average New Yorker. About 302 micromorts — one in
> 3,300. I published the code, the methodology, and the blog post on
> GitHub and Substack.

---

## Technical abstract (for Hacker News, academic contexts)

> Estimates the probability of death for an average Beirut resident
> during the April 8 2026 Israeli strikes on Lebanon, using three
> independent estimators: (1) empirical base rate, (2) physics-based
> strike-density model with lethal-footprint assumption, (3) back-solved
> effective lethality. Data from the Lebanese Ministry of Public Health
> (authoritative nationwide total) decomposed by Civil Defense
> district-level shares. Central estimate for Greater Beirut metro:
> ~82 µM. For Beirut governorate (city proper): ~302 µM. The latter is
> within factor ~1.2× of 9/11 for the average NYC city resident (~372
> µM) on the same per-capita basis. Reproducible notebook and full
> sensitivity sweeps in the repository.

---

## One line for a text message

> I did the math. Tuesday in Beirut was, for the average person in the
> city, about as dangerous as 9/11 was for the average New Yorker.

---

## Email subject lines (A/B options)

- "Beirut just had a 9/11-scale day"
- "The math behind what happened in Beirut on Tuesday"
- "Tuesday was a 9/11 for a city the size of Beirut"
- "I computed the risk of dying in Beirut this week. Here's the answer."
- "What 9/11 and Tuesday in Beirut have in common, statistically"
