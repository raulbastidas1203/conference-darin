# Skill: /check-claims

Claims-evidence audit of a paper section or full draft.
Dispatches Writer-Critic with focus on claim validation.

## Invocation

```
/check-claims [<file or section>]
```

**Examples:**
```
/check-claims                          # Entire draft in /drafts/
/check-claims drafts/introduction.tex
/check-claims drafts/experiments.tex
```

## What this skill does

1. **Reads the target** — specified file or full draft
2. **Reads tables and figures** — to compare numbers against text claims
3. **Dispatches Writer-Critic** in claim-audit mode
4. **Produces a prioritized action list**
5. **Saves output** to `outputs/claims-audit-<date>.md`

## Claim types audited

| Type | Example | Evidence required |
|------|---------|------------------|
| Quantitative | "achieves 86.4%" | Table/figure with exact number |
| Comparative | "outperforms BC by 15pp" | Table showing both; arithmetic correct |
| Causal | "improvement due to component X" | Ablation removing X |
| Qualitative | "more robust to noise" | Ablation or comparative experiment |
| Novelty | "first to combine X and Y" | Literature search evidence (INV-17) |
| About prior work | "X fails at Y" | Citation + specific evidence from that paper |

## Writer-Critic focus areas (claim mode)

### Numbers consistency (INV-9) — highest priority

Extract every number mentioned in the body text. For each:
- Locate the corresponding table/figure
- Verify exact match (86.4 ≠ 86.3; 3× ≠ 2.9×)
- **Any mismatch = CRITICAL** — escalate to user immediately

### Quantitative claims without numbers

Statements like "significantly better", "notably higher", "substantially faster":
- Replace with specific numbers or flag as `[TODO: quantify]`
- All comparative claims need the comparison baseline explicitly stated

### Causal claims (INV-18)

"The improvement is due to X" → requires ablation of X (Table N, row "w/o X")
"Removing Y causes degradation" → requires ablation showing this

### Novelty claims (INV-17)

"We are the first to..." → requires:
- Venues searched + year range
- What was found (or not found)
- If reformulation is safer: "We propose the first method that [specific combo of properties]"

### [TODO: cite] audit

List every `[TODO: cite]` remaining. These must be resolved before submission.
For each, suggest where to search and what the citation should be.

## Output format

```markdown
## /check-claims Audit
File: <path>
Date: <date>

---

## Summary
- Claims audited: <N>
- Supported ✅: <N>
- Partially supported ⚠️: <N>
- Unsupported ❌: <N>
- Require citation 🔍: <N>

---

## Numbers audit (INV-9)

| Claim in text | Section | Expected source | Table value | Match? |
|--------------|---------|----------------|-------------|--------|
| "achieves 86.4%" | Sec V-A | Table II | 86.4 | ✅ |
| "3× faster" | Sec I | Table III | 2.8× | ❌ CRITICAL |

---

## Unsupported claims ❌

### [CRITICAL] <claim>
Location: [Section, paragraph N]
Type: [quantitative / causal / novelty / qualitative]
What's missing: [specific evidence needed]
Fix: [specific action]

---

## Partially supported claims ⚠️

### <claim>
Location: [location]
Issue: [what's weak about the evidence]
Suggested fix: [how to strengthen]

---

## Claims requiring citation 🔍

| Claim | Location | Search suggestion |
|-------|---------|-----------------|
| "Existing methods fail in unstructured environments" | Sec I | Search ICRA 2022-2024 for manipulation failure modes |

---

## [TODO: cite] inventory

| Placeholder | Location | Suggested reference |
|------------|---------|-------------------|
| [TODO: cite] | Sec III, para 2 | This is the DAgger claim — cite Ross et al., AISTATS 2011 |

---

## Supported claims ✅
[Brief list — no action needed]

---

## Priority actions
1. [CRITICAL] Fix number mismatch: "3×" should be "2.8×" (or recheck Table III)
2. [CRITICAL] Add ablation for component X to support causal claim in Sec IV
3. [MAJOR] Resolve [TODO: cite] at Sec III, para 2
```
