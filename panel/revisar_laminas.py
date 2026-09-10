#!/usr/bin/env python3
"""
revisar_laminas.py — ¿cabe cada lámina en su marco?

(Gemelo de SyS/panel/revisar_laminas.py, portado el 2026-09-10; solo cambian
el glob de los decks y la invocación de quarto.)

Abre cada deck reveal.js renderizado en Chrome sin ventana, fuerza todos
los fragmentos a visibles, recorre las láminas una por una y mide, en
coordenadas del marco (1050×700 de Quarto, independiente de la pantalla):

  ✗ desborde   — algún elemento se sale del marco por abajo o por la derecha
                 (texto cortado, fórmula que no cabe, tabla + cierre demasiado largos)
  ✗ colapso    — una imagen cargada con altura 0 (el auto-stretch de Quarto
                 sin {.nostretch}: la lámina sale en blanco sin error alguno)

Esto es lo que antes había que hacer "abriendo la lámina": ahora lo hace
la máquina y el profesor se queda en el contenido.

Uso:
  python3 panel/revisar_laminas.py material/curso/sesion-05/slides_s05.qmd [...]
  python3 panel/revisar_laminas.py --todas            # todos los slides_sNN.qmd
  python3 panel/revisar_laminas.py --sin-render ...   # no renderizar aunque el HTML esté viejo
  python3 panel/revisar_laminas.py --tolerancia 8 ... # px de gracia (por defecto 4)

Si el HTML renderizado no existe o es más viejo que el .qmd, se renderiza
primero (quarto vía conda, como el resto de AM: ~20–40 s por deck). Sale con código 1
si alguna lámina falla. Lo llaman el pre-commit (para los decks que se
están commiteando) y verificar_consistencia.py en modo completo.
"""
import argparse
import base64
import json
import pathlib
import re
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
MATERIAL = RAIZ / "material"
SITE = MATERIAL / "_render" / "site"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# Convención de AM: quarto se invoca a través de conda (ver CLAUDE.md).
QUARTO = ["conda", "run", "-n", "base", "quarto"]

# Se inyecta en una copia temporal del HTML (misma carpeta, para que los
# recursos relativos sigan resolviendo). Recorre las láminas con
# Reveal.slide() y deja el resultado en <title>, que --dump-dom devuelve.
SONDA = r"""
<style>
.reveal .fragment { opacity: 1 !important; visibility: visible !important; }
</style>
<script>
(function () {
  const TOL = __TOL__;
  function medir() {
    const frame = document.querySelector('.reveal .slides').getBoundingClientRect();
    const escala = (window.Reveal && Reveal.getScale) ? Reveal.getScale() : 1;
    const res = [];
    const secciones = Array.from(document.querySelectorAll('.reveal .slides section'))
      .filter(s => !s.querySelector(':scope > section'));   // hojas (sin pilas verticales)
    secciones.forEach((sec, i) => {
      const idx = Reveal.getIndices(sec);
      Reveal.slide(idx.h, idx.v);
      const h2 = sec.querySelector('h1, h2, h3');
      let titulo = '(sin título)';
      if (h2) {   // sin el MathML de accesibilidad de KaTeX (duplica la fórmula)
        const c = h2.cloneNode(true);
        c.querySelectorAll('.katex-mathml').forEach(x => x.remove());
        titulo = c.textContent.trim().replace(/\s+/g, ' ');
      }
      let abajo = 0, derecha = 0, culpaAbajo = '', culpaDerecha = '';
      const colapsadas = [];
      const desc = el => (el.tagName.toLowerCase()
        + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '')
        + ' «' + (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 40) + '»');
      sec.querySelectorAll('*').forEach(el => {
        if (el.closest('aside.notes, .notes, script, style')) return;
        // KaTeX: el <math> de accesibilidad va oculto (clip 1px) pero conserva
        // su ancho natural; no es visible y no cuenta como desborde.
        if (el.closest('.katex-mathml')) return;
        // Dentro de un <svg> (KaTeX dibuja \underbrace y similares con paths de
        // viewBox enorme recortado por su caja) solo cuenta la caja del svg.
        if (el instanceof SVGElement && el.tagName.toLowerCase() !== 'svg') return;
        const cs = getComputedStyle(el);
        if (cs.display === 'none' || cs.visibility === 'hidden') return;
        const r = el.getBoundingClientRect();
        if (r.width === 0 && r.height === 0) return;
        if (el.tagName === 'IMG' && el.complete && el.naturalHeight > 0 && r.height < 2) {
          colapsadas.push(el.getAttribute('src') || '(sin src)');
        }
        const dAbajo = (r.bottom - frame.bottom) / escala;
        const dDerecha = (r.right - frame.right) / escala;
        if (dAbajo > abajo) { abajo = dAbajo; culpaAbajo = desc(el); }
        if (dDerecha > derecha) { derecha = dDerecha; culpaDerecha = desc(el); }
      });
      res.push({
        n: i + 1, titulo,
        abajo: Math.round(abajo), derecha: Math.round(derecha),
        culpaAbajo, culpaDerecha, colapsadas,
        falla: abajo > TOL || derecha > TOL || colapsadas.length > 0,
      });
    });
    const json = JSON.stringify({ total: secciones.length, laminas: res });
    document.title = 'LAMINAS:' + btoa(unescape(encodeURIComponent(json)));
  }
  let intentos = 0;
  const t = setInterval(() => {
    intentos++;
    const listo = window.Reveal && Reveal.isReady && Reveal.isReady()
      && document.querySelector('.reveal.ready');
    if (listo || intentos > 100) {
      clearInterval(t);
      // medir con las fuentes ya cargadas: con la de reemplazo el texto es más ancho
      const listoFuentes = (document.fonts && document.fonts.ready) ? document.fonts.ready : Promise.resolve();
      listoFuentes.then(() => {
        try { medir(); } catch (e) { document.title = 'LAMINAS:ERROR:' + e; }
      });
    }
  }, 100);
})();
</script>
"""


def decks_todos():
    return sorted(MATERIAL.glob("curso/sesion-*/slides_s*.qmd"))


def html_de(qmd: pathlib.Path) -> pathlib.Path:
    rel = qmd.resolve().relative_to(MATERIAL.resolve())
    return SITE / rel.with_suffix(".html")


def renderizar(qmd: pathlib.Path) -> None:
    rel = qmd.resolve().relative_to(MATERIAL.resolve())
    r = subprocess.run([*QUARTO, "render", str(rel)],
                       cwd=MATERIAL, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"quarto render falló para {rel}:\n{r.stderr[-2000:]}")


def sondear(html: pathlib.Path, tol: int) -> dict:
    if not pathlib.Path(CHROME).exists():
        raise SystemExit(f"No encuentro Chrome en {CHROME}")
    texto = html.read_text(encoding="utf-8")
    sonda = SONDA.replace("__TOL__", str(tol))
    # antes de </body>: Reveal ya está definido (sus scripts van en el body)
    if "</body>" in texto:
        texto = texto.replace("</body>", sonda + "</body>", 1)
    else:
        texto += sonda
    tmp = html.with_name(f"_sonda-{html.stem}.html")
    tmp.write_text(texto, encoding="utf-8")
    try:
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                            "--window-size=1050,700", "--virtual-time-budget=20000",
                            "--dump-dom", tmp.as_uri()],
                           capture_output=True, text=True, timeout=180)
    finally:
        tmp.unlink(missing_ok=True)
    m = re.search(r"<title>LAMINAS:([^<]*)</title>", r.stdout)
    if not m:
        raise SystemExit(f"{html.name}: la sonda no devolvió resultado "
                         "(¿reveal.js no inicializó? probar abriendo el HTML a mano)")
    carga = m.group(1)
    if carga.startswith("ERROR:"):
        raise SystemExit(f"{html.name}: la sonda falló: {carga[6:]}")
    return json.loads(base64.b64decode(carga).decode("utf-8"))


def revisar(qmd: pathlib.Path, tol: int, sin_render: bool) -> list[str]:
    """Devuelve la lista de fallas (vacía si todo cabe)."""
    html = html_de(qmd)
    viejo = (not html.exists()) or html.stat().st_mtime < qmd.stat().st_mtime
    if viejo:
        if sin_render:
            return [f"{qmd.name}: render {'ausente' if not html.exists() else 'más viejo que el .qmd'}"
                    " (correr sin --sin-render para renderizarlo)"]
        renderizar(qmd)
    datos = sondear(html, tol)
    fallas = []
    for lam in datos["laminas"]:
        if not lam["falla"]:
            continue
        partes = []
        if lam["abajo"] > tol:
            partes.append(f"se sale {lam['abajo']} px por abajo ({lam['culpaAbajo']})")
        if lam["derecha"] > tol:
            partes.append(f"se sale {lam['derecha']} px por la derecha ({lam['culpaDerecha']})")
        for src in lam["colapsadas"]:
            partes.append(f"imagen colapsada a altura 0: {src}")
        fallas.append(f"{qmd.name} lámina {lam['n']}/{datos['total']} "
                      f"«{lam['titulo']}»: " + "; ".join(partes))
    return fallas


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("decks", nargs="*", help="rutas a slides_sNN.qmd")
    ap.add_argument("--todas", action="store_true", help="todos los decks de material/curso")
    ap.add_argument("--sin-render", action="store_true",
                    help="no renderizar; falla si el HTML está viejo o falta")
    ap.add_argument("--tolerancia", type=int, default=4, help="px de gracia (marco 1050×700)")
    args = ap.parse_args()

    decks = decks_todos() if args.todas else [pathlib.Path(d) for d in args.decks]
    decks = [d if d.is_absolute() else (RAIZ / d) for d in decks]
    if not decks:
        ap.error("indica decks o --todas")
    total_fallas = []
    for qmd in decks:
        if not qmd.exists():
            print(f"  ✗ {qmd}: no existe")
            total_fallas.append(f"{qmd}: no existe")
            continue
        fallas = revisar(qmd, args.tolerancia, args.sin_render)
        if fallas:
            for f in fallas:
                print(f"  ✗ {f}")
            total_fallas += fallas
        else:
            print(f"  ✓ {qmd.name}: todas las láminas caben")
    return 1 if total_fallas else 0


if __name__ == "__main__":
    sys.exit(main())
