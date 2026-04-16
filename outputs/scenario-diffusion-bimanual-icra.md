# End-to-End Scenario: Bimanual Manipulation with Diffusion Policy — ICRA 2026

This document is a **worked example** showing how conference-Darin is used for a realistic
robotics paper. It is not a real paper — it is a concrete scenario to make the workflow
testable end-to-end, so you can follow the sequence of commands and see what each step
produces.

The scenario: a researcher has a new method for bimanual manipulation that extends Diffusion
Policy with a cross-arm attention mechanism, and wants to submit to ICRA 2026.

---

## Paper identity

| Field | Value |
|-------|-------|
| Working title | Cross-Arm Attention for Bimanual Diffusion Policy |
| Contribution | Cross-arm attention module that lets each arm attend to the other arm's state, improving coordination in contact-rich bimanual tasks |
| Target venue | ICRA 2026 |
| Page limit | 8 pages (IEEE RA-L format accepted at ICRA) |
| Submission type | Conference paper |
| Real robot | Yes — ALOHA bimanual platform |

---

## Phase 0 walkthrough

### 0.1 Problem definition

**Filled in `templates/paper-outline.md`:**

```
Problem: Diffusion Policy struggles with bimanual tasks that require tight
arm coordination — tasks where the right arm's action depends on the real-time
state of the left arm (e.g., inserting a connector while the other arm holds a wire).

Gap: Existing bimanual IL methods (ACT, Diffusion Policy) process each arm
independently at the policy level, using joint concatenation as the only
cross-arm communication.

Contribution list:
  C1. A cross-arm attention module that conditions each arm's diffusion trajectory
      on a learned representation of the other arm's state.
  C2. Demonstration that C1 improves success rate on 4 contact-rich bimanual tasks
      by ≥15% over ACT and standard Diffusion Policy on the ALOHA platform.
  C3. An ablation showing that the attention mechanism (not just larger architecture)
      is responsible for the improvement.
```

### 0.2 Literature and baselines

**Command sequence:**
```
/search-lit "bimanual manipulation imitation learning"
/search-lit "diffusion policy action chunking transformer"
/search-lit "cross-attention robot manipulation"
```

**Expected tracker entries (Central):**
- Chi et al. "Diffusion Policy" CoRL 2023 — arXiv:2303.04137 — FULL-TEXT required (baseline)
- Zhao et al. "ACT: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware" RSS 2023 — arXiv:2304.13705 — FULL-TEXT required (baseline + evaluation platform)
- Fu et al. "Mobile ALOHA" arXiv 2024 — CANDIDATE (concurrent work, not a baseline)
- Reuss et al. "GROOT: Learning Generalizable Manipulation Policies with Object-Centric 3D Representations" CoRL 2023 — CANDIDATE

**NEED-PDF:**
- Zhao et al. RSS 2023 (ACT) — paywalled RSS proceedings; needed for ALOHA platform details

### 0.3 Benchmark mapping

**Command:**
```
/map-benchmarks --venue ICRA --category bimanual
```

**Expected Benchmark-Mapper output:**

```markdown
## Benchmark Mapping Report
Research question: Cross-arm attention for bimanual coordination
Target venue: ICRA 2026

### Recommended benchmarks (ranked)

1. ALOHA real-robot tasks — ESSENTIAL
   Fit: paper uses ALOHA platform; real-robot results required for ICRA manipulation claims
   Tasks: 4 contact-rich tasks (wire insertion, connector plugging, cloth folding, cup stacking)
   Metrics: success rate (mean ± std), N=25 trials per task per method
   Reviewer trap: ICRA reviewers expect ≥3 distinct task types; do not cherry-pick easy tasks

2. LIBERO-Bimanual — STRONGLY RECOMMENDED
   Fit: simulated bimanual benchmark for ablation; allows higher N without hardware time
   Tasks: LIBERO-Bimanual standard split (10 tasks)
   Metrics: success rate, N=20 trials per task
   Use: simulation ablation to isolate attention effect with N≥5 seeds

### Gap analysis
| Gap | Severity | Closes with |
|-----|----------|------------|
| Sim-only ablation insufficient for ICRA | ADVISORY | Add 2 real-robot ablation rows |
| N=25 real-robot trials is minimum | ADVISORY | Aim for N=30 if hardware allows |
```

### 0.4 Experiment design

**Command:**
```
/plan-experiments --venue ICRA
```

**Resulting `outputs/experiment-plan-<date>.md` (abbreviated):**

```markdown
## Experiment Plan — Status: APPROVED

### Contribution → hypothesis mapping
| # | Contribution | Hypothesis | Falsification |
|---|---|---|---|
| C1 | Cross-arm attention module | Model with attention > model without attention | SR drops >10% when attention removed |
| C2 | ≥15% SR improvement on 4 real tasks | SR(Ours) ≥ SR(ACT)+15pp AND SR(Ours) ≥ SR(DP)+15pp | Delta < 10pp on any 2+ tasks |
| C3 | Attention (not size) causes improvement | Larger-without-attention baseline < Ours | Size-matched model matches performance |

### Baseline roster
| Baseline | Citation | Input | Version | Fairness |
|---|---|---|---|---|
| Diffusion Policy | Chi et al. CoRL 2023 | RGB + joint state | Latest (official) | FAIR |
| ACT | Zhao et al. RSS 2023 | RGB + joint state | Official ALOHA implementation | FAIR |
| BC (MLP) | Pomerleau 1989 [cite] | RGB + joint state | Standard | FAIR — simple baseline |
| Ours-NoAttn (ablation) | — | RGB + joint state | Same arch, attention removed | — |
| Ours-Large (ablation) | — | RGB + joint state | Same params as Ours but no attention | — |

### Evaluation protocol
- Success criterion: task completed within 60s judged by experimenter
- Primary metric: success rate (binomial, N=25)
- N trials: 25 real-robot per method per task; 20 sim per method per task (5 seeds)
- Statistical reporting: mean ± std across N trials (and across seeds for sim)

### Ablation schedule
| Component | Ablated version | Hypothesis | Table row |
|---|---|---|---|
| Cross-arm attention | Remove attention, keep architecture | SR drops ≥10% | TABLE II row 2 |
| Attention type (cross vs. self) | Replace with self-attention on concatenated state | Lower than full cross-attn | TABLE II row 3 |
| Architecture size (not attention) | Match parameter count, no attention | Same as Ours-NoAttn | TABLE II row 4 |
```

### 0.5 Claim register (Stage A)

**Command:**
```
/track-claims --stage A
```

**Expected `outputs/claim-evidence-map-<date>.md` summary:**

```
SUPPORTED:   0  (no results yet)
PLANNED:     6  (all contributions have experiments)
MISSING:     0  (clean — ready to run experiments)
SPECULATIVE: 1  (C1 novelty: "first bimanual diffusion with cross-arm attention"
                 → Librarian must confirm no prior work)
```

**Action:** Route SPECULATIVE C1 to `/search-lit "cross-arm attention bimanual"` before writing the introduction.

### 0.5 Figure/table blueprint

**Command:**
```
/plan-figures --venue ICRA
```

**Blueprint excerpt:**

```
TABLE I — Main comparison (Sec. V)
  Rows: Ours, Diffusion Policy, ACT, BC
  Columns: Wire Insert SR, Connector SR, Cloth Fold SR, Cup Stack SR, Avg SR
  INV: booktabs, mean±std, N=25 in caption, all baselines cited

TABLE II — Ablation (Sec. VI)
  Rows: Full model, w/o cross-attn, w/ self-attn (not cross), size-matched w/o attn
  Columns: Wire Insert SR, Cloth Fold SR, Avg SR (3 tasks minimum)
  INV: booktabs, mean±std, N=20 in caption, INV-12

Fig. 1 — System diagram (Sec. III)
  Content: input observation → cross-arm attention → diffusion head → actions
  INV: grayscale legible (shapes, not just color), LaTeX labels, autocontained caption

Fig. 2 — Qualitative photo strip (Sec. V)
  Content: 4 tasks × success/failure comparison vs. ACT

Fig. 3 — Learning curve / sim ablation (Sec. VI)
  Content: SR vs. training steps for Ours, Ours-NoAttn, ACT in LIBERO-Bimanual
```

---

## Phase 2–3: Literature and related work

**After running `/search-lit` 3×, tracker should have:**
- ≥5 Central papers VERIFIED
- ACT and Diffusion Policy as FULL-TEXT
- Related: GROOT, Octo, π0, recent bimanual papers

**Run:**
```
/related-work --focus "bimanual IL, diffusion-based policies, cross-attention in manipulation"
```

**Expected related work structure:**
```
2.1 Imitation Learning for Manipulation (BC, ACT, Diffusion Policy)
2.2 Bimanual Manipulation Systems
2.3 Attention Mechanisms in Robot Learning
```

**Novelty claims routed to claim-evidence map:**
- "No prior work applies cross-arm attention in a diffusion policy framework" → SPECULATIVE → Librarian check

---

## Phase 4: Drafting

**Order (from writer.md):** Methodology → Experiments → Results → Related Work → Intro → Abstract → Conclusion

**After experiments run — fill `templates/results-tracker.md`:**

```markdown
## Main comparison results
| Method | Wire Insert | Connector | Cloth Fold | Cup Stack | Avg |
|---|---|---|---|---|---|
| Ours | 84.0 ± 4.2 | 72.0 ± 5.8 | 88.0 ± 3.6 | 76.0 ± 4.9 | 80.0 ± 4.6 |
| Diffusion Policy | 64.0 ± 5.1 | 52.0 ± 6.3 | 72.0 ± 4.8 | 60.0 ± 5.4 | 62.0 ± 5.4 |
| ACT | 68.0 ± 4.8 | 56.0 ± 5.9 | 76.0 ± 4.2 | 64.0 ± 5.0 | 66.0 ± 5.0 |
| BC (MLP) | 32.0 ± 5.6 | 24.0 ± 4.9 | 44.0 ± 6.1 | 28.0 ± 5.2 | 32.0 ± 5.5 |
N = 25 trials per method per task.
```

**Run after each section:**
```
/check-claims
/track-claims --stage B
```

After Results section, claim-evidence map updates:
- C2 → SUPPORTED (Ours avg 80.0% vs. ACT 66.0% = +14pp — note: just under the 15pp threshold → flag)
- C3 → SUPPORTED (ablation confirms attention is causal)

**⚠ INV-9 risk flagged:** C2 claims "≥15%" improvement but results show +14pp on average.
Action: either update the claim to "≥12%" (conservative threshold that data supports) or
re-examine per-task deltas. This is caught by `/track-claims --stage B` before any reviewer sees it.

---

## Phase 5: Review

**Command:**
```
/review-draft --venue ICRA
```

**Expected report highlights:**

Methods-Referee:
- Plan adherence: PASS (baselines match, N=25 as committed)
- MAJOR: sim ablation (LIBERO-Bimanual) has only 2 seeds — plan committed to 5; flag to user
- ADVISORY: real-robot ablation has only 2 rows (Ours + Ours-NoAttn) — reviewer may ask for more

Domain-Referee (SYSTEMS + LEARNING disposition for ICRA):
- Novelty score: 7/10 — contribution is clear; attention mechanism is well-motivated
- MAJOR: concurrent work (Mobile ALOHA) should be acknowledged in related work
- ADVISORY: discuss failure modes on cloth folding (88% success but cloth is deformable)

Writer-Critic:
- Dimension 0 FAIL: C2 threshold mismatch (claim says 15%, data shows 14pp avg) → CRITICAL
- INV-2 PASS: all tables have mean ± std
- MINOR: "leverages" used 3× — replace

**Aggregate score: 74/100 → DRAFT-READY**

Actions before Revision-Ready (≥80):
1. [CRITICAL] Fix C2 threshold — change "≥15%" to "≥12%" or re-examine task-specific deltas
2. [MAJOR] Re-run sim ablation with 5 seeds as planned
3. [MAJOR] Add Mobile ALOHA concurrent work acknowledgment

---

## Phase 6: Pre-submission

After resolving Phase 5 issues:

```
/simulate-review --venue ICRA
/ieee-checklist --venue ICRA
/track-claims --update
```

Target: aggregate score ≥ 90, claim map fully SUPPORTED, zero CRITICAL issues.

Expected final claim-evidence map:
```
SUPPORTED: 8
PLANNED:   0
MISSING:   0
CRITICAL:  0
```

---

## Key lessons from this scenario

1. **The 15% threshold failure** — a common trap: setting a specific quantitative claim in
   the contribution list before having results. The claim-evidence map caught this during
   Stage B, not during peer review.

2. **Sim ablation seeds** — committing to 5 seeds in the plan and then running 2 is a
   plan deviation. Methods-Referee caught it. The fix is 3 additional runs, not hiding the deviation.

3. **Concurrent work** — Mobile ALOHA appeared in the tracker as CANDIDATE and was correctly
   not listed as a baseline (concurrent, not prior work). But it still needs acknowledgment
   in related work. Domain-Referee caught this.

4. **The SPECULATIVE novelty claim** — "first bimanual diffusion with cross-arm attention"
   required a literature check before the introduction could be finalized. Librarian confirmed
   no exact match, but found a concurrent arXiv paper. Reformulated as: "concurrent with our work."

5. **The workflow sequence that worked:**
   ```
   /map-benchmarks → /search-lit → /plan-experiments → /track-claims --stage A →
   /plan-figures → [run experiments] → fill results-tracker → /related-work →
   /track-claims --stage B → draft sections → /check-claims → /review-draft →
   fix CRITICAL → /simulate-review → /ieee-checklist → submit
   ```
