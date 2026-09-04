# Prueba de dictado — s06 (vie 11-sep-2026)

**Pregunta única**: ¿podría el profesor dictar s06 el 2026-09-11 con lo
que existe HOY (2026-09-04) en el repo?

**Método**: no se repite la consistencia entre documentos (ya auditada
cuatro veces, más el barrido `ediciones/2026-2/barridos/s06.md` del
2026-08-14) sino la EXISTENCIA y SERVIBILIDAD de cada material: se abrió
cada archivo declarado, se comprobaron controles de la demo línea por
línea, se regeneró el HTML de impresión desde el `.md` actual para
compararlo byte a byte con lo que hay en `ediciones/2026-2/impresiones_s06/`,
y se buscó en todo el repo el nombre concreto de cada "app"/"software"
mencionado en abstracto.

## Veredicto

**NO dictable tal cual — dictable con 5 arreglos**, dos de ellos
bloqueantes (el estímulo de la escucha del día y el software de E1) y
uno de urgencia inmediata (reimprimir la guía de estaciones, que está
desactualizada respecto del `.md` vigente).

## Tabla principal

| Bloque (módulo, minutos) | Material declarado | Estado | Evidencia (ruta:línea) | Qué falta exactamente |
|---|---|---|---|---|
| M1, 8–18′ — Escucha del día "la mezcla que pierde el bajo" | Estímulo #9: "fragmento musical de mezcla completa con bajo prominente y brillo", dos niveles | **NO EXISTE** | `material/profesor/banco_estimulos.md:? fila 9` = "por grabar o conseguir con licencia"; `ls material/estimulos/` no tiene ningún `e09_*`; `ls ediciones/2026-2/estimulos_candidatos/` (33 archivos) tampoco tiene ninguna mezcla completa — todo son instrumentos solos (bajo, flauta, piano, guitarra, trueno) | No hay archivo de audio. Hay que conseguir/grabar una mezcla completa (canción real, no instrumento solo) con bajo y brillo audibles, y PROBARLA en el equipo de la sala a ambos niveles antes del viernes — es la única forma de saber si "se pierde" el bajo de verdad |
| M1, 8–18′ — mismo bloque, plan B | "espectrograma del celular" para probar antes | **EXISTE Y SIRVE** | `material/apps_recomendadas.md:14-16` (Spectroid/phyphox/SpectrumView) | Nada — cualquiera de las 3 apps cumple |
| M1, 18–36′ — mini-lección del dB | `demo_decibel_sonoridad.html` "como apoyo visual" (proyección, no interactiva en este bloque) | **EXISTE Y SIRVE** | `material/demos/demo_decibel_sonoridad.html` | Nada |
| M1, 36–63′ — Mi curva isofónica | 3 notebooks con `demo_decibel_sonoridad.html`; audífonos; hoja de registro | **EXISTE Y SIRVE** | `material/demos/demo_decibel_sonoridad.html:144-149` (chips `data-f="125" data-req="1"`, `data-f="1000"` ref, `data-f="4000" data-req="1"`, opcionales 250/2000/8000) — coincide exactamente con lo que plan.md y la hoja piden (★ 125/1000/4000, opcionales 250/2000/8000); `material/curso/sesion-06/actividades/hoja_registro_isofonica.md` regenerado y comparado byte a byte con `impresiones_s06/hoja_registro_isofonica.html`: **sin diferencias** | Falta solo una instrucción operativa (ver fila siguiente) |
| M1, 36–63′ — mecánica de turnos de la demo | 3 integrantes rotan por turno en el mismo notebook | **EXISTE PERO NO CUBRE LO QUE EL PLAN PIDE** | `material/demos/demo_decibel_sonoridad.html:158-159,463-469` — el botón "Borrar mi curva" limpia `marcas` pero NO resetea `calibrado`; `material/curso/sesion-06/actividades/hoja_registro_isofonica.md` (íntegro) nunca instruye a apretarlo entre turnos | Si el 2.º/3.er estudiante no aprieta "Borrar mi curva" antes de su turno, empieza con la curva del compañero ya dibujada y puede "completarla" en vez de trazar la suya. Ya señalado por el barrido del 2026-08-14 (indefinido 4) y sigue sin corregirse en el `.md` vigente. Arreglo: 1 línea en la hoja |
| M2, 0–8′ — Gancho de las 4 palmas | "Celular con app SPL proyectado (o lectura en voz alta)" | **AMBIGUO, pero con fallback declarado** — y contradicho por las notas de la slide | `material/curso/sesion-06/plan.md:78` fila 0–8′ dice "proyectado (o lectura en voz alta)"; `material/curso/sesion-06/slides_s06.qmd:169-171` (notas) dice "medir con la app SPL **SIN** proyectar la lectura — el profesor se la guarda" | Plan.md y las notas de la slide se contradicen sobre si el número se proyecta o no en el minuto 0-8′ (el plan permite proyectar; las notas lo prohíben explícitamente porque el número se revela recién en el minuto 55-60′). Es una decisión de guion, no un material faltante: aclarar antes de clase cuál versión se sigue |
| M2, 8–15′ — logística de estaciones | Guía de estaciones (1 por grupo); lámina con mapa de estaciones | **EXISTE Y SIRVE** (guía) / **EXISTE Y SIRVE** (lámina, es una slide del mazo) | `material/curso/sesion-06/actividades/guia_estaciones_niveles.md`; `material/curso/sesion-06/slides_s06.qmd:173-188` | Nada, salvo que la guía IMPRESA está desactualizada — ver fila siguiente |
| M2, 15–55′ — guía de estaciones, **versión impresa** | `ediciones/2026-2/impresiones_s06/guia_estaciones_niveles.html` (paquete ya generado, listo para Cmd+P) | **EXISTE PERO NO CUBRE LO QUE EL PLAN PIDE** (desactualizada) | Regenerado con `pandoc -s --mathml` desde el `.md` actual y comparado con `diff` contra el HTML impreso: difieren en E2 (pregunta de predicción reescrita) y sobre todo en **E4**, que en el `.md` vigente usa "lo que su propio grupo ya midió en E1–E3" y en el HTML impreso trae los 4 ítems VIEJOS con datos inventados ("Un pasaje del ensayo marca 70 dB SPL…", "Un parlante solo produce 60 dB…", "Junto al atril del trompetista…") — un rediseño pedagógico (conectar E4 con los propios datos del grupo, probablemente parte de "Aplicados los 19 arreglos de orden pedagógico", commit `50a9443`) que nunca se propagó a la impresión | El `.md` fuente se editó el 29-ago 22:57; el HTML impreso quedó del 14-ago 10:00 y nunca se regeneró. Si el profesor imprime desde esa carpeta tal cual, reparte E4 con ejercicios que contradicen la instrucción vigente. Arreglo: `python3 ediciones/2026-2/generar_impresiones.py 06` + reimprimir |
| M2, 15–55′, estación E1 | "interfaz + micrófono + notebook con software de medición" | **NO EXISTE (nombre) / AMBIGUO** | `material/curso/sesion-06/plan.md:78,116,139,144`: nunca nombra el software; `METODOLOGIA.md:80` tampoco lo nombra; `material/apps_recomendadas.md` (íntegro) no tiene ninguna categoría de software de escritorio para leer nivel desde una interfaz de audio; el propio plan.md:144 marca "sonómetro de referencia para E1 si existe **[POR VERIFICAR — pendiente global 9 de metodología §6]**"; `METODOLOGIA.md:252` confirma que el pendiente 9 ("verificar disponibilidad de sonómetro de referencia") sigue **[POR VERIFICAR]** | Nadie decidió NI probó un programa concreto. Hace falta: (a) elegir software (p. ej. REW o el medidor de picos/RMS de Audacity — ya recomendado por el barrido del 14-ago), (b) confirmar que existe interfaz de audio + micrófono físicos, (c) verificarlos y fijar la ganancia ANTES del jueves |
| M2, 15–55′, estaciones E2/E3 | "1 celular emisor de tono", "MISMO tono al MISMO volumen" | **NO EXISTE (app nombrada)** | `grep -rn -i "tono\|generador" material/apps_recomendadas.md` → sin resultados; "Requisitos previos" y "Contrato de la semana" de plan.md solo piden a los estudiantes traer app de medición SPL, nunca una app generadora de tono; "Trabajo previo del profesor" (plan.md, Pendientes de producción) no incluye preparar celulares emisores | Falta instalar una app de tono puro en 2-3 celulares (propios del profesor o prestados) y dejarla fija en un tono conocido a volumen constante — sin esto, E2 y E3 (2 de las 5 estaciones) no tienen con qué operar |
| M2, 15–55′, estación E2 | "4 puntos marcados" de la sala | **NO EXISTE (dueño/criterio)** | `material/curso/sesion-06/actividades/guia_estaciones_niveles.md:52` — voz pasiva, sin sujeto; ningún documento dice quién marca los puntos ni con qué criterio de contraste acústico | Si nadie los marca de antemano con contraste real (puerta, esquina, centro, ventana), la pregunta "¿dónde se ensaya más protegido?" puede no tener respuesta interesante el mismo día |
| M2, 15–55′, estaciones E4/E5 | "guía impresa, calculadora del celular" | **EXISTE Y SIRVE** (calculadora es del propio celular del estudiante) | — | Nada, salvo que E4 depende de la reimpresión de la fila de arriba |
| M2, 55–60′ | "Planilla proyectada" | **AMBIGUO** (no es un archivo, es un artefacto sin definir) | `material/curso/sesion-06/plan.md:80` fila 55-60′; no hay slide con tabla vacía en `slides_s06.qmd`, ni archivo de planilla digital en el repo; mismo hueco ya señalado en el barrido de s09 | No bloquea: se resuelve trivialmente dibujando la tabla a mano en el pizarrón (recomendación ya hecha por el barrido del 14-ago, nunca objetada) |
| M2, 60–70′ — Mini-informe SPL | "Formulario de 4 casillas... al dorso de la planilla" (impresa) | **EXISTE Y SIRVE** | `ediciones/2026-2/impresiones_s06/guia_estaciones_niveles.html` incluye la planilla y pauta al final; solo cambia el contenido de E4 (ver arriba), la planilla/pauta del mini-informe en sí no difiere | Nada nuevo — reimprimir junto con el resto |
| M2, 60–70′ — ticket de salida hacia s07 | Papel/lápiz de los estudiantes | **EXISTE Y SIRVE** | — | Nada |
| M1, 0–5′ — re-formación de mesas tramo 2 | "Lista de mesas del tramo 2 proyectada" | **NO EXISTE (artefacto digital)** | `find ediciones/2026-2 -iname "*mesa*"` → sin resultados; el criterio (instrumento/afinidad) vive en las actas de mesa en papel de s01 (`material/curso/sesion-01/plan.md:23`), no en ningún archivo digital | El profesor puede rearmarlas de memoria (9 estudiantes, 5 sesiones de trato), pero no hay dónde consultarlas si duda, y no queda registro para el tramo 3 (tras s10). Ya señalado por el barrido del 14-ago (indefinido 5), sigue sin resolverse |

## Lo que el profesor tiene que llevar (objetos físicos — no verificables desde el repo)

- Interfaz de audio + micrófono para E1 (existencia confirmada solo como
  **[POR VERIFICAR]** en `METODOLOGIA.md:252` y `plan.md:144` — no hay
  registro de que el profesor los tenga).
- Notebook de E1 con el software de medición ya elegido, instalado,
  probado y con ganancia fijada (ver tabla — el software mismo tampoco
  está decidido).
- 2–3 celulares "emisores de tono", configurados y cargados.
- ≥2 celulares con app SPL por grupo (3 grupos → mínimo 6 celulares;
  los traen los propios estudiantes, según el "Contrato de la semana").
- Audífonos personales de cada estudiante (los traen ellos).
- 3 notebooks para la experiencia isofónica (1 por grupo, con la demo
  cargada localmente o con internet para el iframe).
- Cronómetro proyectable.
- Cinta/post-it o similar para marcar los 4 puntos de E2 en la sala.
- 9 entregas corregidas del hito 1, con pauta marcada (ver dependencias
  de s05).
- Lista de recepción / material impreso: guía de estaciones (×3),
  hoja isofónica (×9), rúbrica OA3 (impresión genérica).
- Parlante(s) de la sala probados con el estímulo de la mezcla —
  condicionado a que el estímulo exista (ver bloqueante 1).

## Dependencias de s05

- **Hito 1 recibido**: confirmado que el diseño lo contempla — s05
  recibe 9 entregas contra checklist al inicio
  (`material/curso/sesion-05/plan.md:55`, fila 0–5′) y NO corrige ese
  mismo día ("devolución en s06"). Como s05 es HOY (2026-09-04,
  `ediciones/2026-2/CALENDARIO_2026-2.md:35`), esta pieza depende de que
  la recepción de hoy efectivamente ocurra.
- **Corrección del hito 1**: tarea pendiente del profesor esta semana,
  declarada en `material/curso/sesion-06/plan.md` ("Trabajo previo del
  profesor... corregir el hito 1, pico declarado ≈2 h") — no verificable
  desde el repo si ya se hizo; es trabajo manual sobre las 9 entregas
  físicas.
- **Ticket de salida de s05** ("misma frecuencia ¿distinto volumen?; grave
  y agudo con la misma energía ¿igual de fuerte?"): declarado como
  recogido en `material/curso/sesion-05/plan.md:70` — s06 lo cobra en el
  bloque 18–36′. Depende de que se recoja hoy en s05.
- **Punto de control de s05 / plan B de lectura**: si se activó, la
  lectura previa de s06 se reemplaza por una tarea de escucha ≤30 min
  (`plan.md`, Riesgos y plan B, última viñeta) — condicional a un evento
  de hoy que este informe no puede verificar.

## Conocimientos asumidos sin fuente

Se revisó `material/curso/sesion-0[1-6]/apunte_*.md` y el capítulo del
libro: **no se encontraron vacíos**. En particular:

- 0 dB SPL = umbral de audición, 20 µPa de referencia: cubierto en
  `apunte_s06_sonoridad_y_decibel.md:50-54` y en
  `material/libro/cap06_sonoridad_y_decibel.md:68-70`.
- Criterio NIOSH / 85 dB(A) por 8 h, regla de intercambio de 3 dB
  (usado sin más contexto en `guia_estaciones_niveles.md:94-96`, E5):
  cubierto en `apunte_s06_sonoridad_y_decibel.md:149,154` y en
  `material/libro/cap06_sonoridad_y_decibel.md:128-133` (incluye cita a
  DS 594, MINSAL 1999).
- 1000 Hz como referencia de las isofónicas: cubierto en
  `material/libro/cap06_sonoridad_y_decibel.md:101,107`.
- +10 dB = ×10 / +3 dB = ×2: cubierto en el apunte y repetido en las
  slides (`slides_s06.qmd:90-108`).

Único matiz: la guía de estaciones (E1) da por sentado que el estudiante
sabe qué es una "interfaz de audio" y qué significa "no cambiar la
ganancia" — no es un objetivo de aprendizaje del curso y no está
explicado en ningún apunte, pero tampoco se le pide operarla (la opera
el profesor); no se considera un vacío bloqueante, solo un supuesto de
vocabulario técnico que el profesor debe estar dispuesto a aclarar al
vuelo si preguntan.

## Arreglos mínimos para el 2026-09-11 (por orden de bloqueo)

1. **[BLOQUEANTE] Conseguir o grabar el estímulo #9** (mezcla completa
   con bajo prominente y brillo, dos niveles) y probarlo en el equipo de
   la sala. Sin esto, la escucha del día del módulo 1 (10 min, bloque
   8–18′) no tiene con qué ejecutarse tal como está diseñada — el plan B
   documentado (parlante del celular del profesor a bajo vs. equipo de
   sala a alto) es un respaldo aceptable, pero requiere elegir Y probar
   igual un fragmento concreto. **Esfuerzo: 60–90 min** (buscar/grabar +
   probar en sala).

2. **[BLOQUEANTE] Definir y probar el software de medición de E1** (p.
   ej. REW o Audacity con medidor de picos/RMS), confirmar si existe
   interfaz + micrófono físicos, y fijar la ganancia. Sin esto, E1 (una
   de las 5 estaciones, y la que ancla al profesor durante la rotación)
   no puede operar; el plan B ("app del celular del profesor como
   referencia común") existe pero degrada la estación completa.
   **Esfuerzo: 30–45 min** si el hardware ya existe; **horas** si hay
   que conseguir interfaz/micrófono.

3. **[URGENTE] Regenerar la impresión de la guía de estaciones**:
   `python3 ediciones/2026-2/generar_impresiones.py 06` y reimprimir —
   la copia actual en `ediciones/2026-2/impresiones_s06/` reparte una
   versión vieja de E4 (ejercicios con datos inventados) que contradice
   el rediseño vigente (E4 debe usar los datos que el propio grupo
   midió en E1–E3). Si se imprime tal cual, el mini-informe y la pauta
   rápida no van a calzar con lo que el profesor espera ver.
   **Esfuerzo: 10 min** (regenerar + reimprimir 3 copias).

4. **Preparar 2–3 celulares "emisores de tono"** con una app de tono
   puro instalada, fijos en un tono y volumen conocidos — sin esto, E2
   y E3 no tienen fuente controlada. **Esfuerzo: 15 min.**

5. **Marcar los 4 puntos de E2 antes de que entren los estudiantes**,
   eligiendo contraste acústico real (puerta/pasillo, esquina lejana,
   centro, junto a ventana). **Esfuerzo: 5 min**, pero debe hacerse
   el mismo día antes de clase, no antes.

6. **Agregar una línea a la hoja isofónica**: "antes de empezar su
   turno, apriete 'Borrar mi curva'" — evita que el 2.º/3.er estudiante
   herede la curva del compañero. **Esfuerzo: 5 min** de edición +
   reimpresión (puede ir junto con el arreglo 3).

7. **Decidir si el gancho de las 4 palmas se proyecta o no** (plan.md
   dice "proyectado o en voz alta"; las notas de la slide dicen
   explícitamente que NO se proyecta). No bloquea, pero conviene
   resolverlo antes para no improvisar el guion en el momento.
   **Esfuerzo: 2 min** (decisión, sin necesidad de editar archivos).

8. **Rearmar y registrar las mesas del tramo 2** (criterio: mezcla de
   familia de instrumento y afinidad tecnológica) — puede hacerse de
   memoria, pero conviene dejar un registro simple (p. ej.
   `ediciones/2026-2/mesas.md`) para no repetir el ejercicio a ciegas en
   el tramo 3. **Esfuerzo: 15 min.**

**Total de esfuerzo mínimo antes del viernes** (excluyendo conseguir
hardware de E1 si no existe): **~2–2,5 horas**, concentradas en su
mayoría en el estímulo de audio y la verificación de E1 — exactamente
los dos ítems que, si fallan el mismo día, no tienen degradación
aceptable completa (el estímulo #9 sin probar puede simplemente no
"perder el bajo" en la sala real; E1 sin software probado se cae a un
plan B que reduce la estación a una comparación trivial).
