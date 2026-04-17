Execute the `/search-lit` skill: systematic literature search and classification for a robotics topic.

Read the full protocol in `.claude/skills/search-lit.md` before proceeding.
Follow every step exactly: construct queries, search Tier 1–4 sources, classify papers as
Central/Related/Marginal, update `references/tracker.md`, dispatch Librarian-Critic,
and produce the standard output with coverage gaps and NEED-PDF list.

Arguments: $ARGUMENTS

If no arguments are provided, check `drafts/` for an active paper to infer the topic,
or ask the user for the topic before proceeding.
