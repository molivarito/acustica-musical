# Guía de Quarto y YAML — operación del repo AM

Todo el material del curso está escrito en Quarto. Esta guía explica cómo
funciona el proyecto Quarto de `material/`, la anatomía de su
`_quarto.yml`, el flujo de publicación por CI y la integración con Canvas.
Referencia hermana (más didáctica sobre Quarto/YAML en general):
`GUIA_QUARTO_YML.md` de SyS.

---

## Parte 1 · Dónde pararse: siempre en `material/`

A diferencia de SyS (que tiene varios sub-proyectos Quarto: sitio, Reader,
formularios), en AM hay **un solo proyecto principal**, anclado en
`material/`, más un sub-proyecto book para el libro:

| Proyecto | Carpeta donde pararse | Comando | Produce |
|---|---|---|---|
| **Sitio del curso** | `material/` | `conda run -n base quarto render` | `_render/site/` |
| ídem, mientras editas | `material/` | `conda run -n base quarto preview` | servidor local con recarga automática |
| Perfil canvas (sin sidebar) | `material/` | `conda run -n base quarto render --profile canvas` | `_render/canvas/` |
| **Libro** ("Escuchar como científico") | `material/libro/` (o `quarto render libro` desde `material/`) | `conda run -n base quarto render libro` | `material/libro/LIBRO_CURSO.pdf` |

**El error más común**: correr `quarto render` desde la raíz del repo (`AM/`)
en vez de `material/`. Quarto busca un `_quarto.yml` hacia arriba desde el
directorio actual; si te paras en la raíz no lo encuentra (no hay
`_quarto.yml` en `AM/`, solo en `material/` y `material/libro/`).

Comando `quarto` si el shell no activa conda:
`/Users/pdelac/miniforge3/bin/conda run -n base quarto`.

---

## Parte 2 · Qué es `_render/` y por qué no se edita ni versiona

`material/_render/` es la salida generada: `site/` (el sitio completo) y
`canvas/` (el perfil sin sidebar para los módulos de Canvas). Está en
`.gitignore` (`/material/_render/`) porque:

- Se regenera por completo con `quarto render` — cualquier edición manual
  se pierde en el próximo render.
- El CI de GitHub Actions lo genera desde cero en cada `git push` a `main`
  (ver Parte 5) — no hace falta commitearlo para publicar.
- Confundir fuente y salida es la causa más común de "edité pero no
  cambió nada": si editaste un `.html` dentro de `_render/`, editaste la
  salida, no la fuente.

La única salida que SÍ se versiona es `material/libro/LIBRO_CURSO.pdf`: es
un entregable, no un artefacto intermedio, y no se regenera en el CI (el
PDF del libro se arma a mano, cuando corresponda, con `quarto render libro`).

---

## Parte 3 · Anatomía de `material/_quarto.yml`

```yaml
project:
  type: website
  output-dir: _render/site
  render:
    - index.qmd
    - programa_curso.md
    - curso/**/*.md
    - curso/**/slides_*.qmd
    - "!curso/**/plan.md"
    - "!curso/**/*pauta*.md"
    - "!curso/**/guion_profesor*.md"
    - libro/*.md
    - apps_recomendadas.md
  resources:
    - "demos/*.html"
    - "assets/figuras/*.svg"
    - "assets/figuras/libros/*.png"
    - "libro/LIBRO_CURSO.pdf"
```

### `render:` — la lista blanca (y sus exclusiones)

El sitio es el artefacto **para estudiantes**. `render:` es una lista
blanca de globs: solo lo que calza entra al sitio. Los patrones que
empiezan con `!` son exclusiones DENTRO de un glob ya incluido — por
ejemplo `curso/**/*.md` incluiría `plan.md` y cualquier `*pauta*.md` si no
fuera por las líneas `!` que los vetan explícitamente.

**Por qué esto importa más de lo que parece**: `material/curso/sesion-NN/`
mezcla, en la misma carpeta, archivos para alumnos (`apunte_*.md`,
`actividades/*.md`) y archivos solo-profesor (`plan.md`, `*pauta*.md`,
`slides_sNN.qmd` — este último SÍ se renderiza, ver Parte 4). Como no hay
una carpeta separada "solo-profesor", la exclusión vive en el nombre de
archivo + el patrón `!` en `_quarto.yml`. Si agregas un archivo
solo-profesor nuevo cuyo nombre no calza con ninguna exclusión existente
(ni `plan.md`, ni contiene `pauta`, ni `guion_profesor`), **se publica sin
que nadie lo note** — agrega su patrón a `render:`.

**La regla de los backticks**: aunque un archivo esté fuera de `render:`,
si otra página CON render (un apunte, el libro, `index.qmd`) lo enlaza con
un link Markdown normal (`[texto](plan.md)`), Quarto copia el `.md` crudo
tal cual a `_render/site` para que el link no quede roto — burlando la
exclusión por la puerta de atrás. Por eso, en material solo-profesor,
**nunca usar `[texto](archivo)`; solo mencionarlo entre backticks**
(`` `plan.md` ``). Esta regla se aplica en todo el repo, no solo en
`material/`.

### `resources:`

Archivos que el sitio necesita servir pero que Quarto no debe intentar
"renderizar" como páginas (no son `.qmd`/`.md`): las demos HTML (ya son
páginas completas, se embeben o enlazan tal cual), las figuras SVG, las
imágenes reproducidas de libros, y el PDF del libro. Si agregas un tipo de
recurso nuevo (otro formato de imagen, un audio suelto), agrégalo aquí o
Quarto no lo copiará a `_render/site`.

### La sidebar

Refleja la navegación: mapa → programa → una `section:` por sesión (con
su apunte, sub-`section:` de actividades y la demo asociada) → libro →
materiales transversales. Es la fuente de la que se derivan, a mano,
`canvas/canvas.yml` (mismo orden, para los módulos de Canvas) y el arreglo
`S` de `material/index.qmd` (mismo contenido, para el mapa interactivo).
Las tres NO se sincronizan automáticamente entre sí — de ahí los "4
lugares" de la Parte 4.

---

## Parte 4 · Los 4 lugares al agregar material nuevo para alumnos

Cuando crees un `.md`/`.qmd` nuevo destinado a estudiantes (un apunte, una
guía de actividad, un capítulo), tócalo en los 4 lugares o quedará huérfano
(existe en el repo pero nadie lo encuentra o no se publica):

1. **`render:` de `material/_quarto.yml`** — solo si el archivo cae fuera
   de los globs ya listados (por ejemplo, algo que no está bajo `curso/**`
   ni es `libro/*.md`).
2. **`sidebar` de `material/_quarto.yml`** — para que aparezca en la
   navegación del sitio.
3. **Mapa `material/index.qmd`, arreglo `const S = [...]`** — cada sesión
   es un objeto con sus campos (`ap:` el apunte, `acts:` las actividades,
   etc.); agrega la entrada correspondiente para que el mapa interactivo la
   muestre y filtre por objetivo.
4. **`canvas/canvas.yml`** (+ correr `python3 publicar_canvas.py sync` desde
   `canvas/`) — para que Canvas tenga el ítem espejo, creado sin publicar.

Si además es un **capítulo del libro**, quinto lugar:
`chapters` de `material/libro/_quarto.yml`.

Grep de irradiación útil tras el cambio:

```bash
# ¿el archivo nuevo quedó excluido sin querer?
grep -n "render:" -A 15 material/_quarto.yml
# ¿aparece en el mapa?
grep -n "sesion-NN" material/index.qmd
# ¿aparece en Canvas?
grep -n "sesion-NN\|nombre_del_archivo" canvas/canvas.yml
```

---

## Parte 5 · Slides: fuente, preview y filtrado por CI

Cada sesión tiene su `slides_sNN.qmd` junto al resto de sus archivos en
`material/curso/sesion-NN/`. A diferencia de `plan.md` y `*pauta*.md`, las
slides SÍ están dentro de `render:` (se renderizan como HTML), porque
Quarto necesita procesarlas para generar el `.html` — pero no deben quedar
públicas.

Flujo:

1. Editas `curso/sesion-NN/slides_sNN.qmd`.
2. `conda run -n base quarto preview` (desde `material/`) y navegas a
   `curso/sesion-NN/slides_sNN.html` para verlas con recarga automática; o
   `quarto render curso/sesion-NN/slides_sNN.qmd` para regenerar solo esa.
3. El **filtrado ocurre en el CI**, no localmente: el workflow
   `.github/workflows/publish.yml` tiene un paso explícito, "Filtrar
   material solo-profesor del deploy", que corre después de renderizar y
   antes de publicar:

   ```bash
   find material/_render/site -name 'slides_s*.html' -delete
   ```

   Esto significa que en tu `_render/site/` local (tras un `quarto render`
   normal) las slides SÍ están presentes — solo se eliminan en el paso de
   deploy del CI. Si algún día ese paso desaparece del workflow (se edita
   mal, se borra, se reemplaza), **las slides quedan públicas en el
   próximo push sin que nada avise** — es la pieza más frágil del pipeline
   de privacidad. Verificar tras cualquier cambio al workflow:

   ```bash
   # después de un deploy, confirmar que no hay slides publicadas
   curl -s https://molivarito.github.io/acustica-musical/curso/sesion-01/slides_s01.html -o /dev/null -w "%{http_code}\n"
   # debe dar 404
   ```

---

## Parte 6 · Canvas: `canvas.yml`, sync y verificar

`canvas/canvas.yml` es un espejo manual de la sidebar de
`material/_quarto.yml`: mismos módulos, mismo orden, mismas exclusiones de
privacidad (no incluye pautas, pruebas, `plan.md`, banco de estímulos ni
planilla de rúbrica). El curso es MUC860-1 (`curso_id: 112005`).

```bash
cd canvas
python3 publicar_canvas.py estado          # estado actual del curso en Canvas
python3 publicar_canvas.py sync --dry-run  # qué haría sync, sin escribir
python3 publicar_canvas.py sync            # crea/actualiza módulos e ítems
python3 publicar_canvas.py verificar       # revisa que las URL del sitio no den 404
```

Reglas del script (no negociables, ver `canvas/README.md`):

- Todo lo nuevo se crea con `published: false`.
- **Nunca** cambia el estado de publicación de algo que ya existía.
- **Nunca** borra ni despublica — si algo está en Canvas pero no en
  `canvas.yml`, se reporta como "extra" y no se toca.
- Publicar cada módulo/ítem, semana a semana, es una acción manual tuya
  desde la interfaz de Canvas — el script nunca lo hace por ti.

El token de la API (`CANVAS_TOKEN` o `~/.canvas_token`) nunca debe escribirse
en `canvas.yml`, en código, ni en ningún archivo de este repo.

---

## Parte 7 · Publicación por CI (GitHub Actions)

A diferencia de SyS (que publica con un script que corres a mano,
`publicar_sitio.py liberar`), AM publica automáticamente:
`.github/workflows/publish.yml` se dispara en cada `push` a `main` (o a
mano con `workflow_dispatch`) y:

1. Renderiza el sitio (`quarto render`, perfil por defecto) desde
   `material/`.
2. Renderiza el perfil `canvas` y copia su salida dentro de `_render/site/canvas`.
3. Filtra las slides del deploy (Parte 5).
4. Publica `material/_render/site` a GitHub Pages
   (<https://molivarito.github.io/acustica-musical>).

Implicación práctica: **no hace falta correr `quarto render` a mano para
publicar** — solo para previsualizar antes de hacer push. Si el push no
dispara el deploy esperado, lo primero es mirar la pestaña Actions del
repo en GitHub, no repetir el render local.

---

## Chuleta final

```bash
# preparar (una vez, si el shell no activa conda)
alias quarto="/Users/pdelac/miniforge3/bin/conda run -n base quarto"

# sitio (desde material/)
cd material && quarto render
quarto preview

# perfil canvas
quarto render --profile canvas

# una sola slide (más rápido que el sitio completo)
quarto render curso/sesion-05/slides_s05.qmd

# libro → PDF
quarto render libro

# Canvas (desde canvas/)
cd ../canvas
python3 publicar_canvas.py sync --dry-run
python3 publicar_canvas.py sync
python3 publicar_canvas.py verificar

# figuras: editar el script, no el SVG
python3 material/assets/figuras/gen_s07.py
```

Regla de oro: nunca edites nada dentro de `material/_render/` — es salida
generada; el próximo render (local o del CI) la pisa.
