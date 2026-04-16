# Revision Response Letter — Template

Template para respuesta a revisores de IEEE/ICRA/IROS/CoRL/RA-L.

Usa `/revision-letter` para generar el contenido; este template define la estructura y el tono.

---

```
Dear Editor / Program Chairs,

We sincerely thank the reviewers for their careful reading of our manuscript 
"[PAPER TITLE]" and for their insightful comments. We have carefully addressed 
all concerns as detailed below.

A summary of the main changes is provided at the end of this letter.
All modifications are highlighted in [blue/track-changes] in the revised manuscript.

Sincerely,
The Authors

────────────────────────────────────────────────────────────────────────────────

RESPONSE TO REVIEWER 1

────────────────────────────────────────────────────────────────────────────────

Comment R1.1:
> [Copiar aquí el comentario exacto del revisor, con sangría]

Response:
[Respuesta directa. Ser específico: ¿se hizo el cambio? ¿por qué o por qué no?]

Change: [Sec. X, página Y]: Added/Modified "..." to "..."

────────────────────────────────────────────────────────────────────────────────

Comment R1.2:
> [Comentario]

Response:
[Respuesta]

Change: [ubicación]

────────────────────────────────────────────────────────────────────────────────

RESPONSE TO REVIEWER 2

────────────────────────────────────────────────────────────────────────────────

Comment R2.1:
> [Comentario]

Response:
[Respuesta]

Change: [ubicación]

────────────────────────────────────────────────────────────────────────────────

RESPONSE TO REVIEWER 3 (si aplica)

────────────────────────────────────────────────────────────────────────────────

...

────────────────────────────────────────────────────────────────────────────────

SUMMARY OF CHANGES

────────────────────────────────────────────────────────────────────────────────

| # | Change | Location | Motivated by |
|---|--------|----------|-------------|
| 1 | Added ablation on component X | Table III, Sec. IV-C | R1.2, R2.1 |
| 2 | Revised claim about generalization | Sec. I, para. 2 | R1.3 |
| 3 | Added comparison with [Ref] | Table I, Sec. IV-B | R2.2 |
| 4 | Clarified hardware setup | Sec. IV-A | R3.1 |
| 5 | Added [Ref] to related work | Sec. II, para. 3 | R2.3 |
| 6 | Fixed notation inconsistency | Sec. III | R1.4 |

────────────────────────────────────────────────────────────────────────────────
```

---

## Frases de uso frecuente

### Agradecimiento inicial (variar, no copiar siempre igual)
- "We thank the reviewer for this observation, which helped us strengthen the paper."
- "This is a valid concern that we had not addressed clearly."
- "We agree with the reviewer's assessment."

### Cuando se hizo el cambio
- "We have addressed this by [descripción]. The revised Section X now reads: '...'"
- "Following this suggestion, we conducted [experimento]. Results are shown in Table X."
- "We have revised this paragraph to clarify [aspecto]."

### Cuando se está parcialmente de acuerdo
- "We partially agree with this concern. [Parte correcta + corrección]. However, [parte donde el paper es válido + evidencia]."

### Cuando se está en desacuerdo (requiere evidencia)
- "We respectfully disagree with this characterization. As shown in [evidencia], our method [argumento técnico]. To address the potential confusion, we have added a clarifying sentence in Section X."
- "We believe this concern stems from an ambiguity in our original presentation, which we have now corrected. [Aclaración técnica]."

### Cuando el experimento no es factible
- "We appreciate this suggestion. Unfortunately, [razón concreta: hardware no disponible / fuera del scope del paper / requeriría N meses adicionales]. To address the underlying concern, we [alternativa: ablation en sim / aclaramos el scope en Sec. I / agregamos discusión en Sec. VI]."

### Cuando el revisor sugiere una cita
- "We thank the reviewer for pointing us to [Ref]. We have added this citation in Section II and briefly discuss how our approach differs: [1-2 oraciones de comparación]."

---

## Errores comunes a evitar

| Error | Por qué es problema | Alternativa |
|-------|--------------------|-----------| 
| "We will add X in a future version" | Los revisores esperan cambios en esta revisión | Hacer el cambio o explicar por qué no es posible ahora |
| Respuesta genérica sin citar el change | El revisor no puede verificar que se hizo | Siempre indicar sección + párrafo + texto modificado |
| Capitular en puntos correctos | Debilita el paper innecesariamente | Argumentar con evidencia si el paper tiene razón |
| Ignorar un subpunto del revisor | El revisor nota los puntos sin respuesta | Responder cada punto, incluso los editoriales |
| Prometer resultados que no se pueden obtener | Credibilidad en riesgo | Prometer solo lo que se puede entregar |
