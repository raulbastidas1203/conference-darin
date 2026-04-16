# MEMORY — conference-Darin

Persistent learning log. Updated after each session with non-obvious lessons,
calibrations, and decisions that should survive context compression.

Format: `[LEARN:category] — lesson`

---

## Workflow Patterns

[LEARN:workflow] — Always read existing drafts/sections before suggesting changes. Never rewrite
without first understanding what is there.

[LEARN:workflow] — Phase ordering matters: Methodology before Introduction. Abstract last.
A good abstract requires knowing what experiments actually showed.

[LEARN:workflow] — When a user provides a new paper PDF in /papers/, update references/tracker.md
immediately and add a reading note in /lit-notes/.

[LEARN:workflow] — Do not invent competitor experiments. If a paper does not report a metric,
it does not have that metric. Mark as not reported (—) in comparison tables.

---

## Literature Handling

[LEARN:literature] — Semantic Scholar API can return papers with zero citations that are real
but very new. Do not filter on citation count alone; use venue + year.

[LEARN:literature] — DBLP is reliable for CS/robotics venue metadata. If DBLP has a paper,
treat venue/year as VERIFIED.

[LEARN:literature] — arXiv papers that appear in ICRA/IROS/CoRL proceedings should be cited
as the conference version, not arXiv. Prioritize published DOI.

[LEARN:literature] — Conference names in robotics: use ICRA, IROS, CoRL, RSS — never add
"the" before them (not "the ICRA").

[LEARN:literature] — "Concurrent work" framing: if a competitor arXiv paper appeared within
3 months of submission, it can be acknowledged without extensive comparison.

---

## IEEE Style

[LEARN:style] — "Novel" without quantitative evidence triggers immediate reviewer skepticism.
Replace with specific claims: "We demonstrate X on Y for the first time, achieving Z."

[LEARN:style] — Passive voice for method description ("The policy is trained using...").
Active voice for contributions ("We propose...", "We show that...").

[LEARN:style] — Reviewer pet peeve in robotics: sim-only papers claiming real-world relevance
without real-robot validation. Always scope claims precisely to what was tested.

[LEARN:style] — Table captions go ABOVE the table in IEEE format.
Figure captions go BELOW the figure. This is a frequent LaTeX mistake.

[LEARN:style] — "State-of-the-art" requires direct quantitative comparison in the same paper.
If not compared directly, use "prior work" or "existing methods."

---

## Agent Calibration

[LEARN:agents] — Librarian-Critic should not run new searches. Its role is to verify the
Librarian's output only. If it identifies gaps, the fix is to run Librarian again with
refined queries, not for Critic to search independently.

[LEARN:agents] — Writer-Critic escalates numbers mismatches to the user directly, not to
the Writer, because number errors can indicate underlying result problems.

[LEARN:agents] — Methods-Referee CRITICAL finding = paper cannot be submitted without
addressing it. Do not submit if Methods-Referee has an unresolved CRITICAL.

---

## Venue Calibration

[LEARN:venues] — CoRL reviewers place high weight on real-robot validation. A sim-only
paper needs very strong learning contribution and a compelling argument for why sim is sufficient.

[LEARN:venues] — ICRA is broad; IROS is slightly more systems-focused. Both accept incremental
but solid work. CoRL and RSS have higher novelty bars.

[LEARN:venues] — RA-L allows slightly more incremental contributions than conferences, but
real-robot results are still expected for manipulation/locomotion papers.

---

## Project-Specific Notes

<!-- Add project-specific calibrations here as papers are worked on -->
<!-- Format: [PROJECT:papername] — note -->
