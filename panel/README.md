# Panel de sesión

Mesa de trabajo local para **preparar** una sesión: elegida s01–s15, muestra a la vez su
plan con los dos módulos, la lista de materiales que hay que llevar a la sala, las slides,
el apunte, el capítulo del libro, las guías de actividades, la demo y los objetivos OA.

```
python3 panel/panel.py                     # abre el panel en el navegador
python3 panel/panel.py --permitir-publicar # además habilita la consulta a Canvas
python3 panel/indice.py --verificar        # qué no se pudo parsear
python3 panel/indice.py --json s04         # los datos crudos de una sesión
```

Sirve en `127.0.0.1:8767` (si está ocupado prueba hasta el 8776). Solo stdlib + PyYAML.
El puerto no es casual: el panel de SyS usa el 8766 y el armador de su banco el 8765, así
los tres conviven.

## Es de solo lectura

El panel **nunca escribe en las fuentes** (`.md`, `.qmd`, `.yml`). Lo único que genera es:

- el caché del índice, en `~/.cache/panel-am.json` (fuera del repo);
- los renders de Quarto bajo `material/_render/`, y solo cuando se los pides con `⟳`;
- el PDF del libro, solo si pulsas su botón.

Tras usarlo, `git status` debe seguir sin mostrar cambios en fuentes.

El botón **`✎ editar`** es la única salida hacia la modificación, y no contradice lo
anterior: no sirve para *leer* el plan —eso ya lo hace el panel, completo— sino para
saltar al archivo cuando, preparando, aparece una errata, un material que falta o un
bloque cuyos tiempos no suman. La edición ocurre en el editor externo; el panel solo
detecta el cambio en la siguiente pasada del caché por `mtime`.

Abre con el primer editor instalado de una lista por preferencia, **Readdown** primero.
Para forzar otro:

```bash
python3 panel/panel.py --editor "Visual Studio Code"
```

Un `open` a secas no sirve aquí: en macOS el tipo `public.markdown` lo reclama Xcode
(`com.apple.dt.document.markdown`), así que el comando devuelve 0 y no aparece nada en
pantalla. Por eso el panel elige la app explícitamente y **confirma en el log qué abrió y
con qué**: un botón que tiene éxito en silencio es indistinguible de uno roto.

**Ojo con la visibilidad**: este panel muestra material **solo-profesor** — planes de
sesión, pautas y el rol del profesor de cada bloque. Por eso escucha únicamente en
loopback, sin CORS, y por eso nada de lo que sirve entra en `material/_render/site/`.
`panel/` vive fuera de `material/` justamente para que el `render:`/`resources:` de Quarto
no pueda alcanzarlo y publicarlo por accidente.

## La diferencia con el panel de SyS: `plan.md` no existe en HTML

En SyS el contenido de la clase se ve incrustando el HTML que Quarto ya generó. Aquí eso
no sirve para el artefacto más importante: `material/_quarto.yml` excluye explícitamente
`"!curso/**/plan.md"` y `"!curso/**/*pauta*.md"` por la regla de visibilidad.

Por eso el panel convierte Markdown él mismo, con **pandoc** (`/api/md`, cacheado por
`mtime:size`), y no con un renderizador a mano: en Acústica Musical **las tablas son el
guion**, y las dos tablas de 5 columnas de cada `plan.md` son el corazón del documento.

El guion, en cambio, no se muestra como HTML de pandoc sino a partir de los datos
estructurados de `indice.py`: así caben las 5 columnas en un panel estrecho —`Tiempo`,
`Bloque` y `Actividad del estudiante` siempre visibles; `Rol del profesor` y `Materiales`
en un desplegable por fila (`expandir` los abre todos)— y funciona el selector
`ambos / Mód 1 / Mód 2`.

## Materiales para la sala

La zona **Materiales** no está en el panel de SyS y es probablemente lo más útil de este:
junta los `Materiales` de las diez celdas de las dos tablas, los deduplica y los presenta
como lista de chequeo con memoria (los tildes se guardan por sesión en `localStorage`).

Los ítems se separan por `;` y por ` + `, y la deduplicación **ignora los paréntesis
aclaratorios**: «Guitarra» y «Guitarra (del profesor o de un grupo)» son el mismo objeto
que hay que meter al bolso. Como el corte es sintáctico, alguna celda deja un fragmento
suelto («proyectada»); es preferible a fusionar de más y perder un material real.

## De dónde sale cada cosa

Las rutas de cada sesión **no se buscan, se derivan** del número: `sesion-NN/plan.md`,
`sesion-NN/slides_sNN.qmd`, `sesion-NN/actividades/*.md`. El apunte y el capítulo se
buscan por glob (`apunte_sNN_*.md`, `capNN_*.md`) porque su slug es parte del nombre.

| Fuente | Qué aporta |
|---|---|
| `material/curso/sesion-NN/plan.md` | título, cabecera, los 2 módulos con su tabla, verificación/pendientes/riesgos, enlaces |
| `PLAN_SEMESTRE.md` — «Mapa de las 15 sesiones» | tema, OA, **dependencias entre sesiones**, hitos y demo |
| `OBJETIVOS_APRENDIZAJE.md` | texto completo de cada `OA<n>.<m>` y su *Evaluación posible* |
| `ediciones/2026-2/CALENDARIO_2026-2.md` | fecha real e hito de cada sesión, y las interrupciones |
| `material/_quarto.yml` (sidebar) | título público de la sesión, apunte, actividades y demo |
| `material/curso/sesion-NN/slides_sNN.qmd` | `subtitle` — **segunda fuente de fecha**, con año |
| `canvas/canvas.yml` | módulo y URLs de la sesión en Canvas |

La columna `Depende de` del mapa permite algo que SyS no puede: al elegir una sesión, el
riel marca **en ámbar de cuáles depende** y **en verde cuáles dependen de ella**.

## Los renders envejecen, y el panel te lo dice

El panel incrusta el HTML que Quarto ya generó. Si editaste un `.md` y no renderizaste,
verías material viejo justo cuando preparas — por eso cada panel lleva un semáforo:

| | |
|---|---|
| verde | el render es más nuevo que la fuente |
| ámbar | diferencia ≤ 60 s: probablemente Google Drive reescribiendo mtimes al sincronizar |
| rojo | la fuente es más nueva; el tooltip dice cuánto |
| gris | no existe el HTML |

El tooltip muestra **ambos timestamps exactos**: nunca se esconde información detrás de un
color.

### El semáforo propio de AM: el PDF del libro

`material/libro/LIBRO_CURSO.pdf` es la **única copia** del libro y el CI **no la
reconstruye** — el workflow solo corre `quarto render` y `--profile canvas`, y el PDF
entra como recurso. Es decir: es un *insumo* del build, no una salida, y puede quedarse
atrás en silencio al editar un capítulo (ya pasó una vez: el PDF decía 8 % para el hito 2
donde el capítulo 10 decía 10 %).

`.githooks/pre-commit` corta ese modo de falla al commitear; el botón **PDF del libro** de
la barra lo ve antes, mientras preparas, y lo regenera con un clic. El diálogo de
publicación avisa además si `core.hooksPath` no está configurado — el hook viaja en el
repo, pero activarlo es configuración local de cada clon:

```bash
git config core.hooksPath .githooks
```

## Publicación

En Acústica Musical no hay nada que «liberar»: cada `git push` a `main` dispara
`.github/workflows/publish.yml` y el sitio se reconstruye solo. Por eso el botón de
publicación no publica — informa, y todo de disco, sin red:

- si hay cambios sin commitear y **cuántos commits locales sin pushear** (si los hay, el
  sitio publicado está atrasado respecto a lo que tienes);
- el último commit y su fecha; el estado del PDF del libro; si el hook está activo.

`Consultar GitHub Actions` (`gh run list`) y `Consultar Canvas` sí salen a la red, son de
solo lectura y van en botones aparte. La de Canvas exige además arrancar con
`--permitir-publicar`.

Todas las llamadas a `git` llevan **timeout**: este repo vive en Google Drive y un
`git log` que no vuelve dejaría el panel congelado justo cuando estás preparando clase.

## Atajos

`←` `→` sesión anterior/siguiente · `1`…`6` encienden o apagan cada panel ·
`a` `c` `d` cambian entre apunte, capítulo y demo · `m` rota el selector de módulo ·
`o` vista general de las slides · `Esc` cierra el modal y el log.

Los interruptores de **Paneles**, los presets de **Vistas** y los tildes de materiales se
recuerdan entre sesiones.

## Convenciones que romperían el panel

Ninguna ruptura lo deja en blanco —cada parser degrada y anota un aviso, visible en el
botón `⚠` de la barra—, pero sí perderías el dato. **Después de editar estos archivos,
corre `python3 panel/indice.py --verificar`.**

- **`plan.md` no tiene front-matter YAML.** El título sale de `# Sesión NN — título` y los
  campos de cabecera son párrafos `**Campo**:` a comienzo de línea.
- Los campos de cabecera se reconocen **por prefijo**: de s08 en adelante el campo se llama
  «Reglas aplicadas y decisiones de carga (declaradas)» y no «Reglas aplicadas». Los
  campos desconocidos se muestran igual, en su orden.
- Los módulos son `## Módulo N — título (variante: X)` y su guion es **la primera tabla de
  5 o más columnas** que sigue. Cambiar el número de columnas rompe el guion de ese módulo.
- El tiempo va como `0–10′` (prima, no "min") y **reinicia en cada módulo**; de ahí sale la
  duración de cada bloque y la barra proporcional.
- En `PLAN_SEMESTRE.md`, la tabla del mapa se reconoce porque su primera columna se llama
  `Sesión` y tiene 6 columnas. `Depende de` acepta `s03 (modos)`, listas y rangos
  (`s01–s06`).
- En el calendario, **las fechas no llevan año** (`vie 07-ago`): el año se toma del nombre
  del directorio (`ediciones/2026-2` → 2026). Las filas cuya primera columna es `—` son
  interrupciones (receso, viernes sin clase) y se pintan en su lugar del riel.
- Hay **dos fuentes de fecha** —el calendario y el `subtitle` de las slides, que sí trae
  año— y el panel las compara: si discrepan, sale un aviso. Es un chequeo gratis.
- Los objetivos se declaran `- **OA1.1** texto…` bajo `### OA1 — título`, y su
  `*Evaluación posible*:` se guarda aparte.
- Las actividades se descubren **listando el directorio**, no de un índice. Las `pauta_*`
  se marcan como solo-profesor. `sesion-07` y `sesion-13` no tienen `actividades/`: son
  las sesiones de prueba y el panel lo dice con naturalidad, no como fallo.

### Avisos que hoy son correctos

`--verificar` termina con dos avisos que **no son errores** y conviene no «arreglar»:

- **s02** y **s15**: el slug del apunte no coincide con el del capítulo
  (`apunte_s02_ondas_y_representacion` ↔ `cap02_ondas_y_espectrograma`;
  `apunte_s15_como_defender_un_proyecto_acustico` ↔ `cap15_explicar_es_la_prueba`).
  El panel los empareja por número, no por slug, así que funciona igual; el aviso existe
  para que la divergencia sea una decisión y no un descuido.
