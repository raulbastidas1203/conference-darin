# Benchmark Notes — Robotics

Reference notes on standard benchmarks used in robotics papers. Used by agents to
calibrate baseline expectations, metric requirements, and comparison standards.

---

## Manipulation Benchmarks

### MetaWorld

**Reference:** Yu, T., et al. "Meta-World: A Benchmark and Evaluation for Multi-Task and
Meta Reinforcement Learning." CoRL 2019.

**Description:** 50 tabletop manipulation tasks with a Sawyer robot arm. Tasks range from
simple pushing to complex assembly. Designed for multi-task and meta-RL evaluation.

**Standard evaluation protocol:**
- ML1 (1 task), ML10 (10 tasks), ML45 (45 tasks)
- MT10 / MT50 for multi-task
- Success rate (%) averaged over 50 test episodes per task
- Separate success criterion per task (defined in benchmark)

**Robot:** Sawyer arm, simulated in MuJoCo
**Observation:** State-based (default) or image-based (harder)
**Standard citation:** `yu2019meta` — cite Yu et al., CoRL 2019

**When to use:** Multi-task IL/RL for manipulation, generalization across tasks

**Reviewer notes:**
- Reviewers know this benchmark well; compare to published numbers if available
- State-based is easier; image-based is more realistic; specify which
- "MetaWorld" ≠ "real manipulation" — real robot validation still expected for real claims

---

### LIBERO

**Reference:** Liu, B., et al. "LIBERO: Benchmarking Knowledge Transfer for Lifelong
Robot Learning." NeurIPS 2023.

**Description:** 4 task suites for lifelong learning: LIBERO-Spatial (10 tasks, object position
varies), LIBERO-Object (10 tasks, object identity varies), LIBERO-Goal (10 tasks, goal varies),
LIBERO-Long (10 tasks, long-horizon, hardest).

**Standard evaluation protocol:**
- Success rate (%) per suite, averaged over 20 evaluation trials per task
- Report all 4 suites for fair comparison
- Standard split: 50 demonstrations per task (human-collected)

**Robot:** Franka Panda, simulated in ROBOSUITE
**Observation:** RGB images (front + wrist cameras)
**Standard citation:** `liu2023libero` — cite Liu et al., NeurIPS 2023

**When to use:** Lifelong learning, task generalization, imitation learning evaluation

**Reviewer notes:**
- Must report all 4 suites (LIBERO-Long is hardest and most informative)
- Standard: compare Diffusion Policy and ACT on LIBERO
- 20 evaluation trials minimum; 50 preferred

---

### RoboMimic / RoboSuite

**References:**
- RoboSuite: Zhu, Y., et al. "robosuite: A Modular Simulation Framework and Benchmark
  for Robot Learning." IROS 2021.
- RoboMimic: Mandlekar, A., et al. "What Matters in Learning from Offline Human
  Demonstrations for Robot Manipulation." CoRL 2021.

**Description:** RoboSuite is the simulation framework (Franka, UR5, IIWA, Sawyer in MuJoCo).
RoboMimic is the benchmark built on top with human-collected demonstrations and standard tasks:
Lift, Can, Square, Transport, ToolHang.

**Standard evaluation:**
- Success rate (%), 50 evaluation trials per task
- Standard operator types: "Proficient Human" (PH) and "Multi Human" (MH) datasets

**When to use:** Manipulation IL with image observations, offline RL baseline

**Reviewer notes:**
- Square and ToolHang are the hard tasks; Lift is almost solved
- Report: which tasks, which operator type, image vs state

---

### CALVIN (Compositional Actions from Language Instructions and Visual Observations)

**Reference:** Mees, O., et al. "CALVIN: A Benchmark for Language-Conditioned Policy
Learning for Long-Horizon Robot Manipulation Tasks." RA-L 2022.

**Description:** Long-horizon language-conditioned manipulation. Robot must complete
sequences of up to 5 subtasks. Tested in 4 environments (A, B, C, D) with ABC→D split.

**Standard metric:** LCFSR — Long Chain Functional Success Rate (average task completion
in a chain of T subtasks; reported as average tasks completed per episode).

**Standard split:** Train on A+B+C environments, test on D (zero-shot generalization)

**When to use:** Language-conditioned manipulation, long-horizon reasoning

---

### FurnitureBench

**Reference:** Heo, M., et al. "FurnitureBench: Reproducible Real-World Benchmark for
Long-Horizon Complex Manipulation." RSS 2023.

**Description:** Furniture assembly tasks on a real Franka robot. 5 furniture pieces
(lamp, one-leg chair, round table, square table, cabinet). Designed for reproducible
real-robot evaluation.

**When to use:** Real-robot long-horizon manipulation, contact-rich assembly

---

### IsaacGym / Isaac Lab

**Reference:** Makoviychuk, V., et al. "Isaac Gym: High Performance GPU-Based Physics
Simulation for Robot Learning." NeurIPS 2021 Datasets and Benchmarks.
Isaac Lab: Li, Z., et al. 2023.

**Description:** GPU-accelerated physics simulation for massively parallel RL training.
Used for locomotion, dexterous manipulation, and humanoid control.

**Common use cases:**
- Legged robot locomotion (Unitree A1, Go1, Spot)
- Dexterous hand manipulation (Shadow Hand, Allegro)
- Humanoid whole-body control

**Standard reporting for RL:** training curve (reward vs. timesteps), final policy success rate,
number of parallel environments, total training steps.

**When to use:** RL for locomotion, sim2real for legged robots, large-scale parallel training

---

### Habitat (Navigation)

**Reference:** Savva, M., et al. "Habitat: A Platform for Embodied AI Research." ICCV 2019.
Habitat 2.0: Szot, A., et al. NeurIPS 2021.
Habitat 3.0: Puig, X., et al. ICLR 2024.

**Description:** Simulation framework for embodied navigation and interaction in
photorealistic environments. Uses Matterport3D, HM3D, and Gibson datasets.

**Standard tasks:**
- PointNav: navigate to GPS coordinates
- ObjectNav: navigate to object category
- Pick-and-Place: navigate + manipulate

**Standard metrics:**
- SR: Success Rate (%)
- SPL: Success weighted by Path Length
- dtG: Distance to Goal at episode end

**Standard splits:** Val seen / Val unseen / Test (held-out environments)

**When to use:** Visual navigation, embodied AI, language-conditioned navigation

---

### OpenX-Embodiment

**Reference:** Open X-Embodiment Collaboration. "Open X-Embodiment: Robotic Learning
Datasets and RT-X Models." ICRA 2024.

**Description:** Large-scale cross-embodiment dataset from 22 robot types, 60,000+ tasks.
Used for training generalist robot policies (RT-X, Octo, OpenVLA).

**When to use:** Cross-embodiment generalization, foundation model evaluation

---

## Standard Metric Reference

| Metric | Definition | Used in |
|--------|-----------|--------|
| SR (Success Rate) | % of episodes where task is completed | All manipulation/navigation |
| SPL | SR × (optimal_path / actual_path) | Navigation |
| LCFSR | Avg tasks completed in N-task chain | CALVIN, long-horizon |
| Data efficiency | SR vs. N demonstrations | IL papers |
| Sim-to-real gap | SR_sim - SR_real | Sim2real papers |
| Training efficiency | SR vs. environment steps | RL papers |

---

## Benchmark citation quick-reference

```bibtex
@inproceedings{yu2019meta,
  title={Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning},
  author={Yu, Tianhe and Quillen, Deirdre and He, Zhanpeng and Julian, Ryan and Hausman, Karol and Finn, Chelsea and Levine, Sergey},
  booktitle={Proc. CoRL},
  year={2019}
}

@inproceedings{liu2023libero,
  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
  author={Liu, Bo and Zhu, Yifeng and Garg, Animesh and Mandlekar, Ajay and Zhu, Yuke},
  booktitle={Proc. NeurIPS},
  year={2023}
}

@inproceedings{mandlekar2021matters,
  title={What Matters in Learning from Offline Human Demonstrations for Robot Manipulation},
  author={Mandlekar, Ajay and Xu, Danfei and Wong, Josiah and Nasiriany, Soroush and Wang, Chen and Kulkarni, Rohun and Fei-Fei, Li and Savarese, Silvio and Zhu, Yuke and Mart{\'\i}n-Mart{\'\i}n, Roberto},
  booktitle={Proc. CoRL},
  year={2021}
}

@article{mees2022calvin,
  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},
  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},
  journal={IEEE Robotics and Automation Letters},
  year={2022}
}

@inproceedings{makoviychuk2021isaac,
  title={Isaac Gym: High Performance {GPU}-Based Physics Simulation for Robot Learning},
  author={Makoviychuk, Viktor and Wawrzyniak, Lukasz and Guo, Yunrong and Lu, Michelle and Storey, Kier and Macklin, Miles and Hoeller, David and Rudin, Nikita and Allshire, Arthur and Handa, Ankur and State, Gavriel},
  booktitle={Proc. NeurIPS Datasets and Benchmarks},
  year={2021}
}

@inproceedings{savva2019habitat,
  title={Habitat: {A} Platform for Embodied {AI} Research},
  author={Savva, Manolis and Kadian, Abhishek and Maksymets, Oleksandr and Zhao, Yili and Wijmans, Erik and Jain, Bhavana and Straub, Julian and Liu, Jia and Koltun, Vladlen and Malik, Jitendra and Parikh, Devi and Batra, Dhruv},
  booktitle={Proc. ICCV},
  year={2019}
}
```
