# Resumen del loop autónomo — Fases 3 y 4

Ejecutado 2026-07-12/13 sin consultas, según tus instrucciones. Todo
commiteado en git (repo inicializado en este loop, 18 commits). El
detalle sesión a sesión vive en `ESTADO_LOOP.md`; las auditorías, en
`diseno/revision_20260712.md`, `_s10.md` y `revision_20260713.md`.

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
   [POR VERIFICAR] (lista abajo).
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
9. **Los picos de corrección declarados** (~5 h en s07 y s13, ~4 h en
   s15) caen encima de la producción de figuras/estímulos de esas
   mismas semanas; la revisión movió lo movible a pre-s01, pero el
   calendario real puede volver a apilarlos.
10. **La demo de temperamentos y la de formantes usan "reglas del curso
    para colorear"** (banda crítica simplificada, F1/F2 típicos): son
    honestas pedagógicamente pero no datos finos; está comentado en el
    código.

## Pendientes de producción acumulados (trabajo físico/decisiones)

Lista completa por sesión en `ESTADO_LOOP.md`; lo crítico:

- **Pre-s01**: grabar estímulos #1, #10–#12 (sesión de grabación
  única); 5 kits (reglas, objetos metálicos, botellas); imprimir
  rúbrica y planilla OA3; lista del curso con carreras.
- **Compra única**: kit de lutería s12 (PVC Ø20, cortatubos, tapas,
  lijas) — [POR VERIFICAR] diámetro interior real.
- **Semana a semana**: resto del banco de estímulos (16 ítems,
  `materiales/banco_estimulos.md`); figuras de las pruebas desde las
  demos (~1 h cada prueba); confirmar interfaz/micrófono (s06) y
  espacios+permisos de las rutas T60 (s14, plantilla editable).
- **Decisiones tuyas pendientes**: instrumento de encuesta del curso
  (s15); plazo de publicación de notas; sonómetro de referencia
  [POR VERIFICAR]; Fletcher & Rossing en biblioteca UC [POR VERIFICAR].
- **[POR VERIFICAR] técnicos dejados en los materiales**: norma
  chilena DS 594 y atenuación de protectores (s06); 240 fps de celular
  resolviendo la cuerda + video de respaldo + nota lobo (s11); tracto
  ~17 cm y F1/F2 finos de vocales españolas (s13).

## Cómo retomar

`ESTADO_LOOP.md` tiene la tabla completa (todo `lista`). Si quieres
iterar una sesión: los reportes de revisión indican qué se cambió y por
qué; la regla del loop fue no reescribir sesiones cerradas salvo
exigencia de auditoría. El siguiente paso natural es tu lectura crítica
de `libro/LIBRO_CURSO.pdf` y una pasada por las 14 demos en el
navegador.
