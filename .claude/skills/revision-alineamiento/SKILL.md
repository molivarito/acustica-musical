---
name: revision-alineamiento
description: Audita el alineamiento constructivo del curso de Acústica Musical, o de una sesión específica. Usar cuando el usuario pida revisar coherencia, alineamiento, cobertura de objetivos, carga de trabajo, o una auditoría global del diseño del curso.
context: fork
---

Auditar el alineamiento constructivo del curso (o de la sesión $ARGUMENTS
si se especifica una).

**Insumos obligatorios.** Las verificaciones 1–5 se resuelven con los
`plan.md`, pero la 6 NO: exige abrir además las **láminas**
(`slides_sNN.qmd`, incluidas sus notas de orador) y las **guías**
(`actividades/*.md`). Leer solo los planes fue el punto ciego que dejó
pasar el defecto de s04 por cuatro auditorías (2026-08-28).

## Verificaciones

1. **Cobertura de objetivos**: leer `OBJETIVOS_APRENDIZAJE.md` y
   todos los `material/curso/sesion-NN/plan.md` existentes. Construir la matriz
   objetivo × sesión. Reportar objetivos sin cobertura, objetivos
   sobre-representados y sesiones sin objetivos explícitos.
2. **Coherencia metodológica**: contrastar cada plan con
   `METODOLOGIA.md`. Señalar módulos que son exposición pasiva
   disfrazada (más de 30 min continuos sin actividad del estudiante).
3. **Carga realista**: verificar que cada módulo suma 70 minutos y que la
   actividad cabe en el tiempo asignado considerando logística real
   (instalación, formación de grupos, transiciones). Ser escéptico: los
   planes suelen ser optimistas.
4. **Progresión**: verificar que ningún plan asume conceptos que no se han
   introducido en sesiones anteriores según `PLAN_SEMESTRE.md`.
5. **Producción**: listar el material pendiente (demos, apuntes,
   actividades) acumulado en todos los planes, ordenado por sesión.
6. **Orden interno de la sesión — "predecir antes de ver"**: el curso se
   juega en que el estudiante se compromete (predice por escrito, dibuja
   o vota) ANTES de que se le muestre la respuesta. Un defecto es
   cualquier lugar donde el ver llega antes del predecir. Procedimiento,
   en este orden: (a) de las **guías**, listar cada compromiso del
   estudiante y qué exactamente debe producir, citando las columnas
   textuales; (b) del **plan**, la secuencia de bloques y qué muestra o
   demuestra el profesor en cada uno ("Rol del profesor"); (c) de las
   **láminas**, la línea de tiempo de revelaciones, notas de orador
   incluidas; (d) cruzar: para cada compromiso, ¿algo anterior lo
   responde? Cuatro patrones a buscar:
   - **Lámina spoiler**: una tabla, figura o simulación previa entrega el
     resultado que la actividad debía producir (s04: la tabla "El mapa de
     la cuerda" rellenaba la tabla de predicción de la guía).
   - **Demostración con el mismo caso**: el profesor demuestra con el
     mismo caso/medición que el taller pide predecir (s04: pulsar al
     micrófono con el espectrograma proyectado).
   - **Síntesis duplicada o descolocada**: la misma síntesis ocurre dos
     veces, o el cierre de las láminas contradice el cierre del plan.
   - **Escucha contaminada**: algo se ve antes de oírse, cuando la
     escucha del día exige oír sin pantalla.
   - **Predicción cobrada dos veces**: el ticket de salida de la sesión
     anterior ya recogió la predicción por escrito y la guía vuelve a
     pedirla después de la revelación (s05: la §1 de "el bajo que no
     está" repetía el ticket de s04). Sobra la de la guía, no la del
     ticket: reapuntar esa predicción a la pregunta que sí sigue
     abierta.
   **Cuál es la lectura previa**: el **capítulo del libro**
   (`material/libro/capNN_*.md`, encabezado "*Lectura previa a la sesión
   NN*"), NO el apunte de la sesión — el apunte está narrado en pasado y
   es consolidación posterior. Auditarlo como si fuera previo produce
   falsos positivos. El capítulo está legítimamente en manos del
   estudiante y no cuenta como filtración, pero sí hay que señalar
   cuando una actividad finge descubrimiento de algo que el capítulo ya
   trae explícito.

## Formato del reporte

Reporte crítico y directo, en prosa con la matriz de cobertura como tabla.
Priorizar los 3-5 problemas más graves con propuesta concreta de solución
para cada uno. No suavizar los hallazgos. Guardar el reporte en
`_archivo/bitacora/revision_YYYYMMDD.md` y entregar un resumen ejecutivo en la
conversación.
