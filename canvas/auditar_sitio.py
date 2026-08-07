#!/usr/bin/env python3
"""auditar_sitio — busca fugas de material solo-profesor en el sitio renderizado.

Red de seguridad de la regla de visibilidad (CLAUDE.md, 2026-07-22): el
sitio publicado contiene SOLO material para estudiantes. Este script
recorre el directorio renderizado (material/_render/site por defecto) y
termina con código 1 si encuentra:

  - archivos cuyo nombre delate material solo-profesor (plan.md, *pauta*,
    guion_profesor*, banco_estimulos*, planilla_rubrica*, documentos
    rectores, estado de agenda);
  - fuentes crudas .md o .qmd copiadas como "recurso" (pasa cuando una
    página pública enlaza con link Markdown un archivo excluido del
    render — por eso la regla de "solo backticks");
  - con --sin-slides: cualquier slides_s*.html (se renderizan para el
    profesor pero el CI las borra antes del deploy).

Uso:
  python3 canvas/auditar_sitio.py                # audita material/_render/site
  python3 canvas/auditar_sitio.py --sin-slides   # modo CI (post-filtrado)
  python3 canvas/auditar_sitio.py RUTA           # audita otra carpeta

Patrón heredado de auditar_publico() de SyS/canvas/publicar_sitio.py
(2026-08-06).
"""

import sys
from pathlib import Path

# Subcadenas prohibidas en el NOMBRE de archivo (en minúsculas).
NOMBRES_PROHIBIDOS = [
    "plan.md", "pauta", "guion_profesor", "banco_estimulos",
    "planilla_rubrica", "objetivos_aprendizaje", "metodologia",
    "plan_semestre", "agenda_estado",
]

# Extensiones de fuente cruda que jamás deberían llegar al sitio.
EXTENSIONES_PROHIBIDAS = {".qmd", ".md"}

# Directorios que jamás deberían llegar al sitio (cualquier segmento
# de la ruta). proyectos_antiguos: fotos de archivo con personas
# identificables — solo para proyectar en clase (2026-08-07).
DIRECTORIOS_PROHIBIDOS = {"proyectos_antiguos", "estimulos"}


def auditar(raiz: Path, sin_slides: bool) -> list[str]:
    fugas = []
    for p in sorted(raiz.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(raiz)
        nombre = p.name.lower()
        if sin_slides and any(seg in DIRECTORIOS_PROHIBIDOS
                              for seg in rel.parts[:-1]):
            # solo en modo CI: localmente estos directorios existen en el
            # render (los usan las slides); el CI los borra antes del deploy
            fugas.append(f"directorio solo-profesor copiado al sitio: {rel}")
        elif any(patron in nombre for patron in NOMBRES_PROHIBIDOS):
            fugas.append(f"nombre solo-profesor: {rel}")
        elif p.suffix.lower() in EXTENSIONES_PROHIBIDAS:
            fugas.append(f"fuente cruda copiada al sitio: {rel}")
        elif sin_slides and nombre.startswith("slides_s") and p.suffix == ".html":
            fugas.append(f"slides no filtradas: {rel}")
    return fugas


def main() -> int:
    args = [a for a in sys.argv[1:]]
    sin_slides = "--sin-slides" in args
    args = [a for a in args if a != "--sin-slides"]
    raiz = Path(args[0]) if args else Path("material/_render/site")
    if not raiz.is_dir():
        print(f"ERROR: no existe el directorio renderizado {raiz} "
              "(¿corriste `quarto render` desde material/?)", file=sys.stderr)
        return 2
    fugas = auditar(raiz, sin_slides)
    if fugas:
        print(f"FUGAS DETECTADAS en {raiz} ({len(fugas)}):")
        for f in fugas:
            print(f"  ✗ {f}")
        print("\nRevisar la regla de visibilidad en CLAUDE.md: material "
              "solo-profesor va excluido del render y se menciona solo "
              "con backticks, nunca con links Markdown.")
        return 1
    print(f"OK: sin fugas de material solo-profesor en {raiz}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
