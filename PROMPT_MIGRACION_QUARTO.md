# Prompt: migración del curso AM a Quarto

**Uso**: abrir un terminal en esta carpeta (`cursos/AM`), lanzar `claude` y pegar el prompt de abajo. Contexto previo: el curso hermano SyS ya usa Quarto con éxito (ver `../SyS/material/` como referencia de configuración). Quarto 1.9.38 está instalado vía conda-forge en miniforge3 base (`conda run -n base quarto ...` si el shell no tiene conda activado).

---

Vamos a migrar la infraestructura de publicación de este curso a **Quarto**, reemplazando el pipeline artesanal actual (gemelos HTML generados por `Admin/md2html.py`, mapa manual `Admin/mapa_curso.html`, libro compilado por `Admin/compilar_libro.py`). **El contenido Markdown no se toca salvo enlaces**: los `.md` siguen siendo la fuente de verdad; lo que cambia es cómo se renderizan y navegan. Referencia de un proyecto Quarto funcionando: `../SyS/material/` (`_quarto.yml`, `styles.css`, `README.md`).

Trabaja en fases, **commiteando en git al final de cada fase** (el repo ya existe):

**Fase 0 — Reconocimiento.** Lee `CLAUDE.md`, `README.md`, `Admin/md2html.py`, `Admin/estilo_md_header.html`, `Admin/mapa_curso.html` y 3–4 documentos representativos (un `plan.md` de sesión, un capítulo del libro, un doc de diseño). Inventaria: todos los enlaces internos entre documentos (especialmente los que apuntan a gemelos `.html`), el uso de matemática (el pipeline actual usa MathML), y las rutas de las 14 demos HTML.

**Fase 1 — Sitio Quarto del curso.**
1. Crea `_quarto.yml` (proyecto tipo `website`) en la raíz: barra lateral que replique la organización del mapa actual — Diseño (objetivos, metodología, estructura), Sesiones s01–s15 (cada plan + enlaces a sus apuntes, actividades y demos), Libro (los 15 capítulos como sección), Materiales, Admin/programa. Excluye del render: los gemelos `.html`, `ESTADO_LOOP.md`, `RESUMEN_PARA_PATO.md`, `PROMPT_MIGRACION_QUARTO.md`, `referencias/` y los `diseno/revision_*.md` (o agrúpalos en una sección "Bitácora de diseño" — decide y justifica).
2. Porta el estilo editorial de `Admin/estilo_md_header.html` a un `styles.css` de Quarto: conservar la identidad visual (fondo papel, serif para texto, acento rojo ladrillo, sans para controles). `html-math-method: katex`, `lang: es`.
3. Declara `sesiones/*/demos/` y `figuras/` como `resources` para que las demos autocontenidas y los SVG se copien al sitio; desde cada `plan.md`, enlaza sus demos (y evalúa embeber en iframe las 2–3 más usadas en clase).
4. Reescribe los enlaces internos que apuntan a gemelos `.html` para que apunten al `.md` correspondiente (Quarto los resuelve). Hazlo con un script (guárdalo en `Admin/`) y revisa manualmente una muestra.
5. Renderiza (`conda run -n base quarto render`), abre el resultado y verifica: navegación completa, matemática bien renderizada, figuras SVG visibles, demos accesibles, estilo fiel.

**Fase 2 — El libro como proyecto Quarto book.** Convierte `libro/` en un sub-proyecto `book` de Quarto (o un perfil del proyecto principal, decide y justifica): los 15 capítulos + prólogo → libro web navegable + PDF vía xelatex (las figuras SVG requieren `rsvg-convert`, ya disponible). Compara el PDF resultante con `libro/LIBRO_CURSO.pdf` actual; el nuevo debe ser igual o mejor tipográficamente antes de dar por reemplazado el pipeline.

**Fase 3 — Desmantelamiento y actualización de convenciones.** Solo cuando Fases 1–2 estén validadas: elimina los gemelos `.html` generados (NO las demos ni `Admin/estilo_md_header.html` hasta confirmar que nada más los usa), marca `Admin/md2html.py`, `compilar_libro.py` y `mapa_curso.html` como obsoletos (muévelos a `Admin/obsoleto/` con una nota), y actualiza `CLAUDE.md`, `README.md` y `.claude/rules/estilo-materiales.md`: la regla "tras editar un .md, correr md2html.py" se reemplaza por "tras editar, `quarto render` (o `quarto preview` mientras trabajas)"; documenta cómo agregar una sesión/capítulo nuevo al `_quarto.yml`.

**Reglas**: no edites el contenido pedagógico de los `.md` (solo enlaces y, si hace falta, cabecera YAML con `title`); no toques el interior de las demos HTML ni los scripts de figuras; el pipeline de figuras (`gen_sXX.py`) queda intacto; todo en español; si algo del pipeline actual cumple una función que Quarto no cubre, repórtalo antes de eliminarlo. Al terminar cada fase, muéstrame qué verificar antes de seguir.

Empieza con la Fase 0 y preséntame el plan detallado de la Fase 1 antes de ejecutarla.
