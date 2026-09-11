# Guion del profesor — Estaciones de medición de niveles (s06, módulo 2)

**Solo profesor** (excluido del sitio y de Canvas por el patrón
`guion_profesor*`). Complementa la guía de los estudiantes
(`actividades/guia_estaciones_niveles.md`) y la fila 15–55′ del módulo 2
del plan. Una página: montaje, orden de los bloques, tu rol y qué
provocar en cada uno.

**Por qué en serie (2026-09-11)**: las estaciones que emiten y miden no
pueden correr en paralelo en una sala; la app integra todo lo que suena.
Cinco bloques de 8′, uno tras otro, con los 9 celulares midiendo el mismo
evento. Ganancia colateral: la dispersión entre apps aparece de inmediato.

## Montaje antes de que entren (15 min)

| Bloque | Dónde | Qué dejar listo |
|---|---|---|
| E1 referencia fina | al frente | MOTU con phantom 48 V; AT3035 en pie a altura de boca, filtro 80 Hz ON, pad OFF; REW → SPL Meter (A, Slow, Logger) calibrado contra el iPhone con ruido rosa; ganancia fijada y NO se toca más; cinta en el suelo a 30 cm y 3 m frente al micrófono; una mesita junto al micrófono para poner los 9 celulares en fila; pantalla de REW proyectada |
| E3 dos fuentes | mesa del frente | dos celulares tuyos (o celular + notebook) con el MISMO tono al MISMO volumen, probados parejos; anillo de cinta a ~1 m alrededor de la mesa |
| E2 mapa de la sala | toda la sala | 4 puntos marcados con cinta y numerados (junto al equipo, centro, rincón trasero, junto a la puerta); la fuente es uno de los celulares de E3, fijo al frente |
| E5 dosis | mesas | guía impresa (tabla NIOSH); un voluntario con audífonos avisado de antemano |
| E4 aritmética | mesas | guía impresa; calculadora del celular |
| Común | proyector | cronómetro de 8′; lámina con el orden E1 → E3 → E2 → E5 → E4; tu celular con la app SPL de la lista de apps |

## Orden y tu rol en cada bloque (15–55′)

Diriges desde el frente, con el cronómetro. A los 8′ se pasa al siguiente
con lo que haya; el mínimo por bloque es el ítem ★ de la guía: un dato
anotado CON condiciones (app, celular, distancia). Los roles del grupo
rotan en cada bloque. Antes de cada medición: "¿está escrita la
predicción?".

**1. E1 — La referencia fina (15–23′).** Sala en silencio. Los 9 celulares
en fila junto al AT3035, apps abiertas en dB(A). Un voluntario hace
"aaah" mezzoforte de frente al micrófono, a 30 cm; tú lees el Leq de REW
en voz alta y cada uno anota la referencia y su app. Repiten a 3 m, de
frente (si se corre 45°, pierde dB por ángulo, no por distancia). Nadie
toca la ganancia. Provocación: "¿difieren en el valor, pero coinciden en
cuánto cayó?". Honestidad si preguntan: la referencia está calibrada
contra un celular; lo fino es el micrófono, la ganancia fija y el
promedio, no el número absoluto.

**2. E3 — ¿Dos fuentes = el doble? (23–31′).** Todos de pie en el anillo
de 1 m, apps abiertas. Enciendes A solo, luego B solo (comprueban que
den parejos), luego A+B. Provocación: "¿por qué NO dio +6?" y "¿cuántos
celulares harían falta para el doble de fuerte?". Si alguien obtiene +6
o más, que revise si estaba pegado a una de las dos fuentes. No cobres
el gancho todavía: se cobra en la puesta en común.

**3. E2 — El mapa de la sala (31–39′).** Dejas A sonando fijo al frente,
sin mover ni cambiar volumen. Los 3 grupos recorren en silencio los 4
puntos y miden con el mismo celular en los 4. Provocación al pasar:
"¿dónde ensayaría un violinista que quiere cuidarse el oído?".

**4. E5 — La dosis del oído (39–47′).** Dos casos como curso: "la
banda", todos cantan una nota sostenida 15 s mientras miden a ~1 m de
las bocas; "los audífonos en la micro", el voluntario presta sus
audífonos al volumen que usa y cada mesa mide pegada al auricular (es
silencioso, va en paralelo). Luego la tabla NIOSH en la mesa.
Provocación: "¿cuántos dB le baja un protector, y cuánto tiempo le
compra?" (15 dB = cinco pasos de 3 dB = ×32 de tiempo admisible).
Exige la decisión práctica anotada.

**5. E4 — Aritmética del decibel (47–55′).** Papel, en las mesas, con
los datos propios que ya tienen todos. Pasas por las mesas.
Provocación: "+3 dB es ×2 en intensidad: ¿y en qué tan fuerte se oye?".

## Puesta en común (55–60′) y cierre (60–70′)

Planilla proyectada con tres columnas: E1 diferencia app↔referencia (y
la dispersión entre los 9 celulares); E3 cuánto dio la suma; E2 punto
más ruidoso. Cobras el gancho de las palmas: duplicar fuentes ≈ +3 dB; el
doble de fuerte pide ≈ +10 dB, unas diez fuentes. Remate: comparaciones
con el mismo aparato son confiables, los absolutos sin calibrar no.
Luego formulario de 4 casillas al dorso de la planilla + ticket hacia
s07 mientras anuncias la Prueba 1. Recoges planillas, hojas isofónicas
del m1 y tickets; rúbrica rápida y nota del taller en Canvas hoy (tarea
`taller-06`).

## Plan B

- MOTU no aparece en REW → entrada "iPhone de Patricio Microphone" por
  Continuidad, calibrada con la app NIOSH del mismo teléfono; se pierde
  el AT3035, no el bloque.
- Un estudiante sin app → comparte celular con un compañero de mesa;
  el grupo sigue teniendo ≥2 lecturas por evento.
- Lecturas dispares entre celulares (±10 dB) → es dato, no fracaso: va a
  la casilla "límite" del mini-informe y a la puesta en común.
- El voluntario de los audífonos no aparece → "la banda" basta como caso
  medido; el otro se estima con la tabla y se declara como estimado.
