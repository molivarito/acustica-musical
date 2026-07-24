# Pipeline anterior a Quarto (obsoleto desde 2026-07-17)

Estos archivos eran la infraestructura de publicación previa a la
migración a Quarto y se conservan solo como referencia histórica.
**No usarlos**: regenerarían artefactos que ya no existen.

| Archivo | Qué hacía | Reemplazo |
|---|---|---|
| `md2html.py` | Generaba un gemelo `.html` por cada `.md` (pandoc + MathML) | `quarto render` (sitio completo) |
| `estilo_md_header.html` | CSS embebido en cada gemelo | `styles.css` del sitio |
| `compilar_libro.py` | Concatenaba capítulos en `LIBRO_CURSO.md` y compilaba el PDF | sub-proyecto book: `quarto render libro` |
| `mapa_curso.html` | Mapa interactivo standalone (enlazaba a los gemelos) | `index.qmd` del sitio (misma interactividad) |
| `enlazar_docs.py` | Reescritura masiva de enlaces (herramienta de la migración, ya ejecutada) | — |

Si en el futuro se elimina esta carpeta, no se pierde nada operativo.
