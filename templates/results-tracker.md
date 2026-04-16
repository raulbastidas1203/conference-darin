# Results Tracker

<!-- Fill this as experiments run. One row per (method × task × condition) combination.  -->
<!-- This is the single source of truth for numbers that go into the paper.              -->
<!-- Run /track-claims --stage B after filling this to update the claim-evidence map.    -->

## Header

| Field | Value |
|-------|-------|
| Paper | |
| Experiment plan | `outputs/experiment-plan-<date>.md` |
| Date started | |
| Last updated | |

---

## Main comparison results

<!-- One row per (method × task). Add tasks as columns on the right.                    -->
<!-- Mean ± std over N trials. N must match the approved experiment plan.               -->

| Method | Task-1 SR | Task-2 SR | Task-3 SR | Task-N SR | Avg SR | N trials | Notes |
|--------|-----------|-----------|-----------|-----------|--------|----------|-------|
| **Ours** | | | | | | | |
| Baseline-1 | | | | | | | |
| Baseline-2 | | | | | | | |
| Baseline-3 | | | | | | | |
| Baseline-4 | | | | | | | |

**SR** = success rate (mean ± std). Format: `86.4 ± 2.7`

**N trials per cell:** _______ (must match approved plan: `outputs/experiment-plan-<date>.md`)

**Evaluation conditions:** _______

---

## Ablation results

<!-- One row per ablated variant. Columns = same tasks as main comparison (minimum 3).  -->

| Variant | Task-1 SR | Task-2 SR | Task-3 SR | Avg SR | Component removed | N trials |
|---------|-----------|-----------|-----------|--------|-------------------|----------|
| Full model (Ours) | | | | | — | |
| w/o component A | | | | | [name] | |
| w/o component B | | | | | [name] | |
| w/o component C | | | | | [name] | |
| Simple baseline | | | | | BC / rule-based | |

**Planned ablation components** (from experiment plan):
- [ ] Component A: ___________
- [ ] Component B: ___________
- [ ] Component C: ___________

---

## Generalization results (if claimed)

| Method | Seen objects SR | Unseen objects SR | Unseen tasks SR | N trials |
|--------|----------------|------------------|----------------|----------|
| Ours | | | | |
| Best baseline | | | | |

**Train/test split used:** _______

---

## Sample efficiency (if claimed)

| Method | 10 demos | 25 demos | 50 demos | 100 demos | 500 demos |
|--------|----------|----------|----------|-----------|-----------|
| Ours | | | | | |
| Baseline | | | | | |

---

## Real-robot results (if applicable)

| Method | Task | Trials | Successes | SR | Notes |
|--------|------|--------|-----------|----|----|
| Ours | | | | | |
| Best baseline | | | | | |

**Hardware:** _____ (robot model, end-effector, camera)
**Conditions:** _____ (lighting, table setup, operator)

---

## Learning curves data (if applicable)

<!-- Paste raw data or describe the source file for learning curve plots. -->

| Method | Step | Mean SR | Std SR |
|--------|------|---------|--------|
| Ours | | | |
| Baseline | | | |

---

## Claim-evidence status

<!-- Update after filling results above. Run /track-claims --stage B to auto-update.    -->

| Claim ID | Claim (short) | Evidence here | Status |
|---------|---------------|---------------|--------|
| C-001 | Main perf claim | Main table, row Ours | SUPPORTED |
| C-002 | | | PENDING |
| C-003 | Ablation: component A | Ablation table | SUPPORTED |

---

## Data provenance

| Experiment | Run date | Seed(s) | Hardware / Simulator | Config file | Notes |
|-----------|---------|---------|---------------------|------------|-------|
| Main comparison | | | | | |
| Ablation | | | | | |

---

## Deviations from experiment plan

<!-- Document any deviation from the approved experiment plan here.                     -->
<!-- These must be justified and will be flagged by Methods-Referee during review.      -->

| Deviation | Reason | Impact on claims |
|-----------|--------|-----------------|
| | | |
