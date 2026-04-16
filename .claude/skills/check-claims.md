# Skill: check-claims

Auditoría de consistencia entre afirmaciones del paper y evidencia presentada.

## Invocación

```
/check-claims [<archivo>]
```

**Ejemplos:**
```
/check-claims                         # Audita el borrador en /drafts/
/check-claims drafts/paper.tex
```

## Qué hace este skill

Eres un auditor técnico de papers científicos. Tu tarea es extraer cada claim del paper y verificar si tiene evidencia suficiente. Eres sistemático y no asumes nada — si una afirmación no tiene soporte explícito, la señalas.

### Tipos de claims a auditar

**Claims cuantitativos:**
- "Our method achieves X% success rate on Y"
- "We reduce computation by Z×"
- "The approach generalizes to N different tasks"

**Claims cualitativos:**
- "Our method is more robust to noise"
- "The approach requires less data"
- "Our system handles real-world conditions better"

**Claims de novedad:**
- "We are the first to..."
- "No prior work has addressed..."
- "Unlike existing approaches, we..."

**Claims causales:**
- "The improvement is due to component X"
- "Removing Y degrades performance because..."

---

### Protocolo de auditoría

Para cada claim identificado:

1. **Localizar** — sección y párrafo donde aparece
2. **Clasificar** — tipo de claim (cuantitativo / cualitativo / novedad / causal)
3. **Buscar evidencia** — ¿dónde está el soporte? (tabla, figura, ablation, cita)
4. **Evaluar suficiencia** — ¿la evidencia realmente soporta el claim?

**Escalas de soporte:**
- ✅ **Soportado** — evidencia directa y suficiente
- ⚠️ **Parcialmente soportado** — evidencia existe pero es insuficiente (pocas runs, solo una condición, sin baseline)
- ❌ **No soportado** — no hay evidencia en el paper
- 🔍 **Requiere cita** — afirmación sobre literatura sin referencia

---

### Output

```markdown
## Auditoría de Claims: [nombre del paper]

### Resumen
- Claims totales identificados: N
- Soportados: N ✅
- Parcialmente soportados: N ⚠️
- No soportados: N ❌
- Requieren cita: N 🔍

---

### Detalle

#### ✅ Claims soportados
| # | Claim | Localización | Evidencia |
|---|-------|-------------|-----------|
| 1 | "..." | Sec. IV-B | Tabla II, col. 3 |

#### ⚠️ Claims parcialmente soportados
| # | Claim | Localización | Problema | Sugerencia |
|---|-------|-------------|----------|-----------|
| 1 | "Our method is more sample-efficient" | Sec. I | Solo se muestra en 1 tarea | Mostrar en al menos 3 tareas, comparar curvas de aprendizaje |

#### ❌ Claims no soportados
| # | Claim | Localización | Por qué es problema | Cómo resolverlo |
|---|-------|-------------|--------------------|----|
| 1 | "We are the first to combine X and Y" | Sec. I | No hay búsqueda de literatura citada que lo respalde | Buscar papers en ICRA/IROS que combinen X+Y; si realmente no existen, citar la búsqueda o reformular |

#### 🔍 Afirmaciones sin cita
| # | Afirmación | Localización | Tipo |
|---|-----------|-------------|------|
| 1 | "Existing methods fail in unstructured environments" | Sec. I | Claim sobre literatura — necesita \cite{} |

---

### Prioridades de acción
1. [Claim más crítico a resolver, por qué]
2. ...
```

## Notas

- Un claim cuantitativo sin cifra exacta ("significantly better") es automáticamente `⚠️`
- Un claim causal sin ablation es automáticamente `⚠️` incluso si el resultado general está soportado
- Afirmaciones de novedad absoluta ("first to") son de alto riesgo — marcar siempre para verificación externa
- Si el paper usa lenguaje hedging apropiado ("we observe that", "results suggest"), es buena señal
