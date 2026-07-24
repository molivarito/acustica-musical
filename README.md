# MUC860 · Acústica Musical — repositorio del curso

Repositorio único del curso: contenidos, demos, el libro de lecturas, la
publicación (sitio Quarto + Canvas) y el ensamble de cada semestre. Este
README es el mapa completo; la operación de Quarto/YAML vive en
[`GUIA_QUARTO_YML.md`](GUIA_QUARTO_YML.md).

## Las dos reglas del repo

> **1. El guion bajo significa "no lo edites".**
> `_render/` porque se genera solo (bórralo cuando quieras: se regenera con
> un comando); `_archivo/` porque es pasado del curso (bitácora, pipeline
> anterior, bibliografía — no recibe material nuevo).
>
> **2. Un hecho, un lugar.**
> Cada decisión vive en un solo documento; los demás la referencian. Los
> objetivos están en `OBJETIVOS_APRENDIZAJE.md`, la metodología y evaluación
> en `METODOLOGIA.md`, el mapa de las 15 sesiones en `PLAN_SEMESTRE.md`, las
> fechas reales de este semestre en `ediciones/2026-2/`.

## El árbol

```text
AM/
├── README.md                  ← este mapa
├── OBJETIVOS_APRENDIZAJE.md   ← QUÉ se aprende: objetivos OA y su notación
├── METODOLOGIA.md             ← CÓMO se enseña y evalúa (aprendizaje activo)
├── PLAN_SEMESTRE.md           ← mapa plantilla de las 15 sesiones (sin fechas)
├── GUIA_QUARTO_YML.md         ← CÓMO se opera: Quarto, YAML, CI, Canvas
├── CLAUDE.md                  ← orientación para Claude al inicio de cada sesión
│
├── material/                  ← FUENTE VIVA: contenidos (proyecto Quarto)
│   ├── curso/sesion-NN/       ← plan.md + apunte_*.md + slides_sNN.qmd (+ actividades/)
│   ├── demos/                 ← 14 demos HTML con audio (casa canónica única)
│   ├── libro/                 ← "Escuchar como científico" (sub-proyecto book) + PDF
│   ├── assets/figuras/        ← SVG generados por gen_sXX.py (+ estilo_figuras.py)
│   ├── profesor/              ← transversales solo-profesor: banco de estímulos, rúbrica OA3
│   ├── programa_curso.md, apps_recomendadas.md  ← páginas transversales de alumnos
│   └── _render/                ← TODO lo generado: site/ y canvas/
│
├── canvas/                    ← integración Canvas (MUC860-1): canvas.yml + publicar_canvas.py
│
├── ediciones/2026-2/          ← lo fechado de ESTE semestre
│   ├── CALENDARIO_2026-2.md   ← fechas reales
│   └── pruebas/               ← prueba1/prueba2 + pautas (generadas, solo-profesor)
│
└── _archivo/                  ← pasado del curso (solo lectura; nada nuevo nace aquí)
    ├── bitacora/               ← ESTADO_LOOP, revisiones de alineamiento, planes de migración
    ├── pipeline-viejo/         ← publicación pre-Quarto (no usar)
    └── bibliografia/           ← libros base (PDF, gitignored) + índice de fuentes
```

## Quiero… / Voy a…

| Quiero… | Voy a… |
|---|---|
| preparar la clase de la semana | `material/curso/sesion-NN/plan.md` |
| ver/editar el **apunte** de una sesión | `material/curso/sesion-NN/apunte_sNN_*.md` |
| las **diapositivas** de una clase | `material/curso/sesion-NN/slides_sNN.qmd`; para verlas, `quarto preview` (el CI las filtra del sitio público — ver `GUIA_QUARTO_YML.md`) |
| el **libro** de lecturas previas (o su PDF) | `material/libro/` → PDF en `material/libro/LIBRO_CURSO.pdf` |
| las **guías de taller / hojas de actividad** | `material/curso/sesion-NN/actividades/` |
| una **demo** interactiva | `material/demos/` |
| las **pruebas** (enunciado + pauta) | `ediciones/2026-2/pruebas/` (solo-profesor) |
| las **fechas reales** de este semestre | `ediciones/2026-2/CALENDARIO_2026-2.md` |
| el **programa oficial** del curso | `material/programa_curso.md` (página del sitio) |
| las **decisiones de diseño** del curso | `OBJETIVOS_APRENDIZAJE.md`, `METODOLOGIA.md`, `PLAN_SEMESTRE.md` |
| **publicar una semana** en Canvas | módulo correspondiente en la interfaz de Canvas (a mano — ver "Cómo trabajar") |
| **verificar enlaces** del sitio publicado en Canvas | `canvas/` → `python3 publicar_canvas.py verificar` |
| aprender a **usar Quarto y los YAML** de este repo | [`GUIA_QUARTO_YML.md`](GUIA_QUARTO_YML.md) |

## Fuente → salida generada → comando

Todo se edita en las fuentes; el sitio y el PDF se **generan** (nunca editar
nada bajo un `_render/`).

| Producto | Fuente | Salida | Comando (desde…) |
|---|---|---|---|
| Sitio del curso | `material/*.qmd` + `material/curso/**/*.md` | `material/_render/site/` | `quarto render` (material/) — o lo hace el CI en cada `git push` a `main` |
| Perfil canvas (páginas sin sidebar) | ídem | `material/_render/canvas/` | `quarto render --profile canvas` (material/) |
| PDF del libro | `material/libro/*.md` | `material/libro/LIBRO_CURSO.pdf` | `quarto render libro` (material/) |
| Figuras | `material/assets/figuras/gen_sXX.py` | `material/assets/figuras/sXX_*.svg` | `python3 gen_sXX.py` (material/assets/figuras/) |
| Estructura de módulos en Canvas | `canvas/canvas.yml` | módulos/ítems en Canvas (sin publicar) | `python3 publicar_canvas.py sync` (canvas/) |

Comando `quarto` si el shell no activa conda: `conda run -n base quarto ...`.

## Qué ve el alumno y qué ves solo tú

**Alumnos** (sitio + Canvas): apuntes, guías y hojas de actividades, demos,
libro (+ PDF), `material/programa_curso.md`,
`material/apps_recomendadas.md`, mapa del curso (`material/index.qmd`).

**Solo tú** (en el repo, fuera del sitio y de Canvas):

| Material | Dónde vive |
|---|---|
| Planes de sesión (tu guión docente) | `material/curso/sesion-NN/plan.md` |
| Pruebas y sus pautas | `ediciones/2026-2/pruebas/` |
| Pautas de hitos, clínica, feedback | `material/curso/sesion-NN/actividades/*pauta*` |
| Banco de estímulos (revela las pruebas) | `material/profesor/banco_estimulos.md` |
| Planilla de rúbrica OA3 | `material/profesor/planilla_rubrica_oa3.md` |
| Diseño del curso y bitácora de auditorías | `OBJETIVOS_APRENDIZAJE.md`, `METODOLOGIA.md`, `PLAN_SEMESTRE.md`, `_archivo/bitacora/` |

La regla vive en `material/_quarto.yml` (bloque `render:`, con comentario).
Ojo: el **repo de GitHub es público** — estos archivos no aparecen en el
sitio, pero sí son visibles para quien navegue el código fuente. Si eso te
incomoda, la salida es hacer el repo privado (pídelo).

## Cómo trabajar

- **Editar material**: editas el `.md` → `git commit` → `git push` a `main`.
  El sitio se reconstruye y despliega solo vía GitHub Actions (~2 min) en
  <https://molivarito.github.io/acustica-musical>. Para previsualizar antes:
  `cd material && conda run -n base quarto preview`.
- **Slides de cada clase** (solo tuyas): se ven con `quarto preview`
  navegando a `curso/sesion-NN/slides_sNN.qmd`, o abriendo el `.html`
  generado en `material/_render/site/` — pero el deploy público las filtra
  (paso "Filtrar material solo-profesor" del workflow), así que los alumnos
  no las ven en línea. Tras editar, `quarto render curso/sesion-NN/slides_sNN.qmd`
  (desde `material/`) para regenerarlas localmente.
- **Material nuevo**: crear el `.md` y, si es para alumnos, agregarlo a la
  `sidebar` de `material/_quarto.yml`, al mapa `material/index.qmd` y a
  `canvas/canvas.yml` (+ `python3 publicar_canvas.py sync`). Material tuyo
  (planes, pautas, pruebas…) basta con que calce con las exclusiones de
  `render:` en `material/_quarto.yml`, o agregarlo ahí. Detalle completo de
  los 4 lugares en `GUIA_QUARTO_YML.md`.
- **PDF del libro**: `cd material && conda run -n base quarto render libro`.
- **Figuras**: editar `material/assets/figuras/gen_sXX.py` y re-ejecutarlo —
  nunca el SVG.
- **Canvas**: `cd canvas && python3 publicar_canvas.py sync` (nunca publica
  ni borra); `... verificar` revisa que las URL del sitio no estén rotas.
  Publicar cada módulo/ítem es una acción manual tuya en la interfaz de
  Canvas.
- **Google Drive**: mantén la carpeta AM "Disponible sin conexión"; si
  `git push` se cuelga con "Operation timed out", es Drive deshidratando
  `.git` (el arreglo es re-descargar la carpeta).

## Pendientes del semestre

El detalle completo (checklist físico/administrativo, kits, permisos,
grabaciones pendientes, decisiones abiertas) vive en
`_archivo/bitacora/RESUMEN_PARA_PATO_2026-07.md` §"Pendientes que solo tú
puedes hacer" — es histórico (rutas de la estructura previa a esta
migración) pero la lista de pendientes sigue vigente. Las fechas reales del
semestre están en `ediciones/2026-2/CALENDARIO_2026-2.md`.

## Principio rector de la arquitectura

> La estructura del repositorio refleja la lógica pedagógica, no la
> logística de un semestre en particular.

- `material/` es una plantilla genérica y reutilizable año a año; **todo lo
  que depende de fechas o personas de un año vive en `ediciones/<año>/`**.
- Regla de oro para material nuevo: contenido de sesiones, demos y libro →
  `material/`; lo fechado (pruebas, calendario, programa del semestre) →
  `ediciones/<año>/`. `_archivo/` no recibe nada.
