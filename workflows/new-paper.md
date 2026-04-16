# Workflow: Nuevo Paper desde Cero

Proceso completo para empezar un paper IEEE de robótica desde la idea inicial hasta tener un borrador estructurado listo para escribir.

---

## Fase 1: Definición (antes de buscar literatura)

**Objetivo:** Tener claro QUÉ se va a demostrar antes de empezar a escribir.

### 1.1 Responder estas preguntas

```
¿Cuál es el problema que resuelves?
¿Por qué los métodos actuales no lo resuelven bien?
¿Cuál es tu insight clave? (la idea no obvia)
¿Cómo sabes que funciona? (experimento que lo demuestra)
¿A quién le importa? (aplicación o gap científico)
¿En qué venue encaja mejor?
```

Si no puedes responder todas, el paper no está listo para empezar. Trabajar primero en clarificar la contribución.

### 1.2 Formular la contribución como claim falsable

Bueno: "Un método de imitation learning con solo 10 demos logra >80% success rate en tareas de manipulation contact-rich en un robot real Franka, superando BC y GAIL con 50+ demos."

Malo: "Proponemos un novel approach para robot learning que es más eficiente y generalizable."

---

## Fase 2: Búsqueda de literatura

### 2.1 Búsqueda inicial

```
/search-lit "<tema principal>" --venue <venue objetivo>
```

Objetivo: Mapear el espacio. No leer todo — identificar qué papers son centrales.

### 2.2 Clasificar papers

Para cada paper de los resultados:
- **¿Es mi baseline directo?** → paper central, necesito full text
- **¿Define el benchmark que uso?** → paper central
- **¿Aborda el mismo problema con distinto approach?** → paper central
- **¿Es background general del área?** → relacionado, abstract suficiente
- **¿Comparte keywords pero no el problema?** → marginal, listar sin leer

### 2.3 Leer papers centrales

Para cada paper central:
- Leer abstract + intro + experimentos
- Registrar en `/lit-notes/`: método, métricas, limitaciones, diferencia con mi trabajo
- Identificar los papers QUE ELLOS CITAN como relevantes (snowballing)

### 2.4 Ejecutar segunda ronda si hay gaps

Si la búsqueda inicial reveló subtemas no cubiertos:
```
/search-lit "<subtema específico>"
```

---

## Fase 3: Related Work y Posicionamiento

Una vez que tienes los papers centrales identificados:

```
/related-work
```

Objetivo: Entender exactamente cómo tu trabajo se diferencia de cada grupo de métodos relacionados.

**Output esperado:** Draft de sección de Related Work + identificación clara del gap.

Si el skill revela que alguien ya hizo exactamente lo que propones → revisar la contribución antes de continuar.

---

## Fase 4: Outline del paper

Usa `/templates/paper-outline.md` para crear el outline.

**Reglas:**
- El outline debe estar completo antes de empezar a escribir prosa
- Cada sección debe tener bullets que muestren QUÉ va a decir, no solo el título
- Las contribuciones listadas en la intro deben tener experimento correspondiente
- Los baselines deben estar identificados con citas

Ejecutar al terminar el outline:
```
/ieee-checklist --mode outline
```

---

## Fase 5: Redacción (orden recomendado)

### Orden efectivo (no empezar por la intro)

1. **Metodología** — es lo que mejor conoces; establece la notación
2. **Experimentos (setup)** — define qué vas a medir y contra qué
3. **Resultados** — rellena tablas con resultados reales
4. **Related Work** — con el método claro, es más fácil posicionarlo
5. **Introduction** — escríbela cuando ya sabes qué demostraste
6. **Abstract** — última, sintetiza todo
7. **Conclusion** — con el paper completo, lista contribuciones reales

### Durante la redacción

Por cada sección que escribes:
```
/check-claims <sección>
```
Para verificar que cada afirmación tiene soporte.

---

## Fase 6: Revisión pre-submission

```bash
# 1. Revisión completa del draft
/review-draft

# 2. Auditoría de claims
/check-claims

# 3. Checklist de formato y contenido
/ieee-checklist --venue <venue>
```

Iterar hasta que no haya bloqueantes críticos.

---

## Fase 7: Submission

- [ ] PDF generado desde template LaTeX oficial del venue
- [ ] Verificar page count (dentro del límite)
- [ ] Figuras en resolución >= 300 DPI
- [ ] Anonimización correcta (si double-blind)
- [ ] Supplementary/video listo (si aplica)
- [ ] Co-autores han aprobado la versión final
- [ ] Sistema de submission probado con PDF de prueba antes del deadline

---

## Timeline típico (hacia atrás desde deadline)

| Tiempo antes del deadline | Actividad |
|--------------------------|-----------|
| -8 semanas | Fase 1-2: contribución + literatura |
| -6 semanas | Fase 3-4: related work + outline |
| -4 semanas | Fase 5: primer borrador completo |
| -3 semanas | Revisión interna con co-autores |
| -2 semanas | Iteración y mejoras |
| -1 semana | Revisión final, `/ieee-checklist` |
| -2 días | Congelar texto, solo correcciones de formato |
| -1 día | Submission con tiempo para errores técnicos |
