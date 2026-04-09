"""Generate visual assets for the blog post.

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


# =====================================================================
# 1. Event comparison, log scale (main chart for the body of the post)
# =====================================================================
events = [
    ("London 7/7 bombings (2005)",                7),
    ("Paris Nov 13 attacks (2015)",              11),
    ("Beirut Apr 8 2026 — Greater Beirut metro", 82),
    ("Beirut port explosion (Aug 4 2020)",       99),
    ("Peak COVID day, NYC (Apr 7 2020)",        100),
    ("9/11 — NYC metro basis",                  157),
    ("Beirut Apr 8 2026 — city proper",         302),
    ("9/11 — NYC city basis",                   372),
]
events.sort(key=lambda e: e[1])

fig, ax = plt.subplots(figsize=(11, 6), dpi=150)
labels = [e[0] for e in events]
values = [e[1] for e in events]
colors = [BEIRUT_RED if "Beirut Apr 8" in lbl else "#7a7a7a" for lbl in labels]

ax.barh(labels, values, color=colors, alpha=0.92)
ax.set_xscale("log")
ax.set_xlabel("Micromorts (log scale)  ·  1 µM = 1 in 1,000,000 chance of death")
ax.set_title("Daily risk of death: single-day events, for the population most exposed", pad=16)
ax.grid(axis="x", which="both", linestyle=":", alpha=0.4)

for v, lbl in zip(values, labels):
    ax.text(v * 1.08, lbl, f"{v} µM", va="center", fontsize=9, color="#222")

fig.text(
    0.01, 0.01,
    "Sources: Lebanese Ministry of Public Health, Civil Defense.  "
    "Analysis: github.com/sherifmak/beirut-risk-apr8-2026",
    fontsize=7, color="#666",
)
plt.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(OUT / "event_comparison_log.png", dpi=150, bbox_inches="tight")
plt.close(fig)


# =====================================================================
# 2. Head-to-head Beirut vs 9/11 (the central claim)
# =====================================================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
categories = [
    "Beirut city proper\nApril 8, 2026",
    "NYC city\n9/11 (Sept 11, 2001)",
]
values_h = [302, 372]
colors_h = [BEIRUT_RED, "#555"]

bars = ax.bar(categories, values_h, color=colors_h, width=0.5, alpha=0.92)
ax.set_ylabel("Micromorts  (1 in 1,000,000)")
ax.set_title("Average daily risk of death, single-day events", fontsize=14, pad=16)
ax.grid(axis="y", linestyle=":", alpha=0.4)
ax.set_ylim(0, 460)

for bar, v in zip(bars, values_h):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        v + 12,
        f"{v} µM\n≈ 1 in {1_000_000 // v:,}",
        ha="center", fontsize=11, color="#111",
    )

fig.text(
    0.5, 0.02,
    "Same math, same unit. Beirut city proper on Apr 8 carried ~80% the per-capita daily risk of death that NYC city carried on 9/11.",
    ha="center", fontsize=9, color="#555", style="italic",
)
plt.tight_layout(rect=(0, 0.06, 1, 1))
fig.savefig(OUT / "beirut_vs_911.png", dpi=150, bbox_inches="tight")
plt.close(fig)


# =====================================================================
# 3. By Beirut scope — three sub-populations
# =====================================================================
scopes = [
    "Greater Beirut\nmetro (2.2M)",
    "Dahiyeh\n(southern suburbs, 600k)",
    "Beirut governorate\n(city proper, 361k)",
]
values_b = [82, 120, 302]
colors_b = ["#d35a5a", "#a82828", BEIRUT_RED]

fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
bars = ax.bar(scopes, values_b, color=colors_b, width=0.55, alpha=0.92)
ax.set_ylabel("Micromorts  (1 in 1,000,000)")
ax.set_title("April 8, 2026: Beirut daily risk of death by area", fontsize=14, pad=16)
ax.grid(axis="y", linestyle=":", alpha=0.4)
ax.axhline(25, color="#444", linestyle=":", alpha=0.6,
           label="Normal day, healthy 30yo (~25 µM)")
ax.legend(loc="upper left", frameon=False, fontsize=9)
ax.set_ylim(0, 360)

for bar, v in zip(bars, values_b):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        v + 8,
        f"{v} µM\n({v/25:.1f}× normal)",
        ha="center", fontsize=10, color="#111",
    )

fig.text(
    0.01, 0.01,
    "The citywide average hides block-level variance that can be 100–1,000× higher.",
    fontsize=8, color="#666", style="italic",
)
plt.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(OUT / "beirut_by_scope.png", dpi=150, bbox_inches="tight")
plt.close(fig)


# =====================================================================
# 4. Social card — Twitter/X 1200x675
# =====================================================================
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=150)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")
fig.patch.set_facecolor("white")

ax.text(0.5, 8.4, "Beirut just had a 9/11-scale day",
        fontsize=32, fontweight="bold", color="#111", va="center")

ax.text(0.5, 5.8, "302 µM", fontsize=56, fontweight="bold", color=BEIRUT_RED, va="center")
ax.text(3.4, 5.8, "Beirut city proper\nApril 8, 2026",
        fontsize=13, color="#444", va="center")

ax.text(0.5, 3.2, "372 µM", fontsize=56, fontweight="bold", color="#555", va="center")
ax.text(3.4, 3.2, "NYC city\n9/11 (2001)",
        fontsize=13, color="#444", va="center")

ax.text(0.5, 1.2, "Average daily risk of death. Same math, same unit.",
        fontsize=12, color="#444", style="italic", va="center")
ax.text(0.5, 0.45,
        "sheriff.substack.com   ·   github.com/sherifmak/beirut-risk-apr8-2026",
        fontsize=9, color="#888", va="center")

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

ax.text(5, 9.2, "Beirut just had",
        fontsize=30, fontweight="bold", color="#111", va="center", ha="center")
ax.text(5, 8.3, "a 9/11-scale day",
        fontsize=30, fontweight="bold", color="#111", va="center", ha="center")

ax.text(5, 6.3, "302 µM", fontsize=64, fontweight="bold",
        color=BEIRUT_RED, va="center", ha="center")
ax.text(5, 5.35, "Beirut city proper, April 8, 2026",
        fontsize=12, color="#444", va="center", ha="center")

ax.text(5, 3.9, "vs 372 µM", fontsize=36, fontweight="bold",
        color="#555", va="center", ha="center")
ax.text(5, 3.1, "NYC city, 9/11 (2001)",
        fontsize=12, color="#444", va="center", ha="center")

ax.text(5, 1.6, "same math · same unit",
        fontsize=11, color="#444", style="italic", va="center", ha="center")
ax.text(5, 0.7, "sheriff.substack.com",
        fontsize=10, color="#888", va="center", ha="center")

fig.savefig(OUT / "social_card_instagram.png", dpi=120, bbox_inches="tight", facecolor="white")
plt.close(fig)


# =====================================================================
# 6. Sheet: All Beirut-relevant numbers at a glance
# =====================================================================
fig, ax = plt.subplots(figsize=(11, 6), dpi=150)
ax.axis("off")
fig.patch.set_facecolor("white")

title = "April 8, 2026 — Beirut risk by area, next to familiar anchors"
ax.text(0.02, 0.95, title, fontsize=16, fontweight="bold", color="#111",
        transform=ax.transAxes)

table_data = [
    ("Normal day, healthy 30-year-old",                "",          "25 µM",  "1 in 40,000"),
    ("London 7/7 bombings (2005)",                     "Londoner",  "7 µM",   "1 in 143,000"),
    ("Paris Nov 13 attacks (2015)",                    "Parisian",  "11 µM",  "1 in 91,000"),
    ("Beirut Apr 8 2026 — Greater Beirut metro",       "metro",    "82 µM",  "1 in 12,200"),
    ("Beirut port explosion (2020)",                   "Beiruti",   "99 µM",  "1 in 10,100"),
    ("Peak COVID day, NYC (Apr 7 2020)",               "New Yorker","100 µM", "1 in 10,000"),
    ("Beirut Apr 8 2026 — Dahiyeh",                    "resident", "120 µM", "1 in 8,300"),
    ("9/11 — NYC metro basis",                         "metro",    "157 µM", "1 in 6,400"),
    ("Beirut Apr 8 2026 — Beirut governorate",         "city proper", "302 µM", "1 in 3,300"),
    ("9/11 — NYC city basis",                          "city",     "372 µM", "1 in 2,700"),
]

y_start = 0.84
row_h   = 0.075

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
    "All figures: deaths ÷ population most exposed × 1,000,000.  "
    "Sources: Lebanese Ministry of Public Health, Civil Defense, contemporary reporting. "
    "Full methodology: github.com/sherifmak/beirut-risk-apr8-2026",
    fontsize=7, color="#666",
)
fig.savefig(OUT / "comparison_sheet.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)


print(f"Generated assets in {OUT}")
for f in sorted(OUT.glob("*.png")):
    print(f"  {f.name}")
