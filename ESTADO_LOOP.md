# ESTADO DEL LOOP — Fase 3–4 autónoma

Iniciado: 2026-07-12. Instrucción: desarrollar las 15 sesiones completas
(plan, apuntes, capítulo del libro, demo principal, actividades) sin
consultas al profesor. Para retomar tras una interrupción: leer este
archivo + `diseno/03_estructura_curso.md`, continuar con la primera
unidad no marcada `lista`, en orden s01→s15, y luego el cierre.

Prioridad si falta contexto/tiempo: plan > apuntes > capítulo >
actividades > demo.

## Tabla de avance

| Sesión | Tema (corto) | plan | apuntes | demo | actividades | capítulo |
|---|---|---|---|---|---|---|
| s01 | Del golpe al tono | lista | lista | lista | lista | lista |
| s02 | Ondas y espectrograma | lista | lista | lista | lista | lista |
| s03 | Modos de vibración | pendiente | pendiente | pendiente | pendiente | pendiente |
| s04 | La receta del timbre | pendiente | pendiente | pendiente | pendiente | pendiente |
| s05 | Altura percibida | pendiente | pendiente | pendiente | pendiente | pendiente |
| s06 | Sonoridad y decibel | pendiente | pendiente | pendiente | pendiente | pendiente |
| s07 | Prueba 1 + batidos | pendiente | pendiente | pendiente | pendiente | pendiente |
| s08 | Banda crítica y consonancia | pendiente | pendiente | pendiente | pendiente | pendiente |
| s09 | Escalas y temperamentos | pendiente | pendiente | pendiente | pendiente | pendiente |
| s10 | Resonancia e impedancia | pendiente | pendiente | pendiente | pendiente | pendiente |
| s11 | Cuerdas frotadas y cuerpo | pendiente | pendiente | pendiente | pendiente | pendiente |
| s12 | Vientos y lutería | pendiente | pendiente | pendiente | pendiente | pendiente |
| s13 | Prueba 2 + la voz | pendiente | pendiente | pendiente | pendiente | pendiente |
| s14 | La sala como instrumento | pendiente | pendiente | pendiente | pendiente | pendiente |
| s15 | Presentaciones finales | pendiente | pendiente | n/a | pendiente | pendiente |

## Controles de calidad

| Control | Estado |
|---|---|
| revision-alineamiento al cerrar s05 | pendiente |
| revision-alineamiento al cerrar s10 | pendiente |
| revision-alineamiento final (s15) | pendiente |
| Compilación libro/LIBRO_CURSO.md (+PDF si hay pandoc) | pendiente |
| RESUMEN_PARA_PATO.md | pendiente |

## Registro de decisiones tomadas sin consultar

- **D0 (infraestructura)**: el directorio no era repo git; se ejecutó
  `git init -b main`. Se agregó `referencias/libros/` a `.gitignore`
  (PDFs pesados y con derechos de autor; el índice de fuentes sí queda
  versionado).
- **D1–D5 (estructura)**: ver sección "Decisiones de estructura" en
  `diseno/03_estructura_curso.md` (progresión Benade; voz reducida a
  módulo liviano en s13; salida de medición en s14 con puesta en común
  comprimida; percusión sin sesión propia; electroacústica/audio digital
  fuera del programa).
- **D6 (proceso)**: para conservar contexto en un loop de 15 sesiones,
  cada sesión se produce con un subagente dedicado que sigue al pie de
  la letra las instrucciones de las skills `plan-sesion` y
  `demo-interactiva` (embebidas en su prompt) y las reglas de
  `.claude/rules/`; el orquestador verifica los artefactos, actualiza
  este archivo y hace el commit. s01 se produce en el hilo principal
  como ejemplar de estilo para los subagentes.
- **D7 (fuentes)**: los apuntes se redactan desde conocimiento estándar
  verificable + los capítulos indexados en
  `referencias/notas/indice-fuentes.md`; se citan libro/capítulo(/página
  cuando el índice la da) como lectura complementaria. C&G no admite
  búsqueda por texto (escaneo), así que las páginas citadas de C&G se
  toman de los rangos del índice de fuentes. Dato cuantitativo fino no
  estándar → [POR VERIFICAR].
- **D8 (sobrescritura de diseno/03)**: la regla de CLAUDE.md pide
  confirmar antes de reescribir en `diseno/`; la instrucción explícita
  de esta corrida ("complétalo primero", sin preguntas) la supersede.
  Solo se completó el esqueleto existente; 01 y 02 no se tocan.

## Pendientes de producción acumulados

(Se llena a medida que los planes declaren pendientes; ver también
diseno/02 §6.)

- **s01**: estímulo de audio de la línea base (grabación propia:
  guitarra con batido) — inicia el banco de estímulos; 5 reglas para los
  kits; rúbrica OA3 impresa; lista del curso con carreras.
- **s02**: grabaciones para el banco de estímulos (flauta con ataque
  soploso, trueno); planilla de rúbrica OA3 con nómina y sorteo; lista
  de apps de espectrograma recomendadas; recopilar tickets de s01.
