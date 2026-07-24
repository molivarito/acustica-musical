# Guía del curso para Pato — estado al 2026-07-22

Este es TU documento de entrada: qué existe, dónde está, qué ven los
alumnos, cómo se edita y qué falta. La segunda mitad (bajo la línea)
conserva sin cambios el resumen histórico del loop autónomo que produjo
el material (2026-07-13).

## Estado en una mirada

- **Material**: 15 sesiones completas (plan, apunte, actividades,
  demos), libro de 15 capítulos + PDF, programa, banco de estímulos.
  Diseño auditado 3 veces + verificación post-migración (2026-07-22).
- **Publicado**: sitio en <https://molivarito.github.io/acustica-musical>
  (se regenera solo con cada `git push`) y curso Canvas MUC860-1 con 18
  módulos espejo del sitio, **todos sin publicar** — tú publicas cada
  módulo a mano, semana a semana, desde la interfaz de Canvas.
- **Pruebas 1 y 2**: rediseñadas 2026-07-22 con alternativas en las
  Partes B–D (corrección ~2 h en vez de ~5 h; la Parte A de escucha
  sigue abierta). **Sin commitear aún — esperan tu revisión**
  (`git diff` las muestra).
- **Pendiente grueso**: tu checklist físico/administrativo (abajo).

## Qué ve el alumno y qué ves solo tú

**Alumnos** (sitio + Canvas): apuntes, guías y hojas de actividades,
demos, libro (+PDF), `Admin/programa_curso.md`,
`materiales/apps_recomendadas.md`, mapa del curso.

**Solo tú** (en el repo, fuera del sitio y de Canvas):

| Material | Dónde vive |
|---|---|
| Planes de sesión (tu guión docente) | `sesiones/sNN/plan.md` |
| Pruebas y sus pautas | `sesiones/s07/actividades/prueba1*`, `s13/.../prueba2*` |
| Pautas de hitos, clínica, feedback | `sesiones/*/actividades/*pauta*` |
| Guión de la sesión final | `sesiones/s15/actividades/guion_profesor_s15.md` |
| Banco de estímulos (revela las pruebas) | `materiales/banco_estimulos.md` |
| Planilla de rúbrica OA3 (registro de la ronda) | `materiales/planilla_rubrica_oa3.md` |
| Diseño del curso y bitácora de auditorías | `diseno/` completo |

La regla vive en `_quarto.yml` (bloque `render:`, con comentario). Ojo:
el **repo de GitHub es público** — estos archivos no aparecen en el
sitio, pero sí son visibles para quien navegue el código fuente. Si eso
te incomoda, la salida es hacer el repo privado (pídelo).

## Cómo trabajar

- **Slides de cada clase (solo tuyas)**: abre
  `Admin/slides_profesor/index.html` (doble clic) — es tu mapa privado
  con los 15 decks. `F` = pantalla completa; las demos van embebidas
  dentro de las slides (cargan del sitio: requiere internet en la
  sala). Los fuentes son `sesiones/sNN/slides/slides_sNN.qmd`; si
  editas uno, regenera su deck con
  `bash Admin/genera_slides_profesor.sh NN`. No están en el sitio ni
  en Canvas (los alumnos no las ven).

- **Editar material**: editas el `.md` → `git commit` → `git push`. El
  sitio se reconstruye solo (~2 min). Para previsualizar antes:
  `conda run -n base quarto preview`.
- **Material nuevo**: crear el `.md` y, SOLO si es para alumnos,
  agregarlo a la `sidebar` de `_quarto.yml` y a `canvas/canvas.yml` +
  correr `python3 canvas/publicar_canvas.py sync`. Material tuyo
  (pautas, planes…): basta que el nombre calce con las exclusiones de
  `_quarto.yml` (`plan.md`, `*pauta*`, `prueba*`, `guion_profesor*`) o
  agregarlo ahí.
- **PDF del libro**: `conda run -n base quarto render libro`.
- **Figuras**: editar `figuras/gen_sXX.py` y re-ejecutarlo — nunca el SVG.
- **Google Drive**: mantén la carpeta AM "Disponible sin conexión"; si
  `git push` se cuelga con "Operation timed out", es Drive deshidratando
  `.git` (ya pasó; el arreglo es re-descargar la carpeta).

## Pendientes que solo tú puedes hacer

**Antes de s01** (lo que tiene plazo real — s01 = vie 07-ago):
- Sesión única de grabación: estímulos #1–2, 5–7, 10–12 del banco
  (guitarra + flauta + vaso, una tarde). La #1 se reutiliza en s15.
- Revisar y aprobar las **pruebas rediseñadas** (sin commitear).
- **Probar las 14 demos renovadas en navegador** (2026-07-23 se
  revisaron y mejoraron todas: cobertura del plan completada, juegos y
  modos predicción/oculto agregados, paleta nueva; el audio real sigue
  sin probarse — las de más riesgo: `demo_forma_onda_espectro` con
  micrófono, `demo_modos_sala`, y la captura de figuras de prueba en
  `demo_resonancia`/`demo_tubo_agujeros`).
- Kits: reglas (s01), objetos metálicos (s03), botellas (s10); lista
  del curso con carreras.
- En Canvas: publicar el módulo "Información del curso" cuando quieras
  que los alumnos vean algo.

**Con plazo institucional** (partir temprano):
- s14: permisos/reserva de espacios UC para la salida T60. App de
  medición YA elegida (verificado 2026-07-23): iOS **ClapIR**; Android
  **Room Acoustics: RT60 Meter** (confirmar precio al instalar) —
  probar la elegida en un espacio real.
- s12: compra del kit de lutería (PVC Ø20, cortatubos, tapas, lijas;
  medir diámetro interior real en la ferretería).
- s11: confirmar estudiantes con instrumento frotado; probar cámara
  lenta 240 fps. Video de respaldo y nota lobo YA resueltos
  (2026-07-23): URLs verificadas en `sesiones/s11/plan.md`.
- s06: sonómetro de referencia (¿existe en el instituto?).

**Decisiones tuyas**: encuesta de cierre (s15), plazo de publicación de
notas, contrastar conversiones de nota con normativa UC.

**Resuelto por investigación (2026-07-23)**: apps del curso verificadas
en tiendas (Spectroid, SpectrumView, GuitarTuna, Sound Meter de
rootApps fijada, Decibel X — ojo: la versión gratis solo mide dB(Z));
norma DS 594 citada con fuente oficial (85 dBA/8h, regla de 3 dB — la
tabla de la guía de s06 ya coincidía); atenuación de protectores,
tracto vocal y F1/F2 del español anclados a literatura. Fletcher &
Rossing en biblioteca UC NO fue verificable desde fuera: revisar tú
con credenciales en bibliotecas.uc.cl.

**Control de calidad pendiente** (heredado del loop, sigue vigente):
lectura de continuidad del libro de punta a punta; pasada a las citas
finas de C&G/BEN en los capítulos que más te importan.

---

# Registro histórico — Resumen del loop autónomo (Fases 3 y 4, 2026-07-13)

*(Conservado tal como se escribió; algunos datos fueron superados —
p. ej. las pruebas ya no se corrigen en ≤15 min/estudiante sino ~6 con
el rediseño de alternativas. El detalle sesión a sesión vive en
`ESTADO_LOOP.md`; las auditorías, en `diseno/revision_*.md`.)*

## Qué quedó listo

- **diseno/03_estructura_curso.md**: mapa completo de las 15 sesiones
  (tema, OA, dependencias, hitos, demo asignada) + notación unificada.
- **15 sesiones completas** en `sesiones/s01–s15/`: plan (2×70′ exactos),
  apuntes, actividades (28 guías/pautas, incluidas ambas pruebas con
  pauta de corrección, enunciado y 3 pautas de hitos del proyecto,
  clínica de pares, salida T60, coevaluaciones) y **14 demos HTML** con
  audio (s15 no lleva por diseño).
- **Libro de lecturas previas**: `libro/00_prologo.md` + 15 capítulos +
  compilado `libro/LIBRO_CURSO.md` (índice y bibliografía unificada) +
  `libro/LIBRO_CURSO.pdf` (pandoc/xelatex).
- **materiales/**: planilla operativa de la rúbrica OA3, apps
  recomendadas, banco de estímulos consolidado (16 grabaciones con
  plazos).
- **3 revisiones de alineamiento** (s05, s10, final) con sus ~15
  correcciones ya aplicadas: cobertura OA sin huérfanos, 30 módulos de
  70′ exactos, progresión sin dependencias hacia adelante, cadena de
  tickets s01→s15 verificada.

## Las 10 decisiones más importantes que tomé sin consultarte

1. **Progresión Benade** (impulsivo→modos→percepción→instrumentos→salas)
   en vez del orden 2019; los bloques quedaron A: s01–s04 física,
   B: s05–s09 percepción, C: s10–s13 instrumentos, D: s14–s15 salas y
   cierre.
2. **La voz quedó en 50 minutos** (módulo liviano post-prueba de s13).
   Es el sacrificio de contenido más grande del diseño; ver debilidades.
3. **Salida de medición en s14 con puesta en común comprimida** dentro
   de la propia salida (el formato 8 pedía "la sesión siguiente", pero
   s15 está completa con presentaciones); el informe T60 es la última
   nota de taller.
4. **Percusión sin sesión propia**: modos 2D, sartén, timbal y Chladni
   viven en s03 y reaparecen en la prueba 1.
5. **Pruebas 1 y 2 redactadas completas** (64 pts, exigencia 60 %,
   audio en 3 momentos públicos con pasada de repaso, escucha OA3
   integrada con 25 % del puntaje, corrección ≤15 min/estudiante).
6. **Un solo taller evaluado por semana**: cuando el diseño acumulaba
   dos, el segundo pasó a registro sin nota o a bitácora de proyecto
   (s08 psicoacústico, s09 escala del objeto, s11 acoplamiento).
7. **La serie s08–s12 sobre el objeto del proyecto arma el hito 2
   "solo"**: radiografía espectral (s08) → escala (s09) → resonancias
   (s10) → acoplamiento (s11) → cierre en s12; el hito 2 compila eso +
   bitácora + coevaluación.
8. **Evidencia final de OA3 en s15**: hoja de escucha argumentada por
   presentación (el estudiante diagnostica el instrumento de otro
   grupo) + devolución de las líneas base de s01 en sobres — el cierre
   del arco "escuchar como científico".
9. **Fuentes**: todo el texto es original, redactado desde conocimiento
   estándar verificable; las citas de C&G usan los rangos de página del
   índice de fuentes (el escaneo no admite verificación por texto) y
   BEN se cita por capítulo/sección. Datos finos no estándar quedaron
   [POR VERIFICAR] (lista en `ESTADO_LOOP.md`).
10. **Proceso**: repo git inicializado (PDFs de libros excluidos del
    versionado); cada sesión la produjo un subagente siguiendo las
    skills y reglas del proyecto, con s01 escrita a mano como ejemplar
    de estilo, y el orquestador verificó, corrigió y commiteó.

## Lo más débil — revísalo tú (sin anestesia)

1. **Ninguna demo fue abierta en un navegador real.** Verifiqué
   sintaxis JS (node --check) y convenciones, pero no audio, UX ni
   comportamiento del micrófono (s02). Abre las 14 una a una antes de
   clase; las de mayor riesgo: `demo_forma_onda_espectro.html`
   (getUserMedia + fallback) y `demo_modos_sala.html` (barrido con
   refuerzo modal sintetizado).
2. **OA1.3 "cantado" no tiene huella de evaluación** en ninguna parte:
   la voz se enseña después de la prueba 2 y no hay taller con nota.
   O lo declaras honestamente en el programa, o metes un ítem de voz en
   la escucha de alguna evaluación. Hoy es un objetivo decorativo en su
   cuarto verbo.
3. **OA1.4 y OA4.3 penden de una sola sesión (s14) sin red**: si la
   salida se cae (lluvia, permisos, paro), no hay plan B estructural —
   solo la demo y Sabine en pizarrón, que no evalúa OA4.3.
4. **Las citas bibliográficas finas no están verificadas contra los
   PDF**: C&G se citó por rangos del índice (escaneo sin capa de
   texto) y varias secciones de BEN por el índice, no releyendo el
   original. Antes de repartir el libro a estudiantes, dale una pasada
   a las citas de los capítulos que más te importan.
5. **El libro lo escribieron 15 manos distintas**: el tono es
   consistente por diseño (ejemplar s01 + reglas), pero nadie hizo una
   lectura de continuidad de `LIBRO_CURSO.md` de punta a punta.
   Transiciones a vigilar: cap. 7→8 y 13→14.
6. **Los porcentajes y conversiones de nota** (exigencia 60 %, nota =
   1+(puntaje−4)/2, ajuste ±0,5 por coevaluación) salieron de la
   metodología aprobada, pero nadie los contrastó con normativa UC.
7. **El banco de estímulos es trabajo tuyo real**: 16 grabaciones,
   varias con plazo pre-s01 (la #1 se reutiliza en s15: si no se graba
   antes de la primera clase, se rompe el cierre del curso).
8. **Talleres aún optimistas**: las revisiones recortaron los peores
   casos, pero s02 m1, s08 m1 y la fase de afinación de s12 siguen
   ajustados al minuto; ensáyalos mentalmente con tus tiempos reales.
9. **Los picos de corrección declarados** caen encima de la producción
   de figuras/estímulos de esas mismas semanas; la revisión movió lo
   movible a pre-s01, pero el calendario real puede volver a apilarlos.
   *(Mitigado 2026-07-22: las pruebas pasaron a alternativas, ~2 h de
   corrección en vez de ~5 h.)*
10. **La demo de temperamentos y la de formantes usan "reglas del curso
    para colorear"** (banda crítica simplificada, F1/F2 típicos): son
    honestas pedagógicamente pero no datos finos; está comentado en el
    código.
