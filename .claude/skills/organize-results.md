# Skill: /organize-results

Processes filled experiment data into a verified results ledger, updates the claim-evidence
map, and prepares the numbers layer for drafting.

## Invocation

```
/organize-results
/organize-results --data <path>
/organize-results --plan <path-to-experiment-plan>
```

**Examples:**
```
/organize-results
  # reads templates/results-tracker.md, uses most recent experiment plan and claim map

/organize-results --data outputs/my-results.md
  # use a specific filled results file

/organize-results --plan outputs/experiment-plan-20260416.md
  # explicitly specify which approved plan to compare against
```

---

## What this skill does

`/organize-results` is the entry point to the post-experiment, pre-drafting phase. Run it
after experiments have produced data and you have filled in `templates/results-tracker.md`.

It produces two things:
1. `outputs/results-ledger-<date>.md` — a verified, agent-processable record of all results
   with provenance, consistency status, and explicit links to claim IDs
2. An updated `outputs/claim-evidence-map-<date>.md` — PLANNED claims advanced to SUPPORTED
   or MISSING based on actual data

After running this skill, the results ledger becomes the **single source of truth** for all
numbers that enter the paper. The Writer reads the ledger. The Writer-Critic checks numbers
against the ledger (not against the raw tracker). The Methods-Referee uses it for plan
adherence during `/review-draft`.

---

## When to run

After experiments complete. Before drafting the Experiments or Results section.

```
Phase 0  → /map-benchmarks → /plan-experiments → /track-claims --stage A → /plan-figures
[run experiments] → fill templates/results-tracker.md
Phase 4a → /organize-results          ← here
Phase 4b → /track-claims --stage B    (reads updated claim map from organize-results)
Phase 4c → draft sections             (Writer reads outputs/results-ledger-<date>.md)
Phase 5  → /review-draft              (Methods-Referee reads ledger)
Phase 6  → /track-claims --update     (final audit)
```

---

## Agent dispatch

**Results-Tracker (main)**

Reads the filled results data and the approved experiment plan. Runs the full five-step
protocol described in `.claude/agents/results-tracker.md`:

1. Load inputs (tracker data + plan + claim map)
2. Internal consistency check (averages, INV-2, completeness)
3. Plan adherence check (baselines, tasks, N, ablation coverage)
4. Claim-evidence update (PLANNED → SUPPORTED / MISSING)
5. Produce results ledger + summary report

---

## Prerequisites

Before running this skill:
- `templates/results-tracker.md` (or equivalent) must be filled with actual experiment data
- At least one result must be present (not all empty)

Recommended (not required, but significantly improves output):
- `outputs/experiment-plan-<date>.md` with status APPROVED — enables plan adherence check
- `outputs/claim-evidence-map-<date>.md` from Stage A — enables claim advancement

If no experiment plan exists, the agent flags every check as "no approved plan" and applies
domain norms from `domain-profile.md` as the comparison standard.

---

## Output

**Primary:** `outputs/results-ledger-<date>.md`
— Verified results in structured format. This is what all downstream agents read.

**Secondary:** updated `outputs/claim-evidence-map-<date>.md`
— PLANNED claims advanced to SUPPORTED or MISSING. Added UNCLAIMED-RESULT entries if any.

**Inline report:** a summary table showing:
- Consistency check status (arithmetic, INV-2, N completeness)
- Plan adherence status (baselines, tasks, ablation)
- Claim-evidence advancement (N SUPPORTED, N MISSING, N UNCLAIMED)
- Issues requiring user attention before drafting

---

## After running this skill

1. **Review the issues list.** Any ARITHMETIC-ERROR must be corrected in the source data
   before the ledger is used for writing.
2. **Acknowledge PLAN-DEVIATIONS.** For each deviation, decide: update the approved plan to
   reflect what was actually done, or add a note in the paper (Methods-Referee will flag it).
3. **Address UNCLAIMED-RESULT entries.** If a result exists but no claim was registered for
   it, consider whether it represents an additional contribution.
4. **Run `/track-claims --stage B`** to propagate the updated claim map through the full
   claim register and catch any remaining INV-9 risks before writing.
5. **Begin drafting.** The Writer will read `outputs/results-ledger-<date>.md` automatically.

---

## Connection to the rest of the workflow

| Upstream | What it provides |
|----------|-----------------|
| `/plan-experiments` | Approved protocol: N, tasks, baselines, success criterion, ablation schedule |
| `/track-claims --stage A` | Claim register with PLANNED status and claim IDs |
| `/map-benchmarks` | Benchmark gap analysis (used to flag if any planned benchmark was not run) |
| User (filled tracker) | Raw results: numbers, conditions, seeds, hardware notes |

| Downstream | What it reads |
|-----------|--------------|
| `/track-claims --stage B` | Updated claim map with SUPPORTED/MISSING status |
| Writer | `outputs/results-ledger-<date>.md` for all numbers |
| Writer-Critic | Ledger for INV-9 number cross-reference |
| Methods-Referee | Ledger for plan-adherence verification during `/review-draft` |
