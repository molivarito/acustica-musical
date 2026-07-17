#!/usr/bin/env python3
"""Convierte referencias en backticks en enlaces markdown (migración Quarto).

Uso:  python3 Admin/enlazar_docs.py [--dry-run]     (desde la raíz)

Los .md del curso se referenciaban entre sí con rutas en backticks
(`libro/cap03_modos_de_vibracion.md`, `demo_batidos.html`) porque la
navegación vivía en los gemelos HTML y el mapa. Con Quarto los enlaces
van en el propio .md. Este script, corrido una vez en la migración
(2026-07-17), convierte:

  `demo_X.html`          -> [`demo_X.html`](<ruta relativa a la demo>)
  `<dir>/<doc>.md`       -> [`<dir>/<doc>.md`](<ruta relativa al doc>)
     (solo si el destino existe y está en diseno/, sesiones/, libro/
      o materiales/)

No toca nada más: ni prosa, ni referencias a archivos inexistentes
(p. ej. `demo_octava.html`, nunca producida), ni lo que ya es enlace.
Es idempotente: una referencia ya convertida no se vuelve a tocar.
"""
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIRS_DOCS = ('diseno/', 'sesiones/', 'libro/', 'materiales/')
EXCLUIR_DESTINOS = {'libro/LIBRO_CURSO.md'}  # compilado, fuera del sitio

# Archivos a procesar: los .md del sitio (no CLAUDE/README/estado/skills)
def archivos_a_procesar():
    for patron in ('diseno/*.md', 'sesiones/**/*.md', 'libro/*.md',
                   'materiales/*.md', 'Admin/programa_curso.md'):
        for p in RAIZ.glob(patron):
            if p.name != 'LIBRO_CURSO.md':   # generado, no se toca
                yield p

# Mapa nombre de demo -> ruta (todas tienen nombre único)
DEMOS = {p.name: p for p in RAIZ.glob('sesiones/*/demos/*.html')}


def rel(destino: Path, desde: Path) -> str:
    return os.path.relpath(destino, desde.parent).replace(os.sep, '/')


def convertir(md: Path, texto: str) -> tuple[str, int]:
    n = 0

    def ya_enlazado(m):
        # `x` precedido de "[" o seguido de "](" ya es un enlace
        return (m.start() > 0 and m.string[m.start() - 1] == '[') or \
               m.string[m.end():m.end() + 2] == ']('

    def reemplazo_demo(m):
        nonlocal n
        nombre = m.group(1)
        if nombre not in DEMOS or ya_enlazado(m):
            return m.group(0)
        n += 1
        return f'[`{nombre}`]({rel(DEMOS[nombre], md)})'

    def reemplazo_doc(m):
        nonlocal n
        ruta = m.group(1)
        destino = RAIZ / ruta
        if (not ruta.startswith(DIRS_DOCS) or ruta in EXCLUIR_DESTINOS
                or not destino.is_file()
                or ya_enlazado(m)):
            return m.group(0)
        n += 1
        return f'[`{ruta}`]({rel(destino, md)})'

    lineas, dentro_fence = [], False
    for linea in texto.splitlines(keepends=True):
        if linea.lstrip().startswith('```'):
            dentro_fence = not dentro_fence
        if not dentro_fence:
            linea = re.sub(r'`(demo_[a-z0-9_]+\.html)`', reemplazo_demo, linea)
            linea = re.sub(r'`([\w./-]+\.md)`', reemplazo_doc, linea)
        lineas.append(linea)
    return ''.join(lineas), n


def main() -> int:
    dry = '--dry-run' in sys.argv
    total = 0
    for md in sorted(archivos_a_procesar()):
        texto = md.read_text(encoding='utf-8')
        nuevo, n = convertir(md, texto)
        if n:
            total += n
            print(f'{md.relative_to(RAIZ)}: {n} referencia(s) enlazada(s)')
            if not dry:
                md.write_text(nuevo, encoding='utf-8')
    print(f'Total: {total} referencias{" (dry-run, sin escribir)" if dry else ""}.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
