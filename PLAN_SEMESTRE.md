# Estructura del curso — 15 sesiones

Fase 3 del diseño — versión de trabajo generada en el loop autónomo
(2026-07-12). Mapa de sesiones: cada sesión indica tema, objetivos que
cubre (códigos de `OBJETIVOS_APRENDIZAJE.md`), dependencias
conceptuales e hitos de evaluación. **Este mapa gobierna el desarrollo
sesión por sesión (fase 4).**

## Lógica de la progresión

Se adopta la secuencia didáctica de Benade (1990, sec. 1.2) — del sonido
impulsivo al sostenido, de la física a la percepción, y de los principios
a los instrumentos — cruzada con las restricciones del calendario de
evaluación de `METODOLOGIA.md`, sección 4:

1. **Bloque A (s01–s04): el sonido como objeto físico.** Vibración,
   ondas, modos, espectro. Herramientas de medición desde la semana 2
   (el espectrograma como "microscopio" del curso).
2. **Bloque B (s05–s09): el sonido percibido.** Altura, sonoridad,
   batidos, consonancia, escalas. Aquí vive el núcleo psicoacústico
   (ROE) y la prueba 1 (s07).
3. **Bloque C (s10–s13): los instrumentos como sistemas.** Resonancia e
   impedancia como puente, luego familias por mecanismo de excitación:
   frotada (s11), soplada (s12, sesión de lutería), cantada (s13). La
   excitación impulsiva quedó cubierta en el bloque A (s03–s04).
4. **Bloque D (s14–s15): la sala y la síntesis final.** Acústica de
   salas con salida de medición (s14) y presentaciones del proyecto
   (s15).

El proyecto (OA5) corre en paralelo desde s03; los talleres de medición
de s08–s12 usan el objeto del proyecto de cada grupo (regla de la
metodología, sección 4).

## Mapa de las 15 sesiones

| Sesión | Tema | Objetivos (OA) | Depende de | Hitos / formatos especiales | Demo principal |
|--------|------|----------------|------------|------------------------------|----------------|
| s01 | Escuchar como científico: del golpe al tono (sonido impulsivo, repetición, frecuencia y altura) | OA3.1 (se instala), OA1.1 (intro), OA2.1 (intro) | — | Formación de 5 grupos estables; presentación de la rúbrica OA3; línea base de escucha (sin nota) | `material/demos/demo_tren_pulsos.html` |
| s02 | Ondas y representación: forma de onda, espectro y espectrograma; propagación y velocidad del sonido | OA4.1, OA1.1 | s01 (frecuencia/altura) | Alfabetización digital (material propio); primer uso de apps de análisis en celular | `material/demos/demo_forma_onda_espectro.html` (micrófono en vivo) |
| s03 | Modos de vibración: por qué cada objeto suena como suena (frecuencias características, modos 1D y 2D, decaimiento) | OA1.1, OA1.2, OA5.1 (intro) | s02 (espectro) | **Lanzamiento del proyecto** (grupos = grupos de proyecto) | `material/demos/demo_modos_cuerda.html` |
| s04 | La receta del timbre: cuerda pulsada, punto de excitación, síntesis aditiva | OA1.1, OA1.2, OA2.1 | s03 (modos) | Instrumentos de estudiantes #1 (cuerdas pulsadas; avisar en s03) | `material/demos/demo_sintesis_aditiva.html` |
| s05 | La altura percibida: fundamental ausente, reconocimiento de patrones, el oído en una pasada | OA2.1, OA2.2 | s04 (parciales, espectro) | **Hito 1 del proyecto** (diseño con predicción, 8%); punto de control metodológico (ronda oral y lectura previa) | `material/demos/demo_fundamental_ausente.html` |
| s06 | Sonoridad y decibel: intensidad, niveles, isofónicas; medir lo fuerte | OA2.1, OA4.2 | s02 (ondas), s05 (percepción no lineal) | Estaciones de medición de niveles (formato 5); mini-informe SPL | `material/demos/demo_decibel_sonoridad.html` |
| s07 | **Prueba 1** (módulo 1) + audición liviana: batidos, primera escucha (módulo 2) | evalúa OA1.1–1.2, OA2.1–2.2, OA4.1–4.2; siembra OA2.2 | s01–s06 | Prueba 1 (módulo 1 completo); módulo 2 liviano por regla de metodología §3 | `material/demos/demo_batidos.html` |
| s08 | Psicoacústica de la superposición: batidos, banda crítica, rugosidad y consonancia | OA2.2, OA2.3, OA5.2 | s07 m2 (batidos oídos) | Taller psicoacústico con registro individual; **comienzan talleres de medición sobre el objeto del proyecto (s08–s12)** | `material/demos/demo_banda_critica.html` |
| s09 | Escalas y temperamentos: afinar de oído (batidos como herramienta) | OA2.3, OA1.2 | s08 (batidos, consonancia) | Actividad de afinación por conteo de batidos (BEN 16.2) | `material/demos/demo_temperamentos.html` |
| s10 | Resonancia, impedancia y acoplamiento: el puente hacia los instrumentos; panorama de mecanismos de excitación | OA1.2, OA1.3, OA5.2, OA3.2 | s03 (modos), s06 (energía/niveles) | **Hito 2 del proyecto** (avance, 8%); clínica de proyecto (formato 6) en módulo 2; revisar coevaluaciones | `material/demos/demo_resonancia.html` |
| s11 | Cuerdas frotadas y el cuerpo del instrumento: stick-slip, movimiento de Helmholtz, puente, caja y radiación | OA1.3, OA1.1, OA1.2 | s10 (resonancia, régimen de oscilación) | Instrumentos de estudiantes #2 (cuerdas frotadas; avisar en s10) | `material/demos/demo_helmholtz.html` |
| s12 | Vientos y lutería: columnas de aire, agujeros, regímenes; construcción y medición de flautas/tubos | OA1.2, OA1.3, OA5.2 | s10 (resonancia, impedancia) | **Sesión-taller completa de lutería (formato 9, 140 min)**; flautas del profesor como caso | `material/demos/demo_tubo_agujeros.html` |
| s13 | **Prueba 2** (módulo 1) + la voz cantada: fuente-filtro y formantes en audición liviana (módulo 2) | evalúa OA1.2–1.3, OA2.2–2.3; OA1.3 (voz) | s08–s12 | Prueba 2 (módulo 1); módulo 2 liviano por regla de metodología §3 | `material/demos/demo_formantes_voz.html` |
| s14 | La sala como instrumento: reflexión, absorción, reverberación, modos de sala; salida de medición de RT | OA1.4, OA4.3, OA3.2 | s03 (modos), s06 (dB), s10 (resonancia) | **Salida de medición (formato 8)** en módulo 2; puesta en común comprimida al cierre de la propia salida (ver decisión D3) | `material/demos/demo_modos_sala.html` |
| s15 | Presentaciones finales del proyecto: explicar es la prueba | OA5.3, OA3.2 | todo el curso | **Presentación final + informe (14%)**; ambos módulos; ~25 min por grupo, preguntas individuales | — (sin demo nueva) |

## Verificación de cobertura de OA

- **OA1.1** s01–s04, s11 · **OA1.2** s03, s04, s09, s10, s12 · **OA1.3**
  s10–s13 (mecanismos: impulsivo s03–s04, frotado s11, soplado s12,
  cantado s13) · **OA1.4** s14.
- **OA2.1** s01, s04–s06 · **OA2.2** s05, s07(m2), s08 · **OA2.3** s08, s09.
- **OA3.1–3.2** transversal: escucha del día en todas las sesiones
  s02–s14; línea base en s01; OA3.2 explícito en clínicas (s10) y
  defensa final (s15).
- **OA4.1** s02 y transversal (espectrogramas en talleres) · **OA4.2**
  s06 · **OA4.3** s14.
- **OA5.1** s03, s05 (hito 1) · **OA5.2** s08–s12 (talleres de medición
  sobre el objeto + lutería) · **OA5.3** s15.

Ningún OA queda sin sesión; ninguna sesión queda sin OA.

## Calendario de evaluación (fijado por METODOLOGIA.md §4)

s01 línea base sin nota · s03 lanzamiento proyecto · s05 hito 1 (8%) ·
s07 prueba 1 (12,5%) · s08–s12 talleres de medición = avance de proyecto ·
s10 hito 2 (8%) · s13 prueba 2 (12,5%) · s15 presentación final + informe
(14%). Ronda oral de escucha (20%) corre de s02 a s14. Talleres (25%):
cuentan las mejores 8 de ~10 guías.

## Notación y convenciones del curso

Definidas una vez aquí; todo apunte, demo y evaluación las respeta.

| Símbolo | Magnitud | Unidad SI |
|---|---|---|
| $f$ | frecuencia | Hz |
| $T = 1/f$ | período | s |
| $\lambda$ | longitud de onda | m |
| $v$ | velocidad del sonido en el aire | m/s (≈ 343 m/s a 20 °C) |
| $A$ | amplitud | según la magnitud |
| $p$ | presión sonora | Pa |
| $L_p$ | nivel de presión sonora | dB (ref. 20 µPa) |
| $f_1$ | frecuencia fundamental | Hz |
| $f_n$ | frecuencia del parcial $n$ (armónico si $f_n = n f_1$) | Hz |
| $T_{60}$ | tiempo de reverberación | s |
| $L$ | longitud (cuerda, tubo) | m |
| $\mu$ | densidad lineal de una cuerda | kg/m |
| $F_T$ | tensión de una cuerda | N |

- **Relación fundamental**: $v = \lambda f$ (se introduce en s02 y se
  reutiliza en todo el curso).
- **Afinación de referencia**: La4 = 440 Hz, temperamento igual salvo
  cuando el tema sea afinación histórica (s09).
- **Octavas**: notación científico-latina — Do4 es el Do central del
  piano, La4 = 440 Hz. Se presenta la equivalencia anglosajona (C4, A4)
  una sola vez en s01 porque las apps de análisis la usan.
- **"Parcial" vs. "armónico"**: parcial es cualquier componente del
  espectro; armónico es un parcial en razón entera con la fundamental.
  La distinción se instala en s03 (objetos inarmónicos) y es vocabulario
  obligatorio de la rúbrica OA3.
- **Decibel**: siempre indicar la referencia (dB SPL re 20 µPa; dB
  relativos en espectros). Ponderación A se nombra en s06 (las apps la
  usan) sin desarrollar teoría de filtros.

## Decisiones de estructura (registradas para ESTADO_LOOP.md)

- **D1 — Progresión Benade**: se ordena el semestre impulsivo→sostenido→
  percepción→instrumentos→salas (BEN 1.2) en lugar del orden 2019.
- **D2 — La voz en módulo liviano (s13)**: con 15 sesiones no alcanza una
  sesión completa para la voz; se cubre OA1.3 (excitación cantada) como
  audición activa post-prueba. Es el sacrificio de contenido más visible
  del diseño.
- **D3 — Salida de medición en s14**: el formato 8 pide puesta en común
  "la sesión siguiente", pero s15 está completa con presentaciones. Se
  comprime la puesta en común a los últimos 15 min de la propia salida
  (planilla compartida) y el informe comparativo (OA4.3) cierra como
  taller evaluado.
- **D4 — Percusión sin sesión propia**: membranas, barras y placas se
  tratan como caso principal de s03 (modos 2D, sartén de BEN 4) y
  reaparecen en la prueba 1; no hay sesión dedicada.
- **D5 — Electroacústica y audio digital fuera del programa**: coherente
  con el alcance declarado en OBJETIVOS_APRENDIZAJE.md ("fuera del alcance"); solo la
  alfabetización digital instrumental de s02 (muestreo mínimo para leer
  espectrogramas).
