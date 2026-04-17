Execute the `/revision-letter` skill: write a point-by-point response to reviewer comments.

Read the full protocol in `.claude/skills/revision-letter.md` before proceeding.
Categorize each reviewer comment (NEW-EXPERIMENT / REWRITE / CLARIFICATION / DISAGREE / MINOR),
draft a professional response for each using standard patterns, track all changes made in the
paper, and produce a complete revision letter ready for submission.

Arguments: $ARGUMENTS

Provide reviewer comments as input (paste inline or reference a file path).
The Writer agent drafts the letter. Does not promise unfeasible experiments, capitulate on
correct claims, or give vague responses.
