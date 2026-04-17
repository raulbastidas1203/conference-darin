# Skill: /related-work

Synthesize the related work section and comparison table for a robotics IEEE paper.
Dispatches Librarian (coverage check) → Writer (draft) → Writer-Critic (review).

## Invocation

```
/related-work [--focus <dimensions>] [--update]
```

**Examples:**
```
/related-work
/related-work --focus "data efficiency, sim2real, real robot validation"
/related-work --update   # Re-run after adding papers to /papers/
```

## What this skill does

1. **Reads context** — `drafts/` for active paper; `references/tracker.md` for available papers;
   `lit-notes/` for reading notes; `domain-profile.md` for subfield calibration
2. **Coverage check** — confirms Central papers in tracker are VERIFIED or FULL-TEXT;
   if important papers are CANDIDATE or NEED-PDF, warns user before writing
3. **Dispatches Writer** — produces organized related work + comparison table
4. **Dispatches Writer-Critic** — verifies claims, INV compliance, positioning accuracy
5. **Saves output** — to `outputs/related-work-draft-<date>.md`

## Prerequisites

Before running this skill:
- At least 5 Central papers must be in `references/tracker.md` with status ≥ VERIFIED
- At least 1 paper from ICRA/IROS/CoRL/RSS/RA-L/T-RO must be in the tracker
- The paper's contribution must be defined (either in `drafts/` or stated to this skill)

If prerequisites are not met, report the gap and suggest running `/search-lit` first.

## Writer protocol (runs as part of this skill)

See `.claude/agents/writer.md` for full protocol.

**Structure enforced:**
- 2–4 subsections organized by technical dimension (not chronology)
- Each subsection closes by positioning own work vs. the group
- No pure listing — each cited paper has a role

**Framing:** "Unlike [X]...", "While [A] and [B]...", "Closest to our work is [X]; however..."

**Anti-patterns eliminated:** Pure paper listings, vague gap statements, claims about
prior work not supported by reading the paper.

## Comparison table

Generates LaTeX table comparing key properties across methods.
Properties selected must be:
1. Technically significant for the contribution
2. Verifiable in the cited papers
3. Not cherry-picked to make "ours" win on trivial dimensions

See `templates/comparison-table.md` for LaTeX templates.

## Writer-Critic checks (runs after Writer)

Verifies: each cited paper's role is clear; gap statement is specific; no misrepresented
prior work; "first to" claims have INV-17 support; all cited papers are VERIFIED in tracker.

## Claim-evidence map update (runs after Writer-Critic)

After producing the related work draft, update or create `outputs/claim-evidence-map-<date>.md`:

1. **Gap claims** — every statement of the form "no prior work addresses X" or "existing
   methods fail at Y" becomes a SPECULATIVE entry in the claim register until the Librarian
   confirms no counter-example exists. Mark each as:
   ```
   Type: About-prior-work / Novelty
   Status: SPECULATIVE — needs Librarian verification for INV-17
   ```

2. **Positioning claims** — "unlike [X], our method does not require Y" → add as
   SUPPORTED if [X] is a FULL-TEXT paper with a confirmed property. Add as SPECULATIVE
   if [X] is only VERIFIED (abstract-level) and the specific limitation was not confirmed
   in the full text.

3. **"First to" claims** — always add as SPECULATIVE with a note to run `/search-lit`
   with specific queries before the paper is submitted.

## Output

```markdown
## /related-work output
Date: <date>
Papers used: [list from tracker with status]
Agent: Writer + Writer-Critic

---

## Draft: Related Work

### [Subsection 1: technical dimension name]
<2–4 paragraphs>

### [Subsection 2]
<2–4 paragraphs>

[additional subsections]

---

## Comparison Table (LaTeX)

\begin{table}[t]
\centering
\caption{...}
\label{tab:related}
...
\end{table}

---

## Writer-Critic report
Score: <N>/100
Issues: [CRITICAL / MAJOR / MINOR list]

---

## Papers used but need verification
[UNVERIFIED entries used — flag to user]

## Papers to retrieve (NEED-PDF)
[Papers flagged as NEED-PDF that would strengthen this section]

## BibTeX keys used
[List for verification]
```

## Saving output

Always save final draft to `outputs/related-work-<date>.md`.
If a previous version exists, keep it and create a new file (do not overwrite).
