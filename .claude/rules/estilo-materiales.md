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
  aprendizaje que cubre (códigos de diseno/01).
- Estética editorial/científica: prosa clara, sin listas de viñetas
  excesivas; figuras con leyenda numerada; ecuaciones en LaTeX
  (`$...$` y `$$...$$`).
- Secciones cortas con títulos informativos (no "Introducción" sino, por
  ejemplo, "¿Por qué una cuerda afina distinto al apretarla?").
- Cerrar cada apunte con: síntesis breve, conexión con la sesión siguiente
  y referencias (libro, capítulo, páginas).

## Publicación

- Los documentos se publican con Quarto: tras editar un `.md`, correr
  `conda run -n base quarto render` (o `quarto preview` mientras se
  trabaja). Documento nuevo → agregarlo a la `sidebar` de `_quarto.yml`.
- Las figuras van como SVG generados por script en `figuras/`
  (`gen_sXX.py`), insertadas con `![**Figura N.** leyenda](ruta)` y
  numeradas por documento.

## Rigor
- Toda afirmación cuantitativa (frecuencias, velocidades, rangos) debe ser
  verificable en las fuentes o marcada [POR VERIFICAR].
- Usar unidades SI y notación consistente en todo el curso (definir la
  notación una vez en diseno/03 y respetarla).
