# Content Invariants — conference-Darin

Non-negotiable standards. Every skill and agent enforces these. Violations are always
flagged as CRITICAL, never as minor issues.

---

## Paper Standards

**INV-1 — Tables: booktabs only**
Use `\toprule`, `\midrule`, `\bottomrule`. Never `\hline`. Never vertical rules.
Rationale: IEEE double-column papers with vertical rules look unprofessional; booktabs is
the standard in top robotics venues.

**INV-2 — Quantitative results include mean ± std**
Every reported number that comes from repeated trials must include central tendency +
dispersion. Acceptable forms: `86.4 ± 2.7`, `86.4 (σ=2.7)`, `86.4 [82.1, 90.7]`.
Exception: if only one trial is reported, say so explicitly and acknowledge the limitation.

**INV-3 — Number of trials specified**
Every experiment table or figure must state N (trials, seeds, runs, episodes).
Minimum: stated in the table caption or a dedicated column.

**INV-4 — Hardware described completely**
Robot learning and manipulation papers must state: robot platform (manufacturer + model),
end-effector, sensors (camera model/position/resolution), control frequency, environment
setup (table size, object set). Navigation papers: vehicle platform, sensor suite, map area.
Humanoid papers: hardware revision, joint count, actuation type. If sim-only: simulator name,
version, physics settings.

**INV-5 — All baselines cited**
Every baseline in tables and comparisons must have a direct citation to its published paper.
Citing "BC" or "GAIL" without a reference is not acceptable.

**INV-6 — Figures legible in grayscale**
All figures must be readable when printed in black and white. Test: convert to grayscale,
verify that data series are still distinguishable (use markers and line styles, not color alone).

**INV-7 — Figure captions are autocontained**
A reader must understand what the figure shows without reading the body text. Captions must
include: what is plotted, what the axes represent (units), what the key takeaway is, and any
abbreviations used in the figure.

**INV-8 — Table captions are autocontained**
Same requirement as INV-7 for tables. Must include: what is measured, units, experimental
conditions, and what N is.

**INV-9 — Numbers in text match tables exactly**
If the text says "our method achieves 86.4%", the table must show 86.4, not 86.3 or 86.
Cross-reference every number mentioned in the body against the tables/figures. No exceptions.

**INV-10 — Acronyms defined on first appearance**
Define every acronym when first used: "behavior cloning (BC)". Use the acronym consistently
thereafter. Do not alternate between the full form and the acronym.

**INV-11 — Equations numbered; notation consistent**
All equations are numbered with `\begin{equation}` or `\begin{align}`. The same symbol must
not denote different quantities in different sections. Define all symbols before use.

**INV-12 — Ablation study covers key design choices**
Every non-trivial component of the proposed method must have a corresponding ablation row.
"Key design choice" = any component the authors claim is important for performance.
Ablation table follows the same INV-1, INV-2, INV-3 requirements.

**INV-13 — Reproducibility information present**
The paper (or supplementary) must state: training procedure, key hyperparameters
(learning rate, batch size, horizon, architecture summary), software stack (framework,
version), random seeds or statement that results are averaged over N seeds.

**INV-14 — Abstract: problem + approach + result**
The abstract must contain: (1) what problem is addressed, (2) what the approach is,
(3) at least one quantitative result. Abstracts that end without a concrete result
("we demonstrate the effectiveness of...") violate this invariant.

**INV-15 — Introduction contains numbered contribution list**
The introduction must list 2–4 specific, verifiable contributions in a numbered or bulleted
list. Generic statements ("we propose a novel approach") do not count as contributions.
Each contribution must be verifiable in the paper (experiment, table, figure, theorem).

**INV-16 — Sim-to-real scope stated explicitly**
Papers that test only in simulation must say so explicitly in abstract and introduction.
Papers that claim real-world validity from sim results must justify the sim-to-real gap.
Papers tested on a real robot must describe the real setup completely (INV-4).

**INV-17 — "First to" claims require evidence**
Any claim of being the first to do X must be supported by a literature search summary
(even if brief: "to the best of our knowledge, no prior work has addressed X [list searched
venues/years]"). Without this, reformulate: "We propose the first method that [specific
combination of properties]" where each property is individually documented.

**INV-18 — Causal claims require ablation support**
Statements like "the improvement is due to component X" or "removing Y causes degradation"
require ablation study results. Correlation is not causation. If ablation was not done,
rewrite as "performance degrades when Y is removed (ablation in Table III)."

**INV-19 — Figure titles in LaTeX captions, not inside plots**
Figure titles and axis labels must be typeset in LaTeX, not embedded in image files.
This ensures font consistency and PDF searchability.

**INV-20 — Code/data availability stated**
If code or datasets are released: include URL (anonymized for blind review if needed).
If not released: do not promise it ("code will be released") without user confirmation.
Acceptable: "Code available at [anonymous URL]" or no statement if not released.

---

## Quick-check matrix (for skills and agents)

When reviewing any section, check these first:

| # | Check | Pass condition |
|---|-------|---------------|
| 1 | Tables | Only booktabs rules |
| 2 | Results | Mean ± std everywhere |
| 3 | Trials | N stated in all tables |
| 4 | Hardware | Platform fully described |
| 5 | Baselines | All cited |
| 6 | Figures | Grayscale-legible |
| 7 | Captions | Autocontained |
| 8 | Numbers | Text matches tables |
| 9 | Acronyms | All defined on first use |
| 10 | Equations | All numbered |
| 11 | Ablation | Covers key components |
| 12 | Repro | Training details present |
| 13 | Abstract | Has quantitative result |
| 14 | Intro | Has numbered contributions |
| 15 | Sim scope | Explicitly stated |
