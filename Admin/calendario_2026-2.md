# Calendario 2026-2 — MUC860 Acústica Musical (solo profesor)

Instancia el mapa de 15 sesiones (`diseno/03_estructura_curso.md`) con
las fechas reales del segundo semestre 2026. Fuente de las restricciones:
`../SyS/ediciones/2026/PLAN_2026-2.md` (que a su vez cita el calendario
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
| s02 | vie 14-ago | **Parte la ronda oral con nota** |
| s03 | vie 21-ago | Lanzamiento del proyecto · **F1: semana universitaria — sin evaluaciones ese día** |
| s04 | vie 28-ago | Instrumentos de cuerda pulsada #1 |
| s05 | vie 04-sep | **Hito 1 del proyecto (8 %)** |
| s06 | vie 11-sep | Estaciones de niveles; mini-informe SPL. Última clase antes del receso |
| — | vie 18-sep | **RECESO (14–19 sep) — sin clase** |
| s07 | vie 25-sep | **Prueba 1 (12,5 %)** — dos semanas después de s06: colchón de estudio natural |
| — | vie 02-oct | **SIN CLASE — actividades suspendidas desde 13:30** |
| s08 | vie 09-oct | Parten talleres de medición sobre el objeto (s08–s12) |
| s09 | vie 16-oct | Afinar por batidos; escala del objeto |
| s10 | vie 23-oct | **Hito 2 del proyecto (8 %)** + clínicas |
| s11 | vie 30-oct | Instrumentos de cuerda frotada #2 |
| s12 | vie 06-nov | Sesión-taller de lutería; cierre serie del objeto |
| s13 | vie 13-nov | **Prueba 2 (12,5 %)** |
| s14 | vie 20-nov | Salida de medición T60; **se publica pauta del hito 3** |
| s15 | vie 27-nov | **Presentaciones finales + informe (14 %)** — coincide con el tope de fin de clases (permitido: mismo caso que I4 de SyS) |

Fechas derivadas: presentaciones de s15 se envían hasta las **20:00 del
jue 26-nov** (regla de la pauta del hito 3); la nota del hito 2 se
publica antes de s12 (**≤ 05-nov**); coevaluaciones del hito 2 se leen
y las conversaciones por asimetría ocurren entre el 24-oct y el 05-nov.

## Verificación de evaluaciones contra ventanas prohibidas

| Evaluación | Fecha | ¿Ventana prohibida? |
|---|---|---|
| Hito 1 | 04-sep | Fuera ✓ |
| Prueba 1 | 25-sep | Fuera (la suspensión llega hasta el 21-sep) ✓ |
| Hito 2 | 23-oct | Fuera ✓ |
| Prueba 2 | 13-nov | Fuera ✓ |
| Presentaciones | 27-nov | Fuera ✓ |
| Ronda oral (s02–s14) | semanal | **s03 (21-ago) cae en semana universitaria → F1** |
| Talleres evaluados | semanal | **s03 (21-ago) → F1** |

### F1 — s03 (21-ago) en semana universitaria: decisión pendiente del profesor

La sesión corre normal (la ventana solo prohíbe evaluaciones), pero la
**ronda oral con nota** y el **taller evaluado** ("la sartén y sus
parientes") no pueden llevar nota ese día. **Recomendación**: ambos
corren formativos en s03 (mismo formato, sin registro en planilla ni en
el 25 % de talleres) — hay precedente de diseño (s01 es formativa) y el
lanzamiento del proyecto, que es lo estructural de s03, no es
evaluación. Consecuencias: la ronda con nota queda s02, s04–s06,
s08–s12, s14 (11 sesiones — igual alcanzan ~2–3 pasadas por estudiante
para "mejores 2"); los talleres evaluados quedan 9 → la regla "mejores
8 de ~10" pasa a **"mejores 8 de 9"**. Si prefieres otra salida (p. ej.
correr la nota del taller de s03 a la guía de s04), decidirlo antes de
s02 para anunciarlo con las reglas del curso.

## Consecuencias de calendario a tener presentes

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
  (ver `RESUMEN_PARA_PATO.md`) tienen fecha tope real: **vie 07-ago**.
