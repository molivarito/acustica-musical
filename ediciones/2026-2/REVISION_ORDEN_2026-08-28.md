# Revisión de orden pedagógico — "predecir antes de ver" (2026-08-28)

Auditoría del ORDEN INTERNO de cada sesión: que nada muestre la
respuesta que una actividad posterior debe producir. Nace del defecto
encontrado en s04 el 2026-08-28 (ver §s04), que sobrevivió a las cuatro
revisiones de alineamiento de julio.

## DECISIONES PENDIENTES DEL PROFESOR

Todo lo de abajo está auditado y verificado, pero **nada se ha aplicado**
en s05–s15: tocar `material/curso/` requiere su visto bueno. Esta lista
se actualiza a medida que avanzan las tandas.

### Arreglos propuestos (un "sí" y se aplican)

| # | Sesión | Qué | Dónde | Riesgo |
|---|---|---|---|---|
| 1 | s05 | Reapuntar la §1 de la hoja: en vez de repredecir si la altura cambia (ya resuelto), predecir **su umbral personal** — que es lo que el capítulo 5 ya deja abierto | `actividades/registro_el_bajo_que_no_esta.md` | bajo |
| 2 | s05 | Mover "las octavas estiradas" de la lámina de instrucciones a la síntesis | `slides_s05.qmd` | nulo |
| 3 | s06 | Borrar de la fila 18–36′ la frase que resuelve la escucha del día ("con ellas resuelve la escucha del día…"): contradice a la fila 8–18′ y revienta la curva isofónica | `plan.md` | nulo |
| 4 | s07 | Reescribir dos pasajes del apunte para que no nombren "aspereza → dos notas" (lo que s08 debe descubrir), copiando la fórmula del capítulo 7 | `apunte_s07_batidos.md` | bajo |
| 5 | s07 | Unificar las frecuencias de la demo en **443/442/437** (el plan dice 442/444/437 y no calza con la lámina) | `plan.md` | nulo |
| 6 | s08 | Volver comparativa la predicción de F3: "¿su umbral será más ancho, más angosto o igual?" en vez de pedir un número recién proyectado | `actividades/registro_mapa_del_choque.md` | bajo |
| 7 | s09 | Reapuntar el ítem 2 de la predicción a la variación personal ("¿su oído distinguirá 2 cents?") en vez de preguntar algo que la mini-lección ya contestó | `actividades/guia_pee_afinar_por_batidos.md` | bajo |
| 8 | s11 | Reformular P3 como contraste contra la demo ("¿la cuerda real mostrará la esquina tan nítida?"), que es lo que el propio plan ya declara en Riesgos | `actividades/guia_pee_punto_de_frotado.md` | bajo |
| 9 | s11 | Sacar de la mini-lección la conclusión "las efes radian los graves" (es la P1 del taller) y moverla a la síntesis del cierre | `slides_s11.qmd` | bajo |
| 10 | s13 | (opcional) Cambiar "respuesta sorpresa" por "¿se lo esperaban después de leer el capítulo?" — el plan declara que ese contenido se consume, no se protege | `slides_s13.qmd` | nulo |
| 11 | s14 | Imprimir la hoja de ruta **sin** la columna "Tipo esperado" (seco/vivo/muy seco): es la respuesta del ranking que el grupo debe predecir | `actividades/rutas_salida_medicion.md` | bajo |
| 12 | s14 | Mover el ítem del T60 de la sala de clases ANTES de la demostración del globo, o eliminarlo: hoy pide "estimar" lo que se acaba de medir delante de ellos | `actividades/guia_salida_medicion_t60.md` | bajo |
| 13 | s12 | En la mini-lección y en la tabla "Dos tubos, dos registros", resolver solo el tubo ABIERTO y dejar el tapado como pregunta: el capítulo pidió expresamente guardar ese secreto | `slides_s12.qmd` + `plan.md` | bajo |

### Ya aplicado sin esperar (fuera de `material/curso/`)

- **s09, demo de temperamentos**: el bloque "¿Qué observar?" entregaba
  los cents objetivo (702 y 700) en la misma pantalla donde los
  estudiantes afinan de oído, anulando el ocultamiento que la propia
  demo implementa. Reescrito sin números. Revertible con `git revert`.
- **s14, demo de modos de sala**: cargaba con la curva REVELADA
  (`checked`), mientras la lámina que la precede dice "con la curva
  oculta". Quitado el `checked`; ahora el estado inicial coincide con lo
  que la lámina asume.

### Decisiones de criterio (no las tomo yo)

| # | Asunto | Las opciones |
|---|---|---|
| A | **s06, el gancho de las cuatro palmas** | Hoy el texto dice "el número queda en suspenso" y a la vez lo proyecta. O no se proyecta el número, o se proyecta y se borra esa frase. |
| B | **s06, la tabla del DS 594** | La lámina adelanta que el protector "compra mucho más tiempo", que es lo que E5 calcula. Gravedad baja (la tabla ya está en la guía impresa). ¿Podar la frase o dejarla? |
| C | **Las pautas de encargo** | `*pauta*` está excluido del sitio, así que los encargos de los hitos 1, 2 y 3 (10 %, 10 %, 15 %) llegan solo en papel. Propuesta: renombrarlos `encargo_*.md` y sumarlos a sidebar y Canvas. Cambia la regla de visibilidad: decisión suya. |

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

### Seis patrones

1. **Lámina spoiler** — una tabla, figura o simulación previa entrega el
   resultado que la actividad debía producir. **Incluye el texto de las
   propias demos**: el bloque "¿Qué observar?" de una demo está a la
   vista en el notebook del grupo mientras trabajan, así que cuenta como
   pantalla (descubierto en s09, donde la demo ocultaba los cents y su
   propio texto daba los dos números objetivo).
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
6. **El apunte de la sesión N filtra la sesión N+1** — el apunte es
   consolidación posterior *de su propia sesión*, pero es material
   PÚBLICO (sitio y Canvas) que los estudiantes leen **entre** clases:
   para la sesión siguiente funciona como lectura previa. Si resuelve
   por escrito lo que la sesión siguiente está diseñada para que
   descubran, la filtración es igual de real que una lámina spoiler
   (descubierto en s07 → s08). Este patrón obliga a un cruce que los
   otros cinco no piden: **apunte de N contra los compromisos de N+1**.

**Los tres documentos y a quién le filtran** (afinado 2026-08-28 al
auditar s06 y s07):

| Documento | Cuándo se lee | ¿Filtra? |
|---|---|---|
| `material/libro/capNN_*.md` — la **lectura previa** ("*Lectura previa a la sesión NN*") | antes de la sesión N | No para N: está legítimamente en sus manos. Pero señalar si una actividad finge descubrimiento de algo que el capítulo ya trae explícito. |
| `material/curso/sesion-NN/apunte_*.md` — **consolidación** (narrado en pasado: "usted lo comprobó") | después de la sesión N, y antes de la N+1 | **No para N, pero SÍ para N+1**: es público y se lee entre clases. Ver patrón 6. |
| `plan.md`, `slides_*.qmd`, `actividades/*.md` | en la sesión N | Sí, es el objeto principal de la auditoría. |

El error inverso también cuenta: auditar el apunte como si fuera lectura
previa de su propia sesión produce falsos positivos (pasó en la primera
auditoría de s05).

## Método por sesión (cinco pasos, en este orden)

1. De las **guías** (`actividades/*.md`): listar cada compromiso del
   estudiante y qué exactamente debe producir, citando las columnas
   textuales.
2. Del **plan**: la secuencia de bloques con tiempos y qué muestra o
   demuestra el profesor en cada uno (columna "Rol del profesor").
3. De las **láminas**: la línea de tiempo de revelaciones, lámina por
   lámina, notas de orador incluidas.
4. **Cruzar**: para cada compromiso, ¿algo anterior lo responde?
   4b. **Cruce entre sesiones**: leer el apunte de la sesión ANTERIOR
   contra los compromisos de esta (patrón 6). Es el único paso que sale
   de la carpeta de la sesión.
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

---

## s07 — Prueba 1 + batidos · AUDITADA 2026-08-28, arreglos pendientes

### Hallazgo 1 (alta) — patrón 6: el apunte de s07 regala el descubrimiento de s08

`apunte_s07_batidos.md` es **público** (sitio y Canvas) y se lee entre
s07 y s08. Dice, textual:

> "en algún punto los batidos se vuelven demasiado rápidos para
> contarlos, la ondulación se convierte en una **aspereza**, y más allá,
> en algún momento, aparecen por fin ***dos notas*** distinguibles."

y lo repite en la síntesis ("aspereza, y luego dos notas").

s08 está diseñada exactamente para que eso lo descubran ellos: su
escucha del día premia "que distingan las etapas (ondulación → aspereza
→ dos notas)" y ordena al profesor **"NO da nombres técnicos todavía"**;
el taller les hace medir sus tres fronteras personales.

**Lo revelador**: el capítulo 7 —la lectura previa— protege el mismo
contenido con disciplina ejemplar:

> "¿Qué se oirá entonces? **No lo busque todavía**: lo va a oír en la
> sala, y lo que su oído le diga ahí es el punto de partida de la
> sesión 08."

O sea: el curso sabe redactar esto sin filtrar. El apunte simplemente no
siguió la misma disciplina.

**Arreglo**: reescribir los dos pasajes del apunte sin nombrar la
secuencia, replicando la fórmula del capítulo. No se toca s08.

### Hallazgo 2 (baja) — el plan y las láminas mandan frecuencias distintas

El plan manda contar con **f₂ = 442, 444 y 437 Hz** ("repite para 2, 4 y
3 Hz de diferencia"); las láminas y el apunte usan **443, 442 y 437**
("tres por segundo… con 442, dos; con 437, tres otra vez"). Si el
profesor sigue el plan y demuestra con 444, la lámina que revela el
resultado no calza con lo que se oyó.

**Arreglo**: unificar en **443/442/437**, que es lo que ya dicen dos de
las tres fuentes y además es mejor demostración — 443 y 437 son
simétricos respecto de 440 y ambos dan tres batidos, que es justo el
punto de "da lo mismo hacia qué lado".

### Lo que está bien

- El módulo 2 cuenta los batidos ANTES de mostrar el número; la regla
  llega después de contar.
- "El borde del fenómeno" se recoge sin explicar, con instrucción
  explícita al profesor de no adelantarlo.
- Sin contaminación cruzada con la Prueba 1 (verificado: "batido" no
  aparece en el enunciado ni en la pauta).
- El capítulo 7 es ejemplar protegiendo su propia sesión y la siguiente.

---

## s08 — Psicoacústica de la superposición · AUDITADA 2026-08-28

Sesión mayormente limpia: **un solo hallazgo**, de gravedad media y con
arreglo de una línea.

### Hallazgo 1 (media) — la predicción de F3 pide un número que se acaba de proyectar

La mini-lección vota y proyecta el orden de magnitud de la banda crítica
("~1/3 de octava; alrededor de 440 Hz, del orden de 100 Hz"). Dos
bloques después, `registro_mapa_del_choque.md` pide: *"Creo que la
aspereza desaparecerá del todo alrededor de Δf ≈ ___ semitonos"* — la
misma cantidad, en las mismas unidades, recién anotada en la pantalla.
Lo más probable es que devuelvan el número, no una predicción propia.

Lo que el plan quiere dejar abierto es la **variación personal**, no el
orden de magnitud (que el capítulo ya adelanta legítimamente).

**Arreglo**: convertir ese ítem de predicción absoluta a comparativa —
*"El curso dijo ~100 Hz, una tercera menor. ¿Su umbral será más ancho,
más angosto o igual? ¿Por qué?"*. Una línea en la hoja; no se tocan la
mini-lección ni la lámina. F1 y F2 no están contaminados.

### Lo que está bien y no hay que romper

- **La cadena s07→s08 está bien resuelta**: se verificó específicamente
  el patrón 5 y no aplica. El ticket de s07 se cobra una sola vez, en la
  escucha del día, y el profesor no da nombres técnicos hasta después.
- El taller de radiografía espectral predice contra el hito 1 del propio
  estudiante: imposible de filtrar desde clase.
- El gancho del módulo 2 vota antes de cualquier explicación; dos
  láminas retienen la respuesta con `. . .`.
- La devolución de la Prueba 1 está aislada de la escucha del día.
- El arranque de la serie del objeto (s08–s12) no adelanta resultados.

---

## s10 — Resonancia, impedancia y acoplamiento · AUDITADA 2026-08-28 · **LIMPIA**

Sin hallazgos. Los seis patrones se revisaron uno por uno y los tres
riesgos que se sospechaban a priori quedaron descartados con evidencia:

- La **demo de resonancia** es un oscilador forzado genérico (440 Hz,
  sin botella ni agua ni Helmholtz — verificado con grep sobre el
  archivo: la única coincidencia de "agua" es el nombre de la paleta en
  un comentario de CSS). Enseña pico, amortiguamiento y transiente: no
  la dirección en que cambia $f_0$ con el volumen de agua, que es lo que
  el taller pide predecir.
- La lámina que precede al taller plantea P1 y P2 como preguntas
  abiertas —"Predigan por escrito, ANTES de soplar nada"— sin revelar
  sube/baja. Verificado.
- La **lectura previa** (cap10) sí revela *quién* vibra al soplar (el
  aire) y al golpear (el vidrio), pero eso solo se pide en la §3 del
  taller, que es la síntesis POSTERIOR a medir. La dirección —lo único
  que se predice por escrito— queda deliberadamente sin responder ("No
  conteste rápido"), con la misma disciplina ejemplar de cap05 y cap07.
- **Patrón 6 en ambos sentidos**: el apunte de s09 nombra "resonancia"
  sin explicar el mecanismo (no contamina s10); el de s10 insinúa
  Helmholtz sin explicar stick-slip (no contamina s11).
- La **pauta de la clínica de pares** define "sugerencia medible" con un
  ejemplo dentro de la propia pauta: no exige un criterio que nadie
  entregó, ni lo da masticado.
- El **hito 2** pide compilar la radiografía espectral de s08 y el mapa
  de escala de s09, ambos declarados explícitamente como su insumo.

### Zona de riesgo (no es hallazgo)

Las notas de orador de la lámina del taller traen la respuesta "para
orientar sin regalarla" (al soplar $f_0$ sube; al golpear baja). Es
material solo-profesor —el CI borra las notas del deploy— y es el mismo
recurso que ya usa s03. Queda anotado solo como recordatorio de que esa
frase es para orientar preguntas, no para decirla en voz alta.

---

## s09 — Escalas y temperamentos · AUDITADA 2026-08-28

### Hallazgo 1 (alta) — **ARREGLADO 2026-08-28**: la demo se saboteaba a sí misma

`material/demos/demo_temperamentos.html`, bloque "¿Qué observar?"
—siempre visible, sin conmutador por modo— decía:

> "En modo afinar de oído (cents ocultos): … ¿Cayó cerca de **702**
> (justa)? En la Fase B … ¿ahora cae cerca de **700** (temperada)?"

La demo implementa correctamente el ocultamiento de los cents para que
las parejas afinen de oído y solo después vean dónde cayeron — y su
propio texto, en la misma pantalla del mismo notebook que usan durante
el turno, les entrega los dos números objetivo.

**Arreglado** (está fuera de `material/curso/`): el ítem ahora pide
anotar lo que marcaron y en qué dirección se movieron, sin números; se
agrega "los dos números salen al pizarrón recién en el cierre", que es
lo que el plan ya hace correctamente.

### Hallazgo 2 (media) — la mini-lección contesta el ítem 2 de la predicción

La mini-lección (10–25′) afirma "cada quinta se estrecha ~2 cents —
ninguna lisa, todas usables". La guía (25–62′) pide: *"El punto 'sin
batidos', ¿coincidirá con la quinta correcta (700 cents)? SÍ / NO,
porque ___"*. Ya está contestado.

**Arreglo propuesto**: reapuntar el ítem a la variación personal
—"¿su oído logrará distinguir la diferencia de 2 cents, o le sonarán
iguales?"— igual que el arreglo de s05 y s08. Los ítems 1 y 3 de esa
predicción quedan genuinamente abiertos y no se tocan.

### Lo que está bien

- El ocultamiento de cents está bien implementado en el código.
- El gancho del módulo 2 vota por escrito, escucha sin nombres y recién
  después revela.
- El apunte de s08 anuncia que "la aritmética va a decir que no" **sin
  dar** la coma ni 702 ni 700: patrón 6 limpio.
- El taller del objeto da la vara de medida sin adelantar el resultado
  de ningún objeto.

---

## s11 — Cuerdas frotadas y el cuerpo · AUDITADA 2026-08-28

### Hallazgo 1 (alta) — la P3 del taller pide predecir lo que la demo ya mostró

La lámina "Antes de ver la demo, prediga" y la demo de Helmholtz
(22–32′) muestran la forma de la cuerda frotada. Diez minutos después la
guía pide: *"Filmada en cámara lenta, la cuerda sonando se verá como:
□ curva suave que ondula · □ otra forma (dibújenla)"*, y luego
"¿Coincide con su P3?" como si siguiera abierta.

**Lo revelador**: el propio plan, en Riesgos, ya dice que "P3 se
contrasta contra la demo" — o sea, el diseño quería contraste y la guía
lo redactó como predicción ciega.

**Arreglo propuesto**: reformular P3 como contraste, no como adivinanza:
*"¿la cuerda real mostrará la esquina tan nítida como la demo
idealizada, o se verá borrosa? ¿por qué?"*.

### Hallazgo 2 (alta, con matiz) — la mini-lección contesta la P1 del taller

Verificado en pantalla: la mini-lección (8–22′) muestra, como contenido
visible, *"La resonancia del aire encerrado ayuda a radiar **los graves**
que la tapa, sola, no puede"*. El taller (22–48′) pide predecir:
*"Si tapamos las efes… □ se hunden sobre todo los **graves** · □ … los
agudos · □ no cambia nada"*. La alternativa correcta está en pantalla.

**Matiz que corrige a la auditoría**: la radiación direccional (la P3 de
ese taller) NO está en la lámina visible, sino solo en las notas de
orador, que el CI borra del deploy. Ahí el riesgo es que el profesor lo
diga en voz alta —la nota misma advierte que "es lo que la fase C pone a
prueba"—, no una filtración en pantalla. Mismo caso que la zona de
riesgo de s10.

**Arreglo propuesto**: sacar de la lámina la conclusión sobre las efes
(dejar solo la pregunta "¿para qué son?") y moverla a la síntesis del
cierre, después del taller.

### Lo que está bien

- `cap11` retiene la forma de Helmholtz ("No le vamos a dibujar aquí lo
  que Helmholtz vio"): otro capítulo disciplinado.
- El apunte de s10 no filtra s11 (patrón 6 limpio).
- El rearme de mesas aclara que objeto y bitácora siguen individuales.
- El gancho de la pinza en el puente vota antes de revelar.
- La P2 de ambos talleres queda genuinamente abierta.

---

## s13 — Prueba 2 + la voz cantada · AUDITADA 2026-08-28 · prácticamente limpia

Sin actividades escritas en el módulo 2 (es plenario por diseño), así
que el patrón 5 no aplica: no hay nada que duplicar.

### Hallazgo único (baja, con atenuantes)

`cap13` afirma como hecho narrado que "los pliegues fijan su frecuencia
solos… y el tracto se limita a filtrar". La lámina monta después una
votación sobre exactamente eso —"¿quién le pone el metrónomo a la
válvula?"— y la resuelve como **"respuesta sorpresa"**, como si fuera
hallazgo nuevo.

**Atenuantes reales**, por los que NO se trata como los hallazgos altos:
el plan declara explícitamente que esa mitad del capítulo está para
**consumirse** en la mini-lección, no para protegerse (a diferencia de
cap05, cap07 y cap10); no hay registro escrito que la votación
contradiga; y es una votación informal, sin nota.

**Arreglo propuesto (opcional)**: cambiar "respuesta sorpresa" por
"¿se lo esperaban después de leer el capítulo?" — convierte la votación
en verificación de lectura en vez de fingir descubrimiento.

### Lo que está bien

- El bloque "¿Qué observar?" de `demo_formantes_voz.html` es
  **enteramente preguntas abiertas**, sin un solo número ni respuesta —
  verificado viñeta por viñeta. Es el contraejemplo exacto del defecto
  de s09.
- El ocultamiento de F1/F2 en el juego está bien implementado en el
  código.
- `cap13` protege el susurro y las sopranos: cierra con "Preguntas que
  la sesión va a responder", sin resolverlas.
- Patrón 6 limpio en ambos sentidos: el apunte de s12 plantea el ticket
  hacia s13 sin responderlo, y el de s13 hace lo mismo hacia s14.
- Sin contaminación cruzada con la Prueba 2 (grep: cero coincidencias de
  vocabulario de voz en el enunciado y la pauta).
- Las votaciones dejan la respuesta solo en notas de orador.

---

## s14 — La sala como instrumento · AUDITADA 2026-08-28

### Hallazgo 1 (alta) — la hoja de ruta trae impresa la respuesta del ranking

`actividades/rutas_salida_medicion.md` tiene, en la tabla de cada ruta,
una columna **"Tipo esperado"** que rotula cada espacio: *seco*, *vivo*,
*muy seco*. Y la guía declara en sus materiales por grupo: "…lápiz, **la
ruta asignada**". O sea, el grupo tiene esa hoja en la mano cuando la
guía le pide:

> "Ranking esperado de los espacios de nuestra ruta, de MÁS a MENOS
> reverberante: 1.º ___ 2.º ___ 3.º ___ · ¿Por qué?"

La columna es literalmente esa respuesta, ya impresa.

**Arreglo propuesto**: imprimir para los estudiantes una versión de la
hoja de ruta **sin** la columna "Tipo esperado", y conservarla solo en
la plantilla de planificación del profesor.

### Hallazgo 2 (alta) — se pide "estimar" algo que se acaba de medir delante de ellos

El plan hace que el profesor demuestre completo en la sala de clases
—globo, caída, **lectura del valor**— y recién después el grupo escribe.
La guía pide:

> "$T_{60}$ estimado de la SALA DE CLASES (**la acabamos de oír con el
> globo del profesor**): ___ s"

El propio texto admite que el valor ya se mostró: eso no es predicción,
es memoria.

**Arreglo propuesto**: mover ese ítem ANTES de la demostración modelo
(que escriban su estimación y después el profesor mida), o eliminarlo y
dejar solo el ranking de la ruta, que sí es genuino.

### Hallazgo 3 (baja, técnico) — **ARREGLADO 2026-08-28**

`demo_modos_sala.html` cargaba con `<input … id="chkRevelar" checked>`,
es decir **con la curva revelada**, mientras la lámina "Prediga, antes
de mover nada" dice explícitamente "con la curva **oculta**". Si el
profesor proyectaba sin acordarse de desmarcar, la demo se spoileaba
sola al abrir.

**Arreglado** (fuera de `material/curso/`): se quitó `checked`, de modo
que el estado inicial coincide con lo que la lámina asume.

### Lo que está bien

- El bloque "¿Qué observar?" de la demo está bien construido: predecir,
  barrer, revelar recién al final.
- `cap14` es ejemplar: declara que no revela espacios ni valores porque
  "eso arruinaría la mejor parte".
- Las votaciones "¿hormigón o cortina?" y "¿cae igual en la sala que en
  la cancha?" retienen la respuesta con `. . .`.
- Patrón 6 limpio: el apunte de s13 plantea la pregunta hacia s14 sin
  resolverla.
- No se siembra ticket hacia s15: decisión explícita y correcta.
- La pauta del hito 3 referencia contenidos que s08–s12 sí entregaron.

---

## s12 — Vientos y lutería · AUDITADA 2026-08-28

### Hallazgo único (alta) — la lámina revienta el secreto que el capítulo pidió guardar

La lectura previa, `cap12`, protege el salto de registro del tubo tapado
con la disciplina más explícita de todo el curso:

> "¿Y en un tubo tapado, donde los modos pares no existen? … **No se lo
> vamos a decir**: dedúzcalo de la serie impar, escríbalo, y en el
> taller lo va a soplar usted mismo (los clarinetistas del curso ya lo
> saben; **que guarden el secreto** y verifiquen)."

Y la lámina "Dos tubos, dos registros" (contenido visible, no notas),
antes del taller, proyecta la tabla:

> "Al soplar más fuerte, salta a… | la **octava** (flauta) | la
> **docena** (clarinete, tubo tapado) |"

La mini-lección del plan repite la misma frase. Eso contesta la Fase B
de la guía —*"la nota saltará al intervalo ___, porque los modos
disponibles son ___"*— y también la Fase C.

**Arreglo propuesto**: en la mini-lección y en la tabla, resolver solo
el caso **abierto** (que es lo necesario para cerrar la escucha del día
con la flauta) y dejar el caso **tapado** como pregunta abierta, tal
como ya hace el capítulo 12.

### Lo que está bien

- La escucha del día es íntegramente auditiva, con flauta en vivo y sin
  pantalla.
- El "¿Qué observar?" de `demo_tubo_agujeros.html` está fraseado como
  pregunta ("¿octava o docena?"), sin dar la respuesta: el riesgo nuevo
  de las demos no se materializa aquí.
- La Fase D (por qué los tubos salieron sistemáticamente bajos) está
  protegida: el profesor "NO explica todavía" y el plenario que la
  resuelve va después de que cada grupo la redactó.
- Patrón 6 limpio: el apunte de s11 deja "¿qué hace de válvula?"
  abierto.
- `pauta_revision_bitacoras.md` no exige nada que no se haya anunciado
  en s10 y s11.
