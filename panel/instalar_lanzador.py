#!/usr/bin/env python3
"""Crea una app de macOS para abrir el panel sin pasar por el terminal.

Genera un bundle en ~/Applications que se puede arrastrar al Dock. Al hacer
clic: si el panel ya está corriendo, solo abre la pestaña; si no, lo arranca
en segundo plano y espera a que responda.

Por qué una app de AppleScript y no un script suelto dentro de un .app:
un ejecutable pelado no tiene bucle de eventos de Cocoa. macOS lo registra
como aplicación en ejecución, y al volver a hacer clic en el Dock le manda el
evento `reopen`, que nadie contesta — el icono se queda rebotando y parece
colgado. Una app de AppleScript sí responde a `run` y a `reopen`, y además
termina enseguida (el servidor queda desacoplado), así que el icono nunca
queda ocupado.

Uso:
    python3 panel/instalar_lanzador.py            # crea/actualiza la app
    python3 panel/instalar_lanzador.py --quitar   # la borra
    python3 panel/instalar_lanzador.py --publicar # la app permitirá consultar Canvas
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile

PANEL_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(PANEL_DIR)
APPS = os.path.expanduser("~/Applications")
# Sin acentos ni espacios raros: `open -a` no resuelve por nombre una app
# con tilde, y el nombre debe ser simétrico con el del otro curso.
NOMBRE = "Panel MUC860"
PUERTO = 8767
# Ruta absoluta a propósito: una app lanzada desde el Finder no hereda el PATH
# del shell, así que `python3` a secas no encontraría el de miniforge.
PYTHON = "/Users/pdelac/miniforge3/bin/python3"

# El applet es deliberadamente mínimo: toda la lógica vive en
# panel/abrir-panel.sh, que se versiona con el repo y se puede probar desde el
# terminal. Solo `on run` — declarar `on reopen` convierte el applet en
# stay-open, el icono queda residente y el segundo clic pasa a depender de que
# el bucle de eventos conteste. Sin él, el applet termina apenas abre la
# pestaña y cada clic es un arranque limpio.
GUION = '''-- Generado por panel/instalar_lanzador.py — no editar a mano.
-- La lógica está en panel/abrir-panel.sh.
on run
	try
		do shell script {comando}
	on error elError number elNumero
		if elNumero is not -128 then
			display alert "{nombre}" message elError giving up after 12
		end if
	end try
end run
'''


# Icono: verde azulado y ondas irradiando desde una fuente sonora. Distinto en
# color Y en símbolo del panel de Señales y Sistemas (azul + sinusoide), para
# poder diferenciarlos de un vistazo en el Dock.
ICONO_FONDO = "#15544C"
ICONO_TRAZO = "#E8B33A"


def _svg():
    arcos = []
    for r in (170, 262, 354):
        x = 360 + r * 0.34
        arcos.append(
            f'<path d="M {x:.0f} {512 - r} A {r} {r} 0 0 1 {x:.0f} {512 + r}" '
            f'fill="none" stroke="{ICONO_TRAZO}" stroke-width="58" '
            'stroke-linecap="round"/>')
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" '
        'viewBox="0 0 1024 1024">'
        f'<rect x="48" y="48" width="928" height="928" rx="208" '
        f'fill="{ICONO_FONDO}"/>'
        f'<circle cx="330" cy="512" r="86" fill="{ICONO_TRAZO}"/>'
        + "".join(arcos) + '</svg>')


def poner_icono(app):
    """Genera el .icns con herramientas del sistema (rsvg-convert + iconutil).

    Nada de dependencias nuevas: el repo se mantiene en stdlib + PyYAML, y
    rsvg-convert ya se usa en el curso hermano para las figuras.
    """
    if not shutil.which("rsvg-convert") or not shutil.which("iconutil"):
        print("  (sin rsvg-convert/iconutil: la app queda con el icono genérico)")
        return
    with tempfile.TemporaryDirectory() as tmp:
        svg = os.path.join(tmp, "icono.svg")
        with open(svg, "w", encoding="utf-8") as fh:
            fh.write(_svg())
        iconset = os.path.join(tmp, "icono.iconset")
        os.makedirs(iconset)
        # Nombres exactos que exige iconutil.
        for px, nombre in [(16, "16x16"), (32, "16x16@2x"), (32, "32x32"),
                           (64, "32x32@2x"), (128, "128x128"),
                           (256, "128x128@2x"), (256, "256x256"),
                           (512, "256x256@2x"), (512, "512x512"),
                           (1024, "512x512@2x")]:
            subprocess.run(["rsvg-convert", "-w", str(px), "-h", str(px),
                            "-o", os.path.join(iconset, f"icon_{nombre}.png"),
                            svg], check=True, capture_output=True)
        icns = os.path.join(tmp, "icono.icns")
        subprocess.run(["iconutil", "-c", "icns", iconset, "-o", icns],
                       check=True, capture_output=True)
        # osacompile deja el icono del applet en Resources/applet.icns.
        shutil.copy(icns, os.path.join(app, "Contents", "Resources",
                                       "applet.icns"))
    # osacompile deja además un Assets.car con el icono genérico de applet, y
    # el catálogo de assets GANA sobre CFBundleIconFile: sin borrarlo, el icono
    # propio se copia pero no se ve.
    assets = os.path.join(app, "Contents", "Resources", "Assets.car")
    if os.path.isfile(assets):
        os.remove(assets)
    # Finder cachea iconos por fecha del bundle: hay que tocarlo.
    subprocess.run(["touch", app], check=False)
    lsreg = ("/System/Library/Frameworks/CoreServices.framework/Frameworks/"
             "LaunchServices.framework/Support/lsregister")
    if os.path.isfile(lsreg):
        subprocess.run([lsreg, "-f", app], check=False)
    print("  icono propio aplicado (si el Dock no lo refresca: killall Dock)")


def ruta_app():
    return os.path.join(APPS, f"{NOMBRE}.app")


def crear(permitir_publicar=False):
    if not os.path.isfile(os.path.join(PANEL_DIR, "panel.py")):
        print("no encuentro panel/panel.py", file=sys.stderr)
        return 1
    os.makedirs(APPS, exist_ok=True)
    app = ruta_app()

    lanzador = os.path.join(PANEL_DIR, "abrir-panel.sh")
    if not os.path.isfile(lanzador):
        print(f"falta {lanzador}", file=sys.stderr)
        return 1
    os.chmod(lanzador, os.stat(lanzador).st_mode | 0o111)

    # Literal AppleScript de la ruta, con las comillas dobles escapadas: la
    # ruta del curso trae espacios y una arroba (Google Drive).
    def literal(s):
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

    comando = f"quoted form of {literal(lanzador)}"
    if permitir_publicar:
        comando += ' & " --permitir-publicar"'

    guion = GUION.format(comando=comando, nombre=NOMBRE)

    with tempfile.TemporaryDirectory() as tmp:
        fuente = os.path.join(tmp, "lanzador.applescript")
        with open(fuente, "w", encoding="utf-8") as fh:
            fh.write(guion)
        if os.path.isdir(app):
            shutil.rmtree(app)
        r = subprocess.run(["/usr/bin/osacompile", "-o", app, fuente],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print("osacompile falló:\n" + (r.stderr or ""), file=sys.stderr)
            return 1

    poner_icono(app)

    print(f"App creada: {app}")
    print(f"  arrástrala al Dock, o ábrela con: open -a {NOMBRE!r}")
    if permitir_publicar:
        print("  OJO: arranca el panel CON publicar habilitado.")
    print(f"\nMarcador para el navegador: http://127.0.0.1:{PUERTO}/")
    print(f"Para detener el panel:      python3 panel/panel.py --detener")
    return 0


def quitar():
    app = ruta_app()
    if os.path.isdir(app):
        shutil.rmtree(app)
        print(f"Borrada: {app}")
    else:
        print(f"No existe: {app}")
    return 0


def main():
    p = argparse.ArgumentParser(description="Lanzador del panel para el Dock")
    p.add_argument("--quitar", action="store_true")
    p.add_argument("--publicar", action="store_true",
                   help="la app arrancará el panel con --permitir-publicar")
    args = p.parse_args()
    if sys.platform != "darwin":
        print("Solo para macOS.", file=sys.stderr)
        return 2
    return quitar() if args.quitar else crear(args.publicar)


if __name__ == "__main__":
    sys.exit(main())
