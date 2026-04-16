# Skill: /revision-letter

Write a point-by-point response to reviewer comments. Dispatches Writer for letter drafting.

## Invocation

```
/revision-letter [<reviewer comments file>]
```

**Examples:**
```
/revision-letter                               # Looks for comments in /outputs/reviewer-comments.md
/revision-letter outputs/iros2025-reviews.md
```

## What this skill does

1. **Reads** reviewer comments (from specified file or asks user to paste them)
2. **Reads** current paper draft to understand what changes were made
3. **Categorizes** each comment: NEW-EXPERIMENT / REWRITE / CLARIFICATION / DISAGREE / MINOR
4. **Dispatches Writer** to draft the response letter
5. **Produces** response letter + change tracker
6. **Saves** to `outputs/revision-letter-<date>.md`

## Comment categorization

| Category | Definition | Action |
|----------|-----------|--------|
| NEW-EXPERIMENT | Requests additional experiment or analysis | Requires user decision: do or justify exclusion |
| REWRITE | Requests structural revision to a section | Writer rewrites the section |
| CLARIFICATION | Requests clearer explanation | Writer adds clarification |
| DISAGREE | Reviewer is factually wrong or off-base | State disagreement with evidence |
| MINOR | Wording, formatting, citations | Writer makes direct fix |

**For NEW-EXPERIMENT:** Always check if the experiment is feasible and strengthening before
agreeing. If not feasible: explain why and offer a concrete alternative (ablation in sim,
scoping clarification, additional discussion).

## Writer protocol (runs as part of this skill)

See `.claude/agents/writer.md` for full protocol.

### Response letter structure

```
Dear Editor / Program Chairs,

We sincerely thank the reviewers for their careful reading of our manuscript
"[PAPER TITLE]" and for their constructive feedback. We have carefully addressed
all concerns as detailed below.

A summary of all changes is provided at the end of this letter. All modifications
are highlighted in [blue / track-changes] in the revised manuscript.

Sincerely,
The Authors

────────────────────────────────────────────────────

RESPONSE TO REVIEWER 1

────────────────────────────────────────────────────

Comment R1.1:
> [Exact text of reviewer comment, indented]

Response:
[Direct, specific response. Always answer: (a) what you did, (b) why.]

Change: [Sec. X, para N]: [Description of what was added/changed. Quote revised text if short.]

────────────────────────────────────────────────────
...
```

### Standard response patterns

**When you agree and made the change:**
> "We agree with this observation. We have [specific action] in Section [X].
> The revised text now reads: '[quote]'."

**When you agree partially:**
> "We partially agree with this concern. [Part where reviewer is right → fix].
> However, [part where paper is correct → evidence]. To avoid ambiguity,
> we have added a clarifying sentence in Section [X]: '[quote]'."

**When you disagree (requires evidence):**
> "We respectfully disagree with this characterization. As shown in [Table/Fig N],
> our method [evidence]. To prevent further confusion, we have added the following
> clarification to Section [X]: '[quote]'."

**When an experiment was requested but is not feasible:**
> "We appreciate this suggestion. Unfortunately, [concrete reason: hardware not available /
> outside the scope of this work / would require N months beyond revision deadline].
> To address the underlying concern, we [alternative: added ablation / scoped claims /
> added discussion in Section VI]: '[quote]'."

**When reviewer suggests a citation:**
> "We thank the reviewer for pointing us to [Ref]. We have added this citation in
> Section [X] and note the key difference from our work: [1–2 sentences comparing]."

### Things the Writer does NOT do in revision letters

- Promise experiments that will not be done
- Capitulate on correct claims to appease reviewer
- Ignore any sub-point within a reviewer comment
- Be vague about what changed ("we have improved the paper")
- Invent changes that were not actually made

## Output format

```markdown
## /revision-letter
Paper: [title]
Date: <date>
Reviewers: R1 / R2 / R3

---

## Comment categorization

| Comment | Category | Feasible? | Action |
|---------|---------|---------|--------|
| R1.1 | CLARIFICATION | Yes | Writer rewrites para 2, Sec III |
| R1.2 | NEW-EXPERIMENT | Yes | Add ablation on component X |
| R2.1 | DISAGREE | — | Evidence from Table II |
| R2.2 | MINOR | Yes | Fix citation format |

---

## Response letter (full text)

[Complete letter text, ready to copy]

---

## Summary of changes table (for end of letter)

| # | Change | Location | Motivated by |
|---|--------|----------|-------------|
| 1 | Added ablation on component X | Table III, Sec IV-C | R1.2, R2.1 |
| 2 | Clarified scope of claims | Sec I, para 2 | R1.3 |
| 3 | Added [Ref] to related work | Sec II, para 3 | R2.3 |
| 4 | Fixed hardware description | Sec IV-A | R3.1 |
```

## Saving output

Save to `outputs/revision-letter-<YYYYMMDD>.md`.
Also save change tracker to `outputs/change-tracker-<YYYYMMDD>.md` for co-author review.
