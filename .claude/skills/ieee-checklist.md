# Skill: /ieee-checklist

Pre-submission verification against IEEE standards and venue requirements.
Dispatches Writer-Critic in checklist mode.

## Invocation

```
/ieee-checklist [--venue icra|iros|corl|rss|ral|tro] [--mode full|format|content|outline]
```

**Examples:**
```
/ieee-checklist --venue icra           # Full checklist for ICRA
/ieee-checklist --mode format          # Format only (pre-camera-ready)
/ieee-checklist --mode outline         # Before writing, verify outline is solid
/ieee-checklist --mode content         # Content standards only
```

## What this skill does

1. **Reads the draft** — from `drafts/` or specified path
2. **Reads venue profile** — from `.claude/references/venue-profiles.md`
3. **Reads content invariants** — from `.claude/rules/content-invariants.md`
4. **Dispatches Writer-Critic** in checklist mode
5. **Produces pass/fail checklist** with specific fixes

## Mode: OUTLINE (before writing)

Verify the outline (from `templates/paper-outline.md`) has:

- [ ] Contribution stated as falsifiable, specific claim
- [ ] 2–4 contributions listed, each verifiable in the paper
- [ ] Gap in literature identified with at least 2 references
- [ ] Target venue confirmed (impacts experiment expectations)
- [ ] Baselines identified with citations (not just names)
- [ ] Metrics defined with units and justification
- [ ] Hardware/sim platform specified (INV-4 planning)
- [ ] Ablation components planned

## Mode: CONTENT (during writing)

### Abstract (INV-14)
- [ ] 150–250 words
- [ ] Contains: problem + approach + quantitative result
- [ ] No "novel" without evidence; no "state-of-the-art" without comparison
- [ ] Readable independently

### Introduction (INV-15)
- [ ] Numbered contribution list with 2–4 specific items
- [ ] Gap cites at least 2 papers
- [ ] Ends with paper organization

### Related Work
- [ ] Organized by technical dimension (not chronological)
- [ ] Each subsection positions vs. own work
- [ ] Closest competitor explicitly compared
- [ ] No "first to" without INV-17 support

### Methodology
- [ ] All symbols defined before use (INV-11)
- [ ] Equations numbered
- [ ] Design choices justified
- [ ] Hardware described (INV-4)

### Experiments
- [ ] Mean ± std for all results (INV-2)
- [ ] N trials stated (INV-3)
- [ ] All baselines cited (INV-5)
- [ ] Ablation for all key components (INV-12)
- [ ] Sim/real scope explicit (INV-16)

### Results & Discussion
- [ ] Text numbers match tables (INV-9 — check every number)
- [ ] Causal claims have ablation support (INV-18)
- [ ] Failure cases discussed

### Conclusion
- [ ] Limitations section (honest)
- [ ] Future work is concrete (not generic)

## Mode: FORMAT (pre-submission final check)

### IEEE template compliance
- [ ] Correct template for venue (download from IEEE Author Center)
- [ ] Double column enforced
- [ ] Times New Roman 10pt body (no font substitutions)
- [ ] No `\vspace{}` or margin hacks

### Page count
- [ ] Within limit: ICRA/IROS/CoRL/RSS/RA-L = 8 pages + references (verify with CFP)
- [ ] T-RO: no limit
- [ ] References don't count toward limit (verify with current CFP)

### Tables (INV-1)
- [ ] All tables use booktabs (`\toprule`, `\midrule`, `\bottomrule`)
- [ ] No `\hline` anywhere
- [ ] No vertical rules
- [ ] Captions above table (IEEE style)

### Figures (INV-6, INV-7, INV-19)
- [ ] All figures ≥ 300 DPI (for print)
- [ ] All figures legible in grayscale
- [ ] All captions below figure (IEEE style)
- [ ] Figure titles in LaTeX captions, not embedded in image
- [ ] All figures referenced in text as "Fig. X" (not "Figure")

### References
- [ ] Format: `[N] A. Author, "Title," Proc. VENUE, pp. X–Y, year.`
- [ ] No raw URLs as standalone references
- [ ] DOI used when available
- [ ] All `\cite{}` keys resolve in .bib file
- [ ] No duplicate entries
- [ ] Ordered by appearance in text

### Anonymization (double-blind venues: ICRA, IROS, CoRL, RSS)
- [ ] No author names in text
- [ ] No institutional affiliations in text
- [ ] Self-citations in third person: "[14]" not "our prior work [14]"
- [ ] No acknowledgments (or "[omitted for blind review]")
- [ ] No repo URLs with identifying names
- [ ] PDF metadata clean: File → Properties → no author name

### Acronyms (INV-10)
- [ ] Every acronym defined on first use
- [ ] No alternation between full form and acronym after definition

## Output format

```markdown
## /ieee-checklist: <venue> — <mode>
Date: <date>

---

## FAILS ❌ (must fix)

| Item | INV | Section | Required action |
|------|-----|---------|----------------|
| Table III uses \hline | INV-1 | Sec V | Replace with \midrule |
| Fig 4 text unreadable in grayscale | INV-6 | Sec IV | Use markers + dashed lines |
| "3×" in text ≠ "2.8×" in Table II | INV-9 | Sec V-A | Fix one of the two |
| Missing N trials in Table II | INV-3 | Table II | Add "N=20" to caption |

---

## PASSES ✅

[List of items verified as correct — reader can confirm no action needed]

---

## VERIFY ⚠️ (manual check required)

- [ ] PDF metadata: check File → Properties for author names (cannot verify automatically)
- [ ] DPI of Figure 2: if generated from matplotlib, check output settings

---

## Page count
Current: X pages + Y pages refs = X total
Limit: 8 pages (body) + refs (unlimited)
Status: [WITHIN / OVER by N lines]

---

## Summary
- Blocking issues: <N>
- Non-blocking issues: <N>
- Ready to submit: [NO — N blocking issues | YES]
```

## Saving output

Save to `outputs/ieee-checklist-<venue>-<YYYYMMDD>.md`.
