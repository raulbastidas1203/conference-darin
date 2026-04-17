Execute the `/analyze-gaps` skill: map the research landscape, identify saturated vs. open
directions, and propose concrete, evaluable paper directions from gathered literature.

Read the full protocol in `.claude/skills/analyze-gaps.md` before proceeding.
Follow every phase exactly: terrain mapping, saturation diagnosis, gap identification,
direction generation (exactly 3–5), comparative ranking, and a single recommendation
with a concrete first step and early invalidation test.

Arguments: $ARGUMENTS

Prerequisite: `references/tracker.md` must have at least 5 papers.
If the tracker is empty, tell the user to run `/search-lit` first.
Save output to `outputs/gap-analysis-<YYYYMMDD>.md`.
