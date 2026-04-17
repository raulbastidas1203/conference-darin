Execute the `/ieee-checklist` skill: pre-submission verification against IEEE standards
and venue-specific requirements.

Read the full protocol in `.claude/skills/ieee-checklist.md` before proceeding.
Check: page count, template compliance, all 20 content invariants, reference format,
figure/table standards, acronym definitions, anonymization (for double-blind venues),
and any venue-specific requirements. Report as FAILS / PASSES / VERIFY.

Arguments: $ARGUMENTS

Specify venue with `--venue icra|iros|corl|rss|ral|tro` to apply venue-specific checks.
Modes: `--mode outline` (before writing) / `--mode content` (during writing) /
`--mode format` (pre-submission final). Defaults to `--mode format` if not specified.
