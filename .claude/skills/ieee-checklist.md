# Skill: ieee-checklist

Verificación pre-submission de paper IEEE para conferencias de robótica.

## Invocación

```
/ieee-checklist [<archivo>] [--venue icra|iros|corl|rss|ral] [--mode full|outline|format|content]
```

**Ejemplos:**
```
/ieee-checklist                          # Checklist completo sobre /drafts/
/ieee-checklist --venue icra             # Con requisitos específicos de ICRA
/ieee-checklist --mode format            # Solo verificación de formato
/ieee-checklist --mode outline           # Verifica estructura antes de empezar a escribir
```

## Qué hace este skill

Ejecutas una verificación sistemática del paper contra los estándares IEEE y los requisitos del venue objetivo. Eres exhaustivo y específico — no chequeos genéricos.

---

### Checklist Modo: OUTLINE (antes de escribir)

Verifica que el outline tiene:

- [ ] Contribuciones listadas explícitamente (mínimo 2-3 bullets concretos)
- [ ] Gap en literatura identificado con al menos 2 citas de referencia
- [ ] Venue objetivo definido (impacta longitud, formato, nivel de detalle de experimentos)
- [ ] Baselines identificados (papers con cita, no solo nombres)
- [ ] Métricas principales definidas y justificadas
- [ ] Hardware/entorno experimental especificado
- [ ] Secciones principales mapeadas con estimación de páginas

---

### Checklist Modo: CONTENT (durante redacción)

#### Abstract
- [ ] Longitud: 150-250 palabras
- [ ] Contiene: motivación (1-2 oraciones) + método principal (1-2 oraciones) + resultado cuantitativo clave (1 oración) + implicación/contribution (1 oración)
- [ ] No usa "novel", "state-of-the-art", "outperforms" sin cifras
- [ ] Se puede leer de forma totalmente independiente del paper

#### Introduction
- [ ] Establece el problema con motivación clara en el primer párrafo
- [ ] Cita evidencia del gap (papers que no resuelven el problema)
- [ ] Lista contribuciones numeradas y específicas
- [ ] Termina con outline ("The rest of the paper is organized as follows...")
- [ ] Cada contribución es verificable en el paper

#### Related Work
- [ ] Organizado por dimensión técnica, no cronológico
- [ ] Cada subsección termina posicionando el trabajo propio
- [ ] Los papers más relevantes tienen análisis crítico (no solo listing)
- [ ] No hay "we are the first" sin soporte de búsqueda
- [ ] Cita papers de los últimos 2 años en el mismo venue objetivo

#### Methodology
- [ ] Notación matemática definida antes de usarse
- [ ] Ecuaciones numeradas
- [ ] Las elecciones de diseño están justificadas (no solo descritas)
- [ ] Pseudocódigo o diagrama para métodos complejos
- [ ] Se puede reproducir el método con la descripción dada

#### Experiments
- [ ] Setup completo: hardware o simulador + versión, tareas, condiciones
- [ ] Cada baseline tiene cita directa
- [ ] Métricas definidas con unidades y justificación
- [ ] Media ± std (o equivalente) en todos los resultados cuantitativos
- [ ] Número de runs/trials especificado
- [ ] Ablation study de componentes principales del método
- [ ] Análisis de fallos o limitaciones observadas

#### Results
- [ ] Tablas con caption autocontenido (el lector entiende sin leer el texto)
- [ ] Figuras con caption autocontenido
- [ ] Los números en el texto coinciden con los de tablas/figuras
- [ ] Análisis cualitativo complementa los números (no solo "Table I shows X is better")
- [ ] Diferencias estadísticamente significativas o con suficientes runs

#### Conclusion
- [ ] Reitera contribuciones (no repite el abstract)
- [ ] Menciona limitaciones honestas
- [ ] Propone trabajo futuro concreto (no genérico)

---

### Checklist Modo: FORMAT (pre-submission final)

#### Formato IEEE Conference
- [ ] Doble columna
- [ ] Fuente: Times New Roman 10pt (body), sin cambiar
- [ ] Márgenes según template oficial IEEE
- [ ] Longitud dentro del límite del venue:
  - ICRA/IROS: 6-8 páginas + referencias (verificar CFP actual)
  - CoRL: 8 páginas + referencias
  - RSS: 8 páginas + referencias
  - RA-L: 8 páginas + referencias

#### Referencias
- [ ] Formato IEEE: [1] Apellido, N., "Título", Venue, año, pp. X-Y.
- [ ] Sin URLs crudas — usar DOI cuando disponible
- [ ] Sin referencias a "Personal Communication"
- [ ] Todas las referencias son citadas en el texto
- [ ] Todas las citas en el texto tienen referencia en la lista
- [ ] Referencias ordenadas por orden de aparición (no alfabético)

#### Figuras y Tablas
- [ ] Todas las figuras referenciadas en el texto con "Fig. X"
- [ ] Todas las tablas referenciadas con "Table X" (mayúscula)
- [ ] Figuras en resolución mínima 300 DPI (para imprenta)
- [ ] Figuras legibles en escala de grises (muchos revisores imprimen en B&W)
- [ ] Caption de figuras al pie, caption de tablas al inicio

#### Texto
- [ ] Acrónimos definidos en primera aparición
- [ ] Consistencia en términos técnicos (no alternar "robot" y "agent" si son lo mismo)
- [ ] Sin secciones vacías o con "TODO"
- [ ] Sin texto en color (excepto figuras)
- [ ] Sin track changes o comentarios de Word/LaTeX visibles

#### Compliance
- [ ] Anonymizado correctamente si el venue es double-blind
- [ ] Sin self-citations que rompan el anonimato
- [ ] Video suplementario/demo link preparado (si requerido por venue)
- [ ] Código/datos en repositorio con URL (si se incluye en el paper)

---

### Output

```markdown
## Checklist IEEE — [venue] [modo]

### PASA ✅
- [item: lo que está bien]

### FALLA ❌
| Item | Sección | Acción requerida |
|------|---------|-----------------|
| Abstract sin resultado cuantitativo | Abstract | Agregar "achieving X% on Y benchmark" |
| Tabla I sin caption autocontenido | Sec. IV | Expandir caption para incluir setup |

### VERIFICAR ⚠️
- [item que requiere revisión manual del usuario]

### Resumen
Paper listo para submission: [Sí / No — N items bloqueantes]
```
