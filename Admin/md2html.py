#!/usr/bin/env python3
"""Convierte todos los .md del proyecto a .html hermanos, con pandoc.

Uso:  python3 Admin/md2html.py        (desde la raíz del proyecto)

- Genera foo.html junto a cada foo.md (sesiones/, libro/, diseno/,
  materiales/, referencias/notas/, Admin/ y la raíz).
- Ecuaciones LaTeX → MathML nativo (sin internet ni CDN).
- Los enlaces internos hacia otros .md se reescriben a .html.
- Estilo compartido: Admin/estilo_md_header.html (queda embebido:
  cada HTML es autocontenido).
- Idempotente: correrlo de nuevo regenera todo. Correrlo después de
  editar cualquier .md del curso.
"""
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
HEADER = RAIZ / 'Admin' / 'estilo_md_header.html'
EXCLUIR = {'.git', 'referencias/libros', 'node_modules'}
# El libro compilado ya tiene su PDF; convertirlo igual no molesta.

def excluido(p: Path) -> bool:
    rel = p.relative_to(RAIZ).as_posix()
    return any(rel == e or rel.startswith(e + '/') for e in EXCLUIR)

def titulo_de(md: Path) -> str:
    for linea in md.read_text(encoding='utf-8').splitlines():
        if linea.startswith('# '):
            return linea[2:].strip()
    return md.stem

def convertir(md: Path) -> bool:
    salida = md.with_suffix('.html')
    cmd = [
        'pandoc', str(md), '-o', str(salida),
        '--standalone', '--mathml',
        '--from', 'markdown+tex_math_dollars',
        '--include-in-header', str(HEADER),
        '--metadata', f'pagetitle={titulo_de(md)}',
        '--metadata', 'lang=es',
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f'  ERROR {md.relative_to(RAIZ)}: {r.stderr.strip()[:200]}')
        return False
    # Reescribir enlaces internos .md → .html (relativos, no URLs externas)
    html = salida.read_text(encoding='utf-8')
    html = re.sub(r'href="(?!https?://)([^"]+)\.md(#[^"]*)?"',
                  r'href="\1.html\2"', html)
    salida.write_text(html, encoding='utf-8')
    return True

def main():
    mds = [p for p in RAIZ.rglob('*.md') if not excluido(p)]
    ok = sum(convertir(p) for p in sorted(mds))
    print(f'{ok}/{len(mds)} archivos convertidos.')
    return 0 if ok == len(mds) else 1

if __name__ == '__main__':
    sys.exit(main())
