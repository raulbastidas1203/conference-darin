Execute the `/review-draft` skill: full critical review of a paper draft.

Read the full protocol in `.claude/skills/review-draft.md` before proceeding.
Dispatch Domain-Referee, Methods-Referee, and Writer-Critic. Compute the weighted aggregate
score (15% literature coverage, 20% positioning, 20% methodology clarity, 30% experimental
rigor, 15% writing/format). Report all CRITICAL, MAJOR, and MINOR issues with severity labels.

Arguments: $ARGUMENTS

Reads draft from `drafts/` unless a specific file is given in arguments.
Save output to `outputs/review-<YYYYMMDD>-<score>.md`.
Gate thresholds: ≥70 draft-ready / ≥80 revision-ready / ≥90 submission-ready.
