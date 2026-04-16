# Workflow: Preparación para Submission

Proceso para las últimas 48-72 horas antes del deadline. Foco en verificación sistemática, no en cambios de contenido.

---

## Regla principal

**Congelar el contenido 48h antes del deadline.** Las últimas 48h son para verificación, no para añadir experimentos o reescribir secciones. Los cambios de último minuto introducen errores nuevos.

---

## Checklist D-3 (3 días antes)

### Contenido
- [ ] `/review-draft` ejecutado y todos los bloqueantes resueltos
- [ ] `/check-claims` ejecutado — sin claims ❌ (no soportados)
- [ ] Todos los `[TODO: cite]` reemplazados por citas reales
- [ ] Ablation study completo
- [ ] Todos los números del texto coinciden con tablas

### Colaboración
- [ ] Co-autores han leído el borrador completo
- [ ] Feedback de co-autores incorporado
- [ ] Orden de autores confirmado
- [ ] Afiliaciones e instituciones correctas

---

## Checklist D-2 (2 días antes)

### Formato

```
/ieee-checklist --venue <venue> --mode format
```

- [ ] Template LaTeX oficial del venue descargado de IEEE Author Center
- [ ] Double column activo
- [ ] Longitud dentro del límite (contar páginas con referencias incluidas)
- [ ] Fuentes: Times New Roman en body, sin cambios manuales
- [ ] Sin `\vspace{}` o trucos de compresión que violan las guidelines

### Figuras y tablas
- [ ] Todas las figuras compiladas en alta resolución (>= 300 DPI para imprenta)
- [ ] Figuras visibles en escala de grises (imprimir en B&W para verificar)
- [ ] Captions autocontenidos: releer cada uno de forma aislada
- [ ] Todas las figuras y tablas referenciadas en el texto
- [ ] Numeración consecutiva y sin saltos (Fig. 1, 2, 3, no 1, 3, 5)

### Referencias
- [ ] BibTeX compilado sin warnings
- [ ] Sin referencias duplicadas
- [ ] Formato IEEE en todas: `Apellido, N., "Título", Venue, año, pp. X-Y.`
- [ ] Sin URLs crudas — usar DOI cuando disponible
- [ ] Todas las citas del texto tienen entrada en referencias y viceversa

---

## Checklist D-1 (1 día antes)

### Anonimización (para double-blind venues: ICRA, CoRL, RSS, ICCV)
- [ ] Sin nombres de autores en el texto
- [ ] Sin afiliaciones en el texto
- [ ] Self-citations reformuladas en tercera persona: "[14]" en lugar de "our prior work [14]"
- [ ] Sin acknowledgments (o con placeholder "[omitted for blind review]")
- [ ] Sin links a repositorios de código propios con nombres identificables
- [ ] Sin watermarks ni metadatos de autor en el PDF
- [ ] Verificar propiedades del PDF: File > Properties — sin nombres

### Para venues no-blind (IROS, T-RO, RA-L)
- [ ] Acknowledgments completos (grants, colaboradores, acceso a hardware)
- [ ] Authors and affiliations revisados y actualizados

### PDF final
- [ ] Compilar con LaTeX desde cero (limpiar archivos auxiliares) y verificar que compila sin errores
- [ ] Abrir el PDF en un lector diferente al editor
- [ ] Verificar que todas las figuras aparecen (no solo placeholders)
- [ ] Verificar que las ecuaciones se ven correctas
- [ ] Verificar hyphenation — sin palabras cortadas incorrectamente
- [ ] Verificar que los hyperlinks/bookmarks (si se usan) funcionan

---

## Checklist D-0 (día del deadline)

### Submission
- [ ] Cuenta en el sistema de submission creada y activa (Papercept/OpenReview/EasyChair)
- [ ] Título exactamente igual en el sistema de submission y en el PDF
- [ ] Abstract: copiar+pegar desde el PDF (no reescribir en el sistema)
- [ ] Todos los co-autores registrados con afiliaciones correctas
- [ ] Keywords seleccionados correctamente
- [ ] Supplementary material (video, código) listo y subido si aplica
- [ ] **Submission de prueba** realizada >2h antes del deadline para detectar errores técnicos

### Después de la submission
- [ ] Guardar el número de submission
- [ ] Guardar el PDF exacto que se subió con fecha y versión
- [ ] Comunicar a todos los co-autores que se completó la submission

---

## Problemas comunes en el último momento

| Problema | Prevención |
|----------|-----------|
| Exceso de páginas | Medir páginas con el template desde el inicio, no al final |
| Figuras borrosas en PDF | Exportar figuras como vectores (PDF/SVG) o >300 DPI desde el inicio |
| BibTeX con errores | Compilar BibTeX regularmente, no solo al final |
| Sistema de submission caído | Nunca dejar para las últimas 2 horas |
| Co-autor no responde | Establecer deadline interno 3 días antes del deadline real |
| PDF con nombres en metadata | Revisar `pdfinfo` o propiedades del PDF antes de subir |

---

## Post-submission: expectativas

| Venue | Tiempo típico de revisión | Tipo de revisión |
|-------|--------------------------|-----------------|
| ICRA | ~3 meses | Double-blind, 3 revisores |
| IROS | ~3 meses | Double-blind, 3 revisores |
| CoRL | ~2 meses | Double-blind, 3+ revisores |
| RSS | ~2 meses | Double-blind, 3+ revisores |
| RA-L | ~3-4 meses | Single-blind, associate editor + revisores |
| T-RO | 4-8 meses | Single-blind, major/minor revisions típicas |

Si la respuesta incluye revisiones, usar `/revision-letter` y `templates/revision-response.md`.
