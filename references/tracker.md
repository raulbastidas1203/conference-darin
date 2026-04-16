# Reference Tracker — conference-Darin

Classification table for all references used or considered in this workspace.
Updated by `/search-lit` (CANDIDATE entries) and manually when papers are read (status upgrades).

**Status definitions:**
- `CANDIDATE` — found in search; title/venue/year unconfirmed from primary source
- `VERIFIED` — confirmed in DBLP / IEEE Xplore / arXiv / publisher page; safe to cite
- `FULL-TEXT` — PDF in /papers/ or arXiv full text read
- `NEED-PDF` — important paper, no free access; flag for user to retrieve
- `UNVERIFIED` — cannot confirm; do NOT include in references.bib

**Read status:**
- `Unread` — not yet read
- `Abstract` — abstract read; relevance assessed
- `Full` — full text read; lit-note created

**Relevance:**
- `Central` — same problem, direct competitor, baseline, or defines benchmark used
- `Related` — relevant to a sub-aspect; background reference
- `Marginal` — shares keywords only; list without citing unless needed

---

## Full-Text References (PDF available in /papers/ or arXiv)

| Key | Title | First Author | Venue / Year | Source | Relevance | Access | Status | Read | Notes |
|-----|-------|-------------|-------------|--------|-----------|--------|--------|------|-------|
| *Add entries here as PDFs are placed in /papers/* | | | | | | | | | |

---

## Verified References (confirmed, in references.bib)

| Key | Title | First Author | Venue / Year | Source | Relevance | Access | Status | Read | Notes |
|-----|-------|-------------|-------------|--------|-----------|--------|--------|------|-------|
| *Add entries here after verification from primary source* | | | | | | | | | |

---

## Candidate References (to evaluate / verify)

| Key | Title | First Author | Venue / Year | Source | Relevance | Access | Status | Read | Notes |
|-----|-------|-------------|-------------|--------|-----------|--------|--------|------|-------|
| *Populated by /search-lit* | | | | | | | | | |

---

## Papers to Retrieve (NEED-PDF)

These papers are Central (important for full-text reading) but have no free access.
Retrieve with university credentials and place in /papers/.

| Key | Title | Authors | Venue / Year | DOI | Why needed |
|-----|-------|---------|-------------|-----|-----------|
| *Populated by Librarian when Central paper has no arXiv version* | | | | | |

---

## Unverified (excluded from references.bib)

Papers found in search that could not be confirmed in any primary source.
Do not cite these.

| Entry | Issue | Date flagged |
|-------|-------|-------------|
| *Populated by Librarian-Critic when a fabricated or unconfirmable citation is detected* | | |

---

## Benchmark citations (pre-filled, verified)

Pre-filled standard benchmark references that are commonly needed.
Verify BibTeX entries against the original publications before use.

| Key | Paper | Venue / Year | Relevance |
|-----|-------|-------------|-----------|
| `yu2019meta` | MetaWorld: A Benchmark and Evaluation for Multi-Task and Meta RL | CoRL 2019 | Benchmark |
| `liu2023libero` | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | NeurIPS 2023 | Benchmark |
| `mandlekar2021matters` | What Matters in Learning from Offline Human Demonstrations | CoRL 2021 | Benchmark + baselines |
| `mees2022calvin` | CALVIN: A Benchmark for Language-Conditioned Policy Learning | RA-L 2022 | Benchmark |
| `makoviychuk2021isaac` | Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning | NeurIPS D&B 2021 | Benchmark |
| `savva2019habitat` | Habitat: A Platform for Embodied AI Research | ICCV 2019 | Benchmark |
| `chi2023diffusion` | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | CoRL 2023 | Central IL baseline |
| `zhao2023act` | Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware | RSS 2023 | Central IL baseline |
| `ross2011reduction` | A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger) | AISTATS 2011 | Foundational IL |
| `ho2016generative` | Generative Adversarial Imitation Learning (GAIL) | NeurIPS 2016 | Foundational IL |
| `haarnoja2018soft` | Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning | ICML 2018 | RL baseline |
| `tobin2017domain` | Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World | IROS 2017 | Sim2real foundational |

---

## Usage notes

1. When `/search-lit` runs, it adds new rows to the Candidate table.
2. When you read a paper and confirm its details from a primary source, move it to Verified and update Read status.
3. When you have the PDF in /papers/, move to Full-Text.
4. When a Candidate paper is needed as a citation, verify first before adding to references.bib.
5. The Librarian-Critic checks this table for UNVERIFIED entries in active citations.
