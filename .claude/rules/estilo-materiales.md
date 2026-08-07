# Estilo de apuntes y documentos del curso

## Registro y tono
- Español (Chile), académico pero cercano; tratar al estudiante de "usted"
  o en impersonal, consistente dentro de cada documento.
- Explicar la física y la matemática apoyándose en la experiencia musical
  concreta (instrumentos reales, audición, ejecución) antes de formalizar.
- La audiencia es mixta: no asumir cálculo avanzado ni lectura musical
  fluida. Cuando un desarrollo matemático sea inevitable, ofrecer primero
  la intuición física/sonora y dejar el detalle formal en un recuadro o
  apéndice opcional.

## Formato (Markdown)
- Un archivo por documento, encabezado con: título, sesión, objetivos de
  aprendizaje que cubre (códigos de `OBJETIVOS_APRENDIZAJE.md`).
- Estética editorial/científica: prosa clara, sin listas de viñetas
  excesivas; figuras con leyenda numerada; ecuaciones en LaTeX
  (`$...$` y `$$...$$`).
- Secciones cortas con títulos informativos (no "Introducción" sino, por
  ejemplo, "¿Por qué una cuerda afina distinto al apretarla?").
- Cerrar cada apunte con: síntesis breve, conexión con la sesión siguiente
  y referencias (libro, capítulo, páginas).

## Publicación

- Los documentos se publican con Quarto: tras editar un `.md`, correr
  desde `material/` `conda run -n base quarto render` (o `quarto preview` mientras se
  trabaja). Documento nuevo → agregarlo a la `sidebar` de `material/_quarto.yml`.
- Las figuras van como SVG generados por script en `material/assets/figuras/`
  (`gen_sXX.py`), insertadas con `![**Figura N.** leyenda](ruta)` y
  numeradas por documento.

## Calendario y contingencias (heredado de SyS, 2026-08-06)

- El material genérico (`material/`) no nombra días de la semana ni
  fechas: "la próxima sesión", "la semana pasada" — nunca "el viernes"
  o "el 12 de septiembre". Todo lo fechado vive en `ediciones/<ed>/`
  (el calendario real cambia año a año).
- Las notas de orador de las slides (`::: {.notes}`) declaran
  contingencias y respaldos operativos: "sin internet: …", "si la demo
  no suena: …", "respaldo local en …". La contingencia se anota donde
  se va a necesitar, no en un documento aparte.

## Rigor
- Toda afirmación cuantitativa (frecuencias, velocidades, rangos) debe ser
  verificable en las fuentes o marcada [POR VERIFICAR].
- Usar unidades SI y notación consistente en todo el curso (definir la
  notación una vez en `PLAN_SEMESTRE.md` y respetarla).
