# Calendario 2026-2 — MUC860 Acústica Musical (solo profesor)

Instancia el mapa de 15 sesiones (`PLAN_SEMESTRE.md`) con
las fechas reales del segundo semestre 2026. Fuente de las restricciones:
`../../SyS/ediciones/2026/PLAN_2026-2.md` (que a su vez cita el calendario
oficial de Dirección Académica, `fechas-importantes-2026-2.pdf`).

**Horario del curso**: viernes, dos módulos seguidos — **14:50–16:00 y
16:10–17:20** (10 min de descanso).

## Restricciones del calendario oficial usadas

- Inicio de clases: mié 05-ago-2026 → primer viernes: **07-ago**.
- Fin de clases: **vie 27-nov-2026** (tope).
- Receso de docencia: lun 14 a sáb 19-sep → **el vie 18-sep no hay clase**.
- Evaluaciones suspendidas: 14 a 21-sep inclusive (no afecta ningún
  viernes de clase: el 18-sep ya cae en receso).
- **Semana universitaria: 17–22-ago — sin evaluaciones** (clases
  normales). Afecta al **vie 21-ago = s03** (ver flag F1).
- **Vie 02-oct: actividades suspendidas desde las 13:30** — a SyS
  (ayudantía 11:00) no lo afectó, pero AM parte a las 14:50: **ese
  viernes NO hay clase de AM**.
- Feriado lun 12-oct: no afecta (es lunes).
- Los viernes disponibles en el rango son **exactamente 15** — las 15
  sesiones caben sin sacrificar ninguna.

## Sesión → fecha

| Sesión | Fecha | Hito / nota |
|---|---|---|
| s01 | vie 07-ago | Grupos + línea base (sin nota, por diseño) |
| s02 | vie 14-ago | Parte la escucha del día (práctica sin nota) |
| s03 | vie 21-ago | Lanzamiento del proyecto · **F1 (resuelto): semana universitaria — taller formativo, sin nota** |
| s04 | vie 28-ago | Instrumentos de cuerda pulsada #1 |
| s05 | vie 04-sep | **Hito 1 del proyecto (10 %)** |
| s06 | vie 11-sep | **SUSPENDIDA** (2026-09-11). Su módulo 1 (decibel, isofónica) se dicta en s07 m2; los batidos de s07 pasan a s08 m1; las estaciones E2/E4/E5 y el mini-informe se eliminan |
| — | vie 18-sep | **RECESO (14–19 sep) — sin clase** |
| s07 | vie 25-sep | **Prueba 1 (10 %, s01–s05) + escucha escrita E1** · m2: sonoridad y decibel (de s06), hoja isofónica = taller de la semana |
| — | vie 02-oct | **SIN CLASE — actividades suspendidas desde 13:30** |
| s08 | vie 09-oct | Batidos en 15′ + banda crítica; parten talleres de medición sobre el objeto (s08–s12) |
| s09 | vie 16-oct | Afinar por batidos; escala del objeto |
| s10 | vie 23-oct | **Hito 2 del proyecto (10 %)** + clínicas |
| s11 | vie 30-oct | Instrumentos de cuerda frotada #2 |
| s12 | vie 06-nov | Sesión-taller de lutería; cierre serie del objeto |
| s13 | vie 13-nov | **Prueba 2 (10 %) + escucha escrita E2** |
| s14 | vie 20-nov | Salida de medición T60; **se publica pauta del hito 3** |
| s15 | vie 27-nov | **Presentaciones finales + informe (15 %) + escucha escrita E3** — coincide con el tope de fin de clases (permitido: mismo caso que I4 de SyS) |

Fechas derivadas: presentaciones de s15 se envían hasta las **20:00 del
jue 26-nov** (regla de la pauta del hito 3); la nota del hito 2 se
publica antes de s12 (**≤ 05-nov**).

## Verificación de evaluaciones contra ventanas prohibidas

| Evaluación | Fecha | ¿Ventana prohibida? |
|---|---|---|
| Hito 1 | 04-sep | Fuera ✓ |
| Prueba 1 | 25-sep | Fuera (la suspensión llega hasta el 21-sep) ✓ |
| Hito 2 | 23-oct | Fuera ✓ |
| Prueba 2 | 13-nov | Fuera ✓ |
| Presentaciones | 27-nov | Fuera ✓ |
| Talleres evaluados | semanal | **s03 (21-ago) → F1** |

La escucha del día (s02–s14) no es evaluación — no lleva nota ninguna
semana — por lo que esta verificación no le aplica: corre igual en s03
pese a la semana universitaria.

### F1 — s03 (21-ago) en semana universitaria: RESUELTO (2026-08-13)

Decisión del profesor: el taller de s03 ("la sartén y sus parientes")
corre **formativo** — mismo formato, sin registro en el 35 % de
talleres (precedente de diseño: s01 es formativa; el lanzamiento del
proyecto, que es lo estructural de s03, no es evaluación).
Consecuencia: los talleres evaluados de la edición quedan 9 y la regla
es **"mejores 8 de 9"** (el material genérico conserva "mejores 8 de
~10"). **Anunciarlo en s02 (14-ago)** junto con las reglas del curso.
Hecho registrado en `DATOS_CURSO.yml` (clave `talleres`).

## Consecuencias de calendario a tener presentes

- **s06 suspendida (11-sep)**, decisión del 2026-09-11: se mantiene el
  calendario. La Prueba 1 evalúa s01–s05 (el decibel entra en la
  Prueba 2); s07 m2 dicta el decibel y la isofónica con 15′ de medición
  compacta; s08 m1 abre con los batidos en 15′. El taller de s06 (hoja
  isofónica) se rinde en s07: siguen 9 talleres, mejores 8 de 9.

- **El receso corta el semestre entre s06 y s07**: la Prueba 1 queda
  dos semanas después de cerrar su materia — regalo de estudio, pero
  también 14 días sin contacto antes de la prueba (recordatorio por
  Canvas la semana del receso).
- **La semana del 02-oct (sin clase) separa s07 de s08**: la
  devolución de la Prueba 1, que el plan de s08 hace "en la puerta",
  queda 2 semanas después de rendida. La corrección tiene holgura
  extra; el anuncio de "objeto del proyecto en s08" (hecho en s07)
  gana una semana de margen para los grupos.
- La sesión de grabación pre-s01 y todo el checklist "antes de s01"
  (ver `../../_archivo/bitacora/RESUMEN_PARA_PATO_2026-07.md`) tienen fecha tope real: **vie 07-ago**.

### F2 — Hito 1 (04-sep): la bitácora no puntúa (2026-09-03)

La víspera de la entrega un estudiante consultó por la bitácora que
exige la rúbrica del hito 1 y pidió postergar una semana. Decisión del
profesor: la fecha se mantiene; en el hito 1 la bitácora se comenta
pero no puntúa (C5 formativo; nota sobre C1–C4 con la fórmula
reescalada 1 + 0,75 × (puntaje − 4)). Quien no la tenga escrita
entrega media página que reconstruya la trayectoria de su idea. Desde
el hito 2 la bitácora vuelve a ser condición de recepción, como dice
el enunciado. Se ajustó `encargo_hito1_diseno.md` y se anunció al
curso por Canvas. Al revisar Canvas se descubrió que los tres encargos
de hito (s04, s10, s14) estaban en `canvas.yml` pero nunca se
sincronizaron; se corrió `sync` ese día (quedan sin publicar).
