# AM — Acústica Musical (UC)

Proyecto de diseño y construcción del curso, trabajado con Claude Code.
La publicación es un **sitio Quarto** (migración 2026-07-17).

- `CLAUDE.md` — memoria del proyecto (Claude Code la carga siempre).
- `.claude/rules/` — convenciones de estilo (apuntes y demos).
- `.claude/skills/` — flujos: /plan-sesion, /demo-interactiva,
  /revision-alineamiento.
- `_quarto.yml` / `index.qmd` / `styles.css` — el sitio del curso:
  configuración, mapa interactivo de inicio y estilo.
- `referencias/` — libros base (PDF) e índice de fuentes (fuera del
  sitio y del git).
- `diseno/` — objetivos, metodología, estructura y bitácora de
  revisiones de alineamiento.
- `sesiones/s01..s15/` — plan, apuntes, demos y actividades por sesión.
- `libro/` — lecturas previas por sesión; sub-proyecto Quarto **book**
  que compila `LIBRO_CURSO.pdf`.
- `materiales/` — planilla rúbrica OA3, apps recomendadas, banco de
  estímulos.
- `Admin/` — programa del curso; `Admin/obsoleto/` guarda el pipeline
  de publicación anterior (solo referencia histórica).
- `canvas/` — integración con Canvas UC (MUC860-1): `canvas.yml` es la
  estructura de módulos (espejo de la sidebar del sitio) y
  `publicar_canvas.py sync` la aplica; nunca publica ni borra.
- `figuras/` — figuras de apuntes y libro: SVG **generados por scripts**
  (`gen_sXX.py` + `estilo_figuras.py`; editar el script y volver a
  correrlo, no el SVG). `figuras/libros/` guarda las pocas figuras
  reproducidas desde la bibliografía, citadas en su leyenda y
  registradas en `figuras/libros/EXTRACCIONES.md`.
- `RESUMEN_PARA_PATO.md` — **la guía vigente del profesor**: estado,
  qué es público vs. solo-profesor, flujos de trabajo y pendientes
  (con el registro histórico del loop al final).
- `ESTADO_LOOP.md` — registro histórico de la producción autónoma de
  las fases 3–4 (2026-07-12/13); no se regenera.

## Flujo de publicación (Quarto)

Los `.md` son la **fuente de verdad**; el sitio se genera en `_site/`
(ignorado por git). Quarto 1.9 está instalado vía conda
(`conda run -n base quarto ...` si el shell no tiene conda activo).

- **Sitio completo**: `conda run -n base quarto render` (desde la raíz).
- **Mientras se edita**: `conda run -n base quarto preview`.
- **PDF del libro**: `conda run -n base quarto render libro`
  (sale a `libro/LIBRO_CURSO.pdf`; requiere LaTeX —Quarto usa
  lualatex— y rsvg-convert para las figuras SVG).
- **Documento nuevo PARA ALUMNOS**: crear el `.md` y agregarlo a la
  `sidebar` de `_quarto.yml` y a `canvas/canvas.yml` (+ `sync`); si es
  capítulo del libro, también a `chapters` de `libro/_quarto.yml` y al
  arreglo `S` del mapa en `index.qmd`.

**Publicación** (desde 2026-07-20): cada `git push` a `main` reconstruye
y despliega el sitio en <https://molivarito.github.io/acustica-musical>
vía GitHub Actions. **Regla de visibilidad** (2026-07-22): el sitio y
Canvas contienen SOLO material para estudiantes; lo solo-profesor
(planes de sesión, pautas, pruebas, guión, banco de estímulos, planilla
de rúbrica, `diseno/`) está excluido en el `render:` de `_quarto.yml` y
no debe enlazarse con links Markdown desde páginas públicas (solo
backticks). Guía completa en `RESUMEN_PARA_PATO.md`.

## Para partir

Copiar los PDF a `referencias/libros/`, abrir una terminal en esta
carpeta y ejecutar `claude`. Para la visión global del curso:
`conda run -n base quarto preview` (o abrir `_site/index.html`).
