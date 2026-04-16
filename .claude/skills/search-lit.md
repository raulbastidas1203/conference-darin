# Skill: search-lit

Búsqueda sistemática y organización de literatura para un tema de robótica.

## Invocación

```
/search-lit <tema> [--venue icra|iros|corl|rss|ral|tro] [--years <desde>-<hasta>] [--type survey|method|benchmark]
```

**Ejemplos:**
```
/search-lit "imitation learning for dexterous manipulation"
/search-lit "sim2real transfer humanoids" --venue icra --years 2021-2025
/search-lit "visual affordance learning" --type survey
```

## Qué hace este skill

Eres un asistente de investigación especializado en robótica. Al ejecutar este skill debes:

### 1. Búsqueda primaria
Busca el tema usando WebSearch en las siguientes fuentes en orden:

1. **arXiv** — `site:arxiv.org cs.RO <tema>` y `site:arxiv.org <tema> robot`
   - Extrae: arxiv ID, título, autores, fecha, abstract
2. **Semantic Scholar** — busca via API: `https://api.semanticscholar.org/graph/v1/paper/search?query=<tema>&fields=title,authors,year,venue,citationCount,abstract&limit=20`
3. **DBLP** — `https://dblp.org/search/publ/api?q=<tema>&format=json&h=20` para papers en ICRA/IROS/CoRL/RSS/RA-L/T-RO

### 2. Clasificación de resultados

Para cada paper encontrado, clasifica:

**Central** — si es relevante directo al tema (método principal, benchmark referencia, paper fundacional, competitor directo)
**Relacionado** — si toca el tema de forma indirecta o parcial
**Marginal** — si solo comparte keywords pero no es directamente relevante

### 3. Extracción de metadata

Para cada paper **central** o **relacionado**, extrae:
- Título completo
- Autores (primer autor + "et al." si >3)
- Venue + año
- DOI o arXiv ID (para trazabilidad)
- Abstract en 1-2 oraciones
- Número de citas (si disponible)

### 4. Output estructurado

Entrega el resultado en este formato:

```markdown
## Resultados: <tema>
Fecha de búsqueda: <fecha>
Fuentes consultadas: arXiv, Semantic Scholar, DBLP

### Papers Centrales (<N> encontrados)

| # | Título | Autores | Venue/Año | Citas | ID |
|---|--------|---------|-----------|-------|----|
| 1 | ... | ... | ICRA 2023 | 142 | arxiv:2301.XXXXX |

**Notas de relevancia:**
- [1] Es el benchmark de referencia para X, define las métricas estándar.
- [2] Método state-of-the-art en Y hasta 2023, superado por [3].

### Papers Relacionados (<N> encontrados)

| # | Título | Autores | Venue/Año | Citas | ID |
|---|--------|---------|-----------|-------|----|

### Gaps Identificados

- No se encontraron papers que aborden [aspecto específico]
- Pocos trabajos combinan [A] con [B]
- La mayoría de métodos asumen [limitación no resuelta]

### Papers a conseguir (sin acceso libre)

Los siguientes papers son centrales pero no tienen versión arXiv disponible. Si necesitas el full text, consíguelos con tus credenciales universitarias:
- [Título], [Autores], [Venue año], DOI: [DOI]
```

### 5. Recomendación de siguiente paso

Al final, sugiere:
- Qué papers centrales leer primero (por impacto + relevancia)
- Si tiene sentido hacer `/related-work` ahora o si falta más cobertura
- Keywords adicionales que podrían ampliar la búsqueda

## Notas importantes

- No inventar papers. Si un paper aparece en una búsqueda pero no puedes verificar sus datos (título, autores, venue, año), marcarlo como `[VERIFICAR]`.
- Si Semantic Scholar devuelve un paper con 0 citas y es de 2020 o antes, puede ser un artefacto — verificar antes de incluirlo.
- Priorizar papers de venues IEEE/ICRA/IROS/CoRL/RSS/RA-L/T-RO sobre workshops o arXiv puro cuando hay opciones.
