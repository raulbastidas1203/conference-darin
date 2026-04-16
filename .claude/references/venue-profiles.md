# Venue Profiles — Robotics

Detailed calibration for target venues. Used by Editor and Domain-Referee to simulate
peer review accurately. Updated from publicly available information; check official CFPs
for current deadlines and requirements.

---

## ICRA — IEEE International Conference on Robotics and Automation

**Status:** Tier 1, primary venue
**Acceptance rate:** ~44% (2023), ~43% (2024) — competitive but not elite
**Scope:** Broad robotics: manipulation, navigation, locomotion, perception, learning,
human-robot interaction, medical, soft robotics, field robotics

**Format:**
- 8 pages + unlimited references (as of 2024)
- IEEE double-column, Times New Roman 10pt
- Double-blind review (since 2020)
- Video submission: recommended, not mandatory

**Review process:**
- 3 reviewers per paper
- ACs make final decisions
- Rebuttal period: yes (~1 week)

**Common reviewer compositions:**
- 2 domain experts + 1 methods generalist typical
- Systems reviewers common; pure ML reviewers rare

**Publication bar:**
- Solid engineering contribution with working system: acceptable
- Sim-only: accepted if learning contribution is clear; challenged if claim is about physical systems
- Incremental: accepted if clearly positioned and well-validated

**Reviewer pet peeves:**
1. Sim results claimed as real-world performance
2. Missing comparison to obvious recent baseline
3. Task designed to favor proposed method
4. Vague contribution (what exactly is new?)

**Submission timeline (approximate, verify with CFP):**
- Full paper deadline: September/October
- Notification: January/February
- Conference: May

**Key statistics for calibration:**
- ~9,000 submissions in 2024; ~3,900 accepted
- Most competitive tracks: manipulation learning, humanoids, navigation

---

## IROS — IEEE/RSJ International Conference on Intelligent Robots and Systems

**Status:** Tier 1, primary venue
**Acceptance rate:** ~46% (2023)
**Scope:** Similar to ICRA; slightly more focus on systems integration and intelligent behavior

**Format:**
- 8 pages + references
- IEEE double-column
- Double-blind

**Review process:**
- 3 reviewers
- ACs
- Rebuttal: yes

**Publication bar:**
- Slightly more systems-oriented than ICRA
- Good engineering integration papers often fare well here
- Strong on field robotics, autonomous vehicles, biorobotics

**Reviewer pet peeves:**
1. Pure learning paper without robotics integration
2. Missing ablation study
3. No failure analysis

**Submission timeline (approximate):**
- Deadline: March
- Notification: June
- Conference: October

---

## CoRL — Conference on Robot Learning

**Status:** Tier 1, selective
**Acceptance rate:** ~26% (2023)
**Scope:** Learning-based methods for robotics. Strong emphasis on real-robot validation,
learning contribution (not just engineering), and generalization.

**Format:**
- 8 pages + unlimited references
- Proceedings template (custom, not IEEE)
- Double-blind

**Review process:**
- 3–4 reviewers
- Senior Program Committee
- Rebuttal: yes

**Publication bar (higher than ICRA/IROS):**
- Real robot results essentially required for manipulation/locomotion papers
- Learning contribution must be clear — not just "we applied X to robot Y"
- Generalization across tasks/objects/environments strongly preferred
- Strong baselines required: must compare to Diffusion Policy, ACT, or equivalent if relevant

**Reviewer dispositions typical:**
- LEARNING: values methodological advance
- SKEPTICAL: assumes results are cherry-picked until proven otherwise
- REPRODUCIBILITY: values code release and complete specs

**Reviewer pet peeves:**
1. Sim-only results for a claim about real-world applicability
2. Missing Diffusion Policy or other state-of-the-art imitation learning baseline
3. Only 1 task / 1 object type
4. No ablation
5. Training details insufficient for reproduction

**Submission timeline (approximate):**
- Deadline: June
- Notification: August/September
- Conference: November

---

## RSS — Robotics: Science and Systems

**Status:** Tier 1, most selective conference
**Acceptance rate:** ~20–25%
**Scope:** Fundamental advances in robotics science. High bar for novelty and scientific insight.
Not a venue for solid-but-incremental engineering contributions.

**Format:**
- 8 pages + references
- Double-blind

**Review process:**
- 3 reviewers
- ACs
- Rebuttal: yes

**Publication bar (highest of conferences):**
- Must make a fundamental contribution to robotics science
- "We applied X to robot Y" is insufficient
- Theory + experiments, or extraordinary experimental results, expected
- New capability that was not previously achievable, or deep understanding of why something works

**Reviewer dispositions:**
- THEORY: values principled design and formal understanding
- SKEPTICAL: very high prior against novelty
- LEARNING: when relevant

**Reviewer pet peeves:**
1. Incremental contribution, no matter how well executed
2. Only tested on tabletop tasks
3. Comparison to weak baselines
4. Missing discussion of why the method works (mechanistic understanding)

**Submission timeline (approximate):**
- Deadline: January/February
- Notification: April
- Conference: July

---

## RA-L — IEEE Robotics and Automation Letters

**Status:** Tier 1 journal with conference presentation option
**Scope:** Complete robotics research contributions; both applied and fundamental
**Review time:** 3–4 months typical
**Single-blind review**

**Format:**
- 8 pages + references (same as ICRA template)
- Can be presented at ICRA or IROS

**Publication bar:**
- Complete, validated contribution expected
- Real robot results strongly expected
- More complete evaluation than typical conference paper

**Advantages over conferences:**
- No page rush
- Can be presented at ICRA or IROS with the journal

**Reviewer expectations:**
- More thorough evaluation than conference
- Discussion of limitations expected
- Broader set of experiments than minimum conference paper

---

## T-RO — IEEE Transactions on Robotics

**Status:** Flagship journal of IEEE RAS
**Scope:** Comprehensive robotics research; extended work
**Review time:** 4–8 months; major/minor revisions common
**Single-blind review**

**Format:**
- No page limit
- Extended contributions (typically 12–20 pages)

**Publication bar:**
- Extended, comprehensive contribution
- Often journal version of conference paper with significantly more experiments
- Strong theoretical contribution or comprehensive experimental evaluation required

**Review structure:**
- Associate Editor + 3 reviewers
- Multiple revision rounds common
- High reproducibility expectations

---

## Humanoids — IEEE-RAS International Conference on Humanoid Robots

**Status:** Specialized tier 1 venue
**Scope:** Humanoid robotics: locomotion, manipulation, learning, teleoperation, hardware
**Acceptance rate:** ~50%
**Format:** 8 pages + references, IEEE, double-blind

**Calibration notes:**
- Hardware-in-the-loop results expected
- Whole-body control papers: MPC comparison expected
- Teleoperation papers: quantify operator effort and task success
- Strong venue for loco-manipulation and bimanual papers

---

## HRI — ACM/IEEE International Conference on Human-Robot Interaction

**Status:** Tier 1 for HRI research
**Scope:** Human factors, user studies, social robots, assistive robotics
**Acceptance rate:** ~28%

**Calibration notes:**
- User study required for most claims about human behavior
- IRB approval mentioned
- Statistical significance testing expected (not just descriptive results)
- Perception metrics (NASA-TLX, trust scales) commonly expected

---

## Quick comparison table

| Venue | Bar | Real robot? | Blind? | Pages | Deadline |
|-------|-----|------------|--------|-------|----------|
| ICRA | Moderate | Preferred | Double | 8+refs | Sep/Oct |
| IROS | Moderate | Preferred | Double | 8+refs | March |
| CoRL | High | Required* | Double | 8+refs | June |
| RSS | Very high | Required* | Double | 8+refs | Jan/Feb |
| RA-L | Moderate-high | Required | Single | 8+refs | Rolling |
| T-RO | High | Required | Single | Unlimited | Rolling |
| Humanoids | Moderate | Required | Double | 8+refs | July |

*Required for manipulation/locomotion claims; sim acceptable with strong justification
