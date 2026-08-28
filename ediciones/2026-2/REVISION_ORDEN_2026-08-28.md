# Revisión de orden pedagógico — "predecir antes de ver" (2026-08-28)

Auditoría del ORDEN INTERNO de cada sesión: que nada muestre la
respuesta que una actividad posterior debe producir. Nace del defecto
encontrado en s04 el 2026-08-28 (ver §s04), que sobrevivió a las cuatro
revisiones de alineamiento de julio.

## Origen del defecto

Las 15 sesiones se generaron en el loop autónomo del 2026-07-13
(`_archivo/bitacora/ESTADO_LOOP.md`). El loop produjo material coherente
en objetivos, tiempos, cobertura y progresión entre sesiones —lo que las
cuatro auditorías de julio sí verificaban— pero **nunca comprobó el
orden dentro de la sesión**, porque esa regla no estaba escrita en
ninguna parte. De las tres sesiones auditadas el 2026-08-28, las tres
tienen el defecto, cada una en un sitio distinto (láminas, guía, plan).
Es una falla sistemática de generación, no un descuido puntual: hay que
barrer las 15, no apagar incendios de a uno.

## Por qué no se detectó antes

La skill `revision-alineamiento` revisaba cinco cosas —cobertura de
objetivos, exposición pasiva, tiempos, progresión entre sesiones,
material pendiente— y **leía solo los `plan.md`**. El defecto de s04
vivía repartido entre la guía del taller, las láminas y la columna "Rol
del profesor" del plan: tres insumos que la auditoría no cruzaba. Su
"progresión", además, era entre sesiones, no dentro de una.

Corregido el 2026-08-28: la skill tiene una **verificación 6** que
obliga a abrir láminas y guías (ver `.claude/skills/revision-alineamiento/SKILL.md`).

## La regla que se audita

El curso se juega en que el estudiante se compromete —predice por
escrito, dibuja o vota— ANTES de que se le muestre la respuesta. **Todo
defecto de esta familia es un lugar donde el ver llega antes del
predecir.** La convención quedó escrita en
`.claude/rules/estilo-materiales.md` §"Orden de la sesión".

### Cinco patrones

1. **Lámina spoiler** — una tabla, figura o simulación previa entrega el
   resultado que la actividad debía producir.
2. **Demostración con el mismo caso** — el profesor demuestra con el
   mismo caso o medición que el taller pide predecir.
3. **Síntesis duplicada o descolocada** — la misma síntesis ocurre dos
   veces, o el cierre de las láminas contradice el cierre del plan.
4. **Escucha contaminada** — algo se ve antes de oírse, cuando la
   escucha del día exige oír sin pantalla.
5. **Predicción cobrada dos veces** — el ticket de salida de la sesión
   anterior ya recogió la predicción por escrito; la guía de la sesión
   siguiente vuelve a pedirla, después de que la respuesta ya se reveló.
   La predicción duplicada es la que sobra, no la del ticket
   (descubierto en s05).

**Cuál es la lectura previa** (corregido 2026-08-28, al auditar s06): la
lectura previa es el **capítulo del libro** (`material/libro/capNN_*.md`,
que se encabeza "*Lectura previa a la sesión NN*"), NO el apunte de la
sesión. El apunte está narrado en pasado ("esta sesión repitió la
jugada", "usted lo comprobó") — es consolidación POSTERIOR. Auditar el
apunte como si fuera previo produce falsos positivos: lo que el apunte
revela, el estudiante lo lee cuando ya hizo la actividad.

El capítulo sí está legítimamente en manos del estudiante y no cuenta
como filtración; pero hay que señalar cuando una actividad finge
descubrimiento de algo que el capítulo ya trae explícito.

## Método por sesión (cinco pasos, en este orden)

1. De las **guías** (`actividades/*.md`): listar cada compromiso del
   estudiante y qué exactamente debe producir, citando las columnas
   textuales.
2. Del **plan**: la secuencia de bloques con tiempos y qué muestra o
   demuestra el profesor en cada uno (columna "Rol del profesor").
3. De las **láminas**: la línea de tiempo de revelaciones, lámina por
   lámina, notas de orador incluidas.
4. **Cruzar**: para cada compromiso, ¿algo anterior lo responde?
5. Reportar: patrón, gravedad, ubicación exacta, cita de lo que se
   filtra, cita de lo que el estudiante debía producir, y el movimiento
   propuesto.

## Orden de ataque

Atado al calendario, no al número de sesión.

| Lote | Sesiones | Cuándo | Estado |
|---|---|---|---|
| 1 | s05, s06 | antes del 04-sep | en curso (2026-08-28) |
| 2 | s07–s10 | antes del receso | pendiente |
| 3 | s11–s15 | octubre | pendiente |
| 4 | s01–s03 | cuando se pueda | pendiente — ya dictadas: los hallazgos son para 2027 |

## Prevención (para que no se repita)

- **Verificación 6** de `revision-alineamiento`, que obliga a leer
  láminas y guías además de los planes.
- **Regla `orden-{ses}` en la agenda** del panel, a −3 días de cada
  sesión: "Revisar que ninguna lámina de la sNN adelante la respuesta
  del taller" (`panel/agenda_reglas.yml`). Genera tareas atrasadas para
  s01–s03: son el lote 4, no ruido.
- **Convención escrita** en `.claude/rules/estilo-materiales.md`.

No hay chequeo automático: esto exige juicio pedagógico, no una regla
mecánica. El verificador de consistencia (`verificar_consistencia.py`)
seguirá cubriendo los HECHOS del diseño, no el orden.

---

# Plan de ejecución — barrido nocturno del 2026-08-28

Diseñado para correr **sin supervisión** y que el profesor encuentre por
la mañana decisiones tomadas, no trabajo pendiente. Doce sesiones:
s07–s15 y s01–s03 (s04 resuelto; s05 y s06 auditadas, arreglos
pendientes de su OK).

## Paso 0 — dejar la mesa limpia (antes de arrancar)

Se compromete en un commit aparte todo el trabajo acumulado del día
(estímulo e04, slides y plan de s04, skill, regla de agenda, convención,
este documento, PDF del calendario). Así los cambios del barrido no se
mezclan con lo de hoy y cada cosa se puede revertir por separado.

## Las cinco olas

1. **Auditoría** (12 agentes en paralelo, solo lectura). Uno por sesión,
   con el método de cinco pasos y los cinco patrones. Cada uno devuelve
   hallazgos estructurados: patrón, gravedad, ubicación exacta, cita de
   lo que se filtra, cita de lo que el estudiante debía producir y
   movimiento propuesto.
2. **Verificación adversarial** (un agente por hallazgo). Comprueba
   contra los archivos que la cita existe, que la filtración es real y
   que el movimiento propuesto no rompe otra cosa. Mata los falsos
   positivos. **Esta ola no es opcional**: la auditoría de s05 produjo
   un error de encuadre (tomó el apunte por lectura previa) que solo se
   detectó al verificarlo a mano.
3. **Aplicación** de los hallazgos confirmados, **un commit por sesión**
   (`orden(sNN): …`), en `main`. Cada sesión se puede revertir sola con
   `git revert`. Los cambios de juicio pedagógico ambiguo NO se aplican:
   quedan como propuesta en el informe.
4. **Verificación de integridad**: re-render de cada mazo tocado, medida
   de desborde de cada lámina (ninguna sobre 700 px),
   `verificar_consistencia.py` completo y `panel/indice.py --verificar`.
   Si algo falla, se revierte esa sesión y se reporta.
5. **Informe**: este documento, con una sección por sesión, y arriba un
   resumen de qué se cambió, qué quedó propuesto y qué no se tocó.

## Barandas (lo que el barrido NO hace)

- No toca `DATOS_CURSO.yml` ni ningún hecho del diseño (matrícula,
  pesos, hitos): eso es rediseño, no orden.
- No cambia tiempos de los bloques ni contenido técnico.
- No reescribe apuntes ni capítulos del libro.
- No aplica nada en s05 ni s06 (esperan OK explícito).
- No hace `git stash` ni cambia de rama (regla del repo: Drive).
- Ante duda pedagógica genuina, propone en vez de aplicar.

## Segundo eje: material que no llega a quien debe

Descubierto el 2026-08-28 al buscar la pauta del hito 1. La regla de
visibilidad excluye del sitio todo lo que haga match con `*pauta*`, pero
ese glob atrapa dos cosas opuestas: las pautas de CORRECCIÓN (deben
esconderse) y las pautas de ENCARGO (los estudiantes las necesitan).
Hoy el encargo del hito 1 (10 %) llega solo como hoja de papel; lo mismo
pasará con el hito 2 (10 %) y el hito 3 (15 %).

| Archivo | Qué es | ¿Estudiante? |
|---|---|---|
| `pauta_hito1_diseno` (s04) | encargo, 10 % | sí |
| `pauta_hito2_avance` (s10) | encargo, 10 % | sí |
| `pauta_hito3_presentacion_final` (s14) | encargo, 15 % | sí |
| `pauta_clinica_pares` (s10) | instrucciones de la clínica | probablemente sí |
| `pauta_feedback_ideas_proyecto` (s04) | guion del profesor | no |
| `pauta_revision_bitacoras` (s12) | guion del profesor | no |

El barrido **audita este eje y reporta**, pero no lo arregla solo:
cambiar la regla de visibilidad es delicado y necesita decisión del
profesor (renombrar los encargos a `encargo_*.md` para que dejen de
hacer match, y sumarlos a la sidebar y a Canvas).

## Lo que el profesor encuentra por la mañana

- Un commit por sesión tocada, revertible por separado.
- Este documento con el detalle y las propuestas que quedaron sin
  aplicar.
- La lista de decisiones que son suyas, en un solo lugar y al principio.

---

## s04 — La receta del timbre · RESUELTO 2026-08-28

Tres hallazgos, todos de la misma familia. Los dos primeros eran de
orden de láminas; el tercero era estructural y venía de s03.

### Hallazgo 1 (alta) — lámina spoiler

`slides_s04.qmd`, lámina **"El mapa de la cuerda"**, ubicada justo antes
del taller. Contenía:

| Punto | Modos encendidos | Timbre |
|---|---|---|
| $L/2$ | solo impares (2, 4, 6… mudos) | hueco, redondo |
| $\sim L/10$ | casi todos, agudos incluidos | brillante, metálico |

…más la regla general "pulsar a $1/n$ silencia el modo $n$", que cubre
el $L/4$. La guía del taller pide predecir, para $L/2$, $L/4$ y
$\sim L/10$: qué parciales quedan mudos y **cómo sonará en una palabra**.
La lámina rellenaba esa tabla casi celda por celda, incluida la columna
de la palabra.

**Arreglo**: movida DESPUÉS del taller, como síntesis. Coincide con lo
que el propio plan manda en el cierre ("sintetiza en el pizarrón el mapa
de la cuerda con los hallazgos de los 3 grupos").

### Hallazgo 2 (media) — simulación adelantada

La lámina **"El punto de pulsación, en vivo"** (Falstad *Loaded String*)
mostraba en vivo qué armónicos se encienden al pulsar en cada punto.
Introducida el 2026-08-27 y mal ubicada por razonar "regla → evidencia →
tabla": esa evidencia es justamente la que el taller debe producir.

**Arreglo**: movida después del taller y marcada como opcional, con
consigna nueva — pulsar donde ningún grupo midió y hacerlos apostar,
ahora que tienen su propio mapa.

### Hallazgo 3 (alta) — demostración con el mismo caso

El bloque 10–25′ mandaba al profesor "pulsar al micrófono **con el
espectrograma proyectado**". La cadena completa era:

| Momento | Qué pasa |
|---|---|
| s03, ticket de salida | "¿pulsar al medio o cerca del puente cambia la nota o el timbre?" |
| s04, 0–10′ | Lo **oyen**: misma cuerda, al medio y al puente |
| s04, 10–25′ | El profesor lo **proyecta resuelto** en espectrograma |
| s04, 25–62′ | Taller: "prediga qué parciales quedan mudos en $L/2$, $L/4$, $\sim L/10$" |

Dos de los tres puntos del taller quedaban resueltos en pantalla antes
de que escribieran una sola predicción. Mover láminas no lo tocaba.

**Arreglo**: el espectrograma sale del bloque 10–25′. El ticket de s03
preguntó algo **binario** —¿nota o timbre?— y eso se responde sin
pantalla: el timbre se oye, y que la nota no cambió lo dice el afinador.
El espectrograma resuelve la pregunta *siguiente* —"¿cuáles parciales,
exactamente?"— que es la del taller, con sus instrumentos. Actualizados
el plan (fila 10–25′, materiales y nota de orden) y las notas de orador
de la lámina "¿Cambió la nota o cambió el timbre?".

### Lo que quedó bien y no hay que romper

- Las láminas **Votación 1** y **Votación 2** retienen la respuesta con
  `. . .`: se vota antes de revelar. Patrón correcto.
- **La regla de la receta** se queda ANTES del taller: es la lectura
  previa y el taller la aplica. No es filtración.
- La escucha del día abre **sin pantalla**, como corresponde.

---

## s05 — La altura percibida · AUDITADA 2026-08-28, arreglos pendientes

### Hallazgo 1 (alta) — predicción cobrada dos veces

La cadena, verificada archivo por archivo:

| Momento | Qué pasa |
|---|---|
| s04, ticket de salida | "Apaguen el parcial 1. ¿La nota baja una octava, desaparece o sigue igual? **Escriban su predicción**" ← el compromiso, por escrito |
| s05, 15–33′ | Votan a mano alzada su predicción del ticket; el profesor **apaga $f_1$ con la demo proyectada, devela que la altura no cambia y nombra el fenómeno** (fundamental ausente / altura virtual) |
| s05, 33–60′ | `registro_el_bajo_que_no_esta.md` §1: "cada uno **predice** y marca: ☐ baja una octava ☐ desaparece ☐ sigue igual" ← la MISMA pregunta, ya respondida hace 20 minutos |

La §1 de la hoja es idéntica al ticket de s04, con las mismas tres
opciones, y llega después de la revelación. El encabezado de la hoja
dice, sin ironía: "la predicción se escribe ANTES de escuchar".

**Diagnóstico**: aquí NO sobra la demo. El bloque 15–33′ es el cobro
legítimo del ticket de s04 — la misma relación que s04 tiene con el
ticket de s03. Lo que sobra es la §1 de la hoja: pide por tercera vez
(ticket → votación → hoja) una predicción ya resuelta.

**Arreglo propuesto — reapuntar la predicción, no borrarla.** La
pregunta genuinamente abierta de ese bloque es **el umbral personal**:
cuántos parciales aguanta el patrón antes de que la altura se rompa. No
lo revela ni el plan, ni las láminas, ni el apunte, y la propia lámina
"¿Hasta dónde aguanta el patrón?" dice que "la respuesta es personal".
Entonces la §1 pasa a pedir: *"¿cuántos parciales cree que podrá quitar
antes de que la altura se rompa? ¿su umbral será igual al de sus
compañeros?"*, escrito antes de escuchar. La §2 (apagar $f_1$ uno mismo,
por turnos) se queda: oírlo en carne propia no es lo mismo que verlo
proyectado, y encadena con el filtro. El "¿le achuntó?" del cierre pasa
a contrastar el umbral y el ticket de s04.

### Hallazgo 2 (media) — lámina spoiler

`slides_s05.qmd`, lámina **"Taller — 'el oído y la octava'"**: el
blockquote de instrucciones ya nombra **"las octavas estiradas"**, que
es justo lo que la §3 de `registro_el_oido_y_la_octava.md` pide observar
y describir "en sus palabras" después de escuchar.

**Arreglo**: mover ese blockquote a "Síntesis del día", dejando la
lámina de instrucciones solo con la lista de tareas.

### Lo que está bien y no hay que romper

- La **escucha del día** es íntegramente auditiva y las notas dicen "NO
  resuelva el misterio todavía".
- El **umbral personal** es el compromiso mejor protegido de la sesión:
  nada lo anticipa.
- La lámina **"Por turnos: predigan antes de subir el filtro"** va antes
  de su demo. Patrón correcto.
- El gancho **"un tono y su doble"** vota antes de cualquier explicación.

### La lectura previa de s05 es ejemplar (y confirma el arreglo)

`material/libro/cap05_la_altura_percibida.md` —la lectura previa real—
retiene la respuesta a propósito:

> "**No le adelantamos si la conjetura resiste el experimento. Para eso
> está la sesión.** Pero le adelantamos su nombre, porque lo va a oír
> mucho: fundamental ausente, o altura virtual."

Y a continuación planta, textual, la pregunta que el arreglo propone
para la §1 de la hoja:

> "si el patrón es lo que importa, ¿cuántos parciales se pueden ir
> quitando —de abajo hacia arriba— antes de que el oído pierda el hilo y
> la altura se rompa? ¿Será igual para usted que para su compañero de
> banco?"

O sea: el capítulo ya deja esa pregunta abierta y la hoja debería
recogerla. El arreglo no inventa nada — cierra un circuito que el libro
ya había abierto. (La primera auditoría marcó el *apunte* como filtrador;
era el documento equivocado: el apunte se lee después.)

## s06 — Sonoridad y decibel · AUDITADA 2026-08-28, arreglo pendiente

### Hallazgo 1 (alta) — el plan se contradice a sí mismo tres veces

Todo ocurre dentro de `plan.md`, en el módulo 1, y **las láminas están
bien**: el defecto es un residuo de una versión anterior del plan que no
se sincronizó con las láminas ya corregidas.

| Fila | Qué dice |
|---|---|
| 8–18′ (escucha del día) | "**NO explica todavía** — anuncia que la sesión termina de resolverlo" |
| 18–36′ (mini-lección) | "presenta las **isofónicas** cualitativamente y **con ellas resuelve la escucha del día** (a bajo nivel el oído pierde graves y agudos)" ← 20 minutos después |
| 63–70′ (cierre) | "**cierra conectando con la escucha del día** (por eso la mezcla suave 'perdió' el bajo)" ← el mismo cierre, otra vez |

Además revienta la actividad insignia del módulo: la hoja de registro
pide predecir por escrito si 125 Hz necesita más o menos nivel que
1000 Hz, y el bloque 36–63′ hace que cada uno **dibuje SU curva**. La
mini-lección de 18–36′ ya entregó la conclusión ("a bajo nivel el oído
pierde graves y agudos").

**Las láminas no cometen el error** — verificado: van de la pregunta
("¿Mi oído mide parejo en toda la escala musical?") a la demo, y solo
después a "Lo que dibujaron las curvas". El riesgo es que el profesor
use el texto del plan como guion.

**Arreglo**: quitar de la fila 18–36′ la frase "presenta las isofónicas
(fones) cualitativamente y con ellas resuelve la escucha del día (a bajo
nivel el oído pierde graves y agudos)". La mini-lección se queda con la
aritmética del dB; el anuncio pasa a ser neutro ("esto se resuelve al
final del módulo, con su propia curva"). El contenido ya está en su
lugar correcto en la fila 63–70′ y en la lámina de revelación.

### Hallazgo 2 (media) — el gancho dice "queda en suspenso" y muestra el número

El gancho de las cuatro palmas indica "muestra la lectura sin
comentarla — el número queda en suspenso hasta la estación E3". Se
contradice: lo que queda en suspenso es la interpretación, no el dato.
No viola el orden para E3 (la predicción se vota en blanco, y además los
casos son distintos: cuadruplicar ≈ +6 dB vs. duplicar ≈ +3 dB), pero
ancla la sorpresa antes de que E3 la redescubra.

**Arreglo**: decidir cuál de las dos cosas se quiere y redactarlo así —
o no se proyecta el número, o se proyecta y se borra la frase "queda en
suspenso".

### Hallazgo 3 (baja) — la tabla del DS 594 en lámina

La lámina "El oído no tiene párpados" adelanta cualitativamente que el
protector "compra mucho más tiempo", que es lo que E5 calcula. Gravedad
baja: la misma tabla ya está impresa en la guía que reciben ANTES de
rotar, y es una norma que se aplica, no un resultado que se descubra.
Opcional: cortar esa frase y dejar solo el dato normativo.

### Lo que está bien y no hay que romper

- **La lectura previa** (`cap06`) es ejemplar: "No le damos el número: en
  la sesión lo va a **medir**… Prediga antes" y "No le mostramos todavía
  su forma… usted va a **dibujar la suya propia**".
- **Las cinco estaciones**: cada una trae su casilla de predicción ANTES
  de las instrucciones de medición, sin excepción.
- **"El mapa de las cinco estaciones"** solo lista preguntas, sin
  adelantar ningún dato.
- La escucha del día no lleva nada visual.
