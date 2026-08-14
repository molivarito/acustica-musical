# Curso: Acústica Musical (AM) — UC

## Contexto
Diseño y construcción de un curso nuevo de Acústica Musical, Pontificia
Universidad Católica de Chile. Profesor: Patricio de la Cuadra (Instituto
de Música + Departamento de Ingeniería Eléctrica). Audiencia esperada:
mixta, estudiantes de música e ingeniería, con niveles heterogéneos de
formación matemática y musical. **Edición 2026-2: los 9 inscritos son
estudiantes de música** — los grupos se mezclan por familia de
instrumento y afinidad tecnológica, no por carrera; el diseño mixto se
conserva para ediciones futuras.

## Formato del curso
- 15 sesiones semanales; cada sesión tiene 2 módulos de 70 minutos.
- Matrícula 2026-2: 9 estudiantes = 3 grupos de 3 (ajuste 2026-08-06);
  la metodología y todo el material operativo están dimensionados a ese
  número. El cupo formal del programa sigue siendo 20; el diseño para 5
  grupos de 4 queda en la bitácora.
- Metodología basada en aprendizaje activo (definida en
  `METODOLOGIA.md`).
- Los objetivos de aprendizaje viven en `OBJETIVOS_APRENDIZAJE.md`
  y son la referencia obligada: toda actividad, contenido y evaluación debe
  mapearse explícitamente a al menos un objetivo.
- La estructura general (qué sesión cubre qué) vive en
  `PLAN_SEMESTRE.md`.

## Fuentes
- Los libros base están en `_archivo/bibliografia/libros/` (PDF), con jerarquía:
  - **Campbell & Greated (1987)** — texto principal de lectura.
  - **Benade (1990)** — intuición física y experimentos/actividades para
    aprendizaje activo (secciones EEQ). Citar por capítulo y sección,
    nunca por página (PDF convertido desde .mobi).
  - **Roederer (1997)** — percepción y psicoacústica; lectura alternativa
    en español.
  - **Rossing et al. (2002)** — banco de problemas y ejercicios para
    evaluaciones; no es lectura obligatoria.
- El índice de fuentes está en `_archivo/bibliografia/notas/indice-fuentes.md`:
  consultarlo primero y abrir el PDF solo en el capítulo necesario.
- `_archivo/bibliografia/notas/programa_2019.md` es el programa anterior del
  curso: antecedente útil, pero no plantilla — el diseño nuevo no debe
  copiarlo.
- Citar siempre con libro, capítulo y página cuando se usen como fuente.
- No inventar contenido técnico: si algo no está en las fuentes ni es
  conocimiento estándar verificable, marcarlo como **[POR VERIFICAR]**.

## Convenciones de trabajo
- Todo el material en español (Chile), registro académico pero cercano.
- Feedback directo y crítico; no complaciente. Señalar debilidades
  pedagógicas o técnicas aunque no se pregunte por ellas.
- Antes de reescribir archivos existentes en `OBJETIVOS_APRENDIZAJE.md`,
  `METODOLOGIA.md`, `PLAN_SEMESTRE.md` o `material/curso/`, reportar
  específicamente qué se va a cambiar y esperar confirmación.
- Los apuntes y documentos siguen `.claude/rules/estilo-materiales.md`.
- Las demos interactivas HTML siguen `.claude/rules/formato-demos.md`.
- Los planes de sesión se generan con la skill `/plan-sesion` y se guardan
  en `material/curso/sesion-NN/plan.md`.
- **Publicación con Quarto + GitHub Pages** (migrado a `material/` como
  sub-proyecto Quarto el 2026-07-24; pipeline anterior en
  `_archivo/pipeline-viejo/`, no usarlo). Los `.md` son la fuente de
  verdad. Cada `git push` a `main` reconstruye y despliega el sitio
  (molivarito.github.io/acustica-musical) vía GitHub Actions; para
  previsualizar localmente, `cd material && conda run -n base quarto
  preview`. El PDF del libro: `cd material && conda run -n base quarto
  render libro`. Ese PDF (`material/libro/LIBRO_CURSO.pdf`) es la única
  copia del libro y el CI no lo reconstruye — lo copia como recurso —,
  así que un hook versionado en `.githooks/` rechaza los commits que
  cambien capítulos o figuras del libro sin incluirlo regenerado
  (activar una vez por clon: `git config core.hooksPath .githooks`).
  Canvas (curso MUC860-1, id 112005): estructura en
  `canvas/canvas.yml`, se aplica con `python3 canvas/publicar_canvas.py
  sync` (nunca publica ni borra).
- **Panel de sesión** (`panel/`, 2026-07-28): mesa de trabajo local para
  preparar una sesión — `python3 panel/panel.py` (127.0.0.1:8767). Vive
  FUERA de `material/` a propósito: muestra material solo-profesor
  (planes, pautas, rol del profesor) y dentro del proyecto Quarto correría
  riesgo de publicarse. Es de solo lectura sobre las fuentes; convierte
  `plan.md` con pandoc porque la regla de visibilidad lo excluye del
  render. Qué parsea de dónde y qué convenciones lo romperían:
  `panel/README.md`; tras editar planes o documentos rectores,
  `python3 panel/indice.py --verificar`. El panel incluye además la
  **agenda administrativa** del semestre (botón ⚑, o `python3
  panel/agenda.py`): tareas derivadas del CALENDARIO de la edición +
  reglas en `panel/agenda_reglas.yml`; estado en
  `ediciones/<ed>/agenda_estado.yml`. El curso hermano SyS (`../SyS`)
  tiene panel y agenda gemelos (equivalencias en `README.md` §"El curso
  hermano").
- **Regla de visibilidad (2026-07-22)**: el sitio y Canvas contienen
  SOLO material para estudiantes (apuntes, guías/hojas, demos, libro,
  programa, apps). Material solo-profesor — planes de sesión
  (`plan.md`), pautas (`*pauta*`), pruebas (`ediciones/*/pruebas/`),
  `guion_profesor*`, `material/profesor/` completo (banco de estímulos,
  planilla OA3, `como_operar_el_curso.md` — la guía de operación del
  profesor, 2026-08-13; la carpeta no está en los globs de `render:`,
  así que lo nuevo ahí queda excluido por construcción) y los documentos raíz de
  diseño/bitácora (`OBJETIVOS_APRENDIZAJE.md`, `METODOLOGIA.md`,
  `PLAN_SEMESTRE.md`, `_archivo/`) — está excluido del `render:` de
  `material/_quarto.yml` y NO se enlaza con links Markdown desde páginas
  públicas (Quarto copiaría el `.md` crudo a `material/_render/site`):
  solo backticks. **Las slides tampoco se publican**: `render:` las
  genera (para el render local del profesor y el panel), pero el paso
  "Filtrar material solo-profesor" de `.github/workflows/publish.yml`
  borra las `slides_s*.html` del deploy, poda sus entradas de
  `search.json` (2026-08-14; el índice se construye antes del borrado
  y arrastraría su texto) y `canvas/auditar_sitio.py --sin-slides`
  audita la ausencia. Las **notas de orador** (`::: {.notes}`, con
  apoyo pedagógico desde 2026-08-14) son solo-profesor por partida
  doble: además del borrado anterior, el filtro
  `material/filtros/quitar_notas_en_ci.lua` las elimina de todo render
  del CI; los renders locales las conservan (tecla S). **Antes de
  afirmar qué es público, leer `publish.yml` completo**: la verdad del
  deploy vive ahí, no en `_quarto.yml` ni en `_render/` local. Al crear material nuevo, revisar 4 lugares: `render:`
  de `material/_quarto.yml`, sidebar, mapa de `material/index.qmd`,
  `canvas/canvas.yml`.
- Para agregar una sesión/capítulo/documento nuevo PARA ALUMNOS: crear
  el `.md` y agregarlo a la `sidebar` de `material/_quarto.yml` (y a
  `render:` si cae fuera de los globs) y a `canvas/canvas.yml` + `sync`;
  si es un capítulo, también a `chapters` de `material/libro/_quarto.yml`
  y al arreglo `S` del mapa en `material/index.qmd`.
- Las figuras de apuntes/libro son SVG generados por
  `material/assets/figuras/gen_sXX.py` (con
  `material/assets/figuras/estilo_figuras.py`): para cambiar una figura,
  editar y re-ejecutar su script, nunca el SVG. Reproducciones desde la
  bibliografía: solo datos medidos irreemplazables, con cita completa en
  la leyenda y registro en
  `material/assets/figuras/libros/EXTRACCIONES.md`.

## Fases del proyecto
1. Objetivos de aprendizaje (OBJETIVOS_APRENDIZAJE.md) — discutir en plan mode.
2. Metodología de aprendizaje activo (METODOLOGIA.md).
3. Estructura del curso: mapa de las 15 sesiones (PLAN_SEMESTRE.md).
4. Desarrollo sesión por sesión: plan, apuntes, demos, actividades.
5. Revisión de alineamiento constructivo (skill `revision-alineamiento`).

## Estado del proyecto
- Fases 1–5 completadas. Fases 1–2 (objetivos, metodología) 2026-07-12;
  fases 3–4 en loop autónomo 2026-07-13 (15 sesiones + libro; registro
  en `_archivo/bitacora/ESTADO_LOOP.md`, no regenerar); cuatro revisiones
  de alineamiento (`_archivo/bitacora/revision_*.md`, la última
  2026-07-22). Revisión del profesor hecha en entrevista de
  recalibración (2026-07-22): pruebas rediseñadas con alternativas y
  regla de visibilidad aplicada. Publicado: sitio (GitHub Pages) +
  Canvas MUC860-1 (18 módulos, sin publicar). La guía vigente del
  profesor es `_archivo/bitacora/RESUMEN_PARA_PATO_2026-07.md`. Pendiente:
  checklist físico/administrativo del profesor (ver
  `_archivo/bitacora/RESUMEN_PARA_PATO_2026-07.md` §Pendientes).
  **Migración estructural (2026-07-24)**: reorganización del repo en
  `material/` (sub-proyecto Quarto: `curso/sesion-NN/`, `demos/`,
  `libro/`, `assets/figuras/`, `profesor/`), `ediciones/2026-2/`
  (pruebas y calendario del semestre en curso, fuera del sitio),
  `_archivo/` (bitácora, bibliografía y pipeline obsoleto) y los
  documentos raíz `OBJETIVOS_APRENDIZAJE.md` / `METODOLOGIA.md` /
  `PLAN_SEMESTRE.md`; ver rama `migracion-estructura`. (Actualizar
  manualmente.)
  **Decisión de evaluación (2026-07-24)**: la escucha del día es
  práctica de 10 min **sin nota** (en la mesa del grupo, con pregunta
  selectiva del profesor); OA3 se evalúa **solo por escrito** — Parte A
  de cada prueba + hoja de s15, mejores 2 de 3, 10 % del curso. Pesos:
  talleres 35 · proyecto 35 (hitos 10/10/15) · pruebas 20 (48 puntos
  cada una) · escucha escrita 10. Regla derivada: **ningún documento
  del curso promete nota por hablar en clase** (la única instancia oral
  evaluada es la defensa del proyecto en s15). El detalle vive en
  `METODOLOGIA.md` §§1–5 y §7.7.

- **Semestre 2026-2 en curso (2026-08-14)**: s01 y s02 dictadas
  (calendario real en `ediciones/2026-2/CALENDARIO_2026-2.md`; la
  agenda del panel gobierna el ciclo semanal). Novedades operativas de
  la primera quincena: guía del profesor
  `material/profesor/como_operar_el_curso.md` (botón 📖 del panel),
  generador de paquetes de impresión
  (`ediciones/2026-2/generar_impresiones.py`), estímulos e02
  (flauta C4, CC-BY) y e03 (trueno, CC-BY-SA) instalados con
  atribuciones en `material/estimulos/ATRIBUCIONES.md`, **notas de
  orador con apoyo pedagógico en las 15 sesiones** (respuestas
  esperadas, conducción y complementos citados; solo en renders
  locales — ver regla de visibilidad), F1 resuelto (taller s03
  formativo, "mejores 8 de 9") y auditoría de coherencia completa
  (`ediciones/2026-2/REVISION_MATERIAL_2026-08-13.md`).
- **Consistencia del diseño (2026-08-07)**: los hechos del diseño
  (matrícula, mesas, pesos, hitos, defensas, estímulo consagrado)
  viven en **`DATOS_CURSO.yml`** — fuente única — junto con el mapa de
  relaciones (qué archivo debe afirmar qué, qué términos quedaron
  prohibidos tras cada rediseño). **Todo rediseño parte por actualizar
  ese archivo y termina cuando `python3 verificar_consistencia.py`
  pasa en limpio**; el verificador corre además en el pre-commit
  (`--rapido`) y en el CI. Nada de barridos por memoria: si un
  rediseño invalida una afirmación, se actualiza en DATOS_CURSO.yml y
  en el documento, nunca solo en uno. Los agentes delegados **no
  ejecutan `git stash`** (sobre Google Drive dejó archivos a medio
  restaurar el 2026-08-07); ante dudas de estado, `git status`/`diff`
  y avisar.

## Pendientes conocidos (no resueltos a propósito)

Patrón heredado del CLAUDE.md de SyS: decisiones fechadas que se
posponen conscientemente, para no re-litigarlas ni olvidarlas.

- (2026-08-06) **Fusión plan+apunte con perfiles Quarto**
  (`content-hidden`/`content-visible when-profile=`, patrón SyS):
  reduciría la doble fuente de verdad plan/apunte, pero implica
  refactorizar las 15 sesiones y el panel que parsea `plan.md`.
  Pospuesta para el receso o la edición 2027.
- (2026-08-06, CERRADO 2026-08-14) **Cabeceras con tiempos
  inconsistentes**: la auditoría del 2026-08-13 encontró 8 guías con
  tiempos pre-ajuste; el 2026-08-14, con OK del profesor, se alinearon
  todas con la aritmética declarada de su plan (+ los títulos de
  `canvas/canvas.yml` y una contradicción interna del plan de s12).
  Detalle y dos decisiones de criterio (s03, s04) en
  `ediciones/2026-2/REVISION_MATERIAL_2026-08-13.md`.
- (2026-08-14) **s15, re-escucha de la línea base**: en s01 los
  estudiantes oyeron el golpe EN VIVO; `e01_linea_base.wav` es la
  captura de ese golpe, no lo que sonó por parlantes. Decidir antes de
  preparar s15: reproducir la captura (recomendado: repetible y no
  depende de conservar el objeto) o repetir el golpe en vivo con el
  mismo objeto. Si es la captura, revisar niveles en la sala con
  anticipación.
- (2026-08-06, CERRADO 2026-08-13) **s15, preguntas del grupo 1**:
  describía el diseño por grupos anterior; el plan vigente de s15 tiene
  9 defensas individuales de 11′ (8′ + 3′) iguales para todos, así que
  la asimetría que había que decidir ya no existe. Verificado en la
  auditoría del 2026-08-13.
