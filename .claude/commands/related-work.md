Execute the `/related-work` skill: synthesize a related work section and comparison table
from gathered literature.

Read the full protocol in `.claude/skills/related-work.md` before proceeding.
Follow every step exactly: group Central papers into 2–4 thematic subsections, frame each
paper relative to the proposed contribution, produce the LaTeX comparison table, and
dispatch Writer-Critic to verify the output.

Arguments: $ARGUMENTS

Prerequisite: at least 5 Central papers verified in `references/tracker.md`, with 1+ from
ICRA/IROS/CoRL/RSS/RA-L/T-RO. If this is not met, tell the user to run `/search-lit` first.
