# Demos — inventario técnico (uso del profesor)

Cara de mantenimiento de las demos, separada de la cara pedagógica
(las demos se enlazan desde los apuntes, los planes y el mapa de
`material/index.qmd`). Patrón heredado de `SyS/material/demos/README.md`
(2026-08-06). Este README está fuera del `render:` de `_quarto.yml`
(no se publica); las demos mismas sí, como `resources`.

Todas las demos siguen `.claude/rules/formato-demos.md`: un archivo
HTML autocontenido, JavaScript vanilla + Web Audio API, **cero
dependencias externas** (verificado: ninguna usa CDN), audio solo tras
interacción del usuario, bloque "¿Qué observar?" con preguntas guía.

| Demo | Sesión | Qué ilustra |
|---|---|---|
| `demo_tren_pulsos.html` | s01 | Tren de pulsos: del ritmo al tono |
| `demo_forma_onda_espectro.html` | s02 | Forma de onda y espectro en vivo (micrófono) |
| `demo_modos_cuerda.html` | s03–s04 | Modos de una cuerda |
| `demo_sintesis_aditiva.html` | s04 | El espectro como receta del timbre |
| `demo_fundamental_ausente.html` | s05 | La altura es un patrón (fundamental ausente) |
| `demo_decibel_sonoridad.html` | s06 | Curvas isofónicas y decibel |
| `demo_batidos.html` | s07 | Batidos: dos tonos casi iguales |
| `demo_banda_critica.html` | s08 | Del batido a la consonancia: banda crítica |
| `demo_temperamentos.html` | s09 | Afinar es elegir un compromiso |
| `demo_resonancia.html` | s10 | Oscilador forzado: resonancia y amortiguamiento |
| `demo_helmholtz.html` | s11 | El resonador de Helmholtz |
| `demo_tubo_agujeros.html` | s12 | Columna de aire: largo, tapa y agujeros |
| `demo_formantes_voz.html` | s13 | La voz por dentro: fuente y filtro |
| `demo_modos_sala.html` | s14 | Modos de sala |

## Cómo probar una demo

Abrirla directo en el navegador (doble clic) o vía el panel de sesión
(pestaña Demo). Antes de clase: verificar que **suena** en el equipo
de la sala — varios planes lo listan como trabajo previo. Varias demos
tienen "modo presentación" (números ocultos) para la escucha del día:
el plan de la sesión indica cuál y cómo.

## Mantenimiento

- Una demo = un concepto; si crece hacia dos ideas, dividirla
  (`.claude/rules/formato-demos.md`).
- s15 no tiene demo (única sesión sin demo, decisión de diseño).
- Deuda técnica conocida: ninguna al 2026-08-06.
