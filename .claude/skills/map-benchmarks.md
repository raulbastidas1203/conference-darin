# Skill: /map-benchmarks

## Invocation

```
/map-benchmarks
/map-benchmarks --venue <venue>
/map-benchmarks --category <manipulation|navigation|sim2real|humanoid|generalization>
```

**Examples:**
- `/map-benchmarks` — reads contribution from `templates/paper-outline.md`, infers venue
- `/map-benchmarks --venue CoRL` — enforce CoRL-specific evaluation expectations
- `/map-benchmarks --category sim2real` — focus on sim-to-real evaluation norms

---

## What this skill does

`/map-benchmarks` answers: **"For this contribution and venue, on what should I evaluate,
with what metrics, and what will reviewers expect?"**

It runs before `/plan-experiments`. The benchmark recommendation feeds directly into the
experiment plan's task and benchmark selection step, replacing guesswork with
community-calibrated choices.

Running it produces:
1. A ranked list of benchmarks with fit justification
2. Standard task/split/metric specifications for each benchmark
3. A gap analysis against venue expectations
4. A minimum viable evaluation set for the target venue

---

## When to run

Run `/map-benchmarks` at the start of Phase 0, before or alongside the first `/search-lit`
for baselines. The benchmark mapping should be done before `/plan-experiments`, because
the experiment plan's task selection step benefits from this output.

Recommended order:
```
/search-lit <topic>          # find papers and baselines
/map-benchmarks --venue <v>  # decide what to evaluate on
/plan-experiments --venue <v>  # design the full experiment plan
```

---

## Agent dispatch

**Benchmark-Mapper (main)**
Reads contribution statement, venue profile, and all entries in `benchmark-notes.md`.
Produces the ranked recommendation with gap analysis.

**Librarian (on demand)**
If a benchmark referenced in the recommendation is not in `benchmark-notes.md`, the
Librarian is dispatched to find the benchmark paper and add a CANDIDATE entry.

---

## Output

Primary output: `outputs/benchmark-map-<date>.md`

Also updates `templates/experiment-plan.md` section "Benchmarks and tasks" with the
top recommendations pre-filled (marked DRAFT — user must confirm).

---

## Integration with experiment plan

After running `/map-benchmarks`, the outputs file contains the "Minimum viable evaluation"
section. When you then run `/plan-experiments`, the Experiment-Planner reads this file and
uses it to populate the benchmark selection step — you do not need to re-specify benchmarks
manually.

The gap analysis becomes part of the Methods-Referee's evaluation standard when
`/review-draft` is run: the reviewer knows what was flagged as BLOCKING or ADVISORY before
experiments were designed, and can check whether gaps were addressed or acknowledged.
