# Curso: Acústica Musical (AM) — UC

## Contexto
Diseño y construcción de un curso nuevo de Acústica Musical, Pontificia
Universidad Católica de Chile. Profesor: Patricio de la Cuadra (Instituto
de Música + Departamento de Ingeniería Eléctrica). Audiencia esperada:
mixta, estudiantes de música e ingeniería, con niveles heterogéneos de
formación matemática y musical.

## Formato del curso
- 15 sesiones semanales; cada sesión tiene 2 módulos de 70 minutos.
- Cupo: 20 estudiantes (semestre actual); la metodología está
  dimensionada para ese número.
- Metodología basada en aprendizaje activo (definida en
  `diseno/02_metodologia.md`).
- Los objetivos de aprendizaje viven en `diseno/01_objetivos_aprendizaje.md`
  y son la referencia obligada: toda actividad, contenido y evaluación debe
  mapearse explícitamente a al menos un objetivo.
- La estructura general (qué sesión cubre qué) vive en
  `diseno/03_estructura_curso.md`.

## Fuentes
- Los libros base están en `referencias/libros/` (PDF), con jerarquía:
  - **Campbell & Greated (1987)** — texto principal de lectura.
  - **Benade (1990)** — intuición física y experimentos/actividades para
    aprendizaje activo (secciones EEQ). Citar por capítulo y sección,
    nunca por página (PDF convertido desde .mobi).
  - **Roederer (1997)** — percepción y psicoacústica; lectura alternativa
    en español.
  - **Rossing et al. (2002)** — banco de problemas y ejercicios para
    evaluaciones; no es lectura obligatoria.
- El índice de fuentes está en `referencias/notas/indice-fuentes.md`:
  consultarlo primero y abrir el PDF solo en el capítulo necesario.
- `referencias/notas/programa_2019.md` es el programa anterior del curso:
  antecedente útil, pero no plantilla — el diseño nuevo no debe copiarlo.
- Citar siempre con libro, capítulo y página cuando se usen como fuente.
- No inventar contenido técnico: si algo no está en las fuentes ni es
  conocimiento estándar verificable, marcarlo como **[POR VERIFICAR]**.

## Convenciones de trabajo
- Todo el material en español (Chile), registro académico pero cercano.
- Feedback directo y crítico; no complaciente. Señalar debilidades
  pedagógicas o técnicas aunque no se pregunte por ellas.
- Antes de reescribir archivos existentes en `diseno/` o `sesiones/`,
  reportar específicamente qué se va a cambiar y esperar confirmación.
- Los apuntes y documentos siguen `.claude/rules/estilo-materiales.md`.
- Las demos interactivas HTML siguen `.claude/rules/formato-demos.md`.
- Los planes de sesión se generan con la skill `/plan-sesion` y se guardan
  en `sesiones/sXX/plan.md`.
- **Publicación con Quarto + GitHub Pages** (pipeline anterior en
  `Admin/obsoleto/`, no usarlo). Los `.md` son la fuente de verdad.
  Cada `git push` a `main` reconstruye y despliega el sitio
  (molivarito.github.io/acustica-musical) vía GitHub Actions; para
  previsualizar localmente, `conda run -n base quarto preview`. El PDF
  del libro: `conda run -n base quarto render libro`. Canvas (curso
  MUC860-1, id 112005): estructura en `canvas/canvas.yml`, se aplica
  con `python3 canvas/publicar_canvas.py sync` (nunca publica ni borra).
- **Regla de visibilidad (2026-07-22)**: el sitio y Canvas contienen
  SOLO material para estudiantes (apuntes, guías/hojas, demos, libro,
  programa, apps). Material solo-profesor — planes de sesión
  (`plan.md`), pautas (`*pauta*`), pruebas (`prueba*`),
  `guion_profesor*`, `banco_estimulos.md`, `planilla_rubrica_oa3.md` y
  todo `diseno/` — está excluido del `render:` de `_quarto.yml` y NO se
  enlaza con links Markdown desde páginas públicas (Quarto copiaría el
  `.md` crudo a `_site`): solo backticks. Al crear material nuevo,
  revisar 4 lugares: `render:` de `_quarto.yml`, sidebar, mapa de
  `index.qmd`, `canvas/canvas.yml`.
- Para agregar una sesión/capítulo/documento nuevo PARA ALUMNOS: crear
  el `.md` y agregarlo a la `sidebar` de `_quarto.yml` (y a `render:`
  si cae fuera de los globs) y a `canvas/canvas.yml` + `sync`; si es un
  capítulo, también a `chapters` de `libro/_quarto.yml` y al arreglo
  `S` del mapa en `index.qmd`.
- Las figuras de apuntes/libro son SVG generados por `figuras/gen_sXX.py`
  (con `figuras/estilo_figuras.py`): para cambiar una figura, editar y
  re-ejecutar su script, nunca el SVG. Reproducciones desde la
  bibliografía: solo datos medidos irreemplazables, con cita completa en
  la leyenda y registro en `figuras/libros/EXTRACCIONES.md`.

## Fases del proyecto
1. Objetivos de aprendizaje (diseno/01) — discutir en plan mode.
2. Metodología de aprendizaje activo (diseno/02).
3. Estructura del curso: mapa de las 15 sesiones (diseno/03).
4. Desarrollo sesión por sesión: plan, apuntes, demos, actividades.
5. Revisión de alineamiento constructivo (skill `revision-alineamiento`).

## Estado del proyecto
- Fases 1–5 completadas. Fases 1–2 (objetivos, metodología) 2026-07-12;
  fases 3–4 en loop autónomo 2026-07-13 (15 sesiones + libro; registro
  en ESTADO_LOOP.md, no regenerar); cuatro revisiones de alineamiento
  (diseno/revision_*.md, la última 2026-07-22). Revisión del profesor
  hecha en entrevista de recalibración (2026-07-22): pruebas
  rediseñadas con alternativas y regla de visibilidad aplicada.
  Publicado: sitio (GitHub Pages) + Canvas MUC860-1 (18 módulos, sin
  publicar). La guía vigente del profesor es RESUMEN_PARA_PATO.md.
  Pendiente: checklist físico/administrativo del profesor (ver
  RESUMEN_PARA_PATO.md §Pendientes). (Actualizar manualmente.)
