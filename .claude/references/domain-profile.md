# Domain Profile — Robotics

Field calibration for conference-Darin. Agents read this file to calibrate search queries,
referee dispositions, baseline expectations, and writing standards to the robotics subfield.

---

## 1. Field specification

**Primary field:** Robotics (IEEE Robotics and Automation Society)
**Adjacent fields:** Machine Learning, Computer Vision, Control Theory, Cognitive Science

**Active subfields in conference-Darin:**

| Subfield | Key problems | Typical method types |
|----------|-------------|---------------------|
| Robot learning | Skill acquisition, generalization, sample efficiency | IL, RL, offline RL |
| Imitation learning | Learning from demonstrations, distribution shift | BC, DAgger, GAIL, diffusion |
| Manipulation | Grasping, assembly, contact-rich, bimanual, dexterous | IL + RL + planning |
| Humanoids | WBC, loco-manipulation, bipedal locomotion | RL + MPC + teleoperation |
| Sim2real | Domain gap, transfer, calibration | DR, adaptation, system ID |
| Perception for manipulation | Affordance, pose, 3D understanding | ViT, CLIP, NeRF, diffusion |
| Navigation | Map-free nav, SLAM, long-horizon | RL + SLAM + planning |
| Control | MPC, trajectory optimization, impedance | Optimal control + learning |

---

## 2. Target venues (ranked by tier)

### Tier 1 — Primary conferences (peer-reviewed, prestigious, high impact)

| Venue | Full name | Cycle | Notes |
|-------|-----------|-------|-------|
| ICRA | IEEE Intl. Conf. on Robotics and Automation | Annual (May) | Largest robotics venue, broad scope |
| IROS | IEEE/RSJ Intl. Conf. on Intelligent Robots and Systems | Annual (Oct) | Slightly more systems-focused |
| CoRL | Conference on Robot Learning | Annual (Nov) | High bar, learning-focused, real robots expected |
| RSS | Robotics: Science and Systems | Annual (July) | Small, very high bar, fundamental contributions |
| Humanoids | IEEE-RAS Intl. Conf. on Humanoid Robots | Annual (Dec) | Humanoids-specific |
| HRI | ACM/IEEE Intl. Conf. on Human-Robot Interaction | Annual (March) | Human factors + robotics |

### Tier 1 — Primary journals

| Venue | Full name | Notes |
|-------|-----------|-------|
| RA-L | IEEE Robotics and Automation Letters | Journal + conference presentation option |
| T-RO | IEEE Transactions on Robotics | Flagship journal, extended contributions |
| IJRR | The International Journal of Robotics Research | SAGE, high impact |
| Science Robotics | Science Robotics | High-profile, multi-disciplinary |

### Tier 2 — Adjacent venues with robotics tracks

| Venue | Relevant tracks |
|-------|----------------|
| NeurIPS | Robot Learning, Embodied AI workshops |
| ICML | Robotics applications |
| ICLR | Embodied AI, robotic control |
| CVPR / ICCV | Manipulation from vision, navigation |

---

## 3. Standard evaluation benchmarks

See `.claude/references/benchmark-notes.md` for detailed benchmark descriptions.

| Benchmark | Domain | Key metric | Standard reference |
|-----------|--------|-----------|-------------------|
| MetaWorld | Tabletop manipulation (50 tasks) | Success rate | Yu et al., CoRL 2019 |
| LIBERO | Lifelong learning, 4 task suites | Success rate | Liu et al., NeurIPS 2023 |
| RoboSuite / RoboMimic | Manipulation demos | Success rate | Mandlekar et al., IROS 2021 |
| FurnitureBench | Furniture assembly | Success rate | Heo et al., RSS 2023 |
| Calvin | Long-horizon manipulation | LCFSR | Mees et al., RA-L 2022 |
| Habitat | Indoor navigation | SPL, SR | Savva et al., ICCV 2019 |
| IsaacGym / Isaac Lab | GPU RL for locomotion | Reward, success | Makoviychuk et al., 2021 |
| AgiBot / HumanoidBench | Humanoid tasks | Success rate | Various 2024 |
| OpenX-Embodiment | Cross-robot generalization | Success rate | Consortium 2024 |

---

## 4. Common methodology families

See `.claude/references/method-guides.md` for detailed method descriptions and key papers.

| Family | Methods | Key papers (representative) |
|--------|---------|----------------------------|
| Behavior Cloning | BC, DAgger, HG-DAgger | Pomerleau 1989; Ross et al., ICML 2011 |
| Offline RL | IQL, TD3+BC, CQL | Kostrikov et al., ICLR 2022 |
| Diffusion-based IL | Diffusion Policy, BESO | Chi et al., CoRL 2023; Reuss et al., 2023 |
| Transformer IL | ACT, Octo, OpenVLA | Zhao et al., RSS 2023; Team et al., 2024 |
| Adversarial IL | GAIL, AIRL | Ho & Ermon, NeurIPS 2016 |
| RL for manipulation | SAC, TD3, PPO | Haarnoja et al., ICML 2018 |
| Whole-body control | OSC, WBC-IL, loco-manip | Various 2023–2024 |
| Foundation models | RT-2, π0, Octo | Brohan et al., 2023; Black et al., 2024 |

---

## 5. Field conventions

### Reporting standards

- Success rate (%): main metric for manipulation, grasping, navigation
- Sample efficiency: often reported as number of demonstrations required or timesteps to convergence
- Generalization: number of held-out tasks/objects/environments
- Real vs. sim: always clearly distinguished; if both, show both separately

### Notation standards

| Symbol | Convention |
|--------|-----------|
| s, a, r | State, action, reward |
| π, θ | Policy, policy parameters |
| τ | Trajectory |
| D | Demonstration dataset |
| T | Horizon / task horizon |
| N | Number of demonstrations / trials |

### Citation style

- IEEE numeric format: `[1]` in text, numbered reference list
- Author names: "A. Surname" not "Surname, A."
- Conference: "Proc. ICRA 2023" or "in Proc. IEEE ICRA, 2023, pp. X–Y"
- arXiv: cite published version if available; arXiv otherwise with arXiv:XXXX.XXXXX

---

## 6. Key papers a reviewer will expect

These papers are so foundational in robotics that any reviewer will notice if they are
missing from a paper in the relevant subfield:

### Imitation learning foundational
- DAgger: Ross, Gordon, Bagnell — AISTATS 2011
- GAIL: Ho, Ermon — NeurIPS 2016
- BC-Z: Jang et al. — CoRL 2022

### Manipulation learning
- Diffusion Policy: Chi et al. — CoRL 2023 (arXiv:2303.04137)
- ACT: Zhao et al. — RSS 2023
- RoboMimic: Mandlekar et al. — IROS 2021
- GATO: Reed et al. — TMLR 2022

### Foundation models for robotics
- RT-1: Brohan et al. — CoRL 2023
- RT-2: Brohan et al. — CoRL 2023
- Octo: Team et al. — RSS 2024
- π0: Black et al. — 2024 (arXiv:2410.24164)

### Sim2real
- Domain Randomization: Tobin et al. — IROS 2017
- OpenAI Dactyl: Andrychowicz et al. — Science Robotics 2020

### Navigation
- Habitat: Savva et al. — ICCV 2019
- VLN-BERT: Hong et al. — CVPR 2021

---

## 7. Common reviewer concerns by subfield

### Manipulation
- "The task is too simple" — add contact-rich or deformable object tasks
- "Sim-only results are insufficient" — add real robot experiments
- "No comparison to DiffusionPolicy/ACT" — these are the current baselines
- "The number of demonstrations is unrealistic" — address in discussion

### Humanoids / WBC
- "How does this scale to full-body?" — address scope explicitly
- "No comparison to MPC baseline" — add or justify exclusion
- "Teleoperation quality not quantified" — add HRI or motion quality metrics

### Sim2real
- "The sim-to-real gap is not characterized" — add domain gap analysis
- "Domain randomization range not justified" — cite calibration source

### Navigation
- "SPL not reported" — add this standard metric
- "Only tested in one environment" — add at least 2 environments

---

## 8. Quality tolerances

| Metric | Minimum for credible result | Strong result |
|--------|---------------------------|--------------|
| Manipulation success rate | N ≥ 20 trials per condition | N ≥ 50 |
| Navigation success rate | N ≥ 100 episodes | N ≥ 500 |
| RL training runs | N ≥ 5 seeds | N ≥ 10 |
| Sim2real transfer gap | Reported for both | <10pp gap documented |
| Generalization tasks | N ≥ 5 held-out | N ≥ 20 |
