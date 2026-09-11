---
title: "s06 · Módulo 2 — Estaciones de medición en serie · guion de clase del profesor"
subtitle: "vie 11-sep-2026 · solo profesor · llevar impreso"
---

## 0. Antes de que entren (15 min) — lista de chequeo

**E1, referencia (al frente)**

- [ ] MOTU conectada, phantom 48 V encendido, AT3035 en pie a altura de boca, de frente a la sala. Filtro 80 Hz ON, pad OFF.
- [ ] REW abierto → Preferencias → Soundcard: entrada = MOTU, canal del micrófono, 48 kHz. Salida = equipo de la sala.
- [ ] SPL Meter: ponderación **A**, respuesta **Slow**, pestaña **Logger** lista. Botón rojo para medir.
- [ ] Calibración: Generator → ruido rosa por el equipo de la sala, volumen medio. iPhone con app NIOSH (dB(A)) junto al micrófono a 1 m. SPL Meter → **Calibrate** → escribir la lectura del iPhone. Apagar el generador.
- [ ] Prueba: "aaah" a 30 cm ≈ nivel de entrada −20 dBFS, sin rojo. **Fijar la ganancia y no tocarla más.** Anotar aquí: 30 cm = ______ dB(A) · 3 m = ______ dB(A) · sala vacía = ______ dB(A).
- [ ] Cinta en el suelo a **30 cm** y a **3 m** frente al micrófono; mesita junto al micrófono para poner los 9 celulares en fila; pantalla de REW proyectada.
- [ ] Plan B si la MOTU no aparece: entrada "iPhone de Patricio Microphone" (Continuidad), calibrada con NIOSH del mismo teléfono.

**E3 y E2, fuentes (mesa del frente)**

- [ ] Dos celulares tuyos (o celular + notebook) con **la misma señal de RUIDO ROSA** (no un tono puro: dos tonos iguales son coherentes y en cada punto suman entre 0 y +6 dB según la fase; con ruido la suma es incoherente y da +3 limpios; el tono puro además excita los modos de la sala y arruina el mapa de E2). Probar que A y B den parejos en la app (±1 dB).
- [ ] Anillo de cinta a ~1 m alrededor de la mesa del frente (E3).
- [ ] 4 puntos de E2 marcados y numerados: ① junto al equipo · ② centro · ③ rincón trasero · ④ junto a la puerta.
- [ ] **Anunciar en voz alta al presentar la logística**: "las fuentes emiten ruido, no un tono; la guía dice tono, hoy usamos ruido".

**Común**

- [ ] Cronómetro de 8′ proyectado. Lámina del orden **E1 → E3 → E2 → E5 → E4** (está en el deck).
- [ ] Tu celular con la app SPL de la lista, para el gancho de las palmas.
- [ ] Voluntario de los audífonos avisado (E5). Voluntario para la voz de E1 elegido.
- [ ] Guías impresas (1 por grupo, versión "en serie"), hojas isofónicas (1 por estudiante), 9 entregas corregidas del hito 1.

## 1. Gancho (0–8′): ¿cuatro palmas son cuatro veces más fuerte?

Un voluntario aplaude sostenido; tu app mide, **no muestres el número**. Votación a mano alzada ANTES de los cuatro: ¿+3, +6 o +12 dB? Aplauden los cuatro. Guardas la lectura: "queda en suspenso hasta E3". *Lo que debería dar*: cuatro fuentes incoherentes ≈ **+6 dB**. La mayoría votará +12 (o "el cuádruple").

## 2. Logística (8–15′)

Pregunta de la semana: "¿qué tan fuerte es nuestro mundo musical, y cómo se mide con juicio?". Lámina de los 5 bloques. Reglas: **8′ por bloque, en serie, todos miden el mismo evento con su app**; roles (ejecuta / mide y registra / vocero) rotan por bloque; **silencio absoluto durante E1, E3 y E2**; predicción escrita ANTES de medir; el mínimo por bloque es el ítem ★. Dudas de procedimiento ahora. Recordatorio: apps en **dB(A)**.

## 3. Los cinco bloques (15–55′): qué hacer, qué esperar, qué puede fallar

### Bloque 1 — E1 · La referencia fina (15–23′)

**Hacer**: los 9 celulares en fila junto al AT3035, apps abiertas. Voluntario de frente al micrófono, "aaah" mezzoforte a 30 cm, 5 s. Lees el **Leq** de REW en voz alta; cada uno anota referencia y su app. Repetir a 3 m, **de frente** (a 45° pierde dB por ángulo, no por distancia). Nadie toca la ganancia.

**Esperar**: 30 cm ≈ 70–75 dB(A). Caída a 3 m ≈ **10–15 dB** (en campo libre serían 20; la reverberación de la sala aplana). Los celulares discrepan en el absoluto (±5 dB Android, ±2 iPhone/NIOSH) pero **coinciden en la caída** dentro de 2–3 dB.

**Provocar**: "¿difieren en el valor, pero coinciden en cuánto cayó?". El celular que muestra una caída mucho menor tiene control automático de ganancia: **es el mejor dato del bloque**, no un error; nómbralo.

**Honestidad**: la referencia está calibrada contra un celular; lo "fino" es el micrófono, la ganancia fija y el promedio Leq, no el número absoluto.

### Bloque 2 — E3 · ¿Dos fuentes = el doble? (23–31′)

**Hacer**: todos de pie en el anillo de 1 m. Enciendes A (ruido) solo → miden; B solo → miden (¿parejos?); A+B → miden. Cada uno anota los tres.

**Esperar**: A ≈ B dentro de 1 dB; **A+B = +2,5 a +3,5 dB**. Si alguien obtiene +5 o más: estaba pegado a una de las fuentes o las fuentes no eran parejas. Si obtienes dispersión grande (0 a +6): las fuentes están emitiendo tono puro y no ruido → cambia a ruido y repite (2′).

**Provocar**: "¿por qué NO dio +6?", "¿cuántos celulares harían falta para el doble de fuerte?" (respuesta: +10 dB ≈ diez celulares). **No cobrar el gancho todavía.**

### Bloque 3 — E2 · El mapa de la sala (31–39′)

**Hacer**: dejas A (ruido) sonando fijo al frente, sin mover ni cambiar volumen. Los 3 grupos recorren **en silencio** los puntos ① a ④, midiendo con el **mismo celular del grupo** en los 4. Anotan el mapa.

**Esperar**: el punto ① (junto al equipo) claramente más ruidoso; ②, ③ y ④ bastante parejos, 5–8 dB por debajo: pasado 1–2 m manda el campo reverberante y el nivel se aplana. Puede haber un rincón un poco más alto por los graves.

**Provocar**: "¿dónde ensayaría un violinista que quiere cuidarse el oído?" → lejos de la fuente; y después de cierta distancia da casi lo mismo dónde.

### Bloque 4 — E5 · La dosis del oído (39–47′)

**Hacer**: caso 1, "la banda": todos cantan una nota sostenida 15 s mientras el registrador de cada grupo mide a ~1 m de las bocas. Caso 2, "los audífonos en la micro": el voluntario presta sus audífonos al volumen que usa; cada mesa mide pegada al auricular (silencioso, en paralelo). Luego tabla NIOSH en la mesa; una decisión práctica anotada.

**Esperar**: la banda ≈ **80–85 dB(A)** → en el límite de las 8 h admisibles. Los audífonos medidos desde afuera dan un número poco fiable y más bien bajo: **eso es lección** (el nivel en el tímpano no se mide así) y va a la casilla "límite".

**Provocar**: "¿cuántos dB le baja un protector, y cuánto tiempo le compra?" → 15 dB = cinco pasos de 3 dB = **×32** el tiempo admisible.

### Bloque 5 — E4 · Aritmética del decibel (47–55′)

**Hacer**: papel, en las mesas, con sus propios datos. Pasas por las mesas.

**Esperar**: diferencia de E2 (6–8 dB) ≈ **×4 a ×6** en intensidad; +3 de E3 = **×2**; discrepancia de E1 (p. ej. 5 dB) ≈ ×3; "la mitad de fuerte" = **−10 dB = 1/10 de la energía**. Error típico: **sumar en vez de multiplicar**.

**Provocar**: "+3 dB es ×2 en intensidad: ¿y en qué tan fuerte se oye?" → apenas se nota.

## 4. Puesta en común (55–60′)

Planilla proyectada, tres columnas; un dato por vocero, sin discurso:

| Grupo | E1: app − referencia (30 cm) y dispersión entre celulares | E3: A+B − A | E2: punto más ruidoso |
|---|---|---|---|
| G1 | | | |
| G2 | | | |
| G3 | | | |

**Cobrar el gancho**: las palmas dieron ______ dB (≈ +6 por cuatro fuentes); los celulares ≈ +3 por duplicar. **Moraleja**: duplicar fuentes ≈ +3 dB; el doble de fuerte pide ≈ +10 dB, unas diez fuentes (por eso duplicar la orquesta no duplica lo fuerte, Benade cap. 13). **Remate**: comparaciones con el mismo aparato son confiables; los absolutos sin calibrar, no.

## 5. Cierre (60–70′)

Formulario de 4 casillas al dorso de la planilla (pregunta / dato / interpretación / límite), sin prosa. Ticket hacia s07 mientras anuncias: **Prueba 1 en s07** (módulo 1 completo; entra s01–s06, lo de s06 solo básico; con audio); el módulo 2 de s07 será audición liviana donde el ticket de hoy se responde con los oídos. Recoges: planillas con formulario, hojas isofónicas del m1, tickets.

**Después de clase**: rúbrica rápida (logrado / parcial / incipiente: dato con unidad, condiciones, regla +10/+3 bien usada, un límite declarado) y nota del taller en Canvas (tarea `taller-06` de la agenda).

## 6. Plan B rápido

- **MOTU no aparece** → micrófono del iPhone por Continuidad + calibración NIOSH; se pierde el AT3035, no el bloque.
- **Estudiante sin app** → comparte celular en la mesa; ≥2 lecturas por evento igual.
- **Lecturas dispares (±10 dB)** → es dato: a la casilla "límite" y a la puesta en común.
- **E3 con dispersión rara** → las fuentes están en tono puro: cambiar a ruido.
- **Sala muy ruidosa a 3 m** (voz apenas sobre el fondo) → acortar a 2 m y decirlo; la caída sigue siendo el dato.
- **Un bloque se alarga** → a los 8′ se pasa con lo que haya; el ★ basta.
