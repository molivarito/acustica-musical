"""Figuras de la sesión 05 — La altura percibida.

Genera:
  s05_fundamental_ausente.svg : el tono completo y el mismo tono SIN su
      fundamental; ambas formas de onda tienen el mismo período (misma
      altura) aunque el espectro pierda f1.
  s05_oido_esquema.svg : esquema de bloques del oído (externo/medio/interno)
      y mapa tonotópico de la membrana basilar (agudos a la entrada,
      graves al fondo).
  s05_octava_log.svg : la altura se organiza por razones: octavas
      equiespaciadas sobre un eje de frecuencia logarítmico (duplicar = subir
      una octava, aunque el salto en Hz crezca).

Ejecutar desde figuras/:  python3 gen_s05.py
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()

F1 = 200.0                       # Hz


def fig_fundamental_ausente():
    t = np.linspace(0, 2 / F1, 1200)     # dos períodos de f1
    T_ms = 1000.0 / F1

    def onda(parciales):
        y = np.zeros_like(t)
        for n in parciales:
            y += (1.0 / n) * np.cos(2 * np.pi * n * F1 * t)
        return y

    completa = [1, 2, 3, 4, 5, 6]
    sin_f1 = [2, 3, 4, 5, 6]

    fig, axes = plt.subplots(2, 2, figsize=(8.6, 4.4),
                             gridspec_kw={'width_ratios': [1.3, 1]})

    for fila, (parc, titulo, col) in enumerate([
            (completa, 'Tono completo', COLORES['acento']),
            (sin_f1, 'Sin la fundamental ($f_1$ apagada)', COLORES['azul'])]):
        # forma de onda (izquierda)
        axw = axes[fila, 0]
        y = onda(parc)
        axw.plot(t * 1000, y, color=col)
        axw.axhline(0, color=COLORES['gris'], lw=0.7)
        axw.set_ylabel('presión (u.a.)')
        axw.set_yticks([])
        # marcar el período común T
        axw.annotate('', xy=(T_ms, y.max() * 1.15), xytext=(0, y.max() * 1.15),
                     arrowprops=dict(arrowstyle='<->', color=COLORES['tinta'],
                                     lw=1.0))
        axw.text(T_ms / 2, y.max() * 1.22, r'$T = 1/f_1$', ha='center',
                 fontsize=9, va='bottom')
        axw.set_ylim(y.min() * 1.15, y.max() * 1.45)
        axw.set_title(titulo, fontsize=10.5)

        # espectro (derecha)
        axs = axes[fila, 1]
        frecs = np.array(parc) * F1
        amps = 1.0 / np.array(parc)
        axs.stem(frecs, amps, basefmt=' ', linefmt=col, markerfmt='o')
        axs.set_xlim(0, 7 * F1)
        axs.set_ylim(0, 1.1)
        axs.set_yticks([])
        axs.set_ylabel('nivel')
        if fila == 1:
            axs.annotate('falta $f_1$', xy=(F1, 0.05), xytext=(F1, 0.6),
                         ha='center', fontsize=9, color=COLORES['acento'],
                         arrowprops=dict(arrowstyle='->', color=COLORES['acento']))

    axes[1, 0].set_xlabel('tiempo (ms)')
    axes[1, 1].set_xlabel('frecuencia (Hz)')
    fig.suptitle('Mismo período → misma altura, aunque el espectro pierda la fundamental',
                 fontsize=11, y=1.01)
    fig.tight_layout()
    guardar(fig, 's05_fundamental_ausente', ancho=8.6, alto=4.4)


def fig_oido_esquema():
    fig, ax = plt.subplots(figsize=(8.4, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis('off')

    bloques = [
        (0.3, 'Oído externo', 'pabellón y canal\n(capta y colorea)', COLORES['panel']),
        (3.5, 'Oído medio', 'tímpano + 3 huesecillos\n(adapta aire→líquido)', COLORES['panel']),
        (6.7, 'Oído interno', 'cóclea:\nmembrana basilar', COLORES['panel']),
    ]
    ancho = 2.6
    for x0, titulo, detalle, color in bloques:
        caja = FancyBboxPatch((x0, 2.0), ancho, 1.5,
                              boxstyle='round,pad=0.02,rounding_size=0.12',
                              linewidth=1.1, edgecolor=COLORES['tinta'],
                              facecolor=color)
        ax.add_patch(caja)
        ax.text(x0 + ancho / 2, 3.15, titulo, ha='center', va='center',
                fontsize=10.5, fontweight='bold', color=COLORES['tinta'])
        ax.text(x0 + ancho / 2, 2.55, detalle, ha='center', va='center',
                fontsize=8.5, color=COLORES['tinta'])
    # flechas entre bloques
    for x0 in (2.9 + 0.0, 6.1 + 0.0):
        ax.add_patch(FancyArrowPatch((x0, 2.75), (x0 + 0.6, 2.75),
                     arrowstyle='-|>', mutation_scale=14,
                     color=COLORES['tinta'], lw=1.2))
    ax.text(0.0, 2.75, 'sonido', fontsize=9, style='italic', va='center')

    # Mapa tonotópico: membrana basilar "desenrollada"
    xg = np.linspace(0.3, 9.3, 300)
    grad = xg.reshape(1, -1)
    ax.imshow(grad, extent=[0.3, 9.3, 0.5, 1.2], aspect='auto',
              cmap='cividis', alpha=0.85)
    ax.add_patch(plt.Rectangle((0.3, 0.5), 9.0, 0.7, fill=False,
                 edgecolor=COLORES['tinta'], lw=1.0))
    ax.text(0.4, 1.45, 'Membrana basilar (analizador por lugar):',
            fontsize=9.5, style='italic', color=COLORES['tinta'])
    ax.text(0.5, 0.28, 'entrada — agudos (rígida, estrecha)', fontsize=8.5,
            ha='left', color=COLORES['tinta'])
    ax.text(9.1, 0.28, 'fondo — graves (blanda, ancha)', fontsize=8.5,
            ha='right', color=COLORES['tinta'])
    guardar(fig, 's05_oido_esquema', ancho=8.4, alto=3.4)


def fig_octava_log():
    # La en varias octavas: 110, 220, 440, 880, 1760 Hz
    las = np.array([110, 220, 440, 880, 1760])
    octavas = np.arange(len(las))          # 0,1,2,3,4 -> altura en octavas

    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    ax.plot(las, octavas, 'o-', color=COLORES['acento'], ms=7)
    ax.set_xscale('log', base=2)
    ax.set_xticks(las)
    ax.set_xticklabels([f'{v}' for v in las])
    ax.set_xlabel('frecuencia (Hz, escala logarítmica)')
    ax.set_ylabel('altura (octavas)')
    ax.set_yticks(octavas)
    ax.set_yticklabels(['La2', 'La3', 'La4', 'La5', 'La6'])
    ax.grid(True, which='major', axis='both', color=COLORES['gris'],
            lw=0.5, alpha=0.4)
    ax.set_title('La altura se organiza por razones: cada octava = duplicar $f$')

    # anotar dos saltos de una octava con distinto Δf (bajo la recta, con caja)
    caja = dict(boxstyle='round,pad=0.15', fc=COLORES['papel'], ec='none', alpha=0.9)
    ax.annotate(r'$220\to440$: $+220$ Hz', xy=(311, 1.28), fontsize=8.5,
                ha='center', color=COLORES['azul'], bbox=caja)
    ax.annotate(r'$440\to880$: $+440$ Hz', xy=(622, 2.28), fontsize=8.5,
                ha='center', color=COLORES['azul'], bbox=caja)
    ax.text(0.98, 0.06, 'igual paso perceptual, distinto salto en Hz',
            transform=ax.transAxes, ha='right', va='bottom', fontsize=9,
            style='italic')
    fig.tight_layout()
    guardar(fig, 's05_octava_log', ancho=7.4, alto=3.4)


if __name__ == '__main__':
    fig_fundamental_ausente()
    fig_oido_esquema()
    fig_octava_log()
