#!/usr/bin/env python3
"""Genera el paquete de impresión de una sesión (tarea `imprimir-NN`).

Convierte con pandoc cada actividad de material/curso/sesion-NN/actividades/
a HTML imprimible en ediciones/<ed>/impresiones_sNN/, más la hoja de rúbrica
OA3 del profesor. Imprimir es abrir cada HTML en el navegador y Cmd+P.

Uso (desde la raíz del repo):
    python3 ediciones/2026-2/generar_impresiones.py 03       # una sesión
    python3 ediciones/2026-2/generar_impresiones.py --todas  # todas
Re-ejecutar refresca todo: conviene correrlo el mismo jueves de la
impresión, por si una guía cambió después de generado el paquete.
"""

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
EDICION = Path(__file__).resolve().parent          # ediciones/2026-2
# La "hoja de escucha" de todas las semanas es la rúbrica OA3 de los
# estudiantes (vive en s01, se reimprime cada sesión con escucha).
RUBRICA = RAIZ / "material/curso/sesion-01/actividades/rubrica_oa3_hoja.md"


def generar(nn):
    origen = RAIZ / f"material/curso/sesion-{nn}/actividades"
    destino = EDICION / f"impresiones_s{nn}"
    if not origen.is_dir():
        print(f"s{nn}: sin actividades/ (sesión de prueba) — nada que imprimir")
        return
    destino.mkdir(exist_ok=True)
    # Fuentes: las actividades de la sesión, la rúbrica del profesor y los
    # .md locales del propio paquete (p. ej. el guion relámpago de s01).
    # Se excluyen los archivos históricos que el diseño conserva como
    # registro pero que no se imprimen (hallazgo del barrido de s15).
    HISTORICOS = {"hoja_coevaluacion_final.md"}
    fuentes = [f for f in sorted(origen.glob("*.md")) if f.name not in HISTORICOS] \
        + [RUBRICA] + sorted(destino.glob("*.md"))
    for f in fuentes:
        salida = destino / (("rubrica_oa3_hoja" if f == RUBRICA else f.stem) + ".html")
        subprocess.run(["pandoc", "-s", "--mathml", str(f), "-o", str(salida),
                        "--metadata", "lang=es"], check=True)
        print(f"s{nn}: {salida.name}")
    # HTMLs huérfanos (su .md ya no existe) y frescura
    esperados = {("rubrica_oa3_hoja" if f == RUBRICA else f.stem) + ".html"
                 for f in fuentes}
    for h in destino.glob("*.html"):
        if h.name not in esperados:
            print(f"s{nn}: AVISO — {h.name} no tiene fuente .md (¿borrarla?)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--todas":
        nns = [f"{i:02d}" for i in range(1, 16)]
    else:
        nns = [sys.argv[1].zfill(2)]
    for nn in nns:
        generar(nn)
