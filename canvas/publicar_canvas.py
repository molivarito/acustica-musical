#!/usr/bin/env python3
"""publicar_canvas — sincroniza los módulos del curso MUC860 Acústica Musical en Canvas.

Fuente de verdad: canvas.yml (estructura de módulos e ítems). Este script
NUNCA publica nada por sí mismo: todo lo que crea queda unpublished, y
nunca borra ni despublica algo que ya estaba en Canvas.

El token de la API se lee de la variable de entorno CANVAS_TOKEN o, si no
está, de ~/.canvas_token. El token JAMÁS se escribe en canvas.yml, en
logs ni en ningún archivo de este repo.

Uso:
  publicar_canvas.py estado                 # lista módulos/ítems actuales
  publicar_canvas.py sync [--dry-run]       # crea/actualiza según canvas.yml
  publicar_canvas.py verificar              # revisa external_url rotas (404)

Opciones globales:
  --config RUTA   archivo de configuración (default: canvas.yml junto al script)
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

try:
    import yaml
except ImportError:
    print("Requiere PyYAML (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG = os.path.join(SCRIPT_DIR, "canvas.yml")


# ------------------------------------------------------------------ token --
def get_token():
    """Token de Canvas: variable de entorno CANVAS_TOKEN o ~/.canvas_token.

    PROHIBIDO persistirlo en ningún archivo del repo.
    """
    tok = os.environ.get("CANVAS_TOKEN")
    if tok and tok.strip():
        return tok.strip()
    ruta = os.path.expanduser("~/.canvas_token")
    if os.path.isfile(ruta):
        with open(ruta, encoding="utf-8") as f:
            tok = f.read().strip()
        if tok:
            return tok
    print("ERROR: no se encontró el token de Canvas.\n"
          "Defínelo en la variable de entorno CANVAS_TOKEN o guárdalo en "
          "~/.canvas_token (un archivo con el token y nada más).",
          file=sys.stderr)
    sys.exit(2)


# -------------------------------------------------------------- config.yml --
def cargar_config(ruta):
    with open(ruta, encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    for campo in ("curso_id", "base_url", "modulos"):
        if campo not in cfg:
            print(f"ERROR: {ruta} no define '{campo}'", file=sys.stderr)
            sys.exit(2)
    sitio = (cfg.get("sitio") or "").rstrip("/")
    for m in cfg["modulos"]:
        for it in m.get("items", []):
            if it.get("url"):
                it["url"] = it["url"].replace("{sitio}", sitio)
    return cfg


# ------------------------------------------------------------------- HTTP --
def _next_link(link_header):
    """Extrae la URL rel="next" de un header Link (paginación Canvas)."""
    if not link_header:
        return None
    for parte in link_header.split(","):
        segs = parte.split(";")
        if len(segs) < 2:
            continue
        url = segs[0].strip().strip("<>")
        rel = segs[1].strip()
        if rel == 'rel="next"':
            return url
    return None


def _request(method, url, token, data=None, reintento=True):
    body = None
    headers = {"Authorization": f"Bearer {token}"}
    if data is not None:
        body = urllib.parse.urlencode(data, doseq=True).encode()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            link = resp.headers.get("Link", "")
            payload = resp.read()
            data_out = json.loads(payload) if payload else None
            return data_out, link
    except urllib.error.HTTPError as e:
        errbody = e.read().decode(errors="replace")
        if e.code == 403 and "rate limit" in errbody.lower() and reintento:
            print("  (rate limit de Canvas, esperando 5s y reintentando...)",
                  file=sys.stderr)
            time.sleep(5)
            return _request(method, url, token, data, reintento=False)
        if e.code == 401:
            print("ERROR 401: token de Canvas inválido o expirado.",
                  file=sys.stderr)
        elif e.code == 404:
            print(f"ERROR 404: recurso no encontrado ({url}). "
                  "¿curso_id correcto en canvas.yml?", file=sys.stderr)
        else:
            print(f"ERROR HTTP {e.code} en {method} {url}: {errbody[:400]}",
                  file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR de red al conectar con {url}: {e}", file=sys.stderr)
        sys.exit(1)


def api_get_all(base_url, path, token, params=None):
    """GET con paginación completa (sigue Link: rel=next)."""
    url = base_url + path
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)
    out = []
    while url:
        data, link = _request("GET", url, token)
        out.extend(data or [])
        url = _next_link(link)
    return out


def api_post(base_url, path, token, data):
    result, _ = _request("POST", base_url + path, token, data)
    return result


def api_put(base_url, path, token, data):
    result, _ = _request("PUT", base_url + path, token, data)
    return result


def api_delete(base_url, path, token):
    result, _ = _request("DELETE", base_url + path, token)
    return result


# --------------------------------------------------------------- comandos --
def cmd_estado(args):
    token = get_token()
    cfg = cargar_config(args.config)
    base = cfg["base_url"].rstrip("/")
    curso = cfg["curso_id"]
    modulos = api_get_all(base, f"/api/v1/courses/{curso}/modules", token,
                           {"include[]": "items", "per_page": 100})
    if not modulos:
        print("(el curso no tiene módulos)")
        return 0
    for m in sorted(modulos, key=lambda m: m.get("position") or 0):
        pub = "publicado" if m.get("published") else "NO publicado"
        print(f"[{m['id']}] {m['name']}  (posición {m.get('position')}, {pub})")
        items = m.get("items") or []
        if not items:
            print("    (sin ítems)")
        for it in items:
            pubit = "publicado" if it.get("published") else "no publicado"
            sangria = "  " * (it.get("indent") or 0)
            extra = f" -> {it['external_url']}" if it.get("external_url") else ""
            print(f"    {sangria}[{it['id']}] ({it.get('type')}, {pubit}) "
                  f"{it['title']}{extra}")
    return 0


def cmd_sync(args):
    token = get_token()
    cfg = cargar_config(args.config)
    base = cfg["base_url"].rstrip("/")
    curso = cfg["curso_id"]
    dry = args.dry_run
    prefijo = "[dry-run] " if dry else ""

    existentes = api_get_all(base, f"/api/v1/courses/{curso}/modules", token,
                              {"include[]": "items", "per_page": 100})
    por_nombre = {m["name"]: m for m in existentes}
    nombres_config = set()
    cambios = 0

    for i, modcfg in enumerate(cfg["modulos"], start=1):
        nombre = modcfg["nombre"]
        nombres_config.add(nombre)
        m = por_nombre.get(nombre)

        if m is None:
            print(f"{prefijo}CREAR módulo: \"{nombre}\" (posición {i}, unpublished)")
            cambios += 1
            if not dry:
                m = api_post(base, f"/api/v1/courses/{curso}/modules", token, {
                    "module[name]": nombre,
                    "module[position]": i,
                    "module[published]": "false",
                })
                print(f"    -> creado id={m['id']}")
            else:
                m = {"id": None, "items": []}
        elif (m.get("position") or 0) != i:
            print(f"{prefijo}ACTUALIZAR posición de módulo \"{nombre}\": "
                  f"{m.get('position')} -> {i}")
            cambios += 1
            if not dry:
                api_put(base, f"/api/v1/courses/{curso}/modules/{m['id']}",
                        token, {"module[position]": i})

        items_actuales = {it["title"]: it for it in (m.get("items") or [])}
        titulos_config = []

        for j, itcfg in enumerate(modcfg.get("items", []), start=1):
            titulo = itcfg["titulo"]
            titulos_config.append(titulo)
            tipo = itcfg.get("tipo", "external_url")
            indent = itcfg.get("indent", 0)
            url = itcfg.get("url")
            tipo_canvas = "SubHeader" if tipo == "subheader" else "ExternalUrl"
            existente = items_actuales.get(titulo)

            if existente is None:
                print(f"{prefijo}  CREAR ítem en \"{nombre}\": \"{titulo}\" "
                      f"({tipo}, unpublished)")
                cambios += 1
                if not dry:
                    payload = {
                        "module_item[title]": titulo,
                        "module_item[position]": j,
                        "module_item[indent]": indent,
                        "module_item[type]": tipo_canvas,
                        "module_item[published]": "false",
                    }
                    if tipo != "subheader":
                        payload["module_item[external_url]"] = url
                        payload["module_item[new_tab]"] = "true"
                    api_post(base,
                             f"/api/v1/courses/{curso}/modules/{m['id']}/items",
                             token, payload)
                continue

            if existente.get("type") != tipo_canvas:
                print(f"  AVISO: \"{titulo}\" cambió de tipo "
                      f"({existente.get('type')} -> {tipo_canvas}); Canvas no "
                      "permite editar el tipo de un ítem por API. Bórralo y "
                      "recréalo a mano si corresponde.")
                continue

            diffs = []
            if tipo != "subheader" and existente.get("external_url") != url:
                diffs.append(f"url: {existente.get('external_url')!r} -> {url!r}")
            if (existente.get("indent") or 0) != indent:
                diffs.append(f"indent: {existente.get('indent')} -> {indent}")
            if (existente.get("position") or 0) != j:
                diffs.append(f"posición: {existente.get('position')} -> {j}")

            if diffs:
                print(f"{prefijo}  ACTUALIZAR ítem \"{titulo}\": "
                      f"{', '.join(diffs)}")
                cambios += 1
                if not dry:
                    payload = {
                        "module_item[position]": j,
                        "module_item[indent]": indent,
                    }
                    if tipo != "subheader":
                        payload["module_item[external_url]"] = url
                    api_put(base,
                            f"/api/v1/courses/{curso}/modules/{m['id']}/items/"
                            f"{existente['id']}", token, payload)

        for titulo in items_actuales:
            if titulo not in titulos_config:
                print(f"  (extra, no tocado) ítem en Canvas fuera de la config "
                      f"en \"{nombre}\": \"{titulo}\"")

    for nombre in por_nombre:
        if nombre not in nombres_config:
            print(f"(extra, no tocado) módulo en Canvas fuera de la config: "
                  f"\"{nombre}\"")

    if cambios == 0:
        print(f"{prefijo}Sin cambios: Canvas ya refleja canvas.yml.")
    else:
        verbo = "Se aplicarían" if dry else "Se aplicaron"
        print(f"{prefijo}{verbo} {cambios} cambio(s).")
    return 0


def _check_url(url):
    """HEAD (con fallback a GET si el servidor no lo soporta)."""
    for metodo in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=metodo)
            with urllib.request.urlopen(req, timeout=10) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if metodo == "HEAD" and e.code in (405, 501):
                continue
            return e.code
        except Exception:
            return None
    return None


def numero_semana_modulo(nombre_modulo):
    """Extrae el N de un nombre de módulo "N.- tema"; None si no matchea
    (p.ej. "Información del curso", que siempre se considera liberado).

    Función reusada por publicar_sitio.py (import directo, mismo directorio).
    """
    m = re.match(r"\s*(\d+)\.-", nombre_modulo)
    return int(m.group(1)) if m else None


def cmd_verificar(args):
    cfg = cargar_config(args.config)
    publicado_hasta = cfg.get("publicado_hasta", 0)
    total = 0
    rotos = 0
    saltados = 0
    for modcfg in cfg["modulos"]:
        semana = numero_semana_modulo(modcfg["nombre"])
        if semana is not None and semana > publicado_hasta:
            for itcfg in modcfg.get("items", []):
                if itcfg.get("url"):
                    saltados += 1
                    print(f"[--- ] {itcfg['titulo']}  (no liberada aún)")
            continue
        for itcfg in modcfg.get("items", []):
            url = itcfg.get("url")
            if not url:
                continue
            total += 1
            estado = _check_url(url)
            ok = estado is not None and 200 <= estado < 400
            if not ok:
                rotos += 1
            marca = "OK " if ok else f"FALLA({estado})"
            print(f"[{marca}] {itcfg['titulo']}  {url}")
    extra = f", {saltados} sin liberar (no revisado)" if saltados else ""
    print(f"\n{total} enlace(s) revisado(s), {rotos} con problemas{extra}.")
    return 1 if rotos else 0


# ----------------------------------------------------------------- main --
def main():
    p = argparse.ArgumentParser(
        description="Sincroniza los módulos del curso MUC860 Acústica Musical en Canvas "
                     "desde canvas.yml.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--config", default=DEFAULT_CONFIG,
                    help="archivo de configuración (default: canvas.yml junto "
                         "al script)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser(
        "estado", help="lista módulos e ítems existentes en Canvas"
    ).set_defaults(fn=cmd_estado)

    s = sub.add_parser(
        "sync", help="crea/actualiza módulos e ítems según canvas.yml "
                      "(idempotente; nunca publica ni borra)")
    s.add_argument("--dry-run", action="store_true",
                    help="imprime el plan sin llamar a la API de escritura")
    s.set_defaults(fn=cmd_sync)

    sub.add_parser(
        "verificar",
        help="hace HEAD/GET a cada external_url de canvas.yml y reporta 404s"
    ).set_defaults(fn=cmd_verificar)

    args = p.parse_args()
    sys.exit(args.fn(args) or 0)


if __name__ == "__main__":
    main()
