#!/usr/bin/env python3
"""verificar_consistencia — el mapa de relaciones del curso, ejecutable.

Chequea que los HECHOS del diseño (DATOS_CURSO.yml) sigan afirmados en
todos los documentos que los repiten, y que ningún documento conserve
términos de diseños anteriores.

MOTOR GEMELO (regla publicar_canvas): este archivo es IDÉNTICO en AM y
en SyS — al mejorarlo en un curso, copiarlo al otro. Todo lo específico
de cada curso vive en su DATOS_CURSO.yml: cada chequeo se activa solo
si su clave existe ahí (AM: estímulo consagrado, chips de slides;
SyS: banco↔specs, fichas de ayudantes).

Nació el 2026-08-07 en AM tras una semana de rediseños en que los
barridos manuales dejaron pasar inconsistencias semánticas. Regla de
proceso (CLAUDE.md de cada curso): todo rediseño parte por
DATOS_CURSO.yml y termina cuando este verificador pasa en limpio.

Uso:
  python3 verificar_consistencia.py            # todo
  python3 verificar_consistencia.py --rapido   # sin chequeos que requieran render

Corre además en el hook pre-commit (--rapido) y en el momento de
publicación de cada curso (CI en AM; pre-flight de `liberar` en SyS).
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

EXT_TEXTO = {".md", ".qmd", ".yml"}

fallas, avisos = [], []


# ------------------------------------------------------------------ util
def frontmatter(texto):
    """Frontmatter YAML de un .md, o {} si no tiene."""
    m = re.match(r"\A---\n(.*?)\n---\n", texto, re.S)
    try:
        return yaml.safe_load(m.group(1)) if m else {}
    except yaml.YAMLError:
        return {}


def archivos_ambito(bases):
    for base in bases:
        p = RAIZ / base
        if p.is_file():
            yield p
        elif p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.suffix in EXT_TEXTO and "_render" not in f.parts:
                    yield f


# -------------------------------------------------------------- chequeos
def chequear_numeros():
    if {"mesas", "integrantes_por_mesa", "matricula"} <= DATOS.keys():
        if DATOS["mesas"] * DATOS["integrantes_por_mesa"] != DATOS["matricula"]:
            fallas.append("DATOS_CURSO: mesas × integrantes ≠ matrícula")
    if "pesos" in DATOS and sum(DATOS["pesos"].values()) != 100:
        fallas.append("DATOS_CURSO: los pesos no suman 100")
    if "proyecto" in DATOS and "hitos" in DATOS.get("proyecto", {}):
        if (sum(h["pct"] for h in DATOS["proyecto"]["hitos"])
                != DATOS["pesos"]["proyecto"]):
            fallas.append("DATOS_CURSO: los hitos no suman el peso del proyecto")


def chequear_estimulo():
    if "estimulo_linea_base" not in DATOS:
        return
    e = RAIZ / DATOS["estimulo_linea_base"]["archivo"]
    if not e.exists():
        fallas.append(f"no existe el estímulo consagrado {e.relative_to(RAIZ)}")


def chequear_afirmaciones():
    for regla in DATOS.get("afirmaciones", []):
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


def chequear_prohibidos():
    cfg = DATOS.get("prohibidos")
    if not cfg:
        return
    patrones = [p.lower() for p in cfg["patrones"]]
    marcas = [m.lower() for m in cfg["permitir_si_contiene"]]
    exentos = {str(RAIZ / e) for e in cfg.get("archivos_exentos", [])}
    for f in archivos_ambito(cfg["ambito"]):
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
                # borde de palabra al final: «exprés» no debe cazar «exprésela»
                if re.search(re.escape(pat) + r"\b", baja):
                    # ventana de contexto: línea anterior + actual +
                    # siguiente (la prosa a 72 columnas corta frases)
                    ventana = " ".join(
                        lineas[j].lower()
                        for j in range(max(0, i - 1), min(len(lineas), i + 2)))
                    if not any(m in ventana for m in marcas):
                        fallas.append(
                            f"término obsoleto «{pat}» en "
                            f"{f.relative_to(RAIZ)}:{i + 1}: {linea.strip()[:90]}")


def chequear_chips_slides():
    # si un mazo usa chips {.tiempo}, toda slide no-demo debe llevar uno
    cfg = DATOS.get("chips_slides")
    if not cfg:
        return
    for f in sorted(RAIZ.glob(cfg["glob"])):
        texto = f.read_text()
        if "{.tiempo}" not in texto:
            continue
        for b in re.split(r"(?m)^(?=## )", texto)[1:]:
            titulo = b.split("\n", 1)[0]
            if "background-iframe" in titulo:
                continue
            if "{.tiempo}" not in b:
                fallas.append(f"{f.relative_to(RAIZ)}: slide sin chip de "
                              f"tiempo: {titulo[:60]}")


def chequear_banco_specs():
    # specs de pruebas/CVs: cada ejercicio citado existe y está en el
    # estado exigido; el formulario referido existe (SyS)
    cfg = DATOS.get("banco")
    if not cfg:
        return
    dir_ej = RAIZ / cfg["ejercicios"]
    requerido = cfg["estado_requerido"]
    for spec_f in sorted((RAIZ / cfg["specs"]).glob("*.yml")):
        try:
            spec = yaml.safe_load(spec_f.read_text()) or {}
        except yaml.YAMLError as e:
            fallas.append(f"spec ilegible {spec_f.name}: {e}")
            continue
        for sid in spec.get("seleccion") or []:
            ej = dir_ej / f"{sid}.md"
            if not ej.exists():
                fallas.append(f"{spec_f.name}: ejercicio {sid} no existe en el banco")
                continue
            estado = frontmatter(ej.read_text()).get("estado")
            if estado != requerido:
                fallas.append(
                    f"{spec_f.name}: {sid} está en estado «{estado}», "
                    f"se exige «{requerido}»")
        formulario = spec.get("formulario")
        if formulario:
            ff = RAIZ / cfg["formularios"] / f"{formulario}.qmd"
            if not ff.exists():
                fallas.append(f"{spec_f.name}: formulario «{formulario}» no "
                              f"existe en {cfg['formularios']}/")


def chequear_prerrequisitos_sesiones():
    # cada sesión de práctica (ayudantía) asume materia hasta cierta
    # clase; esa clase debe ocurrir ANTES en el calendario real del año.
    # Nació el 2026-08-15: Ay2 practicó la delta de Dirac tres días
    # antes de que C4 la introdujera (semana 1 sin lunes ⇒ Ay2–Ay4
    # caen entre las dos clases de su semana plantilla).
    cfg = DATOS.get("prerrequisitos_sesiones")
    if not cfg:
        return
    plan = RAIZ / cfg["plan"]
    if not plan.exists():
        fallas.append(f"prerrequisitos: no existe el plan {cfg['plan']}")
        return
    meses = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
             "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12}
    pat = re.compile(r"^\|\s*\*{0,2}(C\d+|Ay\d+)[^|]*\|\s*\*{0,2}\w{3}\s+"
                     r"(\d{1,2})-([a-z]{3})-(\d{4})", re.M)
    fechas = {}
    for m in pat.finditer(plan.read_text()):
        sid, d, mes, a = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
        fechas.setdefault(sid, (a, meses[mes], d))
    import datetime
    hoy = datetime.date.today()
    for sesion, requiere in cfg["materia_hasta"].items():
        if sesion not in fechas or requiere not in fechas:
            fallas.append(f"prerrequisitos: {sesion} o {requiere} sin fecha "
                          f"en {cfg['plan']} (¿cambió el formato de la tabla?)")
            continue
        if fechas[requiere] >= fechas[sesion]:
            msj = (f"DESFASE: {sesion} ({fechas[sesion][2]:02d}-"
                   f"{fechas[sesion][1]:02d}) asume materia de {requiere}, que "
                   f"recién se dicta el {fechas[requiere][2]:02d}-"
                   f"{fechas[requiere][1]:02d} — ajustar contenido de la "
                   f"sesión o el mapeo materia_hasta")
            if datetime.date(*fechas[sesion]) < hoy:
                avisos.append(msj + " (sesión ya realizada: solo se puede "
                              "documentar y corregir para la próxima edición)")
            else:
                fallas.append(msj)


def chequear_autocontencion():
    # material escrito que el estudiante lee solo (listas, Reader): los
    # enunciados no pueden apoyarse en algo efímero de la sala ("el tramo
    # graficado en clase") — quien faltó no puede resolverlo y al año
    # siguiente la referencia apunta al vacío. Nació el 17-ago-2026 con
    # L2.1. Los bloques ocultos (respuestas para ayudantes) sí pueden.
    cfg = DATOS.get("autocontencion")
    if not cfg:
        return
    patrones = [p.lower() for p in cfg["patrones"]]
    for glob in cfg["globs"]:
        for f in sorted(RAIZ.glob(glob)):
            oculto_en, prof = None, 0
            for i, linea in enumerate(f.read_text().splitlines()):
                s = linea.strip()
                if s.startswith(":::"):
                    if "{" in s:                       # apertura de bloque
                        prof += 1
                        if "content-hidden" in s and oculto_en is None:
                            oculto_en = prof
                    else:                              # cierre
                        if oculto_en == prof:
                            oculto_en = None
                        prof = max(0, prof - 1)
                    continue
                if oculto_en is not None:
                    continue
                baja = linea.lower()
                for pat in patrones:
                    # borde de palabra al final (gemelo con SyS)
                    if re.search(re.escape(pat) + r"\b", baja):
                        fallas.append(
                            f"{f.relative_to(RAIZ)}:{i + 1}: enunciado se apoya "
                            f"en algo efímero («{pat}») — escribir el dato "
                            "explícito o citar material escrito "
                            "(ver GUIA_ESTILO_SESIONES.md §Listas)")


def chequear_estilo_decks():
    # decks reveal.js: (1) sin `$…$` dentro de bloques .notes (KaTeX
    # duplica la fórmula en la vista de presentador); (2) toda imagen
    # con .nostretch (sin él, auto-stretch colapsa la lámina a altura
    # 0); (3) aviso si una clase próxima sigue sin notas o sin figuras
    # (recordatorio de tanda — ver AUDITORIA_NOTAS_FIGURAS.md).
    cfg = DATOS.get("estilo_decks")
    if not cfg:
        return
    import datetime
    meses = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
             "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12}
    fechas = {}
    plan = RAIZ / cfg.get("plan", "")
    if plan.is_file():
        pat = re.compile(r"^\|\s*\*{0,2}(C\d+)[^|]*\|\s*\*{0,2}\w{3}\s+"
                         r"(\d{1,2})-([a-z]{3})-(\d{4})", re.M)
        for m in pat.finditer(plan.read_text()):
            fechas.setdefault(m.group(1), datetime.date(
                int(m.group(4)), meses[m.group(3)], int(m.group(2))))
    hoy = datetime.date.today()
    horizonte = datetime.timedelta(days=cfg.get("aviso_dias", 10))
    for f in sorted(RAIZ.glob(cfg["glob"])):
        texto = f.read_text()
        lineas = texto.splitlines()
        en_notas, con_notas = False, 0
        for i, linea in enumerate(lineas):
            if re.match(r"^:::+\s*\{\.notes\}", linea.strip()):
                en_notas = True
                con_notas += 1
            elif en_notas and linea.strip().startswith(":::"):
                en_notas = False
            elif en_notas and "$" in linea:
                fallas.append(f"{f.relative_to(RAIZ)}:{i + 1}: LaTeX `$…$` "
                              "dentro de .notes (KaTeX lo duplica en la vista "
                              "de presentador — escribirlo en texto plano)")
            if not en_notas:
                for img in re.finditer(r"!\[[^\]]*\]\([^)]+\)(\{[^}]*\})?",
                                       linea):
                    attrs = img.group(1) or ""
                    if ".nostretch" not in attrs:
                        fallas.append(
                            f"{f.relative_to(RAIZ)}:{i + 1}: imagen sin "
                            "{.nostretch} — auto-stretch colapsa la lámina "
                            "a altura 0")
        m = re.match(r"c(\d+)-slides", f.stem)
        fecha = fechas.get(f"C{int(m.group(1))}") if m else None
        if fecha and hoy <= fecha <= hoy + horizonte:
            n_img = len(re.findall(r"!\[[^\]]*\]\(", texto))
            if con_notas == 0 or n_img == 0:
                falta = " y ".join(p for p, v in
                                   (("notas", con_notas), ("figuras", n_img))
                                   if v == 0)
                avisos.append(
                    f"tanda pendiente: {f.stem} se dicta el "
                    f"{fecha:%d-%m} y aún no tiene {falta} "
                    "(ver ediciones/2026/AUDITORIA_NOTAS_FIGURAS.md)")


def chequear_fichas_ayudantes():
    # cada ficha exportada debe existir y no ser más vieja que su fuente
    cfg = DATOS.get("fichas_ayudantes")
    if not cfg:
        return
    destino = RAIZ / cfg["destino"]
    for qmd in sorted(RAIZ.glob(cfg["fuentes_glob"])):
        ficha = destino / (qmd.stem + "." + cfg.get("formato", "html"))
        if not ficha.exists():
            fallas.append(f"ficha de ayudantes sin exportar: {ficha.name} "
                          f"(fuente {qmd.relative_to(RAIZ)})")
        elif ficha.stat().st_mtime < qmd.stat().st_mtime:
            fallas.append(f"ficha de ayudantes OBSOLETA: {ficha.name} es más "
                          f"vieja que {qmd.relative_to(RAIZ)} — correr "
                          "exportar_fichas.py")


def chequear_canvas_urls():
    cfg = DATOS.get("canvas_urls")
    if not cfg:
        return
    render = RAIZ / cfg["render"]
    if not render.is_dir():
        avisos.append("canvas: sin render local, chequeo de URLs omitido "
                      "(correr quarto render para habilitarlo)")
        return
    canvas = yaml.safe_load((RAIZ / "canvas/canvas.yml").read_text())
    for mod in canvas.get("modulos", []):
        for item in mod.get("items", []):
            url = item.get("url", "")
            if "{sitio}" not in url:
                continue
            ruta = url.split("{sitio}/", 1)[1]
            if ruta and not (render / ruta).exists():
                fallas.append(f"canvas.yml apunta a página inexistente: "
                              f"{ruta} (ítem «{item.get('titulo')}»)")


def main():
    rapido = "--rapido" in sys.argv
    chequear_numeros()
    chequear_estimulo()
    chequear_afirmaciones()
    chequear_prohibidos()
    chequear_chips_slides()
    chequear_banco_specs()
    chequear_prerrequisitos_sesiones()
    chequear_estilo_decks()
    chequear_autocontencion()
    chequear_fichas_ayudantes()
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
