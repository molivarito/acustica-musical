# AM — Acústica Musical (UC)

Proyecto de diseño y construcción del curso, trabajado con Claude Code.

- `CLAUDE.md` — memoria del proyecto (Claude Code la carga siempre).
- `.claude/rules/` — convenciones de estilo (apuntes y demos).
- `.claude/skills/` — flujos: /plan-sesion, /demo-interactiva,
  /revision-alineamiento.
- `referencias/` — libros base (PDF) e índice de fuentes.
- `diseno/` — objetivos, metodología y estructura del curso.
- `sesiones/s01..s15/` — plan, apuntes, demos y actividades por sesión.
- `libro/` — lecturas previas por sesión + compilado `LIBRO_CURSO.md/.pdf`.
- `materiales/` — planilla rúbrica OA3, apps recomendadas, banco de estímulos.
- `Admin/` — mapa navegable del curso (`mapa_curso.html`), programa del
  curso, y la infraestructura de vistas HTML (ver abajo).
- `ESTADO_LOOP.md` / `RESUMEN_PARA_PATO.md` — estado y balance de la
  producción autónoma de las fases 3–4.

## Vistas HTML de los .md

Los `.md` son la **fuente de verdad** (lo que se edita); cada uno tiene
un gemelo `.html` **generado** con formato legible (estilo editorial,
ecuaciones en MathML, sin dependencias de red). El mapa del curso y los
enlaces internos apuntan a esos `.html`.

- Regenerar después de editar cualquier `.md`:
  `python3 Admin/md2html.py` (desde la raíz; requiere pandoc).
- El estilo compartido vive en `Admin/estilo_md_header.html` (queda
  embebido: cada HTML es autocontenido).
- No editar los `.html` generados a mano: se pisan al regenerar.

## Para partir

Copiar los PDF a `referencias/libros/`, abrir una terminal en esta
carpeta y ejecutar `claude`. Para la visión global del curso, abrir
`Admin/mapa_curso.html` en el navegador.
