"""Generate visual assets for the project.

Run from the project root with the venv activated:
    python assets/generate_assets.py

Outputs PNG files to assets/charts/.
"""
from pathlib import Path
import matplotlib.pyplot as plt

OUT = Path(__file__).parent / "charts"
OUT.mkdir(exist_ok=True)

# Clean, serious visual style
plt.rcParams.update({
    "font.family":       "sans-serif",
    "font.sans-serif":   ["Helvetica", "Arial", "DejaVu Sans"],
    "axes.edgecolor":    "#444",
    "axes.labelcolor":   "#222",
    "xtick.color":       "#222",
    "ytick.color":       "#222",
    "axes.titlecolor":   "#111",
    "axes.titleweight":  "bold",
    "savefig.facecolor": "white",
    "figure.facecolor":  "white",
})

BEIRUT_RED = "#8b0000"

# Corrected reference numbers (per-capita daily micromort figures)
#   9/11 NYC numerator: 2,753 (NYC-only; excludes Pentagon 184 + Shanksville 40)
#   COVID NYC Apr 7:    598 (NYC DOH confirmed)
#   Port explosion:     ~220 killed (midpoint of 218–235 disputed range)
#
# Beirut Apr 8 2026 figures are Monte Carlo medians from the notebook:
#   Greater Beirut metro: ~80 µM (90% CI [69, 97])
#   Dahiyeh:              ~191 µM (90% CI [163, 235])
#   Beirut governorate:   ~266 µM (90% CI [228, 327])


# =====================================================================
# 1. Event comparison, log scale (main chart for the body of the post)
# =====================================================================
events = [
    ("London 7/7 bombings (2005)",                7),
    ("Paris Nov 13 attacks (2015)",              11),
    ("Peak COVID day, NYC (Apr 7 2020)",         75),
    ("Beirut Apr 8 2026 — Greater Beirut metro", 80),
    ("Beirut port explosion (Aug 4 2020)",      100),
    ("9/11 — NYC metro basis",                  145),
    ("Beirut Apr 8 2026 — Dahiyeh",             191),
    ("Beirut Apr 8 2026 — Beirut governorate",  266),
    ("9/11 — NYC city basis",                   344),
]
events.sort(key=lambda e: e[1])

fig, ax = plt.subplots(figsize=(11, 6.5), dpi=150)
labels = [e[0] for e in events]
values = [e[1] for e in events]
colors = [BEIRUT_RED if "Beirut Apr 8" in lbl else "#7a7a7a" for lbl in labels]

ax.barh(labels, values, color=colors, alpha=0.92)
ax.set_xscale("log")
ax.set_xlabel("Micromorts (log scale)  ·  1 µM = 1 in 1,000,000 chance of death")
ax.set_title("Daily risk of death: per-capita, for the population most exposed", pad=16)
ax.grid(axis="x", which="both", linestyle=":", alpha=0.4)

for v, lbl in zip(values, labels):
    ax.text(v * 1.08, lbl, f"{v} µM", va="center", fontsize=9, color="#222")

fig.text(
    0.01, 0.01,
    "Beirut figures: Monte Carlo medians, Apr 9 2026 preliminary Health Ministry + Civil Defense data.  "
    "9/11 numerator: 2,753 NYC-only victims.  "
    "github.com/sherifmak/beirut-risk-apr8-2026",
    fontsize=7, color="#666",
)
plt.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(OUT / "event_comparison_log.png", dpi=150, bbox_inches="tight")
plt.close(fig)


# =====================================================================
# 2. Head-to-head Beirut vs 9/11 — both denominator pairs (robustness)
# =====================================================================
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(13, 6), dpi=150)

# Metro-vs-metro
categories_m = [
    "Greater Beirut metro\nApr 8, 2026",
    "NYC metro\n9/11 (Sept 11, 2001)",
]
values_m = [80, 145]
colors_m = [BEIRUT_RED, "#555"]

bars_m = ax_left.bar(categories_m, values_m, color=colors_m, width=0.5, alpha=0.92)
# Add error bar for Beirut (90% CI [69, 97])
ax_left.errorbar(0, 80, yerr=[[80-69], [97-80]], color="#333", capsize=8, lw=1.5)
ax_left.set_ylabel("Micromorts  (1 in 1,000,000)")
ax_left.set_title("Metro-vs-metro basis\n(consistent denominator)", fontsize=12, pad=14)
ax_left.grid(axis="y", linestyle=":", alpha=0.4)
ax_left.set_ylim(0, 400)

for bar, v in zip(bars_m, values_m):
    ax_left.text(bar.get_x() + bar.get_width() / 2, v + 12,
                 f"{v} µM\n≈ 1 in {1_000_000 // v:,}",
                 ha="center", fontsize=11, color="#111")

# City-proper-vs-city-proper
categories_c = [
    "Beirut governorate\nApr 8, 2026",
    "NYC city\n9/11 (Sept 11, 2001)",
]
values_c = [266, 344]
colors_c = [BEIRUT_RED, "#555"]

bars_c = ax_right.bar(categories_c, values_c, color=colors_c, width=0.5, alpha=0.92)
ax_right.errorbar(0, 266, yerr=[[266-228], [327-266]], color="#333", capsize=8, lw=1.5)
ax_right.set_ylabel("Micromorts  (1 in 1,000,000)")
ax_right.set_title("City-proper basis\n(most aggressive matched pair)", fontsize=12, pad=14)
ax_right.grid(axis="y", linestyle=":", alpha=0.4)
ax_right.set_ylim(0, 400)

for bar, v in zip(bars_c, values_c):
    ax_right.text(bar.get_x() + bar.get_width() / 2, v + 12,
                  f"{v} µM\n≈ 1 in {1_000_000 // v:,}",
                  ha="center", fontsize=11, color="#111")

fig.suptitle("Beirut Apr 8 2026 vs NYC 9/11 — per-capita daily risk of death",
             fontsize=14, fontweight="bold", y=0.98)
fig.text(0.5, 0.02,
         "Error bars show Monte Carlo 90% credible intervals for Beirut. On both denominator choices, the comparison is in the same neighborhood.",
         ha="center", fontsize=9, color="#555", style="italic")
plt.tight_layout(rect=(0, 0.05, 1, 0.94))
fig.savefig(OUT / "beirut_vs_911.png", dpi=150, bbox_inches="tight")
plt.close(fig)


# =====================================================================
# 3. By Beirut scope — three sub-populations with CIs
# =====================================================================
scopes = [
    "Greater Beirut\nmetro (2.2M)",
    "Dahiyeh\n(S. suburbs, 400k)",
    "Beirut governorate\n(city proper, 361k–433k)",
]
values_b = [80, 191, 266]
lowers_b = [80-69, 191-163, 266-228]
uppers_b = [97-80, 235-191, 327-266]
colors_b = ["#d35a5a", "#a82828", BEIRUT_RED]

fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
bars = ax.bar(scopes, values_b, color=colors_b, width=0.55, alpha=0.92,
              yerr=[lowers_b, uppers_b], ecolor="#333", capsize=6)
ax.set_ylabel("Micromorts  (1 in 1,000,000)")
ax.set_title("April 8, 2026: Beirut per-capita daily risk (Monte Carlo median + 90% CI)",
             fontsize=13, pad=16)
ax.grid(axis="y", linestyle=":", alpha=0.4)
ax.axhline(25, color="#444", linestyle=":", alpha=0.6,
           label="Normal day, healthy 30yo (~25 µM)")
ax.axhline(145, color="#555", linestyle="--", alpha=0.5,
           label="9/11 NYC metro (~145 µM)")
ax.axhline(344, color="#222", linestyle="--", alpha=0.5,
           label="9/11 NYC city (~344 µM)")
ax.legend(loc="upper left", frameon=False, fontsize=9)
ax.set_ylim(0, 420)

for bar, v in zip(bars, values_b):
    ax.text(bar.get_x() + bar.get_width() / 2, v + 30,
            f"{v} µM\n({v/25:.1f}× normal)",
            ha="center", fontsize=10, color="#111")

fig.text(
    0.01, 0.01,
    "The citywide average hides block-level variance that can be 100–1,000× higher.",
    fontsize=8, color="#666", style="italic",
)
plt.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(OUT / "beirut_by_scope.png", dpi=150, bbox_inches="tight")
plt.close(fig)


# =====================================================================
# 4. Social card — Twitter/X 1200x675 (metro-vs-metro LEAD)
# =====================================================================
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=150)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")
fig.patch.set_facecolor("white")

ax.text(0.5, 8.8, "Beirut just had a 9/11-scale day",
        fontsize=30, fontweight="bold", color="#111", va="center")
ax.text(0.5, 8.0, "per capita",
        fontsize=18, color="#8b0000", style="italic", va="center")

# Metro basis (primary, consistent denominator)
ax.text(0.5, 5.6, "80 µM", fontsize=48, fontweight="bold", color=BEIRUT_RED, va="center")
ax.text(2.6, 5.8, "Greater Beirut metro — Apr 8, 2026",
        fontsize=12, color="#333", va="center")
ax.text(2.6, 5.2, "~55% of NYC 9/11 (metro basis)",
        fontsize=10, color="#666", va="center", style="italic")

ax.text(0.5, 3.4, "145 µM", fontsize=48, fontweight="bold", color="#555", va="center")
ax.text(2.6, 3.6, "NYC metro — Sept 11, 2001",
        fontsize=12, color="#333", va="center")
ax.text(2.6, 3.0, "2,753 NYC-specific victims ÷ 19M metro population",
        fontsize=10, color="#666", va="center", style="italic")

# Footer
ax.text(0.5, 1.3,
        "Per-capita daily risk of death, consistent metro denominator.",
        fontsize=11, color="#444", va="center")
ax.text(0.5, 0.8,
        "Numerical comparison, not a moral one. Citywide average — hides block-level variance.",
        fontsize=9, color="#888", style="italic", va="center")
ax.text(0.5, 0.25,
        "github.com/sherifmak/beirut-risk-apr8-2026   ·   github.com/sherifmak/beirut-risk-apr8-2026",
        fontsize=8, color="#888", va="center")

fig.savefig(OUT / "social_card_twitter.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)


# =====================================================================
# 5. Social card — Instagram 1080x1080 (square)
# =====================================================================
fig, ax = plt.subplots(figsize=(9, 9), dpi=120)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")
fig.patch.set_facecolor("white")

ax.text(5, 9.3, "Beirut just had",
        fontsize=28, fontweight="bold", color="#111", va="center", ha="center")
ax.text(5, 8.5, "a 9/11-scale day",
        fontsize=28, fontweight="bold", color="#111", va="center", ha="center")
ax.text(5, 7.8, "per capita",
        fontsize=18, color=BEIRUT_RED, style="italic", va="center", ha="center")

ax.text(5, 6.0, "80 µM", fontsize=56, fontweight="bold",
        color=BEIRUT_RED, va="center", ha="center")
ax.text(5, 5.05, "Greater Beirut metro, April 8, 2026",
        fontsize=11, color="#444", va="center", ha="center")

ax.text(5, 3.7, "vs 145 µM", fontsize=36, fontweight="bold",
        color="#555", va="center", ha="center")
ax.text(5, 2.9, "NYC metro, 9/11 (2001)",
        fontsize=11, color="#444", va="center", ha="center")

ax.text(5, 1.6, "Per-capita daily risk · same denominator",
        fontsize=10, color="#444", style="italic", va="center", ha="center")
ax.text(5, 1.0, "Numerical comparison, not moral",
        fontsize=9, color="#888", style="italic", va="center", ha="center")
ax.text(5, 0.4, "github.com/sherifmak/beirut-risk-apr8-2026",
        fontsize=9, color="#888", va="center", ha="center")

fig.savefig(OUT / "social_card_instagram.png", dpi=120, bbox_inches="tight", facecolor="white")
plt.close(fig)


# =====================================================================
# 6. Comparison sheet (text table rendered as image)
# =====================================================================
fig, ax = plt.subplots(figsize=(11, 7), dpi=150)
ax.axis("off")
fig.patch.set_facecolor("white")

title = "April 8, 2026 — Beirut per-capita daily risk, next to familiar anchors"
ax.text(0.02, 0.96, title, fontsize=15, fontweight="bold", color="#111",
        transform=ax.transAxes)
ax.text(0.02, 0.92, "All values computed as deaths ÷ population most exposed × 1,000,000",
        fontsize=9, color="#666", style="italic", transform=ax.transAxes)

table_data = [
    ("Normal day, healthy 30-year-old",                "",            "25 µM",  "1 in 40,000"),
    ("London 7/7 bombings (2005)",                     "Londoner",    "7 µM",   "1 in 144,000"),
    ("Paris Nov 13 attacks (2015)",                    "Parisian",    "11 µM",  "1 in 92,000"),
    ("Peak COVID day, NYC (Apr 7 2020, DOH)",          "New Yorker",  "75 µM",  "1 in 13,400"),
    ("Beirut Apr 8 2026 — Greater Beirut metro",       "metro",       "~80 µM",  "1 in 12,500"),
    ("Beirut port explosion (2020)",                   "Beiruti",    "100 µM",  "1 in 10,000"),
    ("9/11 — NYC metro basis",                         "metro",      "145 µM",  "1 in 6,900"),
    ("Beirut Apr 8 2026 — Dahiyeh",                    "resident",  "~191 µM",  "1 in 5,200"),
    ("Beirut Apr 8 2026 — Beirut governorate",         "city proper","~266 µM", "1 in 3,800"),
    ("9/11 — NYC city basis",                          "city",       "344 µM",  "1 in 2,900"),
]

y_start = 0.84
row_h   = 0.065

ax.text(0.02, y_start + 0.04, "Event", fontweight="bold", fontsize=10, color="#333", transform=ax.transAxes)
ax.text(0.56, y_start + 0.04, "For",   fontweight="bold", fontsize=10, color="#333", transform=ax.transAxes)
ax.text(0.72, y_start + 0.04, "Risk",  fontweight="bold", fontsize=10, color="#333", transform=ax.transAxes)
ax.text(0.86, y_start + 0.04, "Odds",  fontweight="bold", fontsize=10, color="#333", transform=ax.transAxes)

for i, (ev, who, risk, odds) in enumerate(table_data):
    y = y_start - i * row_h
    is_beirut = "Beirut Apr 8" in ev
    color = BEIRUT_RED if is_beirut else "#222"
    weight = "bold" if is_beirut else "normal"
    ax.text(0.02, y, ev,   fontsize=9, color=color, fontweight=weight, transform=ax.transAxes)
    ax.text(0.56, y, who,  fontsize=9, color=color, fontweight=weight, transform=ax.transAxes)
    ax.text(0.72, y, risk, fontsize=9, color=color, fontweight=weight, transform=ax.transAxes)
    ax.text(0.86, y, odds, fontsize=9, color=color, fontweight=weight, transform=ax.transAxes)

fig.text(
    0.02, 0.02,
    "Beirut figures: Monte Carlo medians (Apr 9 2026 preliminary data).  "
    "9/11 numerator: 2,753 NYC-only victims.  "
    "Full methodology + code: github.com/sherifmak/beirut-risk-apr8-2026",
    fontsize=7, color="#666",
)
fig.savefig(OUT / "comparison_sheet.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)


print(f"Generated assets in {OUT}")
for f in sorted(OUT.glob("*.png")):
    print(f"  {f.name}")
