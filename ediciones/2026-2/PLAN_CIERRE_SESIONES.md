# Plan de cierre de las sesiones s03–s15 (2026-08-14)

Escrito tras la s02: ese día costó horas de ida y vuelta descubrir en
caliente lo que el material asumía sin definir. Este plan lo hace UNA
vez, por adelantado, para las 13 sesiones restantes. Meta: **cada
sesión llega a su viernes "cerrada como quedó s02"** — mazo
autocontenido (audios con reproductor, figuras y láminas embebidas,
demo adentro), notas de orador con el guion en el punto de uso, cero
materiales fantasma, cero decisiones sorpresa en la sala — y el costo
semanal del profesor baja a ~20 minutos de rutina.

## El estándar "sesión cerrada" (lo que s02 tiene hoy)

1. **Mazo autocontenido**: los estímulos de audio embebidos con
   reproductor en su slide; las figuras del apunte que la clase usa,
   en las slides; la demo embebida; una sola ventana para toda la
   clase.
2. **Notas de orador completas** (tecla S): respuestas esperadas,
   guiones mínimos ("cómo enseño X en 3 minutos"), frases-puente entre
   bloques, y la frontera modelar-vs-descubrir de cada taller.
3. **Cero fantasmas**: todo material que el plan nombra existe (o el
   plan dice explícitamente "se dibuja en pizarrón").
4. **Estímulos resueltos**: grabados o conseguidos con licencia
   (pipeline validado de e02/e03), instalados en `material/estimulos/`
   con lámina y atribución.
5. **Verificado**: diffs revisados, verificadores en limpio,
   impresiones regeneradas, pusheado.

## Los 4 pasos

### Paso 1 — Barridos de supuestos s04–s15 (agentes; 0 min tuyos)

El piloto de s03 ya corrió (encontró 8 indefinidos reales; el más
peligroso ya está corregido). Se lanzan los 12 restantes EN PARALELO
(workflow, un agente por sesión, mismo protocolo del piloto:
INDEFINIDO REAL / DEFINIDO PERO ENTERRADO / CRITERIO DEL PROFESOR),
más verificación por muestreo de Claude. Producto: un dossier por
sesión en `ediciones/2026-2/barridos/`.

**Por qué todos ahora y no semana a semana**: las preguntas que son
tuyas se juntan en UNA sola sesión de decisiones (paso 2) en vez de
interrumpirte 12 veces.

### Paso 2 — La entrevista de decisiones (30–45 min tuyos, UNA vez)

Claude consolida todos los "decisión del profesor" de los 13 barridos
en una lista única de preguntas cerradas con opciones y
recomendación. Tú las respondes de una pasada (formato pregunta por
pregunta, como la entrevista de recalibración de julio). Cada
respuesta queda registrada donde corresponde (DATOS_CURSO.yml si es
hecho del diseño, plan/notas si es operativo).

Ya en cola desde el barrido de s03 (se responden al ejecutar este plan):
1. **Gancho de la cuerda (s03, m2)**: ¿practicas armónicos en
   guitarra antes del viernes, o construimos el monocordio y pasa a
   ser el plan A? (recomendación: monocordio — es trivial y queda
   como material permanente del curso).
2. **Presupuesto de materiales del proyecto**: ¿quién paga los
   materiales de construcción del objeto? (pregunta segura de los
   estudiantes el viernes).
3. **"Media hoja" de ideas del proyecto (s03)**: ¿plantilla impresa o
   papel en blanco + las 3 preguntas proyectadas? (recomendación:
   papel en blanco, declarado en el plan).

### Paso 3 — Cierre por sesión (agentes + Claude; 0 min tuyos)

Con las decisiones tomadas, se aplica el estándar a cada sesión, en
orden de calendario (s03 primero, esta semana):

- Embebido de estímulos/figuras/láminas + notas nuevas donde el
  barrido encontró huecos (frases-puente, guiones, fronteras de
  spoiler).
- Producción de faltantes: figuras nuevas vía `gen_sXX.py` (p. ej. la
  cadena de masas de s03), búsqueda de audios con licencia para los
  ítems "por grabar o conseguir" del banco (trueno-style: candidatos +
  láminas + checklist para tu oído).
- Regenerar impresiones, verificadores, commit + push por sesión.
- Supervisión Claude con evidencia (diffs, renders con exit code real,
  spot-checks contra fuentes) — las salvaguardas aprendidas el 14-ago.

### Paso 4 — Lo que solo tú puedes hacer (calendario, ~20 min/semana)

- **Grabaciones propias del banco** (una tarde con la flauta y un
  celular cubre casi todo): los ítems que el banco marca "grabar
  propio" — la lista consolidada sale del paso 1 con sus fechas tope
  (las de pruebas: #12 ya debía existir, #15 flauta que salta de
  registro, #16 frase seca/reverberante, etc.).
- **Validación auditiva** de los audios conseguidos (checklist tipo
  `estimulos_candidatos/README_VALIDACION.md`, 2 min por audio).
- **Rutina semanal** (la agenda ⚑ la recuerda): leer el plan en el
  panel (ahora con notas y sin sorpresas), `generar_impresiones.py NN`
  + Cmd+P, probar audio EN la sala, registrar la nota del taller.

## Calendario de ejecución

| Cuándo | Qué | Quién |
|---|---|---|
| Hoy vie 14, post-clase | Apruebas este plan y respondes las 3 preguntas de s03 | Tú (5–10 min) |
| Vie 14 noche | Barridos s04–s15 lanzados + consolidación | Claude/agentes |
| Sáb 15 | Lista única de decisiones + lista de grabaciones propias lista para ti | Claude |
| Antes del mié 19 | Entrevista de decisiones (una pasada) | Tú (30–45 min) |
| Mié 19–jue 20 | Cierre completo de s03 (estímulos vaso/timbal, figura, monocordio si aplica) + imprimir-03 | Claude cierra; tú imprimes y pruebas |
| Semanas siguientes | Cierre de s04…s15 por adelantado, ≥1 semana antes de cada una | Claude/agentes |
| Cada jueves | Solo la rutina del paso 4 | Tú (~20 min) |

## Cómo se ejecuta (órdenes de una línea)

- **"Lanza los barridos"** → paso 1 completo esta noche.
- **"Hagamos la entrevista"** → paso 2, pregunta por pregunta.
- **"Cierra la sNN"** → paso 3 para esa sesión (s03 no espera a la
  entrevista completa: solo sus 3 preguntas).
- La agenda del panel sigue mandando la rutina semanal (paso 4).

## Registro

- Barridos: `ediciones/2026-2/barridos/sNN.md`
- Decisiones: `DATOS_CURSO.yml` + este directorio
- Avance: tabla al pie de este archivo (se actualiza por sesión)

| Sesión | Barrido | Decisiones | Cerrada | Notas |
|---|---|---|---|---|
| s02 | (en caliente, 14-ago) | — | ✅ 14-ago | El molde del estándar |
| s03 | ✅ 14-ago | pendientes (3) | — | Contradicción F1 ya corregida |
| s04–s15 | ✅ 14-ago (12 dossiers en `barridos/`) | consolidadas en `ENTREVISTA_DECISIONES.md` | — | 60 indefinidos reales en total; producción de estímulos mapeada |
