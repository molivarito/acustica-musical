"""Estilo compartido para las figuras del curso Acústica Musical UC.

Uso, al inicio de cada script generador (figuras/gen_sNN.py):

    from estilo_figuras import aplicar_estilo, COLORES, guardar
    aplicar_estilo()

Convenciones (coherentes con las demos y los documentos del curso):
- Paleta contenida: tinta, acento (rojo ladrillo), azul; grises de apoyo.
- Ejes siempre rotulados con magnitud y unidad SI (notación de diseno/03).
- Fondo claro, sin decoración gratuita, serif para texto.
- Guardar SIEMPRE con guardar(fig, 'nombre') → figuras/nombre.svg
  (SVG: nítido en HTML y convertible al PDF del libro vía rsvg-convert).
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

AQUI = Path(__file__).resolve().parent

COLORES = {
    'tinta':  '#1a1a1a',
    'acento': '#7a2e2e',   # rojo ladrillo (curvas principales, énfasis)
    'azul':   '#2e4a7a',   # segunda serie / referencia
    'panel':  '#f0ece4',   # relleno suave de zonas
    'gris':   '#8a8a8a',   # guías, curvas secundarias
    'papel':  '#ffffff',   # fondo de la figura (blanco: se imprime bien)
}

# Ciclo de colores por defecto para series múltiples
CICLO = [COLORES['acento'], COLORES['azul'], COLORES['gris'], '#b08b3e']


def aplicar_estilo():
    """Aplica los rcParams del curso (llamar una vez por script)."""
    mpl.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['DejaVu Serif'],
        'font.size': 11,
        'axes.labelsize': 11,
        'axes.titlesize': 11.5,
        'axes.titleweight': 'bold',
        'axes.edgecolor': COLORES['tinta'],
        'axes.labelcolor': COLORES['tinta'],
        'axes.linewidth': 0.9,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.prop_cycle': mpl.cycler(color=CICLO),
        'xtick.color': COLORES['tinta'],
        'ytick.color': COLORES['tinta'],
        'xtick.labelsize': 9.5,
        'ytick.labelsize': 9.5,
        'legend.fontsize': 9.5,
        'legend.frameon': False,
        'lines.linewidth': 1.8,
        'figure.facecolor': COLORES['papel'],
        'axes.facecolor': COLORES['papel'],
        'savefig.facecolor': COLORES['papel'],
        'svg.fonttype': 'none',   # texto real en el SVG (nítido y liviano)
        'figure.dpi': 110,
    })


def guardar(fig, nombre, ancho=7.0, alto=None):
    """Guarda la figura como figuras/<nombre>.svg con tamaño estándar.

    ancho/alto en pulgadas; alto por defecto = 0.55 * ancho.
    """
    if alto is None:
        alto = 0.55 * ancho
    fig.set_size_inches(ancho, alto)
    destino = AQUI / f'{nombre}.svg'
    fig.savefig(destino, bbox_inches='tight', pad_inches=0.06)
    plt.close(fig)
    print(f'  ✓ {destino.relative_to(AQUI.parent)}')
