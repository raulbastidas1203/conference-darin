# Skill: /analyze-gaps

Analyze gathered literature to map the research landscape, identify saturated versus open
directions, and propose concrete, evaluable paper directions. Dispatches Gap-Analyst.

Runs after `/search-lit`. Output feeds into `/map-benchmarks` and `/plan-experiments`.

## Invocation

```
/analyze-gaps [<topic>] [--venue icra|iros|corl|rss|ral|tro] [--mode landscape|directions|full]
```

**Examples:**
```
/analyze-gaps
/analyze-gaps "diffusion models for manipulation" --venue corl
/analyze-gaps --mode landscape
/analyze-gaps "sim2real locomotion" --venue iros --mode directions
```

**Modes:**
- `landscape` — terrain map + saturation diagnosis only; no direction proposals
- `directions` — skip landscape table, go straight to candidate directions (requires prior
  landscape run or a well-populated tracker)
- `full` (default) — complete analysis: landscape → gaps → directions → ranking → recommendation

**Prerequisites:** `references/tracker.md` must contain at least 5 papers (any classification).
If the tracker is empty or has fewer than 5 papers, run `/search-lit <topic>` first.

---

## What this skill does

1. **Checks prerequisites** — verifies `references/tracker.md` is populated; warns if fewer
   than 3 Central papers exist (analysis will be uncertain in that case)
2. **Reads calibration** — loads `domain-profile.md` and `venue-profiles.md` for the target
   venue; reads any available `lit-notes/` for full-text reading context
3. **Dispatches Gap-Analyst** — runs full analysis protocol
   (see `.claude/agents/gap-analyst.md`)
4. **Presents consolidated output** — landscape map, identified gaps, candidate directions,
   comparative ranking, and a single recommended direction
5. **Saves report** — writes to `outputs/gap-analysis-<date>.md`

---

## Gap-Analyst protocol (runs as part of this skill)

See `.claude/agents/gap-analyst.md` for the full protocol.

**Summary of the 6-phase analysis:**

**Phase 1 — Terrain mapping:** Clusters papers from the tracker into subproblems. Assigns
activity level (SATURATED / ACTIVE / SPARSE / UNEXPLORED) to each cluster.

**Phase 2 — Saturation diagnosis:** For each SATURATED cluster, determines whether entry
is still feasible or the area is effectively closed to new papers.

**Phase 3 — Gap identification:** Classifies each non-saturated gap by type:
Methods gap / Evaluation gap / Transfer gap / Scope gap / Negative result gap.
States technical barrier and evaluability for each.

**Phase 4 — Direction generation:** Proposes exactly 3–5 candidate directions.
Each direction has: core claim, gap addressed, required baselines, minimum viable experiment,
risk level, reviewer attack surface, desk-reject triggers.

**Phase 5 — Comparative assessment:** Ranks directions by publication plausibility (1–5).
Critical by default — scores of 5 are rare.

**Phase 6 — Recommendation:** Selects a single direction with a concrete first step and
an early invalidation test.

---

## Interpreting the output

**On plausibility scores:**
A score of 3/5 is not a failure — it means the direction is plausible but requires
careful scoping. Most realistic directions at top venues score 3–4. A score of 2 means the
risk is high enough to reconsider. A score of 1 means do not proceed without rethinking the
framing.

**On SATURATED areas:**
Saturation does not always mean "do not enter." It means the novelty bar is higher and the
contribution must be on a specific axis that prior work has not covered. The Gap-Analyst
will flag this explicitly.

**On UNEXPLORED areas:**
Absence of papers in a topic can mean (a) it is genuinely open, or (b) the search was
incomplete, or (c) the community tried it and it did not work (unpublished negative results).
The Gap-Analyst will flag uncertainty when coverage is sparse. Run additional `/search-lit`
queries before committing to an unexplored direction.

**On the recommended direction:**
The recommendation is a starting point for user decision, not a commitment. The user should
evaluate it against constraints not visible to the analysis: available hardware, team
expertise, compute budget, deadline.

---

## Coverage requirements before running this skill

| Tracker state | Recommendation |
|--------------|----------------|
| < 5 papers total | Run `/search-lit` first — analysis will be unreliable |
| 5–10 papers, few Central | Analysis will be uncertain; proceed with caution |
| ≥ 3 Central papers, 1+ from top venue | Minimum for reliable landscape map |
| ≥ 5 Central papers, 2+ venues covered | Good basis for direction generation |
| ≥ 10 Central papers, 3+ venues | Strong basis; direction ranking will be well-calibrated |

---

## Output format

```markdown
## /analyze-gaps: <topic>
Date: <date>
Mode: [landscape / directions / full]
Source: references/tracker.md (<N> papers: <C> Central, <R> Related, <M> Marginal)
Target venue: <venue or "not specified">

---

### Landscape map

| Subproblem | Papers (C/R/M) | Years | Dominant method | Benchmark | Activity |
|------------|---------------|-------|-----------------|-----------|----------|

---

### Saturation diagnosis

[For each SATURATED cluster:]
#### SATURATED: <subproblem>
Solved: [what has been solved, with paper keys]
Performance ceiling: [best numbers on benchmark]
Entry-closed: [Yes / No — reason]
Possible entry angle: [or "None identified"]

---

### Identified gaps

#### Gap 1: <label>
Type: [Methods / Evaluation / Transfer / Scope / Negative result]
Bounded by: [paper keys]
Technical barrier: [why this has not been done]
Evaluable: [Yes — on <benchmark> / No — requires new evaluation setup]

---

### Candidate directions

#### Direction 1: <title>
**Core claim:** [Abstract-level claim]
**Gap addressed:** [type]
**Builds on:** [paper keys]
**Competes with:** [paper keys]
**Novelty type:** [category]
**Target venue:** [venue]
**Minimum viable experiment:** [description]
**Required baselines:** [paper keys]
**Risk level:** [LOW / MEDIUM / HIGH]
**Risk factors:** [list]
**Reviewer attack surface:** [what first question will be]
**Desk-reject triggers:** [conditions]
**Plausibility:** X/5

#### Direction 2: ...

---

### Comparative ranking

| Rank | Direction | Plausibility | Main risk | Venue | Notes |
|------|-----------|-------------|-----------|-------|-------|

---

### Recommended direction

**Direction N: <title>**

Reason over alternatives: [why this one]
First concrete step: [specific action, not a general plan]
Early invalidation test: [what experiment would tell you this direction does not work,
and when you would know — run this before committing to a full paper]

---

### Coverage gaps in this analysis

[Subproblems where tracker coverage is too sparse to assess confidently. Suggest specific
/search-lit queries to improve coverage before committing to a direction in these areas.]

---

### Suggested next steps

[ ] If proceeding with Direction N: `/map-benchmarks` to confirm evaluation setup
[ ] If coverage is sparse in [area]: `/search-lit "<specific query>"`
[ ] Once benchmark confirmed: `/plan-experiments` for Direction N
[ ] Once at least 5 Central papers are full-text: `/related-work` for synthesis
```

---

## Saving output

Save to `outputs/gap-analysis-<YYYYMMDD>.md`.

If a previous gap analysis exists, do not overwrite it — create a new file. The history
of gap analyses shows how the research direction evolved as more literature was gathered.

---

## Integration with the workflow

This skill sits between DISCOVERY and SYNTHESIS in the workflow:

```
/search-lit → tracker.md populated
     ↓
/analyze-gaps → gap-analysis report + recommended direction
     ↓
/map-benchmarks → evaluation setup confirmed      ← feeds here
/plan-experiments → experimental protocol          ← and here
     ↓
/related-work → related work section drafted
     ↓
/review-draft → full paper review
```

**From `/search-lit`:** The tracker must be populated. The Librarian's coverage gaps
(reported at the end of `/search-lit`) are inputs to this skill's Phase 1 terrain map.

**To `/map-benchmarks`:** The recommended direction's `Minimum viable experiment` and
`Required baselines` fields are direct inputs to benchmark selection.

**To `/plan-experiments`:** The `Core claim` and `Required baselines` fields define the
hypothesis and comparison points for experiment design.

**To `/related-work`:** The landscape map and gap identification directly inform the
structure of the related work section (what clusters become subsections, how the gap is
framed).
