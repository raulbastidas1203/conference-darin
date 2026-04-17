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
| `lhm2025humanoid` | LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation in Diverse Messy Environments | Zhang H. (+ Sun J., Caprio M., Tang J., Zhang S., Zhang Q., Pan W.) | arXiv 2025 | Preprint | Central | Free | FULL-TEXT | Unread | PDF in /papers/ |
| `humanoidcoa2025` | Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation | Wen C. (+ Bethala G., Hao Y., Pudasaini N., Huang H., Yuan S., Huang B., Nguyen A., Wang M., Tzes A., Fang Y.) | arXiv 2025 | Preprint | Central | Free | FULL-TEXT | Unread | PDF in /papers/ |
| `ieee2024safewarehouse` | Safe Human Robot Navigation in Warehouse Scenario | Farrell S., Li C., Yu H., Yoshimitsu R., Gao S., Christensen H.I. | IEEE 2024 | Conference | Central | Paywall | FULL-TEXT | Unread | PDF in /papers/; CBF-based safety for humanoid in warehouse |
| `humanoidcat2026` | Learning Humanoid Loco-manipulation with Constraints as Terminations | Leziart P-A., Morisawa M., Kanehiro F. | SII 2026 (IEEE/SICE) | Conference | Central | Free | FULL-TEXT | Unread | PDF in /papers/; DOI:10.1109/SII64115.2026.11404486; venue corrected from tracker |
| `zhang2025falcon` | FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation | Zhang Y. (CMU) | arXiv / L4DC 2026 | Preprint | Central | Free | CANDIDATE | Unread | Force-adaptive WBC; cart, payload, door tasks |
| `rollo2023semantic` | Semantic-based Loco-Manipulation for Human-Robot Collaboration in Industrial Environments | Rollo F. | arXiv / Springer 2023 | Preprint | Central | Free | CANDIDATE | Unread | Industrial environment; "bring me object" scenario |
| `peron2025pixels` | From Pixels to Shelf: End-to-End Algorithmic Control for Supermarket Stocking and Fronting | Peron D. | arXiv 2025 | Preprint | Central | Free | CANDIDATE | Unread | 98% success on 724 events; closest real-world logistics analogue |
| `he2025hover` | HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots | He T., Xiao W., Lin T., Luo Z., Xu Z., Jiang Z., Liu C., Shi G., Wang X., Fan L., Zhu Y. | ICRA 2025 | Conference | Central | Free | VERIFIED | Unread | arXiv:2410.21229; confirmed ICRA 2025; unifies nav + loco-manip + tabletop |
| `dao2024boxloco` | Sim-to-Real Learning for Humanoid Box Loco-Manipulation | Dao J., Duan H., Fern A. | ICRA 2024 | Conference | Central | Free | VERIFIED | Unread | arXiv:2310.03191; box pickup+carry on Digit humanoid; warehouse-relevant |
| `rigo2024heavyloco` | Hierarchical Optimization-Based Control for Whole-Body Loco-Manipulation of Heavy Objects | Rigo A., Hu M., Gupta S.K., Nguyen Q. | ICRA 2024 | Conference | Central | Free | VERIFIED | Unread | arXiv:2311.00112; 8kg payload on legged robot via MPC |
| `mobiletv2025` | Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control | — (verify authors) | ICRA 2025 | Conference | Related | Free | CANDIDATE | Unread | arXiv:2412.07773; decoupled upper-body via CVAE; teleoperation + manipulation |
| `hat2025humanoid` | Humanoid Policy ~ Human Policy (HAT) | — (verify authors) | ICRA 2025 | Conference | Related | Free | CANDIDATE | Unread | arXiv:2503.13441; cross-embodiment from egocentric demos |
| `li2023hector` | Dynamic Loco-Manipulation on HECTOR: Humanoid for Enhanced ConTrol and Open-source Research | Li J. et al. (USC) | ICRA 2023/2024 (verify) | Conference | Related | Free | CANDIDATE | Unread | arXiv:2312.11868; MPC-based; 2.5kg carry; venue year needs confirmation |
| `gu2025survey` | Humanoid Locomotion and Manipulation: Current Progress and Challenges | Gu Z. | arXiv 2025 | Preprint | Related | Free | CANDIDATE | Unread | Comprehensive survey; required background reading |
| `noreils2024humanoids` | Humanoid Robots at work: where are we? | Noreils F. | arXiv 2024 | Preprint | Related | Free | CANDIDATE | Unread | Industrial deployment feasibility assessment |
| `jiang2025behavior` | BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation | Jiang Y. (Stanford) | CoRL 2025 | Conference | Related | Free | CANDIDATE | Unread | Bimanual WBM framework; household but methods relevant |
| `ferrazza2024humanoidbench` | HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Tasks | Ferrazza C. | RSS 2024 | Conference | Related | Free | CANDIDATE | Unread | 15 whole-body manip + 12 loco tasks; evaluation reference |
| `ciebielski2025tamp` | Task and Motion Planning for Humanoid Loco-Manipulation | Ciebielski M. (TUM) | IEEE Humanoids 2025 | Conference | Related | Paywall | CANDIDATE | Unread | Unified contact-mode planning framework |
| `murooka2021graph` | Humanoid Loco-Manipulation Planning Based on Graph Search and Reachability Maps | Murooka M. | RA-L 2021 | Journal | Related | Paywall | CANDIDATE | Unread | Footstep + grasp sequencing via graph search |
| `taouil2025diffusion` | Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models | Taouil I. (TUM) | IEEE Humanoids 2025 | Conference | Related | Free | CANDIDATE | Unread | Diffusion-based long-horizon trajectory planning |
| `xue2025hugwbc` | A Unified and General Humanoid Whole-Body Controller for Versatile Locomotion (HugWBC) | Xue Y. | arXiv 2025 | Preprint | Related | Free | CANDIDATE | Unread | Versatile locomotion + real-time upper-body manipulation |
| `an2025collaborative` | Collaborative Loco-Manipulation for Pick-and-Place with Dynamic Reward Curriculum | An T. | arXiv 2025 | Preprint | Related | Free | CANDIDATE | Unread | 55% training efficiency gain; ANYmal D real-world |
| `zhang2025multistage` | Learning Multi-Stage Pick-and-Place with a Legged Mobile Manipulator | Zhang H. | T-RO 2025 | Journal | Related | Free | CANDIDATE | Unread | Quadruped but multi-stage task chaining methods relevant |
| `pan2024roboduet` | RoboDuet: Learning a Cooperative Policy for Whole-body Legged Loco-Manipulation | Pan G. (Tsinghua) | RA-L 2025 | Journal | Related | Free | CANDIDATE | Unread | Two-policy cooperative framework; 23% over baselines |
| `amo2025motion` | AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control | — | RSS 2025 | Conference | Related | Free | CANDIDATE | Unread | Hierarchical RL + trajectory optimization; Unitree G1 |
| `chappellet2024slam` | Humanoid Loco-Manipulations using Combined Fast Dense 3D Tracking and SLAM | Chappellet | T-ASE 2024 | Journal | Related | Paywall | CANDIDATE | Unread | Vision + SLAM for bimanual grasping + bipedal loco |
| `yuan2025bfm` | A Survey of Behavior Foundation Models for Humanoid Whole-Body Control | Yuan M. | IEEE 2025 | Journal | Related | Free | CANDIDATE | Unread | BFM survey covering pre-training + adaptation |
| `ieee2018dualarm` | Dual arm robot manipulator for grasping boxes of different dimensions in a logistics warehouse | — | IEEE 2018 | Conference | Related | Paywall | CANDIDATE | Unread | Warehouse logistics, arm-only (not humanoid) |
| `ferrari2021patterns` | Humanoid Loco-Manipulations Pattern Generation and Stabilization Control | — | T-RO 2021 | Journal | Related | Paywall | CANDIDATE | Unread | Foundational stabilization under external manipulation forces |
| `ferrari2017wholebody` | Humanoid whole-body planning for loco-manipulation tasks | Ferrari P. | ICRA 2017 | Conference | Related | Paywall | CANDIDATE | Unread | Foundational whole-body planning |
| `yuan2025bfm` | A Survey of Behavior Foundation Models for Humanoid Whole-Body Control | Yuan M. | IEEE 2025 | Journal | Related | Free | CANDIDATE | Unread | BFM survey |

---

## Papers to Retrieve (NEED-PDF)

These papers are Central (important for full-text reading) but have no free access.
Retrieve with university credentials and place in /papers/.

| Key | Title | Authors | Venue / Year | DOI | Why needed |
|-----|-------|---------|-------------|-----|-----------|

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
