Execute the `/check-claims` skill: claims-evidence audit of a paper section or full draft.

Read the full protocol in `.claude/skills/check-claims.md` before proceeding.
Dispatch Writer-Critic focused on: numbers consistency (INV-9 audit), quantitative claims
without supporting numbers, causal claims without ablation support, novelty claims without
literature evidence, and [TODO: cite] inventory.

Arguments: $ARGUMENTS

If no arguments are provided, audit the full draft in `drafts/`.
Report all findings as CRITICAL / MAJOR / MINOR with exact location and fix required.
