#!/usr/bin/env python3
"""Agenda administrativa del semestre — motor y CLI.

Deriva las tareas administrativas (revisar planes, armar pruebas, registrar
notas de taller, publicar pautas…) cruzando dos fuentes:

- las FECHAS del calendario de la edición (ediciones/<ed>/CALENDARIO_*.md),
  parseadas con el mismo `indice.parsear_calendario` del panel — si una sesión
  o evaluación se mueve, la agenda entera se recalcula sola. Las evaluaciones
  no tienen tabla propia: se detectan en la columna `Hito / nota` ("Hito 1",
  "Prueba 2", "Presentaciones…");
- las REGLAS de panel/agenda_reglas.yml: qué genera cada tipo de evento y con
  cuántos días de anticipación.

Lo único que escribe es el estado de qué está hecho, en
ediciones/<ed>/agenda_estado.yml (fuera de material/, versionable). Nunca
toca el calendario ni las reglas.

Uso:
    python3 panel/agenda.py            # atrasadas + esta semana + próximas
    python3 panel/agenda.py --todo     # el semestre completo
    python3 panel/agenda.py --marcar ID [ID…]     # marca hecha(s)
    python3 panel/agenda.py --desmarcar ID [ID…]
"""

import argparse
import datetime as dt
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indice as idx                                     # noqa: E402

try:
    import yaml
except ImportError:                                       # pragma: no cover
    print("Requiere PyYAML (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

REPO = idx.REPO
REGLAS_YML = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "agenda_reglas.yml")


# ------------------------------------------------------------------ fuentes --
def _calendario(edicion=None):
    """(edición, calendario parseado). Es un archivo chico: se lee directo.

    Las fechas del calendario no llevan año (`vie 07-ago`): lo aporta el
    nombre de la edición (`2026-2` → 2026), igual que hace indice.construir.
    """
    ed = edicion or idx.detectar_edicion()
    if not ed:
        raise FileNotFoundError("no hay edición AAAA-S bajo ediciones/")
    rel = idx._ruta_calendario(ed)
    if not rel:
        raise FileNotFoundError(f"ediciones/{ed} no tiene CALENDARIO_*.md")
    texto = idx._leer(os.path.join(REPO, rel))
    if texto is None:
        raise FileNotFoundError(rel)
    return ed, idx.parsear_calendario(texto, anio=int(ed.split("-")[0]))


def _reglas():
    with open(REGLAS_YML, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _ruta_estado(edicion):
    return os.path.join(REPO, "ediciones", edicion, "agenda_estado.yml")


def _estado(edicion):
    try:
        with open(_ruta_estado(edicion), encoding="utf-8") as fh:
            e = yaml.safe_load(fh) or {}
    except OSError:
        e = {}
    e.setdefault("hecho", {})
    return e


# ------------------------------------------------------------------- fechas --
def _iso(f):
    """Fecha ISO de una celda parseada por indice.fecha_es, o None."""
    return f["iso"] if isinstance(f, dict) and f.get("iso") else None


def _mas(iso, dias):
    d = dt.date.fromisoformat(iso) + dt.timedelta(days=dias)
    return d.isoformat()


# ------------------------------------------------------------ evaluaciones --
# Ancladas al COMIENZO de la columna hito: "pauta del hito 3" en la nota de
# s14 no es el hito 3 — el hito de una sesión abre su celda, lo demás es
# comentario.
def _evaluaciones(sesiones):
    """{P1: (fecha, "Prueba 1", 1), H2: …, Final: …} desde la columna hito."""
    evs = {}
    for _, s in sorted(sesiones.items()):
        f = _iso(s.get("fecha"))
        hito = idx._sin_tildes(s.get("hito") or "").lower()
        if not f or not hito:
            continue
        m = re.match(r"^hito\s*(\d)", hito)
        if m:
            evs.setdefault(f"H{m.group(1)}",
                           (f, f"Hito {m.group(1)}", int(m.group(1))))
        m = re.match(r"^prueba\s*(\d)", hito)
        if m:
            evs.setdefault(f"P{m.group(1)}",
                           (f, f"Prueba {m.group(1)}", int(m.group(1))))
        if re.match(r"^presentaciones", hito):
            evs.setdefault("Final", (f, "Presentaciones finales", 0))
    return evs


def _tiene_taller(n, sesion):
    """¿La sesión N lleva taller evaluado que registrar en Canvas?

    s01 es formativa por diseño (línea base sin nota) y las sesiones de
    prueba o presentaciones no tienen taller. El caso F1 (s03 en semana
    universitaria) NO se excluye aquí: mientras el profesor no decida, la
    tarea recuerda que ese registro está en cuestión — y el hito `f1-decidir`
    es quien pide decidirlo.
    """
    if n == 1:
        return False
    hito = idx._sin_tildes(sesion.get("hito") or "").lower()
    return not re.match(r"^(prueba\s*\d|presentaciones)", hito)


# ------------------------------------------------------------------- motor --
def _expandir(regla, ancla_iso, ctx):
    """Una regla + un ancla -> una tarea concreta (sin estado todavía)."""
    def _f(s):
        return str(s).format(**ctx) if s else None
    return {
        "id": _f(regla.get("id")),
        "fecha": _mas(ancla_iso, int(regla.get("dias", 0))),
        "titulo": _f(regla.get("titulo")) or _f(regla.get("id")),
        "detalle": _f(regla.get("detalle")),
        "ruta": _f(regla.get("ruta")),
        "grupo": ctx.get("grupo", ""),
    }


def generar(edicion=None, hoy=None):
    """Todas las tareas del semestre, con su estado temporal y de avance."""
    ed, cal = _calendario(edicion)
    reglas = _reglas()
    estado = _estado(ed)
    hoy = hoy or dt.date.today().isoformat()

    ses = cal.get("sesiones") or {}
    fecha_ev = _evaluaciones(ses)
    tareas, avisos = [], []

    # 1 · sesiones: el viernes de la sesión N es su ancla.
    for n in sorted(ses):
        f = _iso(ses[n].get("fecha"))
        if not f:
            avisos.append(f"s{n:02d} sin fecha: sesión sin tareas")
            continue
        ctx = {"ses": f"{n:02d}", "ed": ed, "grupo": f"s{n:02d}"}
        for r in reglas.get("sesion") or []:
            if r.get("cuando") == "taller" and not _tiene_taller(n, ses[n]):
                continue
            tareas.append(_expandir(r, f, ctx))

    # 2 · pruebas e hitos del proyecto, cada uno con su paquete. El Final
    #     (presentaciones) no entra aquí: su logística va en `hitos`.
    for clave, (f, nombre, num) in sorted(fecha_ev.items()):
        if clave.startswith("P"):
            lista = reglas.get("prueba") or []
        elif clave.startswith("H"):
            lista = reglas.get("hito") or []
        else:
            continue
        ctx = {"ev": nombre, "n": num, "ed": ed, "grupo": nombre}
        for r in lista:
            tareas.append(_expandir(r, f, ctx))

    # 3 · hitos únicos, anclados a "inicio", a una sesión (sNN) o a una
    #     evaluación detectada (P1, H2, Final…).
    fechas_ses = {n: _iso(s.get("fecha")) for n, s in ses.items()}
    inicio = min((f for f in fechas_ses.values() if f), default=None)
    for r in reglas.get("hitos") or []:
        ancla = str(r.get("ancla", "inicio"))
        if ancla == "inicio":
            base = inicio
        elif re.match(r"^s\d{2}$", ancla):
            base = fechas_ses.get(int(ancla[1:]))
        else:
            base = (fecha_ev.get(ancla) or (None,))[0]
        if not base:
            avisos.append(f"hito {r.get('id')}: ancla '{ancla}' sin fecha")
            continue
        tareas.append(_expandir(r, base, {"ed": ed, "grupo": "Hitos"}))

    # Estado de cada tarea. "Esta semana" = hasta el domingo que viene.
    d_hoy = dt.date.fromisoformat(hoy)
    fin_semana = d_hoy + dt.timedelta(days=6 - d_hoy.weekday())
    for t in tareas:
        t["hecho"] = estado["hecho"].get(t["id"])
        if t["hecho"]:
            t["estado"] = "hecha"
        elif t["fecha"] is None:
            t["estado"] = "atrasada"
        else:
            d = dt.date.fromisoformat(t["fecha"])
            if d < d_hoy:
                t["estado"] = "atrasada"
            elif d <= fin_semana:
                t["estado"] = "esta-semana"
            elif d <= fin_semana + dt.timedelta(days=14):
                t["estado"] = "proxima"
            else:
                t["estado"] = "futura"

    tareas.sort(key=lambda t: (t["fecha"] or "0000", t["grupo"], t["id"]))
    resumen = {}
    for t in tareas:
        resumen[t["estado"]] = resumen.get(t["estado"], 0) + 1
    return {"edicion": ed, "hoy": hoy, "tareas": tareas,
            "resumen": resumen, "avisos": avisos}


# ------------------------------------------------------------------- estado --
def marcar(ids, hecho=True, edicion=None):
    """Marca o desmarca tareas. Devuelve el estado resultante de cada id."""
    ed, _ = _calendario(edicion)
    estado = _estado(ed)
    hoy = dt.date.today().isoformat()
    out = {}
    for i in ids:
        i = str(i)
        if hecho:
            estado["hecho"][i] = hoy
            out[i] = hoy
        else:
            estado["hecho"].pop(i, None)
            out[i] = None
    with open(_ruta_estado(ed), "w", encoding="utf-8") as fh:
        fh.write("# agenda_estado.yml — qué tareas de la agenda están hechas "
                 "(lo escribe panel/agenda.py).\n")
        yaml.safe_dump(estado, fh, allow_unicode=True, sort_keys=True)
    return out


# --------------------------------------------------------------------- CLI --
_ORDEN = ["atrasada", "esta-semana", "proxima", "futura", "hecha"]
_ROTULO = {"atrasada": "ATRASADAS", "esta-semana": "ESTA SEMANA",
           "proxima": "PRÓXIMAS 2 SEMANAS", "futura": "MÁS ADELANTE",
           "hecha": "HECHAS"}


def _imprimir(datos, todo=False):
    print(f"Agenda {datos['edicion']} · hoy {datos['hoy']}")
    for a in datos["avisos"]:
        print(f"  ⚠ {a}")
    visibles = _ORDEN if todo else ["atrasada", "esta-semana", "proxima"]
    for est in visibles:
        grupo = [t for t in datos["tareas"] if t["estado"] == est]
        if not grupo:
            continue
        print(f"\n{_ROTULO[est]} ({len(grupo)})")
        for t in grupo:
            marca = "x" if t["hecho"] else " "
            fecha = t["fecha"] or "sin fecha"
            print(f"  [{marca}] {fecha}  {t['titulo']}   ({t['id']})")
            if t.get("detalle"):
                print(f"            {t['detalle']}")
    pend = sum(v for k, v in datos["resumen"].items() if k != "hecha")
    print(f"\n{pend} pendientes · {datos['resumen'].get('hecha', 0)} hechas")


def main():
    p = argparse.ArgumentParser(description="Agenda administrativa MUC860")
    p.add_argument("--edicion",
                   help="directorio de ediciones/ (por defecto, el mayor)")
    p.add_argument("--todo", action="store_true",
                   help="muestra también lo futuro y lo hecho")
    p.add_argument("--marcar", nargs="+", metavar="ID")
    p.add_argument("--desmarcar", nargs="+", metavar="ID")
    args = p.parse_args()

    if args.marcar or args.desmarcar:
        conocidos = {t["id"] for t in generar(args.edicion)["tareas"]}
        pedidos = (args.marcar or []) + (args.desmarcar or [])
        raros = [i for i in pedidos if i not in conocidos]
        if raros:
            print(f"ids desconocidos: {', '.join(raros)}", file=sys.stderr)
            return 1
        if args.marcar:
            marcar(args.marcar, True, args.edicion)
        if args.desmarcar:
            marcar(args.desmarcar, False, args.edicion)

    _imprimir(generar(args.edicion), todo=args.todo)
    return 0


if __name__ == "__main__":
    sys.exit(main())
