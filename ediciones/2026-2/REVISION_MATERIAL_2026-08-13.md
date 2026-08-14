# Revisión crítica del material — noche del 2026-08-13

Revisión de coherencia operativa de las 15 sesiones (encargada por el
profesor antes de dormir). Método: dos auditores delegados (s03–s08 y
s09–s15) revisaron tiempos de las tablas, cabeceras de guías vs. plan,
referencias rotas, archivos huérfanos, materiales fantasma y supuestos
desactualizados; Claude verificó con evidencia propia una muestra de
cada informe (s04, s08, s12, s15) antes de consolidar. **Ningún archivo
de `material/curso/` fue modificado**: las correcciones propuestas
esperan confirmación del profesor.

## Resultado global: la estructura está sana

- Las 30 tablas de módulo (2 × 15 sesiones) cierran en 70′ sin huecos
  ni traslapes, incluida la estructura especial de s15.
- Cero enlaces rotos: toda demo, capítulo, apunte y actividad que un
  plan menciona existe en la ruta indicada (incluye las pruebas de
  s07/s13 en `pruebas/`).
- Cero huérfanos y cero materiales fantasma en `actividades/`.
- Cero supuestos desactualizados: ni "5 grupos", ni "20 estudiantes",
  ni coevaluación activa, ni nota por participación oral en ninguna
  sesión.
- Sesiones completamente limpias: s01–s02 (ya operadas), s05, s07,
  s13, s14, s15.

## El único patrón real: 8 guías con tiempos desactualizados

Firma común: la cabecera de la guía quedó con la duración anterior al
ajuste que agrandó su bloque (casi siempre +5′, probablemente del
redimensionamiento a 9 estudiantes). **El plan es la fuente correcta**:
sus tablas cierran en 70′ y su "aritmética de taller declarada" es
consistente consigo misma; lo desactualizado es la guía impresa.

| # | Sesión | Archivo (cabecera) | Guía dice | Plan asigna |
|---|---|---|---|---|
| 1 | s03 | `guia_pee_sarten.md` | 30′ | 25–60′ = **35′** |
| 2 | s04 | `guia_pee_mapa_cuerda.md` | 32′ (suma interna: 40′) | 25–62′ = **37′** |
| 3 | s06 | `hoja_registro_isofonica.md` | 22′ | 36–63′ = **27′** (declarado 2×) |
| 4 | s08 | `registro_mapa_del_choque.md` | 22′ | 35–62′ = **27′** (declarado 2×) |
| 5 | s09 | `guia_pee_afinar_por_batidos.md` | 32′ | 25–62′ = **37′** |
| 6 | s10 | `guia_pee_resonancia_botellas.md` | 27′ (suma interna: 25′) | 30–62′ = **32′** |
| 7 | s11 | `guia_pee_punto_de_frotado.md` | 26′ (fases 8/6/6) | 32–63′ = **31′** (fases 9/7/9) |
| 8 | s12 | `guia_pee_construccion_tubo.md` §2 | "Corte y primera medición (14 min)" | 9′ corte + 7′ medición + 8′ registro = **24′** |

Los casos 3 y 5 ya estaban en los pendientes conocidos; los otros 6
son nuevos. **El prioritario es el 8 (s12)**: la fase subestimada
incluye corte y lijado de tubo con herramienta — apurarla por un número
mal rotulado es el único hallazgo con potencial de problema real,
no solo de molestia.

## Corrección propuesta (esperando tu OK)

Alinear cabeceras y números de fase internos de las 8 guías con la
aritmética declarada de su plan (ediciones de una línea por número; el
contenido pedagógico no se toca), y regenerar los paquetes de
impresión (`python3 ediciones/2026-2/generar_impresiones.py --todas`)
para que lo impreso quede correcto. Basta con que digas
**"corrige las cabeceras"**.

Ninguna es urgente para mañana (s02 no está afectada); la primera que
importa es la de s03 (guía de la sartén), que se imprime el jueves 20.

## Además, un pendiente de CLAUDE.md quedó obsoleto

El pendiente "(2026-08-06) s15, preguntas del grupo 1: 5′ vs 7′"
describe el diseño anterior por grupos: el `plan.md` actual de s15
tiene 9 defensas individuales de 11′ (8′ + 3′) **iguales para todos**,
sin asimetría alguna. Se cerró en esta pasada (CLAUDE.md actualizado).
