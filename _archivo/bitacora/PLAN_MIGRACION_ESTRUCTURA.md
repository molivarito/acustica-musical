# Plan de migración: AM a la arquitectura de SyS

**Estado: ACORDADO con el profesor (2026-07-23) — decisiones cerradas:
(1) compuerta = sitio completo + módulos Canvas semanales (se conserva);
(2) pruebas → ediciones/2026-2/pruebas/; (3) demos → material/demos/
centralizadas con README-inventario; (4) README único estilo SyS,
RESUMEN_PARA_PATO se fusiona ahí (histórico → _archivo/bitacora/).
Ejecución programada para ~3 h después del acuerdo.**
Objetivo: que AM y SyS compartan una sola lógica de navegación y
publicación ("la estructura refleja la lógica pedagógica, no la
logística de un semestre"), para que el profesor cargue UN modelo mental
y la lógica sea replicable en cursos futuros.

## Principios (heredados de SyS)

1. **Un hecho, un lugar**: cada decisión vive en un documento raíz que
   los demás referencian.
2. **El guion bajo significa "no lo edites"**: `_render/` (generado),
   `_archivo/` (pasado).
3. **Plantilla vs. edición**: `material/` es genérico y reutilizable;
   todo lo fechado vive en `ediciones/<año>/`.
4. **Respetar las diferencias reales del curso** (no se fuerza
   equivalencia donde no la hay — ver "Diferencias que se conservan").

## Estructura destino

```text
AM/
├── README.md                  ← el mapa del repo (estilo SyS: árbol + "Quiero…/Voy a…")
├── OBJETIVOS_APRENDIZAJE.md   ← hoy diseno/01
├── METODOLOGIA.md             ← hoy diseno/02
├── PLAN_SEMESTRE.md           ← hoy diseno/03 (mapa de las 15 sesiones, plantilla sin fechas)
├── GUIA_QUARTO_YML.md         ← nuevo (operación Quarto/YAML de AM; hereda de la de SyS)
├── CLAUDE.md                  ← igual que hoy, actualizado a la nueva estructura
│
├── material/                  ← FUENTE VIVA (proyecto Quarto; hoy raíz + sesiones/ + libro/ + materiales/)
│   ├── _quarto.yml, _quarto-canvas.yml, index.qmd, styles.css
│   ├── curso/sesion-NN/       ← plan.md + apunte_*.md + slides_sNN.qmd + actividades/*.md
│   ├── demos/                 ← las 14 demos (casa canónica única + README-inventario)
│   ├── libro/                 ← el libro (sub-proyecto book; conserva su nombre: es la marca del curso)
│   ├── assets/figuras/        ← hoy figuras/ (gen_sXX.py + SVG)
│   ├── apps_recomendadas.md   ← página transversal de alumnos
│   ├── profesor/              ← transversales solo-profesor: banco_estimulos.md, planilla_rubrica_oa3.md
│   └── _render/               ← TODO lo generado: site/ y canvas/ (hoy _site/ y _canvas/ en la raíz)
│
├── canvas/                    ← publicación (igual que hoy: canvas.yml + publicar_canvas.py)
│
├── ediciones/2026-2/          ← lo fechado de ESTE semestre
│   ├── CALENDARIO_2026-2.md   ← hoy Admin/calendario_2026-2.md
│   ├── admin/programa_curso.md ← hoy Admin/programa_curso.md (sigue siendo página del sitio)
│   └── pruebas/               ← prueba1/prueba2 con sus pautas (hoy en sesiones/s07 y s13/actividades)
│
└── _archivo/                  ← pasado, solo lectura
    ├── bitacora/              ← ESTADO_LOOP.md, RESUMEN histórico, diseno/revision_*.md
    ├── pipeline-viejo/        ← hoy Admin/obsoleto/
    └── bibliografia/          ← hoy referencias/ (sigue gitignored)
```

## Tabla de mapeo (origen → destino)

| Hoy | Queda en |
|---|---|
| `diseno/01_objetivos_aprendizaje.md` | `OBJETIVOS_APRENDIZAJE.md` |
| `diseno/02_metodologia.md` | `METODOLOGIA.md` |
| `diseno/03_estructura_curso.md` | `PLAN_SEMESTRE.md` |
| `diseno/revision_*.md`, `ESTADO_LOOP.md` | `_archivo/bitacora/` |
| `RESUMEN_PARA_PATO.md` | se fusiona: lo operativo → `README.md` nuevo; lo histórico → `_archivo/bitacora/` |
| `sesiones/sNN/{plan.md,apuntes/,actividades/}` | `material/curso/sesion-NN/` (plan, apunte y actividades como archivos hermanos) |
| `sesiones/sNN/slides/slides_sNN.qmd` | `material/curso/sesion-NN/slides_sNN.qmd` |
| `sesiones/sNN/demos/*.html` | `material/demos/` (+ README-inventario que dice qué demo sirve a qué sesión) |
| `libro/` | `material/libro/` |
| `figuras/` | `material/assets/figuras/` |
| `materiales/apps_recomendadas.md` | `material/apps_recomendadas.md` |
| `materiales/{banco_estimulos,planilla_rubrica_oa3}.md` | `material/profesor/` |
| `Admin/calendario_2026-2.md` | `ediciones/2026-2/CALENDARIO_2026-2.md` |
| `Admin/programa_curso.md` | `ediciones/2026-2/admin/programa_curso.md` |
| `sesiones/s07/actividades/prueba1*`, `s13/.../prueba2*` | `ediciones/2026-2/pruebas/` |
| `Admin/obsoleto/` | `_archivo/pipeline-viejo/` |
| `referencias/` | `_archivo/bibliografia/` |
| `_site/`, `_canvas/` | `material/_render/{site,canvas}` |

## Diferencias con SyS que SE CONSERVAN (deliberadas)

- **Sin banco de ejercicios**: AM no lo necesita (sus "ejercicios" son
  guías de taller ligadas a cada sesión). Si algún día se quiere, el
  slot es `banco/` como en SyS.
- **`sesion-NN`, no `semana-NN` con cXX**: en AM la unidad es la sesión
  única de 2 módulos, no un par de clases + ayudantía.
- **Plan y apunte siguen siendo DOS archivos** (SyS los fusiona con
  perfiles de Quarto): la separación de AM es pedagógica (el apunte se
  escribe para el alumno, el plan es coreografía de taller) y
  fusionarlos sería reescribir 30 documentos con riesgo alto y beneficio
  bajo. La navegación queda igual: ambos viven en la misma carpeta.
- **`libro/` conserva su nombre** (≈ `reader/` de SyS, mismo slot).
- **La compuerta semanal sigue siendo Canvas** (módulos sin publicar),
  no el "liberar --semana N" de SyS. El sitio de AM queda completo desde
  el día 1 por diseño (los apuntes no spoilean; lo sensible está
  excluido). — *punto discutible, ver abajo.*
- **Publicación por CI** (push → GitHub Actions → Pages), que ya
  funciona; SyS publica por script. Mismo resultado, distinto motor.

## Lo que se rompe al mover y cómo se garantiza que NO quede roto

La red de dependencias es grande; TODA la migración es scriptada
(git mv + reescritura mecánica de rutas), nada a mano:

1. `_quarto.yml` (render, sidebar ~180 líneas, resources) y
   `_quarto-canvas.yml` — reescritura completa.
2. `material/libro/_quarto.yml` (rutas de capítulos y figuras).
3. `index.qmd` — arreglo `S` del mapa (~90 hrefs) + accesos del pie.
4. `canvas/canvas.yml` — 86 URLs → nuevas rutas → `sync` a Canvas.
5. `.github/workflows/publish.yml` — working-directory `material/`,
   filtro de solo-profesor con las rutas nuevas.
6. **Cientos de enlaces Markdown internos** entre planes, apuntes,
   guías, libro y documentos raíz — reescritura por script con tabla de
   mapeo + verificación de que no queda ni un enlace a rutas viejas.
7. Slides: iframes `../demos/` → `../../demos/` (nueva profundidad).
8. Referencias a `figuras/` (apuntes y libro) → `assets/figuras/`.
9. Docs (README, CLAUDE.md, memoria de Claude) — actualización.

**Batería de verificación (obligatoria antes del push):**
- `quarto render` completo de ambos perfiles SIN errores ni warnings de
  enlaces.
- Crawler propio sobre `_render/site`: cada `<a href>` y `<iframe src>`
  interno debe resolver a un archivo existente (0 rotos).
- Grep global: cero referencias a rutas viejas (`sesiones/`, `diseno/`,
  `materiales/`, `Admin/calendario`, `figuras/` sin `assets/`).
- Exclusiones de privacidad re-verificadas: planes, pautas, pruebas,
  slides, guión, banco de estímulos y planilla NO aparecen en
  `_render/site` (script, no ojo).
- `publicar_canvas.py verificar` = 0 problemas tras el deploy.
- El PDF del libro recompila.
- Diff de CONTENIDO: `git diff` debe mostrar solo movimientos y rutas —
  ni una palabra de contenido pedagógico cambiada (verificación por
  muestreo + conteo de palabras por archivo).

**Red de seguridad**: todo en una rama `migracion-estructura`; `main` no
se toca hasta que la batería completa pase; el deploy solo ocurre al
mergear. Rollback = descartar la rama.

## Fases de ejecución (delegadas a agentes Sonnet, supervisadas)

- **F0 (orquestador)**: rama nueva; congelar tabla de mapeo definitiva.
- **F1 (agente A)**: movimientos `git mv` según tabla + estructura de
  carpetas. Determinista, un solo agente.
- **F2 (agentes B1–B3 en paralelo)**: reescritura de enlaces por zona
  (B1: material/curso + slides; B2: libro + assets + transversales;
  B3: configs — _quarto*, index.qmd, canvas.yml, CI, docs raíz).
- **F3 (orquestador)**: render local completo + crawler + greps +
  verificación de privacidad + PDF.
- **F4 (agente C)**: README nuevo estilo SyS + GUIA_QUARTO_YML de AM +
  CLAUDE.md actualizado.
- **F5 (orquestador)**: revisión final, merge, push, CI, verificación
  en línea, `canvas sync` + `verificar`, actualización de memoria.

## Nota de ejecución sobre las pruebas rediseñadas

Los 4 archivos de pruebas tienen modificaciones SIN commitear (rediseño
a alternativas, pendiente de revisión del profesor). Para poder moverlos
con git mv, la F0 los commitea como PRIMER commit aislado de la rama de
migración, titulado "Pruebas rediseñadas con alternativas (PENDIENTE DE
REVISIÓN DEL PROFESOR)" — así siguen siendo revisables/reversibles como
unidad en el log.
