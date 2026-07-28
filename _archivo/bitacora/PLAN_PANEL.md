# Plan: panel de sesión para Acústica Musical

> **EJECUTADO el 2026-07-28.** El panel vive en `panel/` y funciona; la
> documentación viva es `panel/README.md`. Este archivo queda como registro del
> encargo original, no como especificación a mantener: donde el plan y el código
> discrepen, manda el código. Desviaciones deliberadas respecto de lo planteado
> aquí:
>
> - El **guion no se pinta con el HTML de pandoc** sino desde los datos
>   estructurados de `indice.py`. Pandoc sí convierte el resto (guías,
>   capítulos, cierre del plan). El motivo: solo con datos estructurados caben
>   las 5 columnas en un panel estrecho (3 visibles + 2 en desplegable) y
>   funciona el selector de módulo.
> - El estado del CI (`gh run list`) quedó en un **endpoint aparte** (`/api/ci`),
>   no dentro de `/api/publicacion`: necesita red y habría bloqueado el arranque.
> - Se añadió `--editor`: en macOS el tipo `public.markdown` lo reclama Xcode, así
>   que `open` a secas devolvía 0 sin abrir nada visible.
>
> Los avisos que `indice.py --verificar` deja hoy (slugs divergentes en s02 y
> s15) son correctos y están explicados en `panel/README.md`.

Documento de encargo para un agente Claude que trabaje **en este repositorio (`AM/`)**.
Lo escribió el agente que construyó el panel equivalente del curso Señales y Sistemas,
tras analizar en detalle las diferencias entre ambos cursos.

## Qué hay que construir

Una **mesa de trabajo local para preparar una sesión**: elegida s01–s15, muestra a la vez
su plan de sesión, sus slides, el apunte del estudiante, el capítulo del libro, las guías
de actividades, los objetivos OA con su texto, la demo, y la planificación del semestre
con fechas reales e hitos. Solo lectura sobre las fuentes; se sirve en `127.0.0.1`.

El curso SyS ya tiene uno funcionando y en uso. **Este plan no describe cómo hacerlo desde
cero: describe qué copiar y qué cambiar.**

## Paso 0 — Leer la implementación de referencia

Antes de escribir una línea, leer los cuatro archivos del panel de SyS, que están en el
repo hermano:

```
../SyS/panel/indice.py       (~900 líneas)  capa de datos: parsers + caché
../SyS/panel/panel.py        (~440 líneas)  servidor http.server + endpoints
../SyS/panel/panel_ui.html   (~780 líneas)  interfaz completa en un archivo
../SyS/panel/README.md                      qué parsea de dónde y qué lo rompería
```

Son el punto de partida: **cópialos a `AM/panel/` y adáptalos**, no los reescribas. La
arquitectura, los guardarraíles de seguridad, el sistema de caché, el layout de paneles
opcionales y el semáforo de frescura son idénticos para los dos cursos. Lo que cambia es
la capa de datos y dos features.

Conviene leer también `../SyS/CLAUDE.md` para entender por qué el panel está donde está.

## Arquitectura (idéntica a SyS, cópiala tal cual)

```
AM/panel/
  indice.py       capa de datos: parsers + caché. Importable y con CLI propia.
  panel.py        servidor HTTP + CLI.
  panel_ui.html   frontend completo en un archivo.
  README.md
```

Directorio de primer nivel, **fuera de `material/`**: `material/` es un proyecto Quarto
cuyo `render:` y `resources:` copian agresivamente, y en AM además hay CI que publica en
cada push — un `.py` ahí dentro corre riesgo real de acabar en GitHub Pages.

Convenciones a heredar sin discusión (todas ya resueltas en el código de SyS):

- **Solo stdlib + PyYAML.** No hay Flask; los scripts de ambos repos documentan esa regla.
- `http.server.ThreadingHTTPServer(("127.0.0.1", puerto), Handler)`, `HTTP/1.1`.
- Puerto **8767** (SyS usa 8766 y el armador de su banco el 8765; así conviven los tres).
- Caché por archivo con clave `f"{st.st_mtime_ns}:{st.st_size}"` en
  `~/.cache/panel-am.json`. **Obligatorio**: el repo vive en Google Drive y leer decenas de
  archivos por red es lento; `os.stat` es solo metadata y es barato.
- Errores JSON `{"error": msg}` con `ValueError→400, FileNotFoundError→404, resto→500`.
- Montajes estáticos `/r/<montaje>/<ruta>` con, **en este orden**: montaje desde un `dict`
  cerrado → `unquote` y rechazo de `\x00` → `realpath` que debe empezar por
  `realpath(raiz)+os.sep` → **allowlist** de extensiones (no blocklist) → content-type →
  bind solo a `127.0.0.1`, sin CORS.
- Filtro `?desnudo=1` que inyecta CSS ocultando el cromo de Quarto (`#quarto-sidebar`,
  `#quarto-header`, `#quarto-margin-sidebar`, `.nav-page`) en **los bytes servidos**, nunca
  en el archivo.
- Ningún parser lanza excepción hacia arriba: devuelve lo que pudo y anota en `avisos`.

---

## Las diferencias con SyS (esto es el corazón del encargo)

| | SyS | **AM** |
|---|---|---|
| Unidad | 30 clases `C1`–`C30`, semana = ⌈n/2⌉ | **15 sesiones `s01`–`s15`**, 1 por semana, **2 módulos de 70′** |
| Plan del profesor | dentro del `cXX.qmd`, bloque `.ficha-profesor` | **`plan.md` aparte, y EXCLUIDO del render de Quarto** |
| Front-matter | YAML `title` + `subtitle` | **`plan.md` no tiene YAML**: `# Sesión NN — título` + párrafos `**Campo**:` |
| Guion | 1 tabla, 3 columnas | **2 tablas (una por módulo), 5 columnas** |
| Objetivos | `U<n>.<m>` en el subtítulo | **`OA<n>.<m>`** en el párrafo `**Objetivos que cubre**` |
| Ejercicios | banco de 372 `E####.md` + `banco.py` | **no hay banco**: `sesion-NN/actividades/*.md` (guías PEE, pautas) |
| Libro | Reader; unidad → capítulo | **`capNN` ↔ sesión `NN`, 1:1 y con el mismo slug** |
| Perfiles Quarto | `profesor` / `esqueleto` / `publico` | **ninguno para el sitio**; existe `_quarto-canvas.yml` (espejo Canvas) |
| Salidas | `_render/{site,esqueleto,publico,reader}` | **`_render/{site,canvas}`** + `libro/LIBRO_CURSO.pdf` |
| Fechas reales | `ediciones/2026/PLAN_2026-2.md`, `mié 05-ago-2026` | **`ediciones/2026-2/CALENDARIO_2026-2.md`, `vie 07-ago` (¡sin año!)** |
| Publicación | manual y gradual (`liberar --semana N`) | **automática: push a `main` → GitHub Actions** |
| Quarto | `/Users/pdelac/miniforge3/bin/quarto` | **`conda run -n base quarto`** (mismo binario, pero respeta la convención) |

### Diferencia crítica nº 1: `plan.md` no existe en HTML

En SyS, el contenido de la clase se veía incrustando el HTML que Quarto ya había generado.
**En AM eso no sirve para el artefacto más importante**: `material/_quarto.yml` excluye
explícitamente `"!curso/**/plan.md"`, `"!curso/**/*pauta*.md"` y `"!curso/**/guion_profesor*.md"`
por la regla de visibilidad (son material solo-profesor y no pueden llegar al sitio).

Entonces el panel **tiene que renderizar Markdown él mismo**. No escribas un renderizador a
mano: el `md()` mínimo del panel de SyS no sabe de tablas, y aquí las tablas *son* el guion.

**Solución: usar pandoc**, que ya está instalado en `/Users/pdelac/miniforge3/bin/pandoc`
(viene con Quarto). Un endpoint que convierte un `.md` a HTML bajo demanda y cachea el
resultado por `mtime:size`:

```python
subprocess.run([PANDOC, ruta, "-f", "gfm+tex_math_dollars", "-t", "html",
                "--mathjax"], capture_output=True, text=True)
```

Con `--mathjax` la matemática sale como `\(...\)` y la renderiza KaTeX en el cliente (mismo
CDN que ya usa el panel de SyS). Esto da tablas, listas y enlaces con fidelidad completa,
y sirve igual para `plan.md`, las guías de `actividades/` y los capítulos del libro.

**Comprobado** sobre `material/curso/sesion-04/plan.md`: ese comando exacto produce las
2 tablas con sus **5 columnas de cabecera**, 11 filas y 13 expresiones matemáticas
marcadas. La apuesta técnica del plan está verificada, no supuesta.

Aplica el mismo guardarraíl `realpath` que a los estáticos: solo se convierten archivos
dentro del repo.

### Diferencia crítica nº 2: dos módulos, cinco columnas

Cada `plan.md` tiene dos tablas con esta cabecera:

```
| Tiempo | Bloque | Actividad del estudiante | Rol del profesor | Materiales |
```

bajo encabezados `## Módulo 1 — <título> (variante: <tipo>)` y `## Módulo 2 — …`.
El tiempo va como `0–10′` (con prima `′`, no "min"), y reinicia en cada módulo.

Cinco columnas no caben legibles en un panel estrecho. **Decisión de diseño recomendada**:
mostrar `Tiempo` + `Bloque` + `Actividad del estudiante` siempre, y `Rol del profesor` y
`Materiales` en un desplegable por fila (o en una columna que se enciende con un
interruptor). Añadir un selector `Módulo 1 / Módulo 2 / ambos`, con "ambos" por defecto.

`Materiales` merece además una vista propia agregada: al preparar, lo primero que uno
necesita es **la lista de lo que hay que llevar a la sala**. Junta los `Materiales` de las
dos tablas, deduplica y muéstralos como una lista de chequeo. Esto no existe en SyS y es
probablemente la mayor ganancia del panel de AM.

### Diferencia crítica nº 3: no hay banco, hay actividades

Donde SyS muestra ejercicios `E####` del banco, AM muestra los archivos de
`material/curso/sesion-NN/actividades/`: guías PEE, actas, registros, pautas y hojas.
Se descubren listando el directorio (no hay índice), se clasifican por el prefijo del
nombre (`guia_`, `pauta_`, `hoja_`, `registro_`, `acta_`, `enunciado_`) y se renderizan con
pandoc al desplegarlos.

**Ojo**: `sesion-07` y `sesion-13` no tienen `actividades/` (son las sesiones de prueba).
No es un error — que el panel lo diga con naturalidad, no como fallo.

Marca visualmente las `pauta_*`: son solo-profesor y nunca deben llegar a estudiantes.

---

## Capa de datos: `panel/indice.py`

Índice por sesión, análogo al de SyS. Lo que se deriva **por convención de nombres**, sin
parsear nada:

```
material/curso/sesion-{NN:02d}/plan.md
material/curso/sesion-{NN:02d}/apunte_s{NN:02d}_<slug>.md      (glob: apunte_s*.md)
material/curso/sesion-{NN:02d}/slides_s{NN:02d}.qmd
material/curso/sesion-{NN:02d}/actividades/*.md
material/libro/cap{NN:02d}_<slug>.md                            (glob: cap{NN:02d}_*.md)
material/_render/site/curso/sesion-{NN:02d}/apunte_s{NN:02d}_<slug>.html
material/_render/site/curso/sesion-{NN:02d}/slides_s{NN:02d}.html
material/_render/site/libro/cap{NN:02d}_<slug>.html
```

El slug del apunte y el del capítulo **coinciden** (`apunte_s04_la_receta_del_timbre.md` ↔
`cap04_la_receta_del_timbre.md`), pero no lo asumas: haz glob por número y verifica la
coincidencia, anotando un aviso si difieren.

### Parsers

| # | Fuente | Extrae |
|---|---|---|
| P1 | `plan.md` cabecera | `# Sesión NN — título`; párrafos `**Objetivos que cubre**`, `**Requisitos previos**`, `**Posición en la progresión**`, `**Reglas aplicadas**` |
| P2 | `plan.md` módulos | `## Módulo N — título (variante: X)` + su tabla de 5 columnas |
| P3 | `plan.md` cierre | secciones `## Verificación de aprendizaje` y demás `##` finales |
| P4 | enlaces del `plan.md` | rutas relativas `../../demos/*.html`, `../../libro/cap*.md`, `actividades/*.md` |
| P5 | `PLAN_SEMESTRE.md` | la tabla de 6 columnas del "Mapa de las 15 sesiones" |
| P6 | `OBJETIVOS_APRENDIZAJE.md` | `### OA<n> — <título>` y `- **OA<n>.<m>** <texto>` |
| P7 | `ediciones/2026-2/CALENDARIO_2026-2.md` | tabla `Sesión / Fecha / Hito` + filas de interrupción |
| P8 | `material/_quarto.yml` sidebar | título de cada sesión, apuntes, actividades y **la demo** |
| P9 | `slides_sNN.qmd` front-matter | `subtitle` — **trae también la fecha real** |
| P10 | `canvas/canvas.yml` | módulos y URLs por sesión (espejo del sidebar) |
| — | lector genérico de tablas Markdown | reutiliza el de `../SyS/panel/indice.py` **tal cual** |

**Reutiliza literalmente de SyS**: el lector de tablas Markdown (`tablas_md`, con el
`re.split(r"(?<!\\)\|", ...)` que respeta pipes escapados dentro de fórmulas), la clase
`Indice` con su caché, y `frescura()`.

### Fuentes de datos que AM tiene mejores que SyS — aprovéchalas

- **`PLAN_SEMESTRE.md` "Mapa de las 15 sesiones"** es una tabla de 6 columnas
  `| Sesión | Tema | Objetivos (OA) | Depende de | Hitos / formatos especiales | Demo principal |`.
  Trae el tema, los OA, **las dependencias entre sesiones** y la demo, todo estructurado.
  En SyS esa información estaba dispersa. Úsala como fuente principal.
- **`Depende de`** (`s03 (modos)`, `s10 (resonancia, impedancia)`) permite algo que SyS no
  tiene: mostrar en el panel **de qué sesiones depende esta y cuáles dependen de ella**.
  Muy útil al preparar. Impleméntalo.
- **El sidebar de `material/_quarto.yml`** ya asocia cada sesión con su apunte, sus
  actividades y su demo, con títulos legibles.

### Trampas verificadas

- **Las fechas del calendario no llevan año** (`vie 07-ago`). Toma el año del nombre del
  directorio (`ediciones/2026-2` → 2026) y déjalo explícito en el índice.
- El calendario tiene **filas de interrupción** con `—` en la primera columna
  (`vie 18-sep` receso, `vie 02-oct` sin clase por actividades suspendidas). No las
  descartes: van al riel cronológico, como en SyS.
- Hay **dos fuentes de fecha**: el calendario y el `subtitle` de las slides
  (`"MUC860 · Sesión 04 — La receta del timbre · vie 28-ago-2026"`). Compáralas y **anota
  un aviso si discrepan** — es un chequeo de consistencia gratis que SyS no puede hacer.
- `sesion-07` y `sesion-13` no tienen `actividades/`.
- `s15` no tiene demo (`— (sin demo nueva)` en `PLAN_SEMESTRE.md`).
- `plan.md` **no tiene front-matter YAML**. No copies `_front_matter()` de SyS para él;
  sí sirve para `slides_sNN.qmd`.

---

## Servidor: `panel/panel.py`

Endpoints, calcados de SyS más dos:

| Método | Ruta | Devuelve |
|---|---|---|
| GET | `/` | `panel_ui.html` |
| GET | `/api/indice` | índice completo |
| GET | `/api/frescura` | estado de los renders (`stat`, barato) |
| GET | `/api/md?ruta=…` | **nuevo**: Markdown convertido con pandoc, cacheado |
| GET | `/r/<montaje>/<ruta>` | estáticos |
| POST | `/api/abrir` | `open <ruta>` |
| POST | `/api/render` | re-render con Quarto |
| GET/POST | `/api/publicacion`, `/api/publicar` | ver abajo |

Montajes: `site` → `material/_render/site`, `canvas` → `material/_render/canvas`,
`figuras` → `material/assets/figuras`, `demos` → `material/demos`,
`libro` → `material/libro` (para servir `LIBRO_CURSO.pdf`).

Las demos son HTML autocontenido: se incrustan directamente desde el montaje `demos`.

Comandos de render (respetando la convención de AM):

```python
["conda", "run", "-n", "base", "quarto", "render", <ruta>]      # sitio
["conda", "run", "-n", "base", "quarto", "render", "libro"]     # PDF del libro
```

---

## Publicación: el modelo de AM es otro

**No copies el diálogo de publicación de SyS.** Allá la publicación es manual y gradual
(`liberar --semana N`) y por eso lleva tres capas de seguros. Aquí el sitio se publica
**solo**: cada `git push` a `main` dispara `.github/workflows/publish.yml` y el sitio se
reconstruye. No hay nada que "liberar".

Lo que el panel de AM debe mostrar en su lugar — todo de solo lectura y sin red:

1. **¿Hay cambios sin commitear?** (`git status --porcelain`).
2. **¿Está pusheado?** (`git rev-list --count @{u}..HEAD`) — si hay commits locales sin
   subir, el sitio publicado está atrasado respecto a lo que tienes.
3. **Último commit** y su fecha.
4. **Estado del último workflow** con `gh run list --limit 1` — `gh` está instalado
   (verificado, v2.90.0). Aun así, maneja su ausencia diciéndolo en vez de fingir.
5. **Canvas**: `python3 canvas/publicar_canvas.py estado` como acción explícita.
   `sync` **nunca publica ni borra** (así está escrito el script), así que es mucho menos
   peligroso que su equivalente en SyS — pero **igual va detrás de confirmación explícita**,
   y el panel debe arrancar con `--permitir-publicar` para siquiera ofrecerlo.

### Feature propia de AM: el PDF del libro se queda atrás en silencio

`.githooks/pre-commit` existe porque `material/libro/LIBRO_CURSO.pdf` es la única copia
versionada del libro y **el CI no lo reconstruye** (lo copia como recurso). El hook rechaza
commits que toquen capítulos sin regenerar el PDF, pero solo actúa al commitear.

El panel puede detectarlo antes: compara el `mtime` de `material/libro/cap*.md` contra el
del PDF y **muestra un semáforo propio**, con un botón que corre
`conda run -n base quarto render libro`. Es el equivalente AM del semáforo de frescura de
SyS y ataca un modo de falla real y documentado del repo.

Añade a la verificación: recordar que el hook se activa una vez por clon con
`git config core.hooksPath .githooks`, y avisar si no está configurado.

---

## Interfaz: `panel/panel_ui.html`

Parte del archivo de SyS y ajusta el contenido de las zonas. Conserva **tal cual**: el
CSS Grid/flex, las variables de color con modo oscuro, los interruptores por panel, los
presets, la persistencia en `localStorage`, los atajos de teclado, el control de reveal.js
por la API del mismo origen, y el `poner()/vacio()` que evita iframes en blanco.

Zonas propuestas:

- **Riel** — s01…s15 con fecha real, hito y las interrupciones intercaladas
  (receso 18-sep, sin clase 02-oct). Añade las dependencias: al elegir una sesión, resalta
  de cuáles depende y cuáles dependen de ella.
- **Plan de sesión** — el `plan.md` convertido con pandoc; selector Módulo 1/2/ambos;
  `Rol del profesor` y `Materiales` desplegables por fila.
- **Materiales de la sesión** — lista de chequeo agregada y deduplicada. Novedad de AM.
- **Slides** — iframe de `slides_sNN.html` con los controles de reveal.
- **Panel grande con pestañas** — `Apunte` · `Capítulo del libro` · `Demo`. Los dos
  primeros por iframe del render; la demo, del montaje `demos`.
- **Actividades** — las guías/pautas de la sesión, expandibles vía pandoc, con las
  `pauta_*` marcadas como solo-profesor.
- **Objetivos** — cada `OA<n>.<m>` con su texto completo y en qué otras sesiones aparece.

**Advertencia de visibilidad**: este panel muestra material solo-profesor (planes, pautas).
Es local y solo escucha en `127.0.0.1`, pero deja constancia en el README y **no escribas
nunca nada dentro de `material/_render/site/`**, que es lo que se publica.

---

## Orden de trabajo

1. **`indice.py` solo**, con `--verificar` y `--json s04`. Criterio de salida: las 15
   sesiones parsean, y los avisos que queden son explicables. Es la fase de más riesgo y no
   necesita una línea de HTML.
2. **`panel.py`**: `/api/indice`, montajes, `/api/md` con pandoc, guardarraíles.
3. **UI**: adaptar el HTML de SyS zona por zona.
4. **Frescura**: renders + el semáforo del PDF del libro.
5. **Publicación**: estado de git/CI/Canvas.
6. **`panel/README.md`**: qué parsea de dónde y, lo más valioso, **qué convenciones lo
   romperían** si se editan a mano.
7. Añadir `panel/` al mapa del `README.md` raíz y una línea en `CLAUDE.md`.

## Verificación (no te fíes del log: abre la pantalla)

1. `python3 panel/indice.py --verificar` → 15 sesiones sin avisos inexplicables.
2. Abrir el panel y **mirarlo**. En SyS esto encontró tres defectos que los tests no vieron.
   El `CLAUDE.md` de SyS documenta un caso donde el HTML se generaba sin error y la lámina
   salía en blanco: el log no basta.
3. Recorrer s01→s15 comprobando que ninguna zona queda vacía y que no aparece `undefined`
   ni `[object Object]`. Casos borde: `s07` y `s13` sin actividades, `s15` sin demo.
4. Verificar que la tabla del plan se ve **con sus cinco columnas** y la matemática
   renderizada (`$f_1 \propto 1/L$` aparece en varios planes).
5. Apagar y encender cada panel; recargar; confirmar que la combinación persiste.
6. Seguridad, con `curl`: `/r/site/../../../CLAUDE.md`, `/r/site/curso/sesion-01/plan.md`,
   un montaje inexistente, y `/api/md?ruta=../../etc/passwd` → los cuatro **404**.
7. `git status` no debe mostrar cambios en fuentes tras usar el panel.
8. Confirmar que `panel/` no aparece en `material/_render/site/`.

## Nota sobre el alcance

El panel de SyS quedó en ~2.100 líneas y fue descrito por el profesor como "tal vez la
herramienta más útil que hemos desarrollado". La mayor parte de ese valor viene de dos
decisiones que conviene repetir: **derivar las rutas por convención de nombres** en vez de
mantener un índice, y **decir la verdad sobre el estado de los artefactos** (semáforos de
frescura con ambos timestamps a la vista, avisos de parseo visibles) en lugar de aparentar
que todo está bien.
