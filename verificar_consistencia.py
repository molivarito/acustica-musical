#!/usr/bin/env python3
"""verificar_consistencia — el mapa de relaciones del curso, ejecutable.

Chequea que los HECHOS del diseño (DATOS_CURSO.yml) sigan afirmados en
todos los documentos que los repiten, y que ningún documento conserve
términos de diseños anteriores (2026-08: 20→9 estudiantes, proyecto
grupal→individual, grupos estables→mesas por tramo).

Nació el 2026-08-07 tras una semana de rediseños en que los barridos
manuales dejaron pasar inconsistencias semánticas. Regla de proceso
(CLAUDE.md): todo rediseño parte por DATOS_CURSO.yml y termina cuando
este verificador pasa en limpio.

Uso:
  python3 verificar_consistencia.py            # todo
  python3 verificar_consistencia.py --rapido   # sin chequeo de canvas/render

Corre además en el hook pre-commit (--rapido) y en el CI (completo).
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: falta PyYAML (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

RAIZ = Path(__file__).resolve().parent
DATOS = yaml.safe_load((RAIZ / "DATOS_CURSO.yml").read_text())

# Dónde buscar términos prohibidos (fuentes vivas; _archivo/ y las
# memorias quedan fuera: son registro histórico).
AMBITO_PROHIBIDOS = [
    "METODOLOGIA.md", "PLAN_SEMESTRE.md",
    "material/programa_curso.md", "material/index.qmd",
    "material/curso", "material/libro", "material/demos",
    "material/profesor", "panel/agenda_reglas.yml",
    "ediciones/2026-2",
]
EXT_TEXTO = {".md", ".qmd", ".yml"}

fallas, avisos = [], []


def archivos_ambito():
    for base in AMBITO_PROHIBIDOS:
        p = RAIZ / base
        if p.is_file():
            yield p
        elif p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.suffix in EXT_TEXTO and "_render" not in f.parts:
                    yield f


def chequear_prohibidos():
    cfg = DATOS["prohibidos"]
    patrones = [p.lower() for p in cfg["patrones"]]
    marcas = [m.lower() for m in cfg["permitir_si_contiene"]]
    exentos = {str(RAIZ / e) for e in cfg.get("archivos_exentos", [])}
    for f in archivos_ambito():
        if str(f) in exentos:
            continue
        try:
            lineas = f.read_text().splitlines()
        except Exception:
            continue
        for i, linea in enumerate(lineas):
            baja = linea.lower()
            if baja.lstrip().startswith("#"):
                continue                      # comentario (yml) deliberado
            for pat in patrones:
                if pat in baja:
                    # ventana de contexto: línea anterior + actual +
                    # siguiente (la prosa a 72 columnas corta frases)
                    ventana = " ".join(
                        lineas[j].lower()
                        for j in range(max(0, i - 1), min(len(lineas), i + 2)))
                    if not any(m in ventana for m in marcas):
                        fallas.append(
                            f"término obsoleto «{pat}» en "
                            f"{f.relative_to(RAIZ)}:{i + 1}: {linea.strip()[:90]}")


def chequear_afirmaciones():
    for regla in DATOS["afirmaciones"]:
        f = RAIZ / regla["archivo"]
        if not f.exists():
            fallas.append(f"afirmaciones: no existe {regla['archivo']}")
            continue
        texto = f.read_text()
        for frase in regla["debe_contener"]:
            if frase not in texto:
                fallas.append(
                    f"{regla['archivo']} ya no afirma «{frase}» "
                    "(¿rediseño a medio propagar, o actualizar DATOS_CURSO.yml?)")


def chequear_numeros():
    if DATOS["mesas"] * DATOS["integrantes_por_mesa"] != DATOS["matricula"]:
        fallas.append("DATOS_CURSO: mesas × integrantes ≠ matrícula")
    if sum(DATOS["pesos"].values()) != 100:
        fallas.append("DATOS_CURSO: los pesos no suman 100")
    if sum(h["pct"] for h in DATOS["proyecto"]["hitos"]) != DATOS["pesos"]["proyecto"]:
        fallas.append("DATOS_CURSO: los hitos no suman el peso del proyecto")


def chequear_estimulo():
    e = RAIZ / DATOS["estimulo_linea_base"]["archivo"]
    if not e.exists():
        fallas.append(f"no existe el estímulo consagrado {e.relative_to(RAIZ)} "
                      "(s01 y s15 dependen de ESTE archivo)")


def chequear_chips_slides():
    # si un mazo usa chips {.tiempo}, toda slide no-demo debe llevar uno
    for f in sorted((RAIZ / "material/curso").glob("sesion-*/slides_*.qmd")):
        texto = f.read_text()
        if "{.tiempo}" not in texto:
            continue
        bloques = re.split(r"(?m)^(?=## )", texto)[1:]
        for b in bloques:
            titulo = b.split("\n", 1)[0]
            if "background-iframe" in titulo:
                continue
            if "{.tiempo}" not in b:
                fallas.append(f"{f.relative_to(RAIZ)}: slide sin chip de "
                              f"tiempo: {titulo[:60]}")


def chequear_canvas_urls():
    render = RAIZ / "material/_render/site"
    if not render.is_dir():
        avisos.append("canvas: sin render local, chequeo de URLs omitido "
                      "(correr quarto render para habilitarlo)")
        return
    cfg = yaml.safe_load((RAIZ / "canvas/canvas.yml").read_text())
    for mod in cfg.get("modulos", []):
        for item in mod.get("items", []):
            url = item.get("url", "")
            if "{sitio}" not in url:
                continue
            ruta = url.split("{sitio}/", 1)[1]
            # el sitio de canvas es un espejo del render con perfil canvas;
            # basta que la página exista en el render normal
            if ruta and not (render / ruta).exists() and ruta != "":
                fallas.append(f"canvas.yml apunta a página inexistente: "
                              f"{ruta} (ítem «{item.get('titulo')}»)")


def main():
    rapido = "--rapido" in sys.argv
    chequear_numeros()
    chequear_estimulo()
    chequear_afirmaciones()
    chequear_prohibidos()
    chequear_chips_slides()
    if not rapido:
        chequear_canvas_urls()

    for a in avisos:
        print(f"  aviso · {a}")
    if fallas:
        print(f"\nINCONSISTENCIAS ({len(fallas)}):")
        for f in fallas:
            print(f"  ✗ {f}")
        print("\nRegla de proceso: el rediseño parte por DATOS_CURSO.yml y "
              "termina cuando este verificador pasa en limpio.")
        return 1
    print("OK: diseño consistente con DATOS_CURSO.yml "
          f"({'modo rápido' if rapido else 'chequeo completo'}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
