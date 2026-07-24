# ESTADO DEL LOOP — Fase 3–4 autónoma

> **Registro histórico (cerrado).** La producción que este archivo
> gobernaba terminó el 2026-07-13 con las 15 sesiones listas; se
> conserva por su registro de decisiones (D0–D9) y de pendientes
> físicos del profesor. Las instrucciones operativas de este archivo
> (md2html, compilar_libro, "continúa el loop") quedaron obsoletas con
> la migración a Quarto del 2026-07-17 — el flujo vigente está en
> `README.md` y `CLAUDE.md`.

Iniciado: 2026-07-12. Instrucción: desarrollar las 15 sesiones completas
(plan, apuntes, capítulo del libro, demo principal, actividades) sin
consultas al profesor. Para retomar tras una interrupción: leer este
archivo + `diseno/03_estructura_curso.md`, continuar con la primera
unidad no marcada `lista`, en orden s01→s15, y luego el cierre.

Prioridad si falta contexto/tiempo: plan > apuntes > capítulo >
actividades > demo.

## Tabla de avance

| Sesión | Tema (corto) | plan | apuntes | demo | actividades | capítulo |
|---|---|---|---|---|---|---|
| s01 | Del golpe al tono | lista | lista | lista | lista | lista |
| s02 | Ondas y espectrograma | lista | lista | lista | lista | lista |
| s03 | Modos de vibración | lista | lista | lista | lista | lista |
| s04 | La receta del timbre | lista | lista | lista | lista | lista |
| s05 | Altura percibida | lista | lista | lista | lista | lista |
| s06 | Sonoridad y decibel | lista | lista | lista | lista | lista |
| s07 | Prueba 1 + batidos | lista | lista | lista | lista | lista |
| s08 | Banda crítica y consonancia | lista | lista | lista | lista | lista |
| s09 | Escalas y temperamentos | lista | lista | lista | lista | lista |
| s10 | Resonancia e impedancia | lista | lista | lista | lista | lista |
| s11 | Cuerdas frotadas y cuerpo | lista | lista | lista | lista | lista |
| s12 | Vientos y lutería | lista | lista | lista | lista | lista |
| s13 | Prueba 2 + la voz | lista | lista | lista | lista | lista |
| s14 | La sala como instrumento | lista | lista | lista | lista | lista |
| s15 | Presentaciones finales | lista | lista | n/a | lista | lista |

## Controles de calidad

| Control | Estado |
|---|---|
| revision-alineamiento al cerrar s05 | **lista** — reporte en `diseno/revision_20260712.md`; 5 correcciones recomendadas antes de abrir s06 (P1–P5) |
| revision-alineamiento al cerrar s10 | **lista** — reporte en `diseno/revision_20260712_s10.md`; 5 correcciones recomendadas antes de abrir s11 (P1–P5: cierres de s06 m2 y s08 m1, rotulación OA2.2 en Prueba 1, plazos del banco #10–#12, hoja isofónica) |
| revision-alineamiento final (s15) | **hecha** — reporte en diseno/revision_20260713.md; 5 problemas menores corregidos (P1–P5, 6 archivos) |
| Compilación libro/LIBRO_CURSO.md (+PDF si hay pandoc) | **hecha** — MD (15 caps + índice + bibliografía) y PDF vía pandoc/xelatex |
| RESUMEN_PARA_PATO.md | **hecho** — en la raíz del proyecto |

## Registro de decisiones tomadas sin consultar

- **D0 (infraestructura)**: el directorio no era repo git; se ejecutó
  `git init -b main`. Se agregó `referencias/libros/` a `.gitignore`
  (PDFs pesados y con derechos de autor; el índice de fuentes sí queda
  versionado).
- **D1–D5 (estructura)**: ver sección "Decisiones de estructura" en
  `diseno/03_estructura_curso.md` (progresión Benade; voz reducida a
  módulo liviano en s13; salida de medición en s14 con puesta en común
  comprimida; percusión sin sesión propia; electroacústica/audio digital
  fuera del programa).
- **D6 (proceso)**: para conservar contexto en un loop de 15 sesiones,
  cada sesión se produce con un subagente dedicado que sigue al pie de
  la letra las instrucciones de las skills `plan-sesion` y
  `demo-interactiva` (embebidas en su prompt) y las reglas de
  `.claude/rules/`; el orquestador verifica los artefactos, actualiza
  este archivo y hace el commit. s01 se produce en el hilo principal
  como ejemplar de estilo para los subagentes.
- **D7 (fuentes)**: los apuntes se redactan desde conocimiento estándar
  verificable + los capítulos indexados en
  `referencias/notas/indice-fuentes.md`; se citan libro/capítulo(/página
  cuando el índice la da) como lectura complementaria. C&G no admite
  búsqueda por texto (escaneo), así que las páginas citadas de C&G se
  toman de los rangos del índice de fuentes. Dato cuantitativo fino no
  estándar → [POR VERIFICAR].
- **D8 (sobrescritura de diseno/03)**: la regla de CLAUDE.md pide
  confirmar antes de reescribir en `diseno/`; la instrucción explícita
  de esta corrida ("complétalo primero", sin preguntas) la supersede.
  Solo se completó el esqueleto existente; 01 y 02 no se tocan.

- **D9 (correcciones post-revisión s05)**: se reescribieron archivos de
  sesiones ya cerradas por exigencia del reporte de alineamiento
  (autorizado por las reglas del loop): s02 plan+guía retratos (taller a
  2 sonidos por grupo); s02–s05 planes (ronda oral = 3′+2′+4×2,5′ con
  cronómetro); s04 plan+2 guías (armónicos opcional, tarea b eliminada);
  s05 plan+registro (experiencia I en parejas). Se creó `materiales/`
  con planilla OA3, apps recomendadas, banco de estímulos consolidado, y
  la pauta de feedback de ideas de proyecto en s04/actividades. Detalle
  en la sección final de diseno/revision_20260712.md.

## Pendientes de producción acumulados

(Se llena a medida que los planes declaren pendientes; ver también
diseno/02 §6.)

- **s01**: estímulo de audio de la línea base (grabación propia:
  guitarra con batido) — inicia el banco de estímulos; 5 reglas para los
  kits; rúbrica OA3 impresa; lista del curso con carreras.
- **s02**: grabaciones para el banco de estímulos (flauta con ataque
  soploso, trueno); planilla de rúbrica OA3 con nómina y sorteo; lista
  de apps de espectrograma recomendadas; recopilar tickets de s01.
- **s03**: 5 kits de objetos metálicos + vaso "oficial"; guitarra o
  monocordio (plan B); grabaciones de timbal/tom; imágenes Chladni con
  licencia; enunciado de proyecto impreso; pauta de feedback de medias
  hojas (la produce s04). [POR VERIFICAR] Fletcher & Rossing en
  biblioteca UC.
- **s04**: comentar medias hojas de proyecto (~45 min profe); grabar e
  invertir nota de guitarra; guitarra de respaldo, huinchas, cinta de
  papel; probar espectrograma con guitarra; publicar demo tras la
  sesión.
- **s05**: demo opcional `demo_octava.html` NO producida (se reúsa la de
  s04); fragmento de bajo para parlante chico + dos octavas de piano
  (banco de estímulos); imprimir hojas de registro y lista de recepción
  hito 1; probar demo en audífonos.
- **s06**: estímulo #9 del banco; verificar interfaz+mic+software E1;
  app SPL del profesor; corregir hito 1 (~3 h); redactar prueba 1.
  [POR VERIFICAR] norma chilena DS 594 (exposición a ruido) y
  atenuación de protectores de músico.
- **s07**: generar e imprimir 3 figuras desde grabaciones #10–#12 del
  banco; probar estímulos de la prueba en el equipo de sala; imprimir
  22 cuadernillos; pico de corrección ≈5 h; devolución de prueba 1
  comprometida para s08.
- **s08**: lámina de errores frecuentes de prueba 1; imprimir hojas
  "mapa del choque" y guías de radiografía espectral; planilla OA3
  pasada 2. Taller psicoacústico registra SIN nota (decisión de carga).
- **s09**: imprimir guías (afinación por batidos, escala del objeto);
  guitarra levemente desafinada para demostración; hito 2 anunciado.
- **s10**: botellas iguales por grupo + agua; pauta clínica impresa;
  revisar coevaluaciones hito 2 (riesgo 4); corrección hito 2 (~2 h).
  Nota: el agente de s10 fue cortado tras escribir todo; la verificación
  final la hizo el orquestador (JS OK, 70+70, aviso s11 presente).
- **s11**: resina, sordina, lámina holografías C&G 6, confirmar
  instrumentos frotados por correo, video de respaldo cámara lenta.
  [POR VERIFICAR] 240 fps de celular resuelve la cuerda; derechos del
  video de respaldo; grabación de nota lobo.
- **s12**: kit de lutería (compra única: PVC Ø20, cortatubos, tapas,
  lijas) + cortar brutos y calibrar un ciclo; leer coevaluaciones hito 2.
  [POR VERIFICAR] diámetro interior real del PVC nominal 20 mm.
- **s13**: generar figuras 1–2 de la prueba desde las demos (~1 h);
  sintetizar estímulos #13–#14, grabar #15; imprimir cuadernillos;
  pico corrección ≈5 h. [POR VERIFICAR] tracto ~17 cm; F1/F2 finos de
  vocales españolas.
- **s14**: estímulo #16 (frase seca/reverberante); confirmar acceso y
  horarios de los espacios de las rutas de medición (plantilla editable:
  espacios concretos los fija el profesor); globos para impulso;
  lámina de errores de prueba 2. Nota: agente cortado tras escribir todo;
  verificación final del orquestador (JS OK, 70+70, hito 3 y rutas OK).
- **s15**: ver el checklist canónico y completo en
  `sesiones/s15/actividades/guion_profesor_s15.md` §0 (la víspera) y
  "Trabajo físico del profesor" del plan de s15 — no se duplica aquí.
  Ítems críticos: estímulo #1 probado en el equipo de sala,
  presentaciones recibidas hasta las 20:00 de la víspera, sobres de
  línea base, encuesta del curso [decisión del profesor] y plazo de
  publicación de notas.
