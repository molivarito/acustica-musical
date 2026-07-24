#!/usr/bin/env python3
"""Compila el libro del curso: libro/LIBRO_CURSO.md (+ PDF si hay pandoc).

Uso:  python3 Admin/compilar_libro.py        (desde la raíz del proyecto)

- Concatena libro/00_prologo.md + cap01..cap15 con portada, índice y
  bibliografía unificada.
- Genera el PDF con pandoc/xelatex (las figuras SVG requieren
  rsvg-convert instalado; las rutas ../figuras/ se resuelven ejecutando
  pandoc con cwd=libro/).
- Correrlo después de editar cualquier capítulo o agregar figuras.
"""
import glob
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
LIBRO = RAIZ / 'libro'

PORTADA = """# Escuchar como científico
### Lecturas del curso Acústica Musical

Patricio de la Cuadra · Pontificia Universidad Católica de Chile
Instituto de Música / Departamento de Ingeniería Eléctrica

Compilado del material de lectura previa de las 15 sesiones del curso.
Cada capítulo se lee antes de la sesión correspondiente (≤1 hora).

---

## Índice
"""

BIBLIO = """
---

# Bibliografía del curso

Las cuatro fuentes que respaldan este libro, en su jerarquía de uso.
Cada capítulo cita al cierre las secciones específicas que lo respaldan;
las figuras reproducidas desde las fuentes lo indican en su leyenda.

- **Campbell, M. & Greated, C. (1987).** *The Musician's Guide to
  Acoustics*. Oxford: Oxford University Press (reimpresión 2001).
  ISBN 0-19-816505-6. — Texto principal de lectura complementaria;
  se cita por página impresa.
- **Benade, A. H. (1990).** *Fundamentals of Musical Acoustics: Second,
  Revised Edition*. New York: Dover. ISBN 0-486-26484-X. — Intuición
  física y experimentos (secciones EEQ); se cita por capítulo y sección.
- **Roederer, J. G. (1997).** *Acústica y Psicoacústica de la Música*
  (trad. G. D. Pozzati). Buenos Aires: Ricordi Americana.
  ISBN 950-22-0444-1. — Percepción y psicoacústica; lectura alternativa
  en español; se cita por página impresa.
- **Rossing, T. D., Moore, F. R. & Wheeler, P. A. (2002).** *The Science
  of Sound*, 3.ª ed. San Francisco: Addison-Wesley. — Banco de problemas
  y ejercicios (no es lectura obligatoria); se cita por capítulo.

Referencia avanzada opcional para el proyecto (disponibilidad en
biblioteca UC **[POR VERIFICAR]**): Fletcher, N. H. & Rossing, T. D.,
*The Physics of Musical Instruments*, 2.ª ed., Springer, 1998.
"""


def titulo_de(md: Path) -> str:
    for linea in md.read_text(encoding='utf-8').splitlines():
        if linea.startswith('# '):
            return linea[2:].strip()
    return md.stem


def ancla(t: str) -> str:
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^\w\s-]', '', t.lower())
    return re.sub(r'\s+', '-', t).strip('-')


def main() -> int:
    caps = sorted(LIBRO.glob('cap[0-9][0-9]_*.md'))
    prologo = LIBRO / '00_prologo.md'
    partes = [PORTADA]
    indice = [prologo] + caps
    partes += [f'- [{titulo_de(p)}](#{ancla(titulo_de(p))})' for p in indice]
    partes.append('- [Bibliografía del curso](#bibliografia-del-curso)')
    partes.append('\n---\n')
    partes.append(prologo.read_text(encoding='utf-8').strip())
    for c in caps:
        partes.append('\n---\n')
        partes.append(c.read_text(encoding='utf-8').strip())
    partes.append(BIBLIO)
    (LIBRO / 'LIBRO_CURSO.md').write_text('\n'.join(partes) + '\n',
                                          encoding='utf-8')
    print(f'LIBRO_CURSO.md: {len(caps)} capítulos compilados.')

    # PDF (pandoc corre con cwd=libro/ para resolver ../figuras/)
    r = subprocess.run(
        ['pandoc', 'LIBRO_CURSO.md', '-o', 'LIBRO_CURSO.pdf',
         '--pdf-engine=xelatex', '-V', 'lang=es',
         '-V', 'geometry:margin=2.5cm', '--toc-depth=1'],
        cwd=LIBRO, capture_output=True, text=True)
    if r.returncode:
        print('PDF FALLÓ (el .md sí quedó compilado):')
        print(r.stderr[-600:])
        return 1
    print('LIBRO_CURSO.pdf generado.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
