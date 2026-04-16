# Method Guides — Robotics

Technical reference for the main method families used in robotics papers.
Agents use this to calibrate baseline requirements, ablation expectations,
and reviewer concerns for each method type.

---

## 1. Imitation Learning (IL)

### Problem setting
Learn a policy π(a|s) from expert demonstrations D = {(s, a)} without reward signal.

### Method family tree

```
Imitation Learning
├── Behavior Cloning (BC)           — Supervised learning on (s, a) pairs
│   ├── DAgger                      — Interactive IL, reduces covariate shift
│   └── HG-DAgger                   — Human-gated DAgger
├── Inverse RL (IRL)                — Learn reward, then optimize
│   └── GAIL / AIRL                 — Adversarial IRL
├── Diffusion-based IL
│   ├── Diffusion Policy            — DDPMs for action sequences (Chi et al., CoRL 2023)
│   └── BESO / ConsistencyPolicy    — Consistency models for faster inference
└── Transformer-based IL
    ├── ACT                         — Action Chunking with Transformers (Zhao et al., RSS 2023)
    ├── Octo                        — Transformer IL pretrained on cross-embodiment data
    └── OpenVLA                     — VLA: vision-language-action model
```

### Key papers (required as baselines or citations)

| Paper | Venue | Key contribution | When to cite |
|-------|-------|-----------------|-------------|
| DAgger (Ross et al.) | AISTATS 2011 | Online IL, covariate shift fix | Any IL paper |
| GAIL (Ho & Ermon) | NeurIPS 2016 | Adversarial IL | Adversarial methods |
| BC-Z (Jang et al.) | CoRL 2022 | Multi-task BC with language | Language-conditioned |
| Diffusion Policy (Chi et al.) | CoRL 2023 | Diffusion for visuomotor | Manipulation IL |
| ACT (Zhao et al.) | RSS 2023 | Action chunking, transformer | Bimanual, dexterous |
| RoboMimic (Mandlekar et al.) | IROS 2021 | Benchmark + algorithm comparison | Manipulation baselines |

### Standard baselines

Any IL paper for manipulation should compare against:
1. **BC** — vanilla behavior cloning (the baseline)
2. **Diffusion Policy** (Chi et al., CoRL 2023) — current state of the art
3. **ACT** (Zhao et al., RSS 2023) — transformer-based alternative
4. If offline RL relevant: **IQL** (Kostrikov et al., ICLR 2022)

### Common failure modes (reviewer will ask about)

- **Covariate shift**: BC degrades when test distribution differs from demos
- **Compounding errors**: small errors accumulate over long horizons
- **Multi-modality**: BC struggles with multiple valid action modes (averaging problem)
- **Sample inefficiency**: needs many demonstrations for complex tasks

### Metrics

- Success rate (%) — primary
- Number of demonstrations required — for efficiency claims
- Rollout length / task completion time — for efficiency
- Generalization to new objects/tasks — for transfer claims

### Ablation requirements

If proposing new IL method, ablate:
- vs. vanilla BC
- Effect of each key component (loss function, architecture choice, training procedure)
- Data efficiency curve (success rate vs. number of demos)

---

## 2. Reinforcement Learning for Robotics

### Problem setting
Learn π(a|s) via trial-and-error in an environment with reward r(s, a).

### Key algorithm families

| Algorithm | Type | Key paper | When to use |
|-----------|------|----------|------------|
| SAC | Off-policy, continuous | Haarnoja et al., ICML 2018 | Continuous manipulation |
| TD3 | Off-policy, continuous | Fujimoto et al., ICML 2018 | Alternative to SAC |
| PPO | On-policy, continuous | Schulman et al., 2017 | GPU sim (Isaac) |
| DDPG | Off-policy, continuous | Lillicrap et al., ICLR 2016 | Baseline |
| DreamerV3 | Model-based | Hafner et al., ICLR 2023 | Sample efficiency claims |

### Standard concerns (reviewer)

- Reward shaping: if reward is dense, is it fair to compare with sparse-reward methods?
- Sample efficiency: how many environment steps? (should be reported)
- Sim2real: RL in sim only is weak for manipulation claims
- Reproducibility: must show results over N ≥ 5 seeds

---

## 3. Diffusion Policy (detailed)

**Reference:** Chi, C., Feng, Z., Du, Y., et al. "Diffusion Policy: Visuomotor Policy Learning via
Action Diffusion." CoRL 2023. arXiv:2303.04137

**Key ideas:**
- Models action distribution as a diffusion process (DDPM)
- Handles multi-modal action distributions (unlike BC which averages)
- Works with image observations via CNN encoder
- Action chunking: predicts T_p steps, executes T_a steps

**Variants:**
- CNN-based (faster, lower memory)
- Transformer-based (better for complex tasks, more memory)
- Consistency Policy (faster inference, fewer diffusion steps)

**Standard benchmark:** PushT (toy), RoboMimic (state + image), Real robot ALOHA tasks

**Required comparison:** Any manipulation IL paper must compare vs. Diffusion Policy
or explicitly justify why (out of scope, different embodiment, different modality).

---

## 4. ACT — Action Chunking with Transformers

**Reference:** Zhao, T., Kumar, V., Levine, S., Finn, C. "Learning Fine-Grained Bimanual
Manipulation with Low-Cost Hardware." RSS 2023.

**Key ideas:**
- CVAE-based policy with transformer architecture
- Action chunking: predict and execute k-step chunks to handle temporal consistency
- Designed for bimanual manipulation with ALOHA hardware
- Real-world focus: demonstrated on contact-rich bimanual tasks

**When this is the right baseline:** Bimanual manipulation, ALOHA hardware,
fine-grained manipulation with low-cost setup.

---

## 5. Sim2Real Transfer

### Problem setting
Train policy in simulation, deploy on real robot. The sim-to-real gap is the main challenge.

### Key approaches

| Approach | Key idea | Reference |
|----------|---------|----------|
| Domain Randomization (DR) | Randomize sim parameters to cover real | Tobin et al., IROS 2017 |
| System Identification | Calibrate sim to match real | Various |
| Domain Adaptation | Train adapter between sim and real features | Various |
| Real-to-Sim | Use real observations to improve sim | OpenAI Dactyl 2020 |

### Standard evaluation requirements

Papers claiming sim2real transfer must report:
1. Performance in sim (as reference)
2. Performance on real robot (as target)
3. Sim-to-real gap: how much performance is lost?
4. Description of real hardware (robot, sensors, environment — INV-4)

**Reviewer will ask:** "What is the sim-to-real gap?" — must be quantified.

### Domain randomization parameters (common for manipulation)

- Object mass, friction, geometry
- Camera viewpoint jitter
- Lighting conditions
- Actuator delays and noise
- Table surface properties

---

## 6. Whole-Body Control (WBC) and Humanoids

### Problem setting
Control a humanoid (or mobile manipulation robot) to perform tasks requiring
coordinated whole-body motion.

### Key approaches

| Approach | Key idea | Reference |
|----------|---------|----------|
| OSC (Operational Space Control) | Task-space PD control | Khatib 1987; implemented in RoboSuite |
| WBC-IL | Learn WBC policy from demonstrations | Various 2023–2024 |
| MPC-based WBC | Trajectory optimization + whole-body | Various |
| Teleoperation + IL | Collect demos via teleoperation, train IL | UMI, HumanPlus, etc. |

### Humanoid-specific papers (reviewer expects these)

- Figure-01, Unitree H1, Boston Dynamics Atlas papers
- UMI (Universal Manipulation Interface) — Chi et al., RSS 2024
- HumanPlus — Fu et al., 2024
- Teleoperation for humanoids: OmniH2O, HumanoidBench

### Metrics for humanoids

- Task success rate (primary)
- Motion quality (jerk, smoothness — if claimed)
- Teleoperation latency / operator fatigue (if claimed)
- Base stability during manipulation

---

## 7. Foundation Models for Robotics

### Overview

Large pretrained models applied to robot control, either as policy backbone or
as semantic/visual representation encoder.

### Key architectures

| Model | Type | Paper | Notes |
|-------|------|-------|-------|
| RT-1 | Transformer policy | Brohan et al., CoRL 2023 | Large-scale manipulation |
| RT-2 | VLA (vision-language-action) | Brohan et al., CoRL 2023 | Instruction following |
| Octo | Transformer IL, cross-embodiment | Team et al., RSS 2024 | Open weights |
| OpenVLA | VLA, open | Kim et al., CoRL 2024 | Open weights |
| π0 (pi-zero) | Flow matching + VLA | Black et al., 2024 | Physical Intelligence |
| GROOT | Visual representation for generalization | Various 2024 | |

### When foundation models are relevant baselines

If your paper claims generalization or language-conditioned manipulation, compare to:
- Octo (open weights, strong baseline)
- OpenVLA (open weights)
- RT-2 (if compute is available)

---

## 8. Evaluation design principles

### What makes a credible evaluation

1. **Task diversity:** At least 5 tasks for generalization claims; 1–2 tasks for proof-of-concept
2. **Object diversity:** Multiple objects for grasping/manipulation generalization
3. **Environment realism:** Clutter, lighting variation, pose variation for real-world claims
4. **Train-test split:** Objects/tasks not seen during training for generalization
5. **Trial count:** N ≥ 20 per condition for manipulation; N ≥ 50 for navigation

### Ablation design

For any proposed method, ablate in this priority order:
1. Key architectural choice (if novel)
2. Key training procedure (if novel)
3. Key data/representation (if novel)
4. Hyperparameter sensitivity for the 2 most important hyperparameters

### Failure mode analysis

Strong papers include a qualitative analysis of when the method fails.
Show 2–3 representative failure cases with explanation of why they fail.
This demonstrates understanding of the method's limitations.
