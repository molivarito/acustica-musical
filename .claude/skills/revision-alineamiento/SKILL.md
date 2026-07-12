---
name: revision-alineamiento
description: Audita el alineamiento constructivo del curso de Acústica Musical, o de una sesión específica. Usar cuando el usuario pida revisar coherencia, alineamiento, cobertura de objetivos, carga de trabajo, o una auditoría global del diseño del curso.
context: fork
---

Auditar el alineamiento constructivo del curso (o de la sesión $ARGUMENTS
si se especifica una).

## Verificaciones

1. **Cobertura de objetivos**: leer `diseno/01_objetivos_aprendizaje.md` y
   todos los `sesiones/sXX/plan.md` existentes. Construir la matriz
   objetivo × sesión. Reportar objetivos sin cobertura, objetivos
   sobre-representados y sesiones sin objetivos explícitos.
2. **Coherencia metodológica**: contrastar cada plan con
   `diseno/02_metodologia.md`. Señalar módulos que son exposición pasiva
   disfrazada (más de 30 min continuos sin actividad del estudiante).
3. **Carga realista**: verificar que cada módulo suma 70 minutos y que la
   actividad cabe en el tiempo asignado considerando logística real
   (instalación, formación de grupos, transiciones). Ser escéptico: los
   planes suelen ser optimistas.
4. **Progresión**: verificar que ningún plan asume conceptos que no se han
   introducido en sesiones anteriores según `diseno/03_estructura_curso.md`.
5. **Producción**: listar el material pendiente (demos, apuntes,
   actividades) acumulado en todos los planes, ordenado por sesión.

## Formato del reporte

Reporte crítico y directo, en prosa con la matriz de cobertura como tabla.
Priorizar los 3-5 problemas más graves con propuesta concreta de solución
para cada uno. No suavizar los hallazgos. Guardar el reporte en
`diseno/revision_YYYYMMDD.md` y entregar un resumen ejecutivo en la
conversación.
