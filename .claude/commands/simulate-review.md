Execute the `/simulate-review` skill: venue-calibrated peer review simulation.

Read the full protocol in `.claude/skills/simulate-review.md` before proceeding.
Dispatch Editor → Domain-Referee + Methods-Referee with venue-specific dispositions.
Produce a full simulation: desk review, referee assignment, detailed concerns, editorial
decision (Accept / Major Revision / Reject), and alternative venue recommendation if rejected.

Arguments: $ARGUMENTS

Specify venue with `--venue icra|iros|corl|rss|ral|tro`. Defaults to ICRA if not specified.
Use `--adversarial` for the strictest simulation (SKEPTICAL disposition throughout).
Reads draft from `drafts/`. Venue calibration from `.claude/references/venue-profiles.md`.
