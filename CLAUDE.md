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

## Fases del proyecto
1. Objetivos de aprendizaje (diseno/01) — discutir en plan mode.
2. Metodología de aprendizaje activo (diseno/02).
3. Estructura del curso: mapa de las 15 sesiones (diseno/03).
4. Desarrollo sesión por sesión: plan, apuntes, demos, actividades.
5. Revisión de alineamiento constructivo (skill `revision-alineamiento`).

## Estado del proyecto
- Fase actual: 3 — Estructura del curso: mapa de las 15 sesiones (diseno/03).
  Fase 1 completada: objetivos aprobados en diseno/01_objetivos_aprendizaje.md
  el 2026-07-12. Fase 2 completada: metodología aprobada en
  diseno/02_metodologia.md el 2026-07-12. (Actualizar manualmente.)
