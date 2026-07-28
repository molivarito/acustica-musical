#!/usr/bin/env python3
"""Capa de datos del panel de sesión MUC860 · Acústica Musical.

Reúne, para cada sesión s01–s15, todo lo que hay que mirar al prepararla: el
plan del profesor con sus dos módulos, los objetivos OA con su texto, el
apunte del estudiante, el capítulo del libro, las guías de actividades, la
demo, las dependencias entre sesiones y la fecha real con su hito.

Nada de esto vive en un formato estructurado: hay que derivarlo de la
convención de nombres y parsear las tablas Markdown de los documentos
rectores. Por eso la regla de oro de este módulo es que **ningún parser lanza
excepción hacia arriba**: devuelve lo que pudo y anota el resto en `avisos`,
que el panel muestra al profesor. Un documento editado a mano nunca debe
dejar la pantalla en blanco.

Diferencia grande con el panel hermano de SyS: aquí el artefacto central
—`plan.md`— **no existe en HTML**. `material/_quarto.yml` lo excluye del
render por la regla de visibilidad (es material solo-profesor). El panel lo
convierte con pandoc bajo demanda; ver `panel.py`.

Solo lectura: lo único que escribe es su caché, y vive fuera del repo
(~/.cache/panel-am.json).

Uso:
    python3 panel/indice.py --verificar    # qué no se pudo parsear
    python3 panel/indice.py --json s04     # la entrada completa de una sesión
"""

import argparse
import json
import os
import re
import sys
import unicodedata

try:
    import yaml
except ImportError:
    print("Requiere PyYAML (pip install pyyaml)")
    sys.exit(2)

PANEL_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(PANEL_DIR)
MATERIAL = os.path.join(REPO, "material")
RENDER = os.path.join(MATERIAL, "_render")

CACHE = os.path.expanduser("~/.cache/panel-am.json")
VERSION_CACHE = 1

N_SESIONES = 15


# ------------------------------------------------------------- utilidades --
def _sin_tildes(s):
    s = unicodedata.normalize("NFD", str(s))
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def _leer(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def _limpiar(s):
    """Quita énfasis Markdown, enlaces y espacios sobrantes."""
    s = str(s)
    s = re.sub(r"\[`?([^\]`]+)`?\]\([^)]*\)", r"\1", s)   # [texto](url) -> texto
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    s = s.replace("`", "")
    return " ".join(s.split()).strip()


# ------------------------------------------------- lector de tablas Markdown --
# Reutilizado literalmente del panel de SyS: el `re.split(r"(?<!\\)\|", ...)`
# respeta los pipes escapados que aparecen dentro de las fórmulas.
_SEPARADORA = re.compile(r"^[\s|:\-]+$")


def tablas_md(texto, bajo=None):
    """Devuelve las tablas Markdown de `texto` como listas de filas.

    Cada tabla es `{"header": [...], "filas": [[celda, ...], ...]}`. Las filas
    con celdas de más no se descartan: el sobrante se concatena en la última
    columna, para no perder la anotación.
    """
    if bajo:
        m = re.search(r"^(#{1,6})\s*" + re.escape(bajo), texto, re.M)
        if not m:
            return []
        nivel = len(m.group(1))
        resto = texto[m.end():]
        fin = re.search(r"^#{1,%d}\s" % nivel, resto, re.M)
        texto = resto[: fin.start()] if fin else resto

    tablas, actual = [], None
    for linea in texto.split("\n"):
        s = linea.strip()
        if not s.startswith("|"):
            if actual:
                tablas.append(actual)
                actual = None
            continue
        if _SEPARADORA.match(s):
            continue
        celdas = [c.strip() for c in re.split(r"(?<!\\)\|", s)]
        if celdas and not celdas[0]:
            celdas = celdas[1:]
        if celdas and not celdas[-1]:
            celdas = celdas[:-1]
        if actual is None:
            actual = {"header": celdas, "filas": []}
            continue
        n = len(actual["header"])
        if len(celdas) > n:
            celdas = celdas[: n - 1] + [" ".join(celdas[n - 1:])]
        elif len(celdas) < n:
            celdas = celdas + [""] * (n - len(celdas))
        actual["filas"].append(celdas)
    if actual:
        tablas.append(actual)
    return tablas


# ----------------------------------------------------- fechas en español ----
_MESES = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
          "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12}
# El año es OPCIONAL: el calendario de AM escribe `vie 07-ago` sin año, y el
# subtitle de las slides sí lo trae (`vie 28-ago-2026`). Cuando falta, lo pone
# quien llama, a partir del nombre del directorio de la edición.
_RE_FECHA = re.compile(
    r"(?:(lun|mar|mie|jue|vie|sab|dom)\w*\s+)?(\d{1,2})-([a-z]{3})(?:-(\d{4}))?")


def fecha_es(celda, anio=None):
    """`vie 07-ago` o `vie 28-ago-2026` -> {iso, crudo, dow, anio_supuesto}."""
    crudo = _limpiar(celda)
    if not crudo:
        return None
    m = _RE_FECHA.search(_sin_tildes(crudo).lower())
    if not m:
        return None
    dow, dia, mes, anio_txt = m.groups()
    if mes not in _MESES:
        return None
    a = int(anio_txt) if anio_txt else (int(anio) if anio else None)
    if a is None:
        return {"iso": None, "crudo": crudo, "dow": dow, "anio_supuesto": False}
    return {"iso": f"{a}-{_MESES[mes]:02d}-{int(dia):02d}", "crudo": crudo,
            "dow": dow, "anio_supuesto": not anio_txt}


def _front_matter(texto):
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def _sesiones_citadas(celda):
    """Códigos sNN de una celda, expandiendo rangos `s01–s06`."""
    out = set()
    for m in re.finditer(r"s(\d{2})(?:\s*[–—-]\s*s?(\d{2}))?",
                         _sin_tildes(str(celda)).lower()):
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        if 1 <= a <= N_SESIONES and a <= b <= N_SESIONES:
            out.update(range(a, b + 1))
    return sorted(out)


# ---------------------------------------- P1/P2/P3/P4 · el plan de sesión ---
# Los campos de la cabecera son párrafos `**Campo**: …` a comienzo de línea,
# no una lista de bullets y no front-matter YAML (plan.md no tiene).
_CAMPOS_PLAN = ("Objetivos que cubre", "Requisitos previos",
                "Posición en la progresión", "Reglas aplicadas")


def parsear_plan(texto):
    """P1 cabecera · P2 módulos y su tabla de 5 columnas · P3 cierre · P4 enlaces."""
    avisos = []

    m = re.search(r"^#\s+Sesi[oó]n\s+(\d+)\s*[—–-]\s*(.*)$", texto, re.M)
    if m:
        n, titulo, desde = int(m.group(1)), _limpiar(m.group(2)), m.end()
    else:
        n, titulo, desde = None, "", 0
        avisos.append("sin encabezado '# Sesión NN — título'")

    # -- P1 · cabecera: del título al primer '## '
    prim = re.search(r"^##\s", texto[desde:], re.M)
    cabecera = texto[desde: desde + prim.start()] if prim else texto[desde:]
    campos, orden = {}, []
    partes = re.split(r"(?m)^\*\*([^*\n]+?)\*\*\s*:\s*", cabecera)
    for i in range(1, len(partes) - 1, 2):
        k = _limpiar(partes[i])
        campos[k] = " ".join(partes[i + 1].split()).strip()
        orden.append(k)
    # Comparación por prefijo, no por igualdad: de s08 en adelante el campo se
    # llama "Reglas aplicadas y decisiones de carga (declaradas)", y exigir el
    # nombre exacto produciría ocho avisos falsos — la mejor forma de enseñarle
    # al profesor a ignorar el aviso que sí importa.
    normal = [_sin_tildes(k).lower() for k in campos]
    for k in _CAMPOS_PLAN:
        pref = _sin_tildes(k).lower()
        if not any(x.startswith(pref) for x in normal):
            avisos.append(f"cabecera sin '**{k}**'")

    objetivos = sorted(set(re.findall(r"\bOA\d\.\d\b",
                                      campos.get("Objetivos que cubre", ""))))
    if not objetivos:
        avisos.append("la cabecera no cita ningún OA")

    # -- P2 · módulos
    modulos = []
    heads = list(re.finditer(r"^##\s+M[oó]dulo\s+(\d+)\s*[—–-]?\s*(.*)$",
                             texto, re.M))
    for i, h in enumerate(heads):
        fin = heads[i + 1].start() if i + 1 < len(heads) else len(texto)
        cuerpo = texto[h.end(): fin]
        # el cuerpo del módulo termina en el próximo '## ' aunque no sea módulo
        sig = re.search(r"^##\s", cuerpo, re.M)
        if sig:
            cuerpo = cuerpo[: sig.start()]
        crudo = h.group(2).strip()
        var = re.search(r"\(variante:\s*([^)]*)\)", crudo)
        tabs = [t for t in tablas_md(cuerpo) if len(t["header"]) >= 5]
        filas = []
        if tabs:
            for c in tabs[0]["filas"]:
                c = (c + [""] * 5)[:5]
                dur = None
                mm = re.match(r"\s*(\d+)\s*[–—-]\s*(\d+)", c[0])
                if mm:
                    dur = int(mm.group(2)) - int(mm.group(1))
                filas.append({"tiempo": c[0].strip(), "bloque": c[1].strip(),
                              "actividad": c[2].strip(), "profesor": c[3].strip(),
                              "materiales": c[4].strip(), "dur": dur})
        else:
            avisos.append(f"módulo {h.group(1)} sin tabla de 5 columnas")
        modulos.append({
            "n": int(h.group(1)),
            "titulo": _limpiar(re.sub(r"\(variante:[^)]*\)", "", crudo)),
            "variante": var.group(1).strip() if var else None,
            "filas": filas,
            "cabecera": tabs[0]["header"] if tabs else [],
        })
    if len(modulos) != 2:
        avisos.append(f"{len(modulos)} módulos (se esperaban 2)")

    # -- P3 · secciones de cierre (todo '## ' que no sea un módulo)
    cierre = []
    for h in re.finditer(r"^##\s+(?!M[oó]dulo\s)(.+)$", texto, re.M):
        resto = texto[h.end():]
        sig = re.search(r"^##\s", resto, re.M)
        cierre.append({"titulo": _limpiar(h.group(1)),
                       "cuerpo": (resto[: sig.start()] if sig else resto).strip()})

    # -- P4 · enlaces relativos que el plan cita
    enlaces = {"demos": [], "libro": [], "actividades": [], "otros": []}
    for mm in re.finditer(r"\]\(([^)\s]+)\)", texto):
        u = mm.group(1)
        if u.startswith(("http://", "https://", "#")):
            continue
        base = os.path.basename(u)
        if "/demos/" in u:
            destino = "demos"
        elif "/libro/" in u:
            destino = "libro"
        elif "actividades/" in u:
            destino = "actividades"
        else:
            destino = "otros"
        if base not in enlaces[destino]:
            enlaces[destino].append(base)

    return {"n": n, "titulo": titulo, "campos": campos, "orden_campos": orden,
            "objetivos": objetivos, "modulos": modulos, "cierre": cierre,
            "enlaces": enlaces, "_avisos": avisos}


def materiales_de(modulos):
    """Lista de chequeo agregada y deduplicada de las dos tablas.

    Es la mayor ganancia del panel de AM: al preparar, lo primero que uno
    necesita es qué hay que llevar a la sala, y hoy está repartido en diez
    celdas. Se corta por `;` y por ` + ` (ambos separan ítems de verdad en
    estas celdas) y se deduplica sin tildes ni mayúsculas, conservando la
    primera forma escrita y de qué módulos viene.
    """
    vistos, out = {}, []
    for mod in modulos:
        for fila in mod["filas"]:
            for trozo in re.split(r";|\s\+\s", fila["materiales"]):
                t = _limpiar(trozo).strip(" .·—-")
                if not t:
                    continue
                # La clave ignora los paréntesis aclaratorios: "Guitarra" y
                # "Guitarra (del profesor o de un grupo)" son el mismo objeto
                # que hay que meter al bolso, y verlos dos veces en la lista de
                # chequeo destruye justo aquello para lo que sirve.
                base = re.sub(r"\([^)]*\)", " ", t)
                clave = " ".join(_sin_tildes(base).lower().split()).rstrip("s")
                if not clave:
                    clave = _sin_tildes(t).lower()
                if clave in vistos:
                    ent = out[vistos[clave]]
                    if mod["n"] not in ent["modulos"]:
                        ent["modulos"].append(mod["n"])
                    if len(t) > len(ent["texto"]):
                        ent["texto"] = t      # se queda la forma más informativa
                    continue
                vistos[clave] = len(out)
                out.append({"texto": t, "modulos": [mod["n"]]})
    return out


# --------------------------------------------------- P6 · objetivos OA -----
def parsear_objetivos(texto):
    """`### OA1 — título` y `- **OA1.1** texto…` con su *Evaluación posible*."""
    familias, objetivos = {}, {}
    cod = None
    for linea in texto.split("\n"):
        m = re.match(r"^###\s+OA(\d)\s*[—–-]\s*(.*)$", linea)
        if m:
            familias[f"OA{m.group(1)}"] = _limpiar(m.group(2))
            cod = None
            continue
        m = re.match(r"^-\s+\*\*(OA\d\.\d)\*\*\s+(.*)$", linea)
        if m:
            cod = m.group(1)
            objetivos[cod] = {"codigo": cod, "texto": m.group(2).strip(),
                              "evaluacion": "", "familia": f"OA{cod[2]}"}
            continue
        if cod is None:
            continue
        s = linea.strip()
        if not s or s.startswith(("#", "-", "**")):
            cod = None
            continue
        # continuación del bullet; `*Evaluación posible*: …` va a su campo
        m = re.match(r"^\*Evaluaci[oó]n posible\*\s*:\s*(.*)$", s)
        if m:
            objetivos[cod]["evaluacion"] = m.group(1).strip()
            objetivos[cod]["_en_eval"] = True
        elif objetivos[cod].get("_en_eval"):
            objetivos[cod]["evaluacion"] += " " + s
        else:
            objetivos[cod]["texto"] += " " + s
    for o in objetivos.values():
        o.pop("_en_eval", None)
        o["texto"] = " ".join(o["texto"].split()).rstrip(" .")
        o["evaluacion"] = " ".join(o["evaluacion"].split()).rstrip(" .")
    return {"familias": familias, "objetivos": objetivos}


# ------------------------------------ P5 · mapa de las 15 sesiones ---------
def parsear_mapa_semestre(texto):
    """Tabla de 6 columnas: tema, OA, dependencias, hitos y demo por sesión.

    Es la fuente más rica del repo y la única que declara las dependencias
    entre sesiones (`Depende de`), que el panel usa para mostrar de qué
    sesiones depende esta y cuáles dependen de ella.
    """
    ses, avisos = {}, []
    for tabla in tablas_md(texto):
        h = [_sin_tildes(c).strip().lower() for c in tabla["header"]]
        if not h or h[0] != "sesion" or len(h) < 6:
            continue
        for c in tabla["filas"]:
            m = re.match(r"^s(\d{2})$", _limpiar(c[0]))
            if not m:
                continue
            demo = _limpiar(c[5])
            mm = re.search(r"(demo_[\w-]+\.html)", demo)
            ses[int(m.group(1))] = {
                "tema": _limpiar(c[1]),
                "objetivos": sorted(set(re.findall(r"\bOA\d\.\d\b", c[2]))),
                "objetivos_crudo": _limpiar(c[2]),
                "depende_de": _sesiones_citadas(c[3]),
                "depende_crudo": _limpiar(c[3]),
                "hitos": _limpiar(c[4]),
                "demo": mm.group(1) if mm else None,
                "demo_crudo": demo,
            }
    if not ses:
        avisos.append("no se encontró el 'Mapa de las 15 sesiones'")
    return {"sesiones": ses, "_avisos": avisos}


# ------------------------------------------- P7 · calendario de la edición --
def parsear_calendario(texto, anio=None):
    """Tabla `Sesión | Fecha | Hito`, con sus filas de interrupción.

    Las fechas NO llevan año (`vie 07-ago`): lo aporta quien llama, desde el
    nombre del directorio de la edición. Las filas cuya primera columna es
    `—` son el receso y el viernes sin clase; no son sesiones, pero se
    conservan para pintarlas en su lugar del riel.
    """
    ses, interrupciones, avisos = {}, [], []
    for tabla in tablas_md(texto):
        h = [_sin_tildes(c).strip().lower() for c in tabla["header"]]
        if not h or h[0] != "sesion" or len(h) < 2:
            continue
        # la tabla de "verificación de evaluaciones" empieza por 'evaluación'
        for c in tabla["filas"]:
            ident = _limpiar(c[0])
            f = fecha_es(c[1], anio=anio) if len(c) > 1 else None
            nota = _limpiar(c[2]) if len(c) > 2 else ""
            m = re.match(r"^s(\d{2})$", ident)
            if m:
                ses[int(m.group(1))] = {"fecha": f, "hito": nota or None}
            else:
                interrupciones.append({
                    "crudo": _limpiar(c[1]) if len(c) > 1 else "",
                    "fecha": f, "nota": nota})
    if not ses:
        avisos.append("no se encontró la tabla 'Sesión → fecha'")
    return {"sesiones": ses, "interrupciones": interrupciones,
            "_avisos": avisos}


def detectar_edicion():
    """Directorio de ediciones/ con formato `AAAA-S`; el mayor si hay varios."""
    base = os.path.join(REPO, "ediciones")
    mejor = None
    try:
        for nombre in sorted(os.listdir(base)):
            if not re.match(r"^\d{4}-\d$", nombre):
                continue
            if not os.path.isdir(os.path.join(base, nombre)):
                continue
            mejor = nombre if mejor is None else max(mejor, nombre)
    except OSError:
        return None
    return mejor


def _ruta_calendario(edicion):
    d = os.path.join(REPO, "ediciones", edicion)
    try:
        for f in sorted(os.listdir(d)):
            if re.match(r"^CALENDARIO_.*\.md$", f):
                return os.path.join("ediciones", edicion, f)
    except OSError:
        pass
    return None


# ------------------------------------------------- P8 · sidebar de Quarto --
def parsear_sidebar(texto):
    """Título, apunte, actividades públicas y demo de cada sesión."""
    try:
        cfg = yaml.safe_load(texto) or {}
    except yaml.YAMLError:
        return {"sesiones": {}, "_avisos": ["_quarto.yml ilegible"]}

    def _items(nodo, acc):
        if isinstance(nodo, str):
            acc.append(nodo)
        elif isinstance(nodo, dict):
            if nodo.get("href"):
                acc.append(str(nodo["href"]))
            for hijo in (nodo.get("contents") or []):
                _items(hijo, acc)
        elif isinstance(nodo, list):
            for hijo in nodo:
                _items(hijo, acc)
        return acc

    ses = {}
    contents = (((cfg.get("website") or {}).get("sidebar") or {})
                .get("contents") or [])
    for item in contents:
        if not isinstance(item, dict):
            continue
        m = re.match(r"^Sesi[oó]n\s+(\d+)\s*[—–-]\s*(.*)$",
                     str(item.get("section") or ""))
        if not m:
            continue
        rutas = _items(item.get("contents") or [], [])
        ses[int(m.group(1))] = {
            "titulo": m.group(2).strip(),
            "apunte": next((r for r in rutas if "/apunte_" in r), None),
            "actividades": [r for r in rutas if "/actividades/" in r],
            "demo": next((r for r in rutas if "/demos/" in r), None),
        }
    return {"sesiones": ses}


# ------------------------------------------------------ P10 · canvas.yml ---
def parsear_canvas(texto):
    try:
        cfg = yaml.safe_load(texto) or {}
    except yaml.YAMLError:
        return {"sesiones": {}, "_avisos": ["canvas.yml ilegible"]}
    ses = {}
    for mod in (cfg.get("modulos") or []):
        if not isinstance(mod, dict):
            continue
        m = re.match(r"^Sesi[oó]n\s+(\d+)", str(mod.get("nombre") or ""))
        if not m:
            continue
        items = [i for i in (mod.get("items") or []) if isinstance(i, dict)]
        ses[int(m.group(1))] = {
            "modulo": str(mod.get("nombre")),
            "items": [{"titulo": str(i.get("titulo") or ""),
                       "url": str(i.get("url") or "")}
                      for i in items if i.get("tipo") != "subheader"],
        }
    return {"sesiones": ses, "sitio": cfg.get("sitio"),
            "curso_id": cfg.get("curso_id")}


# ---------------------------------------------------- rutas por convención --
def _glob1(dirrel, patron):
    """Primer archivo de `dirrel` que casa con `patron`, o None."""
    d = os.path.join(REPO, dirrel)
    try:
        for f in sorted(os.listdir(d)):
            if re.match(patron, f):
                return f"{dirrel}/{f}"
    except OSError:
        pass
    return None


def rutas_sesion(n):
    """Rutas de la sesión n, derivadas del número. Casi cero parsing.

    El apunte y el capítulo se buscan por glob del número porque su slug es
    parte del nombre; el resto es convención pura.
    """
    d = f"material/curso/sesion-{n:02d}"
    apunte = _glob1(d, rf"^apunte_s{n:02d}_.*\.md$")
    cap = _glob1("material/libro", rf"^cap{n:02d}_.*\.md$")
    acts = []
    dir_act = os.path.join(REPO, d, "actividades")
    try:
        acts = [f"{d}/actividades/{f}" for f in sorted(os.listdir(dir_act))
                if f.endswith(".md")]
    except OSError:
        pass                       # s07 y s13 no tienen actividades/: legítimo

    def _html(rel, raiz="material/_render/site"):
        if not rel:
            return None
        return f"{raiz}/{rel[len('material/'):-3]}.html"

    return {
        "plan": f"{d}/plan.md",
        "apunte": apunte,
        "slides_qmd": f"{d}/slides_s{n:02d}.qmd",
        "capitulo": cap,
        "actividades": acts,
        "apunte_html": _html(apunte),
        "slides_html": f"material/_render/site/curso/sesion-{n:02d}/slides_s{n:02d}.html",
        "capitulo_html": _html(cap),
    }


# ------------------------------------------------------------------ build --
class Indice:
    """Construye el índice, con caché por archivo (mtime+tamaño).

    El repo vive en Google Drive: leer decenas de archivos por red es lento,
    pero os.stat es solo metadata y es barato. Se re-parsea únicamente lo que
    cambió.
    """

    def __init__(self, edicion=None, sin_cache=False):
        self.sin_cache = sin_cache
        self.avisos = []
        self.edicion = edicion or detectar_edicion()
        try:
            with open(CACHE, encoding="utf-8") as fh:
                viejo = json.load(fh)
            self.cache = (viejo.get("archivos") or {}
                          if viejo.get("version") == VERSION_CACHE else {})
        except (OSError, ValueError):
            self.cache = {}
        self.nueva = {}

    def aviso(self, msg):
        if msg not in self.avisos:
            self.avisos.append(msg)

    def _cached(self, rel, parser, obligatorio=True):
        path = os.path.join(REPO, rel)
        try:
            st = os.stat(path)
        except OSError:
            if obligatorio:
                self.aviso(f"falta {rel}")
            return None
        clave = f"{st.st_mtime_ns}:{st.st_size}"
        ent = self.cache.get(rel)
        if ent and ent.get("clave") == clave and not self.sin_cache:
            datos = ent["datos"]
        else:
            texto = _leer(path)
            if texto is None:
                self.aviso(f"no se pudo leer {rel}")
                return None
            try:
                datos = parser(texto)
            except Exception as e:                      # noqa: BLE001
                # Un parser que falla degrada esa fuente, no el panel entero.
                self.aviso(f"{rel}: {type(e).__name__}: {e}")
                return None
        self.nueva[rel] = {"clave": clave, "datos": datos}
        for a in (datos or {}).get("_avisos", []):
            self.aviso(f"{rel}: {a}")
        return datos

    def guardar_cache(self):
        try:
            os.makedirs(os.path.dirname(CACHE), exist_ok=True)
            with open(CACHE, "w", encoding="utf-8") as fh:
                json.dump({"version": VERSION_CACHE, "archivos": self.nueva},
                          fh, ensure_ascii=False)
        except OSError:
            pass

    def construir(self):
        obj = self._cached("OBJETIVOS_APRENDIZAJE.md", parsear_objetivos) or {}
        objetivos = obj.get("objetivos", {})
        familias = obj.get("familias", {})

        mapa = {int(k): v for k, v in
                ((self._cached("PLAN_SEMESTRE.md", parsear_mapa_semestre)
                  or {}).get("sesiones") or {}).items()}
        sidebar = {int(k): v for k, v in
                   ((self._cached("material/_quarto.yml", parsear_sidebar)
                     or {}).get("sesiones") or {}).items()}
        canvas = {int(k): v for k, v in
                  ((self._cached("canvas/canvas.yml", parsear_canvas,
                                 obligatorio=False)
                    or {}).get("sesiones") or {}).items()}

        cal, anio = {}, None
        interrupciones = []
        if self.edicion:
            anio = self.edicion.split("-")[0]
            rel = _ruta_calendario(self.edicion)
            if rel:
                c = self._cached(
                    rel, lambda t, a=anio: parsear_calendario(t, anio=a)) or {}
                cal = {int(k): v for k, v in (c.get("sesiones") or {}).items()}
                interrupciones = c.get("interrupciones") or []
            else:
                self.aviso(f"edición {self.edicion} sin CALENDARIO_*.md")
        else:
            self.aviso("sin edición detectada: el panel funciona sin fechas")

        sesiones = []
        for n in range(1, N_SESIONES + 1):
            r = rutas_sesion(n)
            plan = self._cached(r["plan"], parsear_plan) or {}
            slides = self._cached(
                r["slides_qmd"],
                lambda t: {"subtitulo": str(_front_matter(t).get("subtitle") or "")}
            ) or {}

            m = mapa.get(n, {})
            f = cal.get(n, {})
            sb = sidebar.get(n, {})

            # Dos fuentes de fecha: el calendario (sin año) y el subtitle de
            # las slides (con año). Compararlas es un chequeo gratis.
            f_cal = f.get("fecha")
            f_sl = fecha_es(slides.get("subtitulo", ""), anio=anio)
            if f_cal and f_sl and f_cal.get("iso") != f_sl.get("iso"):
                self.aviso(f"s{n:02d}: el calendario dice {f_cal['crudo']} y "
                           f"las slides {f_sl['crudo']}")

            # El slug del apunte y el del capítulo suelen coincidir, pero no
            # siempre (s02 y s15 divergen): se avisa en vez de asumirlo.
            if r["apunte"] and r["capitulo"]:
                sa = re.sub(rf"^apunte_s{n:02d}_", "",
                            os.path.basename(r["apunte"]))[:-3]
                sc = re.sub(rf"^cap{n:02d}_", "",
                            os.path.basename(r["capitulo"]))[:-3]
                if sa != sc:
                    self.aviso(f"s{n:02d}: slug del apunte ({sa}) distinto del "
                               f"capítulo ({sc})")
            if not r["capitulo"]:
                self.aviso(f"s{n:02d}: sin capítulo cap{n:02d}_*.md")

            mods = plan.get("modulos") or []
            sesiones.append({
                "id": f"s{n:02d}", "n": n,
                "titulo": plan.get("titulo") or sb.get("titulo") or m.get("tema")
                          or f"Sesión {n:02d}",
                "titulo_sidebar": sb.get("titulo", ""),
                "tema": m.get("tema", ""),
                "fecha": f_cal, "fecha_slides": f_sl,
                "hito": f.get("hito"),
                "hitos_plan": m.get("hitos", ""),
                "objetivos": plan.get("objetivos") or m.get("objetivos") or [],
                "objetivos_mapa": m.get("objetivos") or [],
                "depende_de": m.get("depende_de") or [],
                "depende_crudo": m.get("depende_crudo", ""),
                "campos": plan.get("campos") or {},
                "orden_campos": plan.get("orden_campos") or [],
                "modulos": mods,
                "materiales": materiales_de(mods),
                "cierre": plan.get("cierre") or [],
                "enlaces": plan.get("enlaces") or {},
                "demo": m.get("demo"), "demo_crudo": m.get("demo_crudo", ""),
                "slides_subtitulo": slides.get("subtitulo", ""),
                "canvas": canvas.get(n, {}),
                "archivos": r,
            })

        # Dependencias inversas y referencias cruzadas de objetivos.
        for s in sesiones:
            s["requerida_por"] = [o["id"] for o in sesiones
                                  if s["n"] in o["depende_de"]]
        for cod, o in objetivos.items():
            o["sesiones"] = [s["id"] for s in sesiones if cod in s["objetivos"]]

        return {
            "meta": {"edicion": self.edicion, "anio": anio, "repo": REPO,
                     "avisos": self.avisos, "interrupciones": interrupciones},
            "familias": familias, "objetivos": objetivos,
            "sesiones": sesiones,
        }


def construir(edicion=None, sin_cache=False):
    idx = Indice(edicion=edicion, sin_cache=sin_cache)
    datos = idx.construir()
    idx.guardar_cache()
    return datos


# --------------------------------------------------------------- frescura --
def _mtime(rel):
    try:
        return os.stat(os.path.join(REPO, rel)).st_mtime
    except (OSError, TypeError):
        return None


def _estado(src, dst):
    if src is None:
        return "sin-fuente"
    if dst is None:
        return "falta"
    if src - dst <= 0:
        return "ok"
    if src - dst <= 60:
        return "sospechoso"        # Drive reescribe mtimes al sincronizar
    return "viejo"


def frescura(indice):
    """Compara el mtime de cada fuente contra su HTML renderizado.

    Nunca se oculta información detrás de un color: se devuelven ambos
    timestamps para que el panel los muestre en el tooltip.
    """
    pares = [("apunte", "apunte", "apunte_html"),
             ("slides", "slides_qmd", "slides_html"),
             ("capitulo", "capitulo", "capitulo_html")]
    out, viejos, total = {}, 0, 0
    for s in indice["sesiones"]:
        est = {}
        for nombre, k_src, k_out in pares:
            src, dst = _mtime(s["archivos"][k_src]), _mtime(s["archivos"][k_out])
            e = _estado(src, dst)
            est[nombre] = {"estado": e, "fuente": src, "render": dst}
            total += 1
            if e in ("viejo", "falta"):
                viejos += 1
        out[s["id"]] = est
    return {"sesiones": out, "viejos": viejos, "total": total,
            "libro": frescura_libro()}


PDF_LIBRO = "material/libro/LIBRO_CURSO.pdf"


def frescura_libro():
    """Semáforo propio de AM: ¿el PDF del libro va al día con sus capítulos?

    `material/libro/LIBRO_CURSO.pdf` es la única copia del libro y el CI NO la
    reconstruye (la copia como recurso), así que puede quedarse atrás en
    silencio al editar un capítulo. `.githooks/pre-commit` corta ese modo de
    falla al commitear; este semáforo lo ve antes, mientras se prepara.
    """
    pdf = _mtime(PDF_LIBRO)
    fuentes, mas_nuevo, nombre = [], None, None
    d = os.path.join(REPO, "material", "libro")
    try:
        for f in sorted(os.listdir(d)):
            if not (f.endswith(".md") or f.endswith(".qmd") or f == "_quarto.yml"):
                continue
            t = _mtime(f"material/libro/{f}")
            if t is None:
                continue
            fuentes.append(f)
            if mas_nuevo is None or t > mas_nuevo:
                mas_nuevo, nombre = t, f
    except OSError:
        pass
    return {"estado": _estado(mas_nuevo, pdf), "fuente": mas_nuevo,
            "render": pdf, "archivo": nombre, "n_fuentes": len(fuentes)}


def hook_activo():
    """¿Está configurado core.hooksPath? El hook viaja en el repo, pero su
    activación es configuración local: en un clon nuevo hay que ponerla."""
    try:
        with open(os.path.join(REPO, ".git", "config"), encoding="utf-8") as fh:
            return "hooksPath" in fh.read()
    except OSError:
        return False


# --------------------------------------------------------------------- CLI --
def _verificar(indice):
    problemas = 0
    for a in indice["meta"]["avisos"]:
        print(f"  aviso · {a}")
        problemas += 1
    print()
    for s in indice["sesiones"]:
        faltas = []
        if not s["modulos"]:
            faltas.append("módulos")
        elif any(not m["filas"] for m in s["modulos"]):
            faltas.append("tabla de algún módulo")
        if not s["campos"]:
            faltas.append("cabecera")
        if not s["objetivos"]:
            faltas.append("OA")
        if not s["fecha"]:
            faltas.append("fecha")
        if not s["archivos"]["apunte"]:
            faltas.append("apunte")
        if not s["archivos"]["capitulo"]:
            faltas.append("capítulo")
        if not s["materiales"]:
            faltas.append("materiales")
        marca = f"  {s['id']}  {len(s['modulos'])} mód · " \
                f"{sum(len(m['filas']) for m in s['modulos'])} filas · " \
                f"{len(s['materiales'])} materiales · " \
                f"{len(s['archivos']['actividades'])} actividades"
        print(marca + (f"  ⚠ sin: {', '.join(faltas)}" if faltas else ""))
        if faltas:
            problemas += 1
    fr = frescura(indice)
    lib = fr["libro"]
    print(f"\n  renders desactualizados o ausentes: {fr['viejos']}/{fr['total']}")
    print(f"  PDF del libro: {lib['estado']}"
          + (f" (más nuevo: {lib['archivo']})" if lib["estado"] == "viejo" else ""))
    print(f"  hook pre-commit activo: {'sí' if hook_activo() else 'NO'}")
    print(f"  objetivos: {len(indice['objetivos'])} · "
          f"familias: {len(indice['familias'])}")
    return problemas


def main():
    p = argparse.ArgumentParser(description="Índice del panel de sesión MUC860")
    p.add_argument("--verificar", action="store_true",
                   help="informa todo lo que no se pudo parsear")
    p.add_argument("--json", metavar="SESION",
                   help="imprime una sesión (s04) o 'todo'")
    p.add_argument("--edicion", help="directorio de ediciones/ (por defecto, el mayor)")
    p.add_argument("--sin-cache", action="store_true")
    args = p.parse_args()

    indice = construir(edicion=args.edicion, sin_cache=args.sin_cache)

    if args.json:
        if args.json.lower() == "todo":
            print(json.dumps(indice, ensure_ascii=False, indent=2))
            return 0
        ident = args.json.lower()
        if re.match(r"^\d+$", ident):
            ident = f"s{int(ident):02d}"
        for s in indice["sesiones"]:
            if s["id"] == ident:
                print(json.dumps(s, ensure_ascii=False, indent=2))
                return 0
        print(f"no existe {ident}", file=sys.stderr)
        return 1

    if args.verificar:
        print(f"\nEdición: {indice['meta']['edicion']}  ·  "
              f"{len(indice['sesiones'])} sesiones\n")
        return 1 if _verificar(indice) else 0

    print(f"{len(indice['sesiones'])} sesiones · "
          f"{len(indice['objetivos'])} objetivos · "
          f"{len(indice['meta']['avisos'])} avisos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
