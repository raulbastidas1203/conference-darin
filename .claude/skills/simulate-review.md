# Skill: /simulate-review

Venue-calibrated peer review simulation. Dispatches Editor → Domain-Referee + Methods-Referee
with venue-specific dispositions.

## Invocation

```
/simulate-review [--venue icra|iros|corl|rss|ral|tro] [--adversarial]
```

**Examples:**
```
/simulate-review --venue icra          # Simulate ICRA review panel
/simulate-review --venue corl          # Simulate CoRL review (higher bar)
/simulate-review --venue rss --adversarial  # Worst-case RSS reviewers
/simulate-review                       # Use venue from paper metadata
```

## What this skill does

1. **Reads the draft** — from `drafts/` or specified path
2. **Reads venue profile** — from `.claude/references/venue-profiles.md`
3. **Dispatches Editor** (desk review + referee assignment)
4. **Dispatches Domain-Referee** (calibrated to venue disposition)
5. **Dispatches Methods-Referee** (experimental rigor audit)
6. **Editor synthesizes** — produces editorial recommendation
7. **Saves full report** — to `outputs/simulate-review-<venue>-<date>.md`

## Adversarial mode (`--adversarial`)

When `--adversarial` is set:
- Domain-Referee uses SKEPTICAL disposition
- Methods-Referee uses strictest standards (N ≥ 50 trials, N ≥ 10 seeds)
- Editor applies worst-case realism (best reviewers at this venue, worst possible reading)
- Purpose: expose every weakness before a reviewer does

Use before submitting to CoRL or RSS.

## Referee assignment (from Editor)

See `.claude/references/venue-profiles.md` for default assignments.

| Venue | Default composition |
|-------|-------------------|
| ICRA | SYSTEMS + LEARNING + SKEPTICAL |
| IROS | SYSTEMS + LEARNING + APPLICATIONS |
| CoRL | LEARNING + SKEPTICAL + REPRODUCIBILITY |
| RSS | THEORY + SKEPTICAL + LEARNING |
| RA-L | SYSTEMS + LEARNING + REPRODUCIBILITY |
| T-RO | SYSTEMS + THEORY + REPRODUCIBILITY + LEARNING |

## Output format

```markdown
## /simulate-review: <venue>
Paper: [title]
Date: <date>
Mode: [standard | adversarial]

---

## Editor: Desk review
[PASSES / DESK REJECT: reason]

Referee assignment:
- Reviewer A: [DISPOSITION]
- Reviewer B: [DISPOSITION]
- Reviewer C: [DISPOSITION]

---

## Reviewer A Report ([DISPOSITION])

Summary: [2–3 sentences]

**Recommendation: [Strong Accept | Accept | Weak Accept | Borderline | Weak Reject | Reject]**

Concerns:
CRITICAL: [if any]
MAJOR: [list]
MINOR: [list]

"What would change my mind": [specifics for each MAJOR concern]

---

## Reviewer B Report ([DISPOSITION])

[Same format]

---

## Reviewer C Report ([DISPOSITION])

[Same format]

---

## Editorial Decision

**Decision: [Accept / Minor Revision / Major Revision / Reject]**

Primary reason: [one sentence]

### Classification of concerns

| Concern | Source | Class | Must fix? |
|---------|--------|-------|---------|
| Sim-only results | Reviewer A | ADDRESSABLE | Yes |
| Missing DiffusionPolicy comparison | Reviewer B | ADDRESSABLE | Yes |
| Font size in Figure 3 | Reviewer C | PREFERENCE | No |

### FATAL concerns (if any)
[None — or — must resolve or paper is rejected]

### Must address (addressable concerns)
1. [Concern] — [specific action]
2. [Concern] — [specific action]

### Optional improvements
1. [Suggestion]

---

## Aggregate assessment

| Dimension | Score | Venue bar | Status |
|-----------|-------|-----------|--------|
| Novelty | X/10 | ≥7 for ICRA | [PASS/FAIL] |
| Experimental evidence | X/10 | ≥7 for ICRA | |
| Technical rigor | X/10 | ≥7 for ICRA | |
| Presentation | X/10 | ≥6 for ICRA | |

Overall: [Ready to submit | Needs major work | Not ready for this venue]

---

## Alternative venue recommendation (if rejected)
[If the paper would be a better fit elsewhere, and why]
```

## Saving output

Save to `outputs/simulate-review-<venue>-<YYYYMMDD>.md`.
Keep all simulation reports — they document the paper's evolution and readiness assessment.
