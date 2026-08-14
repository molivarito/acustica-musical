#!/usr/bin/env python3
"""Panel de sesión MUC860 · Acústica Musical — servidor local.

Mesa de trabajo para preparar una sesión: elegida s01–s15, muestra a la vez su
plan (los dos módulos con su guion de 5 columnas), la lista de materiales que
hay que llevar a la sala, las slides, el apunte, el capítulo del libro, las
guías de actividades, la demo y los objetivos OA.

Solo stdlib + PyYAML, y solo escucha en 127.0.0.1 — mismo molde que el panel
hermano de SyS.

No escribe nada en las fuentes del repo. Lo único que genera son los renders
de Quarto bajo material/_render/ (directorio generado) cuando se piden
explícitamente, el PDF del libro si se pulsa su botón, y el caché en ~/.cache.

Ojo con la visibilidad: este panel muestra material SOLO-PROFESOR (planes,
pautas, guiones). Por eso escucha únicamente en loopback y nunca escribe
dentro de material/_render/site/, que es lo que se publica.

Uso:
    python3 panel/panel.py                    # abre el panel en el navegador
    python3 panel/panel.py --permitir-publicar # habilita la acción de Canvas
"""

import argparse
import http.server
import json
import os
import re
import subprocess
import sys
import threading
import urllib.parse
import webbrowser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indice as idx                                       # noqa: E402
import agenda as agd                                       # noqa: E402

REPO = idx.REPO
MATERIAL = idx.MATERIAL
UI_HTML = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "panel_ui.html")

# Convención de AM: quarto se invoca a través de conda (ver CLAUDE.md).
CONDA = ["conda", "run", "-n", "base", "quarto"]
# pandoc viene con Quarto; es lo que convierte el plan.md, que NO existe en
# HTML porque la regla de visibilidad lo excluye del render del sitio.
PANDOC = next((p for p in ("/Users/pdelac/miniforge3/bin/pandoc",
                           "/usr/local/bin/pandoc", "/opt/homebrew/bin/pandoc")
               if os.path.isfile(p)), "pandoc")

# Directorios que el panel puede servir. Diccionario cerrado: el nombre del
# montaje nunca se concatena a una ruta del sistema de archivos.
MONTAJES = {
    "site": os.path.join(MATERIAL, "_render", "site"),
    "canvas": os.path.join(MATERIAL, "_render", "canvas"),
    "figuras": os.path.join(MATERIAL, "assets", "figuras"),
    "demos": os.path.join(MATERIAL, "demos"),
    "libro": os.path.join(MATERIAL, "libro"),
}

# Allowlist, no blocklist: cualquier extensión no listada devuelve 404, así
# nunca se sirve un .md, .qmd, .py o .yml aunque esté dentro del montaje. Es
# lo que impide que un plan.md solo-profesor salga por /r/.
_CTYPE = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".mjs": "application/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".map": "application/json; charset=utf-8",
    ".svg": "image/svg+xml; charset=utf-8",
    ".txt": "text/plain; charset=utf-8",
    ".csv": "text/csv; charset=utf-8",
    ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
    ".gif": "image/gif", ".webp": "image/webp", ".avif": "image/avif",
    ".ico": "image/x-icon",
    ".woff": "font/woff", ".woff2": "font/woff2",
    ".ttf": "font/ttf", ".otf": "font/otf",
    ".mp3": "audio/mpeg", ".wav": "audio/wav", ".ogg": "audio/ogg",
    ".m4a": "audio/mp4", ".mp4": "video/mp4",
    ".pdf": "application/pdf",
}
_RANGEABLE = {".mp3", ".wav", ".ogg", ".m4a", ".mp4", ".pdf"}

# Oculta el cromo de Quarto dentro de los iframes. Se inyecta en los bytes
# servidos; el archivo en disco nunca se toca.
_DESNUDO = """<style id="panel-desnudo">
#quarto-sidebar,#quarto-header,#quarto-margin-sidebar,#quarto-sidebar-glass,
.nav-page,.toc-actions,#quarto-back-to-top{display:none!important}
#quarto-content{padding:0!important;margin:0!important;grid-template-columns:1fr!important}
main.content,#quarto-document-content{margin-left:0!important;margin-right:0!important;
  max-width:none!important;padding:1rem 1.4rem!important}
body{overflow-x:hidden}
</style>"""

_LOCK = threading.Lock()
_ESTADO = {"indice": None, "edicion": None, "sin_cache": False,
           "permitir_publicar": False, "editor": None}
_MD_CACHE = {}

_JOB = {"activo": False, "titulo": "", "lineas": [], "error": None,
        "terminado": False}


# ------------------------------------------------------------------ índice --
def indice_actual(refrescar=False):
    with _LOCK:
        if _ESTADO["indice"] is None or refrescar:
            _ESTADO["indice"] = idx.construir(
                edicion=_ESTADO["edicion"], sin_cache=_ESTADO["sin_cache"])
        return _ESTADO["indice"]


# ------------------------------------------------- Markdown -> HTML (pandoc) --
def _dentro_del_repo(rel, extensiones):
    """realpath dentro del repo y con extensión permitida, o FileNotFoundError.

    Mismo guardarraíl que los estáticos: realpath neutraliza `..`, enlaces
    simbólicos y rutas absolutas de una vez, y el prefijo es quien decide.
    """
    rel = urllib.parse.unquote(str(rel or ""))
    if not rel or "\x00" in rel:
        raise FileNotFoundError("ruta vacía o inválida")
    real = os.path.realpath(os.path.join(REPO, rel))
    raiz = os.path.realpath(REPO)
    if real != raiz and not real.startswith(raiz + os.sep):
        raise FileNotFoundError("fuera del repositorio")
    if os.path.splitext(real)[1].lower() not in extensiones:
        raise FileNotFoundError("extensión no permitida")
    if not os.path.isfile(real):
        raise FileNotFoundError(rel)
    return real


def md_a_html(rel):
    """Convierte un .md/.qmd del repo a HTML con pandoc, cacheado por mtime.

    El plan de sesión, las guías de actividades y los capítulos del libro se
    ven así. No se escribe un renderizador a mano porque en AM **las tablas
    son el guion**: las dos tablas de 5 columnas de cada plan.md son el
    artefacto central, y un md() mínimo no sabe de tablas.

    Con --mathjax la matemática sale como \\(...\\) y la renderiza KaTeX en el
    cliente.
    """
    real = _dentro_del_repo(rel, {".md", ".qmd"})
    st = os.stat(real)
    clave = f"{real}:{st.st_mtime_ns}:{st.st_size}"
    if clave in _MD_CACHE:
        return _MD_CACHE[clave]
    p = subprocess.run(
        [PANDOC, real, "-f", "gfm+tex_math_dollars", "-t", "html", "--mathjax"],
        capture_output=True, text=True, timeout=60)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or "pandoc falló").strip()[:400])
    _MD_CACHE.clear()               # un plan a la vez; no crece sin control
    _MD_CACHE[clave] = p.stdout
    return p.stdout


# ------------------------------------------------------------- publicación --
def _git(*args, timeout=8):
    """git con timeout: el repo vive en Google Drive y puede colgarse.

    Un `git log` que no vuelve dejaría el panel congelado justo cuando se
    está preparando clase, así que aquí nada bloquea: se informa y se sigue.
    """
    try:
        p = subprocess.run(["git", *args], cwd=REPO, capture_output=True,
                           text=True, timeout=timeout)
        return p.stdout.strip() if p.returncode == 0 else None
    except (subprocess.TimeoutExpired, OSError):
        return None


def estado_publicacion():
    """Estado de publicación de AM, todo local y sin red.

    En AM no hay nada que "liberar": cada push a main dispara el workflow y el
    sitio se reconstruye solo. Lo útil aquí es otra cosa — saber si lo que
    tengo en el disco ya salió, y si el PDF del libro va al día.
    """
    out = {"permitir": _ESTADO["permitir_publicar"], "hook": idx.hook_activo(),
           "sucio": None, "sin_push": None, "ultimo": None, "rama": None,
           "sitio": None, "curso_id": None, "libro": idx.frescura_libro(),
           "error": None}

    est = _git("status", "--porcelain")
    if est is None:
        out["error"] = "git no respondió (¿objetos deshidratados en Drive?)"
    else:
        out["sucio"] = [l for l in est.split("\n") if l.strip()]

    out["rama"] = _git("rev-parse", "--abbrev-ref", "HEAD")
    n = _git("rev-list", "--count", "@{u}..HEAD")
    out["sin_push"] = int(n) if (n or "").isdigit() else None
    out["ultimo"] = _git("log", "-1", "--format=%h · %cd · %s",
                         "--date=format:%d-%b %H:%M")

    try:
        import yaml                                        # noqa: PLC0415
        with open(os.path.join(REPO, "canvas", "canvas.yml"),
                  encoding="utf-8") as fh:
            cfg = yaml.safe_load(fh) or {}
        out["sitio"] = cfg.get("sitio")
        out["curso_id"] = cfg.get("curso_id")
    except Exception:                                      # noqa: BLE001
        pass
    return out


# ------------------------------------------------------------------ render --
def _comandos_sesion(n):
    """Render de una sesión: su apunte, sus slides y su capítulo del libro."""
    r = idx.rutas_sesion(n)
    cmds = []
    for k in ("apunte", "slides_qmd", "capitulo"):
        rel = r.get(k)
        if rel:
            cmds.append((CONDA + ["render", os.path.relpath(
                os.path.join(REPO, rel), MATERIAL)], MATERIAL))
    return cmds


def _comandos_todo():
    return [(CONDA + ["render"], MATERIAL)]


def _comandos_libro():
    return [(CONDA + ["render", "libro"], MATERIAL)]


def _correr(comandos, titulo, al_terminar=None):
    _JOB.update({"activo": True, "titulo": titulo, "lineas": [],
                 "error": None, "terminado": False})

    def _tarea():
        try:
            for cmd, cwd in comandos:
                _JOB["lineas"].append(f"$ {' '.join(cmd)}  (en {cwd})")
                p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, text=True)
                for linea in p.stdout:
                    linea = linea.rstrip()
                    if linea:
                        _JOB["lineas"].append(linea)
                        del _JOB["lineas"][:-400]
                if p.wait() != 0:
                    raise RuntimeError(f"salió con código {p.returncode}")
            _JOB["lineas"].append("listo.")
        except Exception as e:                             # noqa: BLE001
            _JOB["error"] = f"{type(e).__name__}: {e}"
        finally:
            _JOB["activo"] = False
            _JOB["terminado"] = True
            if al_terminar:
                al_terminar()

    threading.Thread(target=_tarea, daemon=True).start()


# -------------------------------------------------------------- estáticos ---
def _resolver(mount, ruta):
    raiz = MONTAJES.get(mount)
    if raiz is None:
        return None
    ruta = urllib.parse.unquote(ruta)
    if "\x00" in ruta:
        return None
    real = os.path.realpath(os.path.join(raiz, ruta))
    raiz_real = os.path.realpath(raiz)
    if real != raiz_real and not real.startswith(raiz_real + os.sep):
        return None
    if os.path.isdir(real):
        real = os.path.join(real, "index.html")
    if os.path.splitext(real)[1].lower() not in _CTYPE:
        return None
    if not os.path.isfile(real):
        return None
    return real


# --------------------------------------------------------------- servidor ---
class Handler(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "PanelAM/1.0"

    def log_message(self, fmt, *args):
        pass

    def _bytes(self, status, cuerpo, ctype, extra=None):
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(cuerpo)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(cuerpo)

    def _json(self, status, obj):
        self._bytes(status, json.dumps(obj, ensure_ascii=False).encode("utf-8"),
                    "application/json; charset=utf-8",
                    {"Cache-Control": "no-store"})

    def _error(self, e):
        if isinstance(e, ValueError):
            self._json(400, {"error": str(e)})
        elif isinstance(e, FileNotFoundError):
            self._json(404, {"error": str(e)})
        else:
            self._json(500, {"error": f"{type(e).__name__}: {e}"})

    # -- GET -----------------------------------------------------------------
    def do_GET(self):                                      # noqa: N802
        partes = urllib.parse.urlparse(self.path)
        ruta, q = partes.path, urllib.parse.parse_qs(partes.query)
        try:
            if ruta == "/":
                return self._bytes(200, open(UI_HTML, "rb").read(),
                                   "text/html; charset=utf-8",
                                   {"Cache-Control": "no-store"})
            if ruta == "/api/indice":
                return self._json(200, indice_actual(
                    refrescar=q.get("refrescar", ["0"])[0] == "1"))
            if ruta == "/api/frescura":
                return self._json(200, idx.frescura(indice_actual()))
            if ruta == "/api/md":
                return self._json(200, {
                    "ruta": q.get("ruta", [""])[0],
                    "html": md_a_html(q.get("ruta", [""])[0])})
            if ruta == "/api/render-estado":
                return self._json(200, dict(_JOB))
            if ruta == "/api/publicacion":
                return self._json(200, estado_publicacion())
            if ruta == "/api/agenda":
                return self._json(200, agd.generar(edicion=_ESTADO["edicion"]))
            if ruta.startswith("/r/"):
                return self._estatico(ruta, q)
            return self._json(404, {"error": "ruta desconocida"})
        except BrokenPipeError:
            pass
        except Exception as e:                             # noqa: BLE001
            try:
                self._error(e)
            except BrokenPipeError:
                pass

    do_HEAD = do_GET

    def _estatico(self, ruta, q):
        mount, _, rel = ruta[3:].partition("/")
        real = _resolver(mount, rel)
        if real is None:
            return self._json(404, {"error": "no encontrado"})
        ext = os.path.splitext(real)[1].lower()
        ctype = _CTYPE[ext]

        if ext == ".html":
            datos = open(real, "rb").read()
            if q.get("desnudo", ["0"])[0] == "1" and "slides_" not in \
                    os.path.basename(real):
                texto = datos.decode("utf-8", "replace")
                if "</head>" in texto:
                    texto = texto.replace("</head>", _DESNUDO + "</head>", 1)
                datos = texto.encode("utf-8")
            return self._bytes(200, datos, ctype, {"Cache-Control": "no-store"})

        cache = "no-store" if ext == ".json" else "max-age=3600"
        rango = self.headers.get("Range") if ext in _RANGEABLE else None
        tam = os.path.getsize(real)
        if rango:
            m = re.match(r"bytes=(\d*)-(\d*)", rango.strip())
            if m and (m.group(1) or m.group(2)):
                ini = int(m.group(1)) if m.group(1) else max(
                    0, tam - int(m.group(2)))
                fin = int(m.group(2)) if m.group(1) and m.group(2) else tam - 1
                fin = min(fin, tam - 1)
                if ini <= fin:
                    with open(real, "rb") as fh:
                        fh.seek(ini)
                        datos = fh.read(fin - ini + 1)
                    return self._bytes(
                        206, datos, ctype,
                        {"Content-Range": f"bytes {ini}-{fin}/{tam}",
                         "Accept-Ranges": "bytes", "Cache-Control": cache})
        return self._bytes(200, open(real, "rb").read(), ctype,
                           {"Cache-Control": cache, "Accept-Ranges": "bytes"})

    # -- POST ----------------------------------------------------------------
    def do_POST(self):                                     # noqa: N802
        ruta = urllib.parse.urlparse(self.path).path
        try:
            n = int(self.headers.get("Content-Length") or 0)
            cuerpo = json.loads(self.rfile.read(n) or b"{}")
            if ruta == "/api/abrir":
                return self._json(200, self.api_abrir(cuerpo))
            if ruta == "/api/render":
                return self._json(200, self.api_render(cuerpo))
            if ruta == "/api/ci":
                return self._json(200, self.api_ci())
            if ruta == "/api/canvas-estado":
                return self._json(200, self.api_canvas_estado())
            if ruta == "/api/agenda":
                return self._json(200, self.api_agenda(cuerpo))
            return self._json(404, {"error": "ruta desconocida"})
        except BrokenPipeError:
            pass
        except Exception as e:                             # noqa: BLE001
            try:
                self._error(e)
            except BrokenPipeError:
                pass

    def api_abrir(self, cuerpo):
        rel = str(cuerpo.get("ruta") or "")
        if not rel:
            raise ValueError("falta 'ruta'")
        real = os.path.realpath(os.path.join(REPO, rel))
        raiz = os.path.realpath(REPO)
        if real != raiz and not real.startswith(raiz + os.sep):
            raise ValueError("la ruta debe estar dentro del repo")
        if not os.path.exists(real):
            raise FileNotFoundError(rel)

        # `open` a secas NO sirve para los .md de este curso: en macOS el tipo
        # public.markdown lo reclama Xcode (com.apple.dt.document.markdown), así
        # que el comando devuelve 0 y no aparece nada en pantalla — el botón
        # parece muerto. Se intenta un editor de verdad, luego el editor de
        # texto por omisión, y solo al final el manejador del sistema.
        ed = _editor()
        intentos = []
        if ed:
            intentos.append((["open", "-a", ed, real], ed))
        intentos.append((["open", "-t", real], "editor de texto"))
        intentos.append((["open", real], "app por omisión"))
        errores = []
        for cmd, con in intentos:
            p = subprocess.run(cmd, capture_output=True, text=True)
            if p.returncode == 0:
                return {"ok": True, "ruta": rel, "con": con}
            errores.append((p.stderr or "").strip())
        raise RuntimeError("no se pudo abrir: " + " · ".join(e for e in errores if e))

    def api_render(self, cuerpo):
        if _JOB["activo"]:
            raise ValueError("ya hay un render en curso")
        if cuerpo.get("libro"):
            _correr(_comandos_libro(), "Regenerando el PDF del libro",
                    al_terminar=lambda: indice_actual(refrescar=True))
        elif cuerpo.get("todo"):
            _correr(_comandos_todo(), "Renderizando el sitio completo",
                    al_terminar=lambda: indice_actual(refrescar=True))
        else:
            n = cuerpo.get("sesion")
            if not isinstance(n, int) or not 1 <= n <= idx.N_SESIONES:
                raise ValueError(
                    f"'sesion' debe ser un entero entre 1 y {idx.N_SESIONES}")
            _correr(_comandos_sesion(n), f"Actualizando s{n:02d}",
                    al_terminar=lambda: indice_actual(refrescar=True))
        return {"ok": True, "titulo": _JOB["titulo"]}

    def api_agenda(self, cuerpo):
        """Marca o desmarca tareas de la agenda; lo único que escribe es
        ediciones/<ed>/agenda_estado.yml (nunca el calendario ni las reglas)."""
        ids = cuerpo.get("ids")
        if not isinstance(ids, list) or not all(
                isinstance(i, str) and i for i in ids):
            raise ValueError("'ids' debe ser una lista de strings")
        conocidos = {t["id"] for t in
                     agd.generar(edicion=_ESTADO["edicion"])["tareas"]}
        raros = [i for i in ids if i not in conocidos]
        if raros:
            raise ValueError(f"ids desconocidos: {', '.join(raros[:5])}")
        agd.marcar(ids, hecho=bool(cuerpo.get("hecho", True)),
                   edicion=_ESTADO["edicion"])
        return {"ok": True,
                "agenda": agd.generar(edicion=_ESTADO["edicion"])}

    def api_ci(self):
        """Último workflow de GitHub Actions. Necesita red y `gh`."""
        if _JOB["activo"]:
            raise ValueError("hay otro proceso en curso")
        if not _cual("gh"):
            raise ValueError("gh no está instalado: no se puede consultar el CI")
        _correr([(["gh", "run", "list", "--limit", "3"], REPO)],
                "Consultando GitHub Actions")
        return {"ok": True}

    def api_canvas_estado(self):
        """Consulta de solo lectura del estado de Canvas.

        `publicar_canvas.py sync` nunca publica ni borra, pero igual va detrás
        de --permitir-publicar: es la única acción del panel que sale a la red
        del curso.
        """
        if not _ESTADO["permitir_publicar"]:
            raise ValueError(
                "arranca el panel con --permitir-publicar para consultar Canvas")
        if _JOB["activo"]:
            raise ValueError("hay otro proceso en curso")
        _correr([([sys.executable,
                   os.path.join(REPO, "canvas", "publicar_canvas.py"),
                   "estado"], REPO)], "Consultando el estado en Canvas")
        return {"ok": True}


def _cual(prog):
    import shutil                                          # noqa: PLC0415
    return shutil.which(prog)


# Editores GUI para el plan, en orden de preferencia; Readdown primero porque
# es el editor Markdown que usa el profesor. Se comprueba el bundle instalado,
# no el nombre corto: VS Code es "Visual Studio Code.app" y `open -a Code` falla.
_EDITORES = ("Readdown", "Visual Studio Code", "Cursor", "Sublime Text", "Zed",
             "BBEdit", "TextMate", "MacVim")


def _editor():
    if _ESTADO.get("editor"):
        return _ESTADO["editor"]
    for n in _EDITORES:
        for base in ("/Applications", os.path.expanduser("~/Applications")):
            if os.path.isdir(os.path.join(base, n + ".app")):
                return n
    return None


def _detener():
    """Mata el panel de ESTE curso que esté corriendo, menos este proceso.

    Existe porque la app del Dock deja el servidor desacoplado: sin esto habría
    que ir al terminal justo para lo que la app venía a evitar.

    Se compara contra la **ruta absoluta** de este script, no contra el patrón
    "panel/panel.py": el curso de Señales y Sistemas tiene un panel gemelo en
    la misma ruta relativa, y buscar por patrón detendría el del otro curso.
    """
    yo = os.path.abspath(__file__)
    # -ww: que ps no trunque la línea de comando (la ruta es larga).
    r = subprocess.run(["/bin/ps", "-Awwo", "pid=,command="],
                       capture_output=True, text=True)
    # Un panel arrancado a mano ("python3 panel/panel.py" desde la raíz)
    # sale en ps con la ruta RELATIVA y el filtro por ruta absoluta no lo
    # ve. El puerto sí es inequívoco (SyS usa el 8766, fuera del rango
    # 8767–8776 de este panel): se acepta además cualquier proceso que
    # escuche en nuestro rango y cuyo comando mencione panel.py.
    l = subprocess.run(["/usr/sbin/lsof", "-nP", "-t",
                        "-iTCP:8767-8776", "-sTCP:LISTEN"],
                       capture_output=True, text=True)
    escuchando = {int(p) for p in l.stdout.split() if p.isdigit()}
    pids = []
    for linea in r.stdout.splitlines():
        partes = linea.strip().split(None, 1)
        if len(partes) != 2 or not partes[0].isdigit():
            continue
        pid, cmd = int(partes[0]), partes[1]
        if pid == os.getpid():
            continue
        if yo in cmd or (pid in escuchando and "panel.py" in cmd):
            pids.append(pid)
    if not pids:
        print("no hay ningún panel corriendo.")
        return 0
    for pid in pids:
        try:
            os.kill(pid, 15)
            print(f"detenido (pid {pid})")
        except OSError as e:
            print(f"no se pudo detener {pid}: {e}", file=sys.stderr)
    return 0


def _servir(puerto, abrir):
    ultimo = None
    for p in range(puerto, puerto + 10):
        try:
            httpd = http.server.ThreadingHTTPServer(("127.0.0.1", p), Handler)
        except OSError as e:
            ultimo = e
            continue
        url = f"http://127.0.0.1:{p}/"
        print(f"Panel de sesión · MUC860 — {url}  (Ctrl+C para detener)")
        if abrir:
            threading.Timer(0.4, lambda: webbrowser.open(url)).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nadiós.")
        return 0
    print(f"no se pudo abrir ningún puerto entre {puerto} y {puerto + 9}: "
          f"{ultimo}", file=sys.stderr)
    return 1


def main():
    p = argparse.ArgumentParser(description="Panel de sesión MUC860")
    p.add_argument("--puerto", type=int, default=8767)
    p.add_argument("--no-abrir", action="store_true")
    p.add_argument("--edicion", help="directorio de ediciones/ (por defecto, el mayor)")
    p.add_argument("--sin-cache", action="store_true")
    p.add_argument("--permitir-publicar", action="store_true",
                   help="habilita la consulta a Canvas (curso MUC860-1)")
    p.add_argument("--editor", metavar="APP",
                   help="app con la que abrir el plan (p. ej. 'Cursor'); "
                        "por omisión, el primer editor instalado que se encuentre")
    p.add_argument("--detener", action="store_true",
                   help="detiene el panel que esté corriendo y sale")
    args = p.parse_args()

    if args.detener:
        return _detener()

    _ESTADO["edicion"] = args.edicion
    _ESTADO["sin_cache"] = args.sin_cache
    _ESTADO["permitir_publicar"] = args.permitir_publicar
    _ESTADO["editor"] = args.editor

    if not os.path.isfile(UI_HTML):
        print(f"falta {UI_HTML}", file=sys.stderr)
        return 1

    ind = indice_actual()
    fr = idx.frescura(ind)
    print(f"{len(ind['sesiones'])} sesiones · edición {ind['meta']['edicion']} · "
          f"{len(ind['meta']['avisos'])} avisos · "
          f"{fr['viejos']}/{fr['total']} renders desactualizados")
    lib = fr["libro"]
    if lib["estado"] in ("viejo", "falta"):
        print(f"  ⚠ el PDF del libro está {lib['estado']} "
              f"(más nuevo: {lib['archivo']}) — el botón del panel lo regenera")
    if not idx.hook_activo():
        print("  ⚠ core.hooksPath no está configurado: "
              "git config core.hooksPath .githooks")
    return _servir(args.puerto, not args.no_abrir)


if __name__ == "__main__":
    sys.exit(main())
