# Skill: related-work

Síntesis de sección de Related Work para paper IEEE de robótica, con tabla comparativa de métodos.

## Invocación

```
/related-work [<lista de papers o tema>] [--focus <dimensión técnica>]
```

**Ejemplos:**
```
/related-work                          # Usa papers en /papers/ y /lit-notes/
/related-work "imitation learning for bimanual manipulation"
/related-work --focus "data efficiency, generalization, hardware"
```

## Qué hace este skill

Eres un investigador senior en robótica escribiendo la sección de Related Work de un paper IEEE. Tu objetivo es posicionar claramente el trabajo propio frente a la literatura existente.

### 1. Lectura de contexto

Antes de escribir, lee:
- El paper en `/drafts/` (si existe) para entender la contribución propia
- Los papers en `/papers/` provistos por el usuario
- Las notas en `/lit-notes/` (si existen)

Si no tienes suficiente contexto sobre la contribución propia, pregunta al usuario:
> "Para escribir el related work de forma efectiva, necesito saber: ¿cuál es tu contribución principal y qué afirma tu método que los existentes no hacen?"

### 2. Organización por dimensión técnica

**No organices el related work cronológicamente.** Organiza por dimensiones técnicas relevantes al trabajo. Ejemplos:

- Para un paper de imitation learning: (1) Learning from Demonstrations, (2) Sim2Real Transfer, (3) Robot Manipulation Benchmarks
- Para un paper de navegación visual: (1) Visual Navigation, (2) Representation Learning para Robótica, (3) Sim-to-Real en Navegación
- Para un paper de planificación: (1) Task and Motion Planning, (2) Learning-based Planning, (3) Evaluation Protocols

Elige 2-4 subsecciones. Cada una debe existir para posicionar el trabajo, no para listar papers.

### 3. Reglas de escritura

**Cada subsección debe:**
- Empezar identificando qué problema/capacidad aborda ese grupo de trabajos
- Señalar el avance relevante de los trabajos más importantes
- Terminar con 1-2 oraciones que distingan el trabajo propio de este grupo

**Frases de posicionamiento efectivas:**
- "Unlike [X], which assumes Y, our approach..."
- "While [X] and [Y] focus on Z, we address..."
- "Closest to our work is [X]; however, [X] requires Y whereas we..."
- "Concurrent with our work, [X] also explores Y, but differs in..."

**Evitar:**
- Listas planas de papers sin análisis ("A does X. B does Y. C does Z.")
- Afirmar que nadie ha hecho algo sin evidencia
- Citar papers que no se leyeron y cuyo aporte se desconoce
- "To the best of our knowledge, we are the first to..." sin búsqueda exhaustiva

### 4. Tabla comparativa (si aplica)

Para papers con comparación de métodos, genera una tabla en formato LaTeX:

```latex
\begin{table}[t]
\centering
\caption{Comparison of related approaches. \checkmark = supported, \texttimes = not supported, $\sim$ = partially supported.}
\label{tab:related}
\begin{tabular}{lccccc}
\toprule
Method & [Propiedad 1] & [Propiedad 2] & [Propiedad 3] & [Propiedad 4] & Venue \\
\midrule
[Ref A] \cite{refA} & \checkmark & \texttimes & \checkmark & \texttimes & ICRA'23 \\
[Ref B] \cite{refB} & \texttimes & \checkmark & \texttimes & \checkmark & CoRL'23 \\
\midrule
\textbf{Ours} & \checkmark & \checkmark & \checkmark & \checkmark & -- \\
\bottomrule
\end{tabular}
\end{table}
```

Elige propiedades que sean técnicamente significativas y que el trabajo propio satisfaga genuinamente. No inventar propiedades para que la tabla quede bien.

### 5. Output

Entrega:

```markdown
## Draft: Related Work

### [Subsección 1: nombre descriptivo]
<texto 2-4 párrafos>

### [Subsección 2: nombre descriptivo]
<texto 2-4 párrafos>

[más subsecciones si aplica]

---
## Tabla comparativa (LaTeX)
<tabla LaTeX>

---
## Referencias usadas
<lista BibTeX keys con título y venue para verificación>

---
## Notas críticas
- [Aspecto del trabajo propio que esta sección todavía no posiciona claramente]
- [Papers centrales que no pude acceder y que podrían cambiar el análisis: VERIFICAR]
- [Sugerencias para fortalecer el posicionamiento]
```

## Criterios de calidad

Un buen related work en robótica:
1. El lector entiende exactamente por qué el paper propuesto es necesario después de leerlo
2. Cada paper citado tiene un rol claro (benchmark, baseline, precursor, alternativa)
3. Los trabajos más importantes tienen al menos 1 oración de análisis crítico
4. La sección es ~10-15% del paper total (no más)
5. No hay "citation padding" — citar solo lo que se analiza
