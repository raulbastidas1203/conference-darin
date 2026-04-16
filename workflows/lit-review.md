# Workflow: Literature Review Sistemático

Proceso para construir una revisión de literatura rigurosa en robótica, con trazabilidad de fuentes y organización que alimente directamente el paper.

---

## Cuándo usar este workflow

- Al empezar un nuevo paper o proyecto de investigación
- Cuando necesitas mapear un área nueva antes de proponer un método
- Cuando un revisor señala que el related work es incompleto
- Cuando quieres saber si ya existe un trabajo que hace lo mismo que propones

---

## Fase 1: Definir el scope

**Antes de buscar, define:**

```
Tema central: <qué problema o capacidad>
Período temporal: <desde qué año> (default: últimos 5 años + papers fundacionales)
Venues de interés: ICRA, IROS, CoRL, RSS, RA-L, T-RO, [otros]
Profundidad: survey (>50 papers) vs. targeted (10-20 papers clave)
Output esperado: sección de related work / estado del arte / tabla comparativa
```

---

## Fase 2: Búsqueda primaria

### 2.1 Términos de búsqueda

Genera al menos 3-5 variantes de los términos:
- Término principal: "dexterous manipulation"
- Variantes: "in-hand manipulation", "multi-finger control", "finger gaiting"
- Términos relacionados: "dexterous hand", "articulated hand", "contact-rich manipulation"

### 2.2 Ejecutar búsquedas

```
/search-lit "<término 1>"
/search-lit "<término 2>"
/search-lit "<término 3>"
```

### 2.3 Fuentes manuales adicionales

Para venues de alta relevancia, buscar directamente los proceedings recientes:
- ICRA 2024/2023/2022: `site:ieeexplore.ieee.org ICRA 2024 <tema>`
- CoRL 2024/2023: `site:openreview.net CoRL <tema>`
- arXiv cs.RO últimos 12 meses: `arxiv.org/list/cs.RO/<año>`

---

## Fase 3: Screening y clasificación

Para cada paper encontrado, clasificar en 3 pasos rápidos:

### 3.1 Screening por título (30 seg por paper)
- ¿El título indica que aborda el mismo problema? → Leer abstract
- ¿El título indica que es claramente fuera del scope? → Descartar

### 3.2 Screening por abstract (2 min por paper)
- ¿Aborda el problema central? → Leer intro + experimentos
- ¿Es background relevante pero no central? → Guardar metadata solamente
- ¿No es relevante? → Descartar

### 3.3 Lectura de papers centrales (15-30 min por paper)
- Leer: abstract, intro, método (overview), experimentos, conclusión
- Registrar en lit-notes (ver Fase 4)

---

## Fase 4: Registro en lit-notes

Para cada paper central, crear una nota en `/lit-notes/` con este formato:

**Archivo:** `/lit-notes/<venue>-<year>-<apellido-primer-autor>.md`

```markdown
# [Título del paper]

**Referencia:** [Apellido, N.], "[Título]", [Venue], [Año]. DOI/arXiv: [ID]
**Fecha de lectura:** [fecha]
**Relevancia:** Central / Relacionado

## Qué hace
[1-2 párrafos: método principal, qué problema resuelve]

## Resultados clave
- Métrica principal: [X% en benchmark Y]
- Comparado contra: [baselines]
- Hardware/simulador: [plataforma]

## Limitaciones
[Lo que el paper reconoce que no hace bien o no cubre]

## Diferencia con mi trabajo
[Específico: en qué difiere del paper que estoy escribiendo]

## Citas importantes de este paper
[3-5 papers que cita y que podrían ser relevantes — para snowballing]

## BibTeX
[Entrada BibTeX lista para usar]
```

---

## Fase 5: Snowballing

Para cada paper central:
1. Revisar su sección de Related Work → identificar papers citados relevantes
2. Buscar en Google Scholar "Cited by" → identificar papers posteriores que lo citan
3. Agregar papers no vistos a la lista de screening

Hacer 1-2 rondas de snowballing (más rondas dan retornos decrecientes).

---

## Fase 6: Síntesis

Una vez que tienes los lit-notes completos para los papers centrales:

```
/related-work
```

El skill leerá las notas y generará el draft de related work con tabla comparativa.

---

## Fase 7: Mantenimiento

Una vez enviado el paper, mantener la literatura actualizada:
- Antes de revisiones: ejecutar `/search-lit` nuevamente
- Buscar papers aparecidos después de la submission
- Verificar si algún paper concurrent se publicó mientras el tuyo estaba en revisión

---

## Estructura de carpetas recomendada

```
/lit-notes/
  icra-2023-chi.md
  corl-2023-ze.md
  arxiv-2024-hejna.md
  ...

/papers/                    ← PDFs provistos por el usuario
  chi2023-dexterous.pdf
  ze2023generalizable.pdf
  ...

/references/
  references.bib            ← BibTeX master file
```

---

## Señales de que la revisión de literatura está completa

- [ ] Papers con >100 citas en el tema central están incluidos
- [ ] Últimos 2 años del venue objetivo están cubiertos
- [ ] Los 3-5 trabajos más cercanos están en lit-notes con análisis de diferencia
- [ ] No hay subsección del related work con un solo paper
- [ ] Puedes responder: "¿Por qué nadie ha resuelto esto antes?" con evidencia

---

## Señales de que falta trabajo

- Solo tienes papers de arXiv y ninguno de ICRA/IROS/RA-L/T-RO
- No encontraste ningún paper que use el mismo benchmark que propones usar
- El related work tiene <5 citas de los últimos 2 años
- No puedes nombrar los 3 métodos más competitivos en el área
