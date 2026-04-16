# Skill: /review-draft

Full critical review of a paper draft. Dispatches Domain-Referee + Methods-Referee
in parallel, then synthesizes a scored report.

## Invocation

```
/review-draft [<file or section>] [--mode full|section|experiments|abstract]
```

**Examples:**
```
/review-draft                          # Full draft in /drafts/
/review-draft --mode abstract          # Abstract only
/review-draft --mode experiments       # Experiments + results sections
/review-draft drafts/paper.tex         # Specific file
```

## What this skill does

1. **Reads the draft** — from `drafts/` or specified path
2. **Reads calibration** — `domain-profile.md`, active venue from CLAUDE.md context
3. **Loads Phase 0 artifacts** (if present — each agent uses them independently):
   - `outputs/experiment-plan-<date>.md` → passed to Methods-Referee and Writer-Critic
   - `outputs/claim-evidence-map-<date>.md` → passed to Writer-Critic (Stage B update)
   - `outputs/figures-plan-<date>.md` → passed to Writer-Critic
   - `outputs/results-tracker-<date>.md` → passed to Methods-Referee for number verification
4. **Dispatches in parallel:**
   - Domain-Referee — novelty, positioning, technical content
   - Methods-Referee — experimental rigor, reproducibility, plan adherence (Phase 0)
   - Writer-Critic — IEEE format, claims-evidence, invariants, plan consistency (Dimension 0)
5. **Updates claim-evidence map** — after Writer-Critic runs, its findings update the map
   (SUPPORTED claims confirmed, new CRITICAL INV-9 mismatches added)
6. **Computes aggregate score** — weighted per CLAUDE.md quality framework
7. **Produces consolidated report** — saved to `outputs/review-<date>.md`

## Agent dispatch details

### Domain-Referee reviews:
- Contribution and novelty (30% of domain score)
- Literature positioning (25%)
- Technical content clarity (20%)
- Experimental evidence — high level (15%)
- Presentation quality (10%)

### Methods-Referee reviews (4-phase, early stop on CRITICAL):
- Phase 1: Extract all empirical claims
- Phase 2: Core experimental validity (task, baselines, metrics)
- Phase 3: Statistical validity (N trials, error bars, generalization)
- Phase 4: Reproducibility (ablation, hyperparameters, code)

### Writer-Critic reviews:
- Claims-evidence alignment (INV-9 numbers audit)
- All 20 content invariants
- IEEE format compliance
- Writing quality (banned phrases, voice, acronyms)

## Severity hierarchy

**CRITICAL** (blocks submission — must fix before any gate):
- Quantitative claim not supported by data
- Number in text ≠ table value (INV-9)
- Unfair baseline comparison
- Fabricated citation [UNVERIFIED]
- Real-world claim from sim-only experiments

**MAJOR** (must fix before submission gate ≥ 90):
- Missing mean ± std (INV-2)
- Missing ablation for key component (INV-12)
- Baseline not cited (INV-5)
- Hardware not described (INV-4)
- Novelty claim without INV-17 support

**MINOR** (should fix before submission; does not block if addressed or acknowledged):
- Banned phrase in text
- Acronym not defined on first use (INV-10)
- Figure not grayscale-legible (INV-6)
- Caption not autocontained (INV-7/8)

## Aggregate scoring

| Component | Agent | Weight |
|-----------|-------|--------|
| Literature coverage | Librarian-Critic (last run) | 15% |
| Related work positioning | Domain-Referee | 20% |
| Methodology clarity | Domain-Referee + Methods-Referee | 20% |
| Experimental rigor | Methods-Referee | 30% |
| Writing & IEEE format | Writer-Critic | 15% |

Gate thresholds: 70 (draft-ready) / 80 (revision-ready) / 90 (submission-ready)

## Severity hierarchy

Note: review-draft aligns with content-invariants.md severity tags. MINOR issues in
the `/review-draft` report correspond to items that are not content invariant violations
(writing style, presentation suggestions). INV violations are always CRITICAL or MAJOR.

## Output format

```markdown
## /review-draft Report
File: <path>
Date: <date>
Target venue: <venue if known>
Phase 0 artifacts loaded: [list or "none"]

---

## Aggregate score: <N>/100
Status: [BLOCKED <70 | DRAFT-READY 70–79 | REVISION-READY 80–89 | SUBMISSION-READY ≥90]

| Component | Weight | Score | Notes |
|-----------|--------|-------|-------|
| Literature coverage | 15% | X/10 | |
| Related work positioning | 20% | X/10 | |
| Methodology clarity | 20% | X/10 | |
| Experimental rigor | 30% | X/10 | |
| Writing & IEEE format | 15% | X/10 | |

### Plan adherence summary (if experiment plan loaded)

| Check | Status |
|-------|--------|
| Baselines match approved plan | PASS / FAIL |
| N trials ≥ committed protocol | PASS / FAIL |
| Ablation covers all planned components | PASS / FAIL |
| All SUPPORTED claims in map match draft numbers | PASS / FAIL |

---

## CRITICAL issues (<N>) — must fix

1. [Agent] **[Issue]**
   Location: [section/paragraph]
   Evidence: [what the paper says vs. what the data shows]
   Fix: [specific action]

---

## MAJOR issues (<N>) — fix before submission

1. ...

---

## MINOR issues (<N>) — strengthen before submission

1. ...

---

## Positive aspects to preserve

[What is strong and should not be changed]

---

## Domain-Referee recommendation (full)
[Domain-Referee full report — see agent output]

## Methods-Referee verdict (full)
[Methods-Referee full report — see agent output]

## Writer-Critic score (full)
[Writer-Critic full report — see agent output]

---

## Required actions before next gate

Priority order:
1. [CRITICAL item 1]
2. [CRITICAL item 2]
3. [MAJOR item 1]
...
```

## Saving output

Save to `outputs/review-<YYYYMMDD>-<score>.md`.
Do not overwrite previous reviews — each review creates a new file.
The history shows improvement across iterations.
