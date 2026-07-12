---
name: demo-interactiva
description: Construye una demo interactiva HTML autocontenida (con audio Web Audio API y visualización) para el curso de Acústica Musical. Usar cuando el usuario pida crear, construir o mejorar una demo, simulación, visualización o applet interactivo de un concepto acústico o musical.
---

Construir una demo interactiva sobre: $ARGUMENTS

## Pasos

1. Leer `.claude/rules/formato-demos.md` y respetar todas sus convenciones
   (archivo único, estética editorial, audio con Web Audio API, bloque
   "¿Qué observar?").
2. Identificar en `sesiones/` a qué sesión pertenece la demo; si no está
   claro, preguntar antes de asumir. Revisar el `plan.md` de esa sesión
   para alinear la demo con la actividad donde se usará.
3. Definir el concepto único que ilustra la demo y los 2-4 parámetros que
   el estudiante podrá manipular. Si el concepto requiere más de eso,
   proponer dividir en dos demos.
4. Implementar el HTML autocontenido en `sesiones/sXX/demos/`.
5. Verificar mentalmente los casos límite de los controles (valores
   extremos de sliders, audio detenido/iniciado, redimensionar ventana) y
   corregir antes de entregar.
6. Reportar al final: ruta del archivo, parámetros manipulables, y las
   preguntas guía incluidas en "¿Qué observar?".

## Notas técnicas frecuentes

- AudioContext debe crearse o reanudarse solo tras un click del usuario.
- Siempre incluir botón de detener sonido y limitar la ganancia
  (protección auditiva en sala de clases: gain <= 0.5 por defecto).
- Para espectros usar FFT del AnalyserNode; rotular ejes en Hz y dB.
- Frecuencias musicales de referencia: La4 = 440 Hz, temperamento igual
  salvo que la demo trate justamente de afinación histórica.
