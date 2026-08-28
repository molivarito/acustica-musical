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

## Orden de la sesión: predecir antes de ver (2026-08-28)

El curso se juega en que el estudiante se compromete —predice por
escrito, dibuja o vota— ANTES de que se le muestre la respuesta. De ahí
salen tres reglas para las láminas y los planes:

- **La síntesis va después de la actividad que la produce, nunca antes.**
  Una tabla o figura que resume "qué pasa en cada caso" es material de
  cierre. Si aparece antes del taller, la predicción escrita queda sin
  objeto.
- **La demostración del profesor no usa el mismo caso que el taller.**
  Si el taller pide predecir sobre los puntos A, B y C, la demostración
  previa no los resuelve en pantalla: usa otro caso, o responde solo la
  pregunta anterior (la que quedó abierta la semana pasada) y deja el
  instrumento de medición en manos de los estudiantes.
- **Cada instrumento resuelve su propia pregunta.** Antes de proyectar
  una medición, preguntarse qué pregunta contesta: si contesta la del
  taller, no va todavía.

Precedente: en s04 la tabla "El mapa de la cuerda" y la demostración con
espectrograma adelantaban la tabla de predicción de la guía; se
reordenaron el 2026-08-28. La verificación 6 de la skill
`revision-alineamiento` audita esto, y la agenda del panel lo recuerda a
−3 días de cada sesión.

## Rigor
- Toda afirmación cuantitativa (frecuencias, velocidades, rangos) debe ser
  verificable en las fuentes o marcada [POR VERIFICAR].
- Usar unidades SI y notación consistente en todo el curso (definir la
  notación una vez en `PLAN_SEMESTRE.md` y respetarla).
