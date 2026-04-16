# Skill: /search-lit

Systematic literature search and classification for a robotics topic.
Dispatches Librarian → Librarian-Critic pipeline.

## Invocation

```
/search-lit <topic> [--venue icra|iros|corl|rss|ral|tro] [--years YYYY-YYYY] [--type survey|method|benchmark|all]
```

**Examples:**
```
/search-lit "diffusion models for robot manipulation"
/search-lit "sim2real transfer locomotion" --venue icra --years 2022-2025
/search-lit "bimanual manipulation imitation learning" --type benchmark
```

## What this skill does

1. **Reads context** — checks `drafts/` for active paper to understand the topic;
   reads `.claude/references/domain-profile.md` to calibrate subfield expectations
2. **Dispatches Librarian** — runs full search protocol (Tier 1 venues → APIs → arXiv)
3. **Updates tracker** — adds all papers to `references/tracker.md` under CANDIDATE status
4. **Dispatches Librarian-Critic** — verifies coverage, checks for fabrications, identifies gaps
5. **Presents consolidated output** — merged Librarian + Critic report

## Librarian protocol (runs as part of this skill)

See `.claude/agents/librarian.md` for full protocol.

**Search sources (in priority order):**
1. IEEE Xplore for ICRA/IROS/RA-L/T-RO/Humanoids papers
2. OpenReview for CoRL papers
3. Semantic Scholar API for cross-venue metadata and citations
4. DBLP for CS/robotics conference metadata
5. arXiv cs.RO, cs.AI, cs.CV, cs.LG for preprints (marked [PREPRINT])
6. Google Scholar for broader discovery

**For each paper found, extract:** title, authors, venue, year, DOI or arXiv ID,
citation count, abstract summary (1–2 sentences), access status.

**Classification:** Central / Related / Marginal (see agent spec)

## Librarian-Critic checks (runs after Librarian)

See `.claude/agents/librarian-critic.md` for full protocol.

Verifies: citation integrity (no fabrications), coverage gaps, classification accuracy,
novelty claim support.

## Output

```markdown
## /search-lit: <topic>
Date: <date>
Queries: [list]
Agents: Librarian + Librarian-Critic

---

### Central papers (<N>)
| # | Title | Authors | Venue/Year | Cites | ID | Access | Status |
|---|-------|---------|-----------|-------|----|--------|--------|
| 1 | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | Chi et al. | CoRL 2023 | 847 | arXiv:2303.04137 | Free | VERIFIED |

**Notes:**
- [1] Required baseline for any manipulation IL paper at ICRA/CoRL.
- [2] Defines the LIBERO benchmark used by [1]; cite as benchmark reference.

---

### Related papers (<N>)
| # | Title | Authors | Venue/Year | Cites | ID | Access |
| ...

---

### Coverage gaps (Librarian-Critic)
MAJOR: Missing [description — reviewer will expect this]
MINOR: [description]

---

### Papers to retrieve (NEED-PDF)
These are Central papers with no free access. Fetch with university credentials:
- [Full citation], DOI: [DOI]

---

### UNVERIFIED entries
[list or "none"] — removed from references.bib

---

### tracker.md updated
<N> CANDIDATE entries added to references/tracker.md

---

### Recommended next steps
- Read full text of: [top 3–5 Central papers]
- Additional query suggestion: [if coverage is sparse]
- Ready for /related-work: [Yes / Not yet — need more coverage in X]
```

## Tracker update format

For each paper found, add to `references/tracker.md`:

```
| key | Title | First Author | Venue/Year | Source Type | Relevance | Access | Status | Read |
```

Source type: `Conference` | `Journal` | `Preprint` | `Workshop`
Status: `CANDIDATE` → `VERIFIED` → `FULL-TEXT` | `NEED-PDF` | `UNVERIFIED`
Read: `Unread` | `Abstract` | `Full`
