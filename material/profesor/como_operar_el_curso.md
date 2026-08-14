# Cómo operar el curso — guía de navegación del profesor

**Solo-profesor** (fuera del sitio y de Canvas). Escrita el 2026-08-13, en
la semana de la s02, a partir de las preguntas reales de la primera
semana. Si algo de aquí deja de calzar con el curso, esta página es la
que está mal: avisar a Claude para corregirla.

La idea que ordena todo: **el curso ya está construido** — las 15
sesiones tienen plan, apuntes, capítulo, slides, guías y demos desde
julio. El trabajo semanal no es crear material sino operarlo: revisar,
imprimir, probar audio, dar la clase, registrar una nota. Esta página
dice dónde está cada cosa y en qué orden mirarla.

## El mapa del repo en cuatro líneas

| Dónde | Qué hay | Cuándo se toca |
|---|---|---|
| Raíz (`OBJETIVOS_APRENDIZAJE.md`, `METODOLOGIA.md`, `PLAN_SEMESTRE.md`, `DATOS_CURSO.yml`) | El diseño del curso | Casi nunca: solo en rediseños |
| `material/` | Todo el contenido. Lo público va al sitio y Canvas; `plan.md` y esta carpeta `profesor/` son solo tuyos | Solo para corregir erratas |
| `ediciones/2026-2/` | Lo fechado de este semestre: calendario, agenda, impresiones, pruebas | Todas las semanas — aquí vives tú |
| `panel/` | La mesa de trabajo local (ver abajo) | Se usa, no se edita |

Regla práctica: **no navegues el repo a mano**. El panel junta todo lo
de una sesión en una pantalla.

## El ciclo semanal (la agenda lo recuerda por ti)

El botón **⚑ agenda** del panel (o `python3 panel/agenda.py` en el
terminal) muestra qué toca, con fechas que se derivan solas del
calendario de la edición. El ciclo base de toda semana:

1. **Lunes** — leer el plan de la sesión del viernes (tarea `plan-NN`).
2. **Jueves** — imprimir guías y probar demos y audio, en la sala si se
   puede (`imprimir-NN`). El paquete de impresión se refresca con
   `python3 ediciones/2026-2/generar_impresiones.py NN` y queda en
   `ediciones/2026-2/impresiones_sNN/`: abrir cada HTML y Cmd+P
   (3 copias de cada guía — una por mesa — y la hoja de escucha).
3. **Viernes, al terminar** — registrar en Canvas la nota del taller
   (`taller-NN`) y guardar los tickets de salida para la próxima semana.

Los hitos no semanales (lanzar el proyecto, publicar pautas, recordar
entregas) también aparecen ahí, con anticipación. Marca cada tarea con
su checkbox: el botón se pone rojo cuando acumulas atrasadas, y esa
señal solo sirve si el estado es veraz.

## Cómo leer un `plan.md` (en este orden, no en el del documento)

La cabecera de los planes fue escrita para la trazabilidad del diseño,
no para preparar clase: cita objetivos por código y reglas de
`METODOLOGIA.md` por número. Leerla primero desorienta. El orden que
funciona:

1. **Las tablas de los dos módulos** — son el guion. Fila por fila:
   "Actividad del estudiante" es lo que pasa en las mesas, "Rol del
   profesor" es tu letra, "Tiempo" marca el ritmo (los minutos
   reinician en cada módulo). Con solo esto ya puedes dar la clase.
2. **"Riesgos y plan B"** — las contingencias ya pensadas (qué hacer si
   la demo no suena, si sobra tiempo, si las apps no cooperan).
3. **Los materiales** — mejor en la zona Materiales del panel, que
   junta los de todas las celdas, los deduplica y recuerda tus tildes:
   es la lista del bolso.
4. **La cabecera, al final y en diagonal.** Lo único operativo es
   **"Requisitos previos"**: qué traen los estudiantes y qué traes tú.
   El resto ("Posición en la progresión", "Reglas aplicadas") es
   contabilidad del diseño; ignorarla no tiene consecuencias.

## Diccionario (los ocho términos que los planes dan por sabidos)

- **OA*n.m*** — código de objetivo de aprendizaje. No los memorices: la
  zona de objetivos del panel muestra el texto completo de cada uno.
- **PEE** — el ciclo **predicción → experimento → explicación**: nada
  suena sin predicción escrita antes, y toda actividad cierra
  contrastando predicción y resultado. Es el corazón metodológico del
  curso.
- **Guía PEE** — la hoja impresa de 1 página por mesa que estructura ese
  ciclo (casilla de predicción, bloque de contraste).
- **Escucha del día** — ritual de 10 minutos que abre el módulo 1 desde
  s02: estímulo dos veces, tres líneas escritas
  (describir → hipotetizar → verificar), discusión de mesa, vocero.
  **Nunca lleva nota.**
- **Rúbrica rápida** — logrado / parcial / incipiente, anotada al vuelo
  mientras cierras las guías EN clase. Esa es la nota del taller: no te
  llevas corrección a la casa.
- **Ticket de salida** — la pregunta breve del cierre; se recoge y la
  sesión siguiente la retoma.
- **Formato *n*** — fila *n* del catálogo de formatos de actividad de
  `METODOLOGIA.md` §2 (demo predictiva, taller experimental,
  mini-lección interactiva…). Los planes suelen nombrar el formato en
  palabras junto al número; el número es ignorable.
- **Variante** (experimental / medición / …) — plantilla general del
  módulo, también de `METODOLOGIA.md`. Explica la forma; no cambia lo
  que haces.

## En clase: quién usa qué

- **Tú**: el `plan.md`, impreso o en una ventana que no se proyecte —
  es solo-profesor (revela respuestas esperadas y tu guion).
- **Al proyector**: las slides (públicas; sus notas de orador traen los
  respaldos: "sin internet…", "si la demo no suena…") y la demo — un
  HTML autocontenido que funciona sin internet desde el archivo local.
- **En las mesas**: las guías impresas (de `ediciones/<ed>/impresiones_sNN/`,
  una por mesa). Se trabajan y se cierran en clase con la rúbrica rápida.
- **En los bolsillos**: los celulares con la app de espectrograma —
  instrumento de medición permanente desde s02.
- **La escucha del día**: el estímulo sale de tu equipo
  (`material/estimulos/`), dos pasadas, y cierras con tu versión experta.

## Después de clase (10 minutos)

Nota del taller a Canvas, tickets guardados, tareas marcadas en la
agenda. Nada más: la semana siguiente parte de nuevo en el paso 1.

## Si algo se ve raro

- Render viejo en el panel → semáforo en rojo; el botón ⟳ lo regenera.
- Algo no parsea → `python3 panel/indice.py --verificar` dice qué y dónde.
- Duda de si un hecho del curso sigue vigente (pesos, hitos, reglas) →
  `DATOS_CURSO.yml` es la fuente única; `python3 verificar_consistencia.py`
  confirma que los documentos lo siguen afirmando.
- Más detalle del panel (atajos, semáforos, arquitectura): `panel/README.md`.
- La guía extensa del diseño y sus decisiones:
  `_archivo/bitacora/RESUMEN_PARA_PATO_2026-07.md`.
