# Candidatos a estímulos de s02 — pendientes de TU validación auditiva

Búsqueda 2026-08-13 (banco de estímulos, ítems 2 y 3). **Nada de esto
está aprobado todavía**: los archivos pasaron solo el filtro objetivo
(licencia citada y verificada, formato, duración, forma de onda y
espectrograma revisados). Nadie los ha escuchado. La carpeta vive fuera
de `material/` a propósito: no se publica.

## Cómo validar (10 minutos)

1. **Mira la lámina** (`*_lamina.png`) antes de escuchar: forma de onda
   arriba, espectrograma abajo — los mismos anteojos del curso. Ahí ya
   se ve si el archivo tiene silencio inicial, ruido de fondo o cortes.
2. **Escucha el audio** (doble clic, QuickTime) con la checklist de su
   ítem, idealmente con los audífonos o parlantes que usarás en la sala.
3. **Regla del banco**: apunta la app de espectrograma del curso al
   parlante mientras suena — lo que la clase debe ver tiene que verse
   en la app, no solo en mi lámina.
4. Dime cuál apruebas de cada par; yo lo recorto (silencios), lo
   normalizo, lo convierto a WAV como `e0X_*.wav` en
   `material/estimulos/`, y actualizo el banco de estímulos con la
   atribución. Si ninguno te convence, se vuelve al plan original:
   grabarlo tú.

## Ítem 2 — nota larga de flauta con ataque soploso (escucha del día s02)

Uso: primera escucha del semestre; los estudiantes deben distinguir la
capa impulsiva/ruidosa del soplo y la capa armónica sostenida.

Checklist al escuchar:
- [ ] ¿Se oye el soplo como capa distinta del tono (no solo un inicio limpio)?
- [ ] ¿La nota se sostiene estable ≥ 3 s, sin vibrato exagerado ni quiebres?
- [ ] ¿Sin ruidos ajenos (llaves, tos, sala, edición audible)?
- [ ] ¿Suena natural al volumen de la sala (mp3 128 kbps: sin artefactos)?

| Archivo | Nota | Veredicto objetivo | Fuente y licencia |
|---|---|---|---|
| `flauta_freesound_C4_ccby_mtg.mp3` | C4, ~5 s de tono | **Recomendado**: registro grave = el más soploso; la lámina muestra ruido de soplo entre los armónicos durante todo el sostenido. Tiene ~2,8 s de silencio inicial (se recorta al aprobar) | freesound.org/people/MTG/sounds/354638 · CC-BY 3.0 · atribuir: "MTG (dataset good-sounds), Freesound, CC-BY 3.0" |
| `flauta_freesound_C5_ccby_mtg.mp3` | C5, ~4,4 s | Alternativa: armónicos nítidos, algo menos de soplo | freesound.org/people/MTG/sounds/354387 · CC-BY 3.0 · misma atribución |
| `flauta_freesound_A5_ccby_mtg.mp3` | A5, ~4 s | La más limpia (poco soplo): menos apta para ESTE estímulo, útil como contraste en otra actividad | freesound.org/s/354446 · CC-BY 3.0 · misma atribución |

Descartadas: 2 notas de U. de Iowa (licencia libre excelente pero ~2,4 s,
bajo el mínimo; quedaron en el scratchpad de la sesión por si acaso).

## Ítem 3 — trueno con retardo (gancho $v$ del sonido, s02 módulo 2)

Uso: el estudiante cronometra ~3 s entre "relámpago" (narrado) y trueno
para calcular la distancia. Lo crítico es un inicio nítido.

Checklist al escuchar:
- [ ] ¿El inicio del trueno es un instante claro, cronometrable con celular?
- [ ] ¿La cola de retumbo se oye varios segundos (da tema para la clase)?
- [ ] ¿Sin voces, música ni lluvia que tape el estampido?
- [ ] ¿Suena con cuerpo en graves en el equipo de la sala (no solo en audífonos)?

| Archivo | Veredicto objetivo | Fuente y licencia |
|---|---|---|
| `trueno_wikimedia_03_ccbysa.ogg` | **Recomendado**: ~3,5 s de silencio casi total y luego estampido seco con cola larga — el retardo del ejercicio viene incorporado | commons.wikimedia.org/wiki/File:Thunder_crack_2B.ogg · CC-BY-SA 4.0 · atribuir: "Jud McCranie, Wikimedia Commons, CC-BY-SA 4.0" |
| `trueno_wikimedia_01_pd.ogg` | Alternativa: trueno rodante que emerge a los ~2,5 s, inicio menos seco; licencia sin ninguna obligación | commons.wikimedia.org/wiki/File:Rain_and_thunder.ogg · dominio público |

Descartado: `Thunder.ogg` (Bidgee, CC-BY): lluvia de banda ancha continua
que entierra el trueno — inicio no cronometrable.

## Reproducir el análisis

`validar_estimulos.py` (en esta misma carpeta) genera ficha y lámina
por archivo — sirve para validar cualquier audio futuro del banco:
`conda run -n base python3 validar_estimulos.py <carpeta-o-archivo>`.
