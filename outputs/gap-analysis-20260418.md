# /analyze-gaps: humanoid autonomy in warehouse environments
**Date:** 2026-04-18
**Mode:** full
**Source:** references/tracker.md — 10 Central · 17 Related · 10 Marginal
**Target venue:** ICRA (default)
**Agent:** Gap-Analyst

---

## Landscape map

| Subproblem | Papers (C/R/M) | Years | Dominant method | Benchmark | Activity |
|------------|---------------|-------|-----------------|-----------|----------|
| A. Unified whole-body control (nav + manip) | 3/4/0 | 2024–2025 | RL + policy distillation / VLA | HumanoidBench (parcial) | ACTIVE |
| B. Physical loco-manip (payload, fuerza, constraints) | 4/4/0 | 2021–2026 | RL + MPC + jerarquía | Custom por paper | ACTIVE |
| C. Industrial/logistics deployment | 3/2/0 | 2018–2025 | BT + vision + CBF | Ninguno estándar | SPARSE |
| D. Foundation models / zero-shot autonomy | 2/2/0 | 2025 | VLA + RL teacher distillation | Custom diverse scenes | SPARSE |
| E. Long-horizon task sequencing | 1/2/0 | 2025 | RL + chaining | Ninguno estándar | SPARSE |

Ningún cluster es SATURATED. El campo está ACTIVE en control físico y unificación de modos, pero SPARSE en deployment real en warehouse.

---

## Saturation diagnosis

No hay clusters SATURATED. `ferrazza2024humanoidbench` (RSS 2024) es el benchmark más consolidado para WBC, pero cubre household/locomotion, no warehouse. Ningún área está entry-closed.

---

## Identified gaps

### Gap 1: Ausencia de benchmark estándar para warehouse humanoid
**Tipo:** Evaluation gap
**Acotado por:** `peron2025pixels`, `ieee2024safewarehouse`, `dao2024boxloco`, `humanoidcat2026`
**Barrera técnica:** No hay acuerdo en qué tareas constituyen "warehouse"; cada paper define su propio setup
**Evaluable:** No — requiere construcción de nuevo benchmark

### Gap 2: Long-horizon task chaining en warehouse
**Tipo:** Methods gap
**Acotado por:** `lhm2025humanoid`, `zhang2025multistage`, `peron2025pixels`
**Barrera técnica:** Errores compuestos entre etapas; recuperación de fallos; ningún paper humanoid aborda más de 2 etapas coordinadas
**Evaluable:** Parcialmente — adaptable del setup de `lhm2025humanoid`

### Gap 3: Manipulación force-adaptive en presencia de humanos dinámicos
**Tipo:** Methods gap
**Acotado por:** `zhang2025falcon` (force-adaptive, sin humanos), `ieee2024safewarehouse` (safety, sin manipulación), `rollo2023semantic` (HRC, sin force adaptation)
**Barrera técnica:** CBF + force-adaptive RL opera en timescales distintos y capas incompatibles
**Evaluable:** Sí — success rate + violaciones de seguridad

### Gap 4: Caracterización sistemática del sim-to-real gap en warehouse
**Tipo:** Transfer gap
**Acotado por:** `dao2024boxloco`, `rigo2024heavyloco`, `humanoidcat2026`
**Barrera técnica:** Warehouse tiene superficies, pesos y obstáculos heterogéneos sin caracterización
**Evaluable:** Sí — comparación sim vs. real con protocol de `dao2024boxloco`

---

## Candidate directions

### Direction 1: Force-adaptive loco-manipulation segura en warehouse con humanos
**Core claim:** Un controlador jerárquico que integra CBF-based safety con force-adaptive WBC permite a un humanoid ejecutar pick-and-place en espacios compartidos con humanos dinámicos sin violaciones de seguridad y con >75% success rate — donde `zhang2025falcon` sin CBF produce 40% de violaciones en el mismo setup.
**Gap addressed:** Methods gap (Gap 3)
**Builds on:** `zhang2025falcon`, `ieee2024safewarehouse`, `humanoidcat2026`
**Competes with:** `zhang2025falcon`, `ieee2024safewarehouse`
**Novelty type:** New method — integración de dos capas de control previamente separadas
**Target venue:** ICRA 2026 / RA-L
**Minimum viable experiment:** Workspace 2 personas + humanoid, pick-and-place con humano en movimiento, N≥30 trials, violaciones de seguridad + success rate vs. baseline sin CBF
**Required baselines:** `zhang2025falcon`, `ieee2024safewarehouse`
**Risk level:** MEDIUM
**Risk factors:** CBF+RL en tiempo real arquitectónicamente no trivial; IRB para experimentos con humanos; hardware específico
**Reviewer attack surface:** "¿Por qué CBF y no un simple safety threshold de distancia?"
**Desk-reject triggers:** Sim-only sin humanos reales; sin ground truth de violaciones; solo comparación con método propio
**Plausibility: 4/5**

### Direction 2: Long-horizon warehouse workflow execution en humanoid
**Core claim:** Sistema jerárquico que ejecuta workflows de 5 etapas (navigate → locate → pick → transport → place) con >65% success rate end-to-end, donde política plana logra <20%.
**Gap addressed:** Methods gap (Gap 2)
**Builds on:** `lhm2025humanoid`, `he2025hover`, `dao2024boxloco`
**Competes with:** `lhm2025humanoid`, `zhang2025multistage`
**Novelty type:** New problem formulation + método jerárquico con recuperación de fallos
**Target venue:** ICRA 2026 / CoRL 2026
**Minimum viable experiment:** Workflow 5 etapas en simulación, N≥20 trials, vs. política plana y oracle por etapas
**Required baselines:** `he2025hover`, `lhm2025humanoid`, `zhang2025multistage`
**Risk level:** MEDIUM
**Risk factors:** 65% end-to-end puede ser irrealizable; novedad débil si es solo composición de skills
**Reviewer attack surface:** "¿Cuál es la contribución vs. TAMP clásico (`ciebielski2025tamp`)?"
**Desk-reject triggers:** Workflow <3 etapas; sin comparación con política plana; sin robot real o sim convincente
**Plausibility: 3/5**

### Direction 3: Caracterización del sim-to-real gap en warehouse loco-manipulation
**Core claim:** Caracterizamos el sim-to-real gap en 4 variantes de tarea warehouse, identificando fricción de suelo y varianza de peso como factores dominantes (>60% del gap), y mostramos que DR calibrado reduce el gap de 48% a 15%.
**Gap addressed:** Transfer gap (Gap 4)
**Builds on:** `dao2024boxloco`, `rigo2024heavyloco`, `humanoidcat2026`
**Competes with:** `dao2024boxloco`
**Novelty type:** New analysis + calibración dirigida de domain randomization
**Target venue:** ICRA 2026 / RA-L
**Minimum viable experiment:** 4 variantes × 3 protocolos DR × N≥20 trials sim+real; descomposición de gap
**Required baselines:** `dao2024boxloco`, `rigo2024heavyloco`
**Risk level:** MEDIUM
**Risk factors:** Experimentos reales costosos; paper descriptivo difícil sin método nuevo; gap puede resultar pequeño
**Reviewer attack surface:** "Caracterizan el gap pero no lo cierran"
**Desk-reject triggers:** Solo simulación; una sola tarea; sin conclusión accionable
**Plausibility: 3/5**

### Direction 4: Zero-shot warehouse generalization via multimodal reasoning
**Core claim:** Agente humanoid con chain-of-action reasoning ejecuta 8 categorías warehouse sin re-entrenamiento (>60% SR promedio vs. <25% de políticas especializadas).
**Gap addressed:** Methods gap (zero-shot generalization)
**Builds on:** `humanoidcoa2025`, `lhm2025humanoid`, `he2025hover`
**Competes with:** `humanoidcoa2025`
**Novelty type:** Extensión de scope a warehouse
**Target venue:** CoRL 2026
**Minimum viable experiment:** 8 categorías, N≥10 trials, robot real Unitree G1
**Required baselines:** `humanoidcoa2025`, `he2025hover`, `lhm2025humanoid`
**Risk level:** HIGH
**Risk factors:** Zero-shot en warehouse real muy ambicioso; foundation models fallan en manipulation de precisión; demasiado similar a `humanoidcoa2025`
**Reviewer attack surface:** "¿Qué aporta vs. `humanoidcoa2025`? Parece extensión de aplicación"
**Desk-reject triggers:** Sim-only; <5 categorías; sin comparación con `humanoidcoa2025`
**Plausibility: 2/5**

---

## Comparative ranking

| Rank | Direction | Plausibility | Main risk | Venue |
|------|-----------|-------------|-----------|-------|
| 1 | Force-adaptive + CBF para human-co-present warehouse | 4/5 | IRB + arquitectura CBF+RL | ICRA 2026 / RA-L |
| 2 | Long-horizon workflow execution | 3/5 | Novedad técnica débil si es composición | ICRA 2026 |
| 3 | Sim-to-real gap characterization | 3/5 | Paper descriptivo sin método nuevo | ICRA 2026 / RA-L |
| 4 | Zero-shot warehouse generalization | 2/5 | Demasiado similar a `humanoidcoa2025` | CoRL 2026 |

---

## Recommended direction

**Direction 1: Force-adaptive loco-manipulation segura en warehouse con humanos**

**Razón sobre alternativas:** Gap acotado por dos papers de ICRA verificables (`zhang2025falcon`, `ieee2024safewarehouse`). Integración CBF+RL es técnicamente no trivial. Métricas estándar, sin benchmark nuevo requerido.

**First concrete step:** Reproducir cart-pulling de `zhang2025falcon` en simulación (Unitree G1, IsaacGym/MuJoCo), añadir agente humano estático en el path, medir violaciones de colisión sin safety layer. Establece magnitud del gap que el paper debe cerrar. Tiempo: 1–2 semanas.

**Early invalidation test:** Si un threshold de distancia simple (stop when human <0.8m) produce 0 violaciones con <5% degradación en manipulation success rate → el gap no justifica contribución CBF. Pivotear a Direction 2.

---

## Coverage gaps en este análisis

- **Failure recovery:** Ningún paper en tracker aborda recuperación activa de fallos. Puede ser gap importante.
  → `/search-lit "failure recovery loco-manipulation humanoid"`
- **Bimanual warehouse:** Tareas con dos brazos casi ausentes. `jiang2025behavior` es lo más cercano pero es household.
  → `/search-lit "bimanual humanoid manipulation industrial"`

---

## Suggested next steps

- [ ] Si procede con Direction 1: `/map-benchmarks --venue icra` para confirmar setup de evaluación
- [ ] Cubrir failure recovery: `/search-lit "failure recovery loco-manipulation humanoid"`
- [ ] Cubrir bimanual: `/search-lit "bimanual humanoid manipulation industrial"`
- [ ] Una vez confirmado direction: `/plan-experiments` para Direction 1
- [ ] Leer `ieee2024safewarehouse.pdf` y `zhang2025falcon` (arXiv) antes de planificar arquitectura
