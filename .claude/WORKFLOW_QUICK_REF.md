# Workflow Quick Reference — conference-Darin

---

## Commands

| Command | When to use | Agents dispatched |
|---------|-------------|------------------|
| `/search-lit <topic>` | Start of paper, before related work | Librarian → Librarian-Critic |
| `/related-work` | After ≥5 Central papers verified | Librarian + Writer → Writer-Critic |
| `/review-draft` | After completing any major section | Domain-Referee + Methods-Referee + Writer-Critic |
| `/check-claims` | Before each section is finalized | Writer-Critic (claim mode) |
| `/simulate-review --venue <v>` | Before submission | Editor → Domain-Referee + Methods-Referee |
| `/revision-letter` | After receiving reviewer comments | Writer |
| `/ieee-checklist --venue <v>` | Final pre-submission check | Writer-Critic (format mode) |

---

## Quality gates

| Score | Meaning | Gate |
|-------|---------|------|
| ≥ 90 | No blocking issues | Submission-ready |
| 80–89 | All CRITICAL resolved | Revision-ready |
| 70–79 | Safe to share | Draft-ready |
| < 70 | Fundamental issues | Blocked |

---

## Workflow by phase

```
PHASE 1 — SCOPING
  Fill: templates/paper-outline.md
  Define: contribution (specific + falsifiable), venue, deadline

PHASE 2 — DISCOVERY
  Run: /search-lit <topic>
  Build: references/tracker.md
  Read: papers flagged as Central

PHASE 3 — SYNTHESIS
  Run: /related-work
  Identify: gap + positioning

PHASE 4 — DRAFTING
  Order: Methodology → Experiments → Results → Related Work → Intro → Abstract → Conclusion
  After each section: /check-claims

PHASE 5 — REVIEW
  Run: /review-draft
  Target: score ≥ 80
  Fix: all CRITICAL issues

PHASE 6 — PRE-SUBMISSION
  Run: /simulate-review --venue <v>
  Run: /ieee-checklist --venue <v>
  Target: score ≥ 90, zero CRITICAL issues

PHASE 7 — REVISION
  Run: /revision-letter
  Re-run: /review-draft
  Gate: all reviewer concerns addressed point-by-point
```

---

## Agent roles (one-line summary)

| Agent | Role | Creates? |
|-------|------|---------|
| Librarian | Finds papers, updates tracker | Tracker entries, lit-notes |
| Librarian-Critic | Verifies coverage, flags fabrications | Review reports only |
| Writer | Drafts sections, writes revision letters | Paper content |
| Writer-Critic | Audits IEEE compliance, claims, numbers | Review reports only |
| Domain-Referee | Simulates robotics reviewer | Review reports only |
| Methods-Referee | Audits experimental rigor | Review reports only |
| Editor | Simulates AC/PC, synthesizes reviews | Editorial report only |

**Golden rule:** Critics never edit. Workers never score themselves.

---

## Reference status flow

```
CANDIDATE → VERIFIED → FULL-TEXT
                ↓
           NEED-PDF (tell user) → FULL-TEXT (after user provides PDF)
                ↓
          UNVERIFIED (remove from .bib, tell user)
```

---

## Content invariant quick-check

Before any section is finalized, verify:

| # | Check |
|---|-------|
| INV-1 | Tables: booktabs only, no \hline |
| INV-2 | Results: mean ± std everywhere |
| INV-3 | N trials stated in all tables |
| INV-4 | Hardware fully described |
| INV-5 | All baselines cited |
| INV-6 | Figures legible in grayscale |
| INV-7/8 | Captions autocontained |
| INV-9 | Numbers in text = numbers in tables |
| INV-10 | Acronyms defined on first use |
| INV-12 | Ablation covers key components |
| INV-14 | Abstract has quantitative result |
| INV-15 | Intro has numbered contribution list |

Full list: `.claude/rules/content-invariants.md`

---

## Workspace layout

```
/papers/           User-provided PDFs (gitignored)
/drafts/           Active LaTeX/Markdown draft
/lit-notes/        Per-paper reading notes
/references/       references.bib + tracker.md
/outputs/          Skill outputs, quality reports, review history
/templates/        Paper outline, comparison tables, revision template
/workflows/        Process guides (new-paper, lit-review, submission-prep)
/.claude/
  /agents/         7 agent role specs
  /references/     Domain knowledge (profile, venues, methods, benchmarks)
  /rules/          Content invariants
  /skills/         7 skill implementations
```
