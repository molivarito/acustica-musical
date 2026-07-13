# -*- coding: utf-8 -*-
"""Figuras de la sesión 08 — Banda crítica y consonancia.

Genera:
  s08_recorrido_deltaf.svg   — batido→rugosidad→dos notas ásperas→dos lisas
                               al crecer Δf, con zonas sombreadas
  s08_coincidencia_parciales.svg — peines de parciales: 5ª justa (alineados)
                               vs. tritono (desalineados, rozan)

Ejecutar desde figuras/:  python3 gen_s08.py

Notas: el eje Δf y las fronteras son ESQUEMÁTICOS (las fronteras reales
son personales; el orden es universal — Roederer 1997 sec. 2.4). La banda
crítica en el rango medio es del orden de un tercio de octava (~100 Hz
cerca de 440 Hz).
"""
import numpy as np
import matplotlib.pyplot as plt

from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()


# ----------------------------------------------------------------------
# Figura 1: el recorrido perceptual al crecer Δf
# ----------------------------------------------------------------------
def recorrido_deltaf():
    fig, ax = plt.subplots()

    # Fronteras esquemáticas (Hz), en torno a f ~ 440 Hz
    F0, F1, F2, F3, Fmax = 0, 12, 40, 100, 160

    zonas = [
        (F0, F1, 'Batido\ncontable', COLORES['panel'], 0.9),
        (F1, F2, 'Aspereza\nfusionada\n(una nota)', COLORES['acento'], 0.16),
        (F2, F3, 'Dos notas,\ntodavía ásperas', COLORES['acento'], 0.30),
        (F3, Fmax, 'Dos notas\nlisas', COLORES['papel'], 1.0),
    ]
    for x0, x1, etiqueta, color, alpha in zonas:
        ax.axvspan(x0, x1, color=color, alpha=alpha, zorder=0)
        ax.text((x0 + x1) / 2, 0.72, etiqueta, ha='center', va='center',
                fontsize=9.5, color=COLORES['tinta'])

    # Rótulos de las fronteras
    for x, nombre in [(F1, '≈ límite\nde conteo'),
                      (F2, 'F2\n(emergen 2)'),
                      (F3, 'F3 ≈ banda\ncrítica')]:
        ax.axvline(x, color=COLORES['tinta'], lw=0.9, ls='--')
        ax.text(x, 0.30, nombre, ha='center', va='center', fontsize=8.5,
                color=COLORES['tinta'],
                bbox=dict(boxstyle='round,pad=0.2', fc=COLORES['papel'],
                          ec='none'))

    # Nota sobre el ancho de la banda crítica
    ax.annotate('banda crítica ≈ 1/3 de octava\n(~100 Hz cerca de 440 Hz)',
                xy=(F3, 0.12), xytext=(F3 + 5, 0.05), fontsize=8.5,
                color=COLORES['azul'], ha='left', va='center')

    ax.set_xlim(0, Fmax)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.set_xlabel(r'separación entre los dos tonos  $\Delta f$ (Hz, esquemático)')
    ax.set_title('Al separar dos tonos desde el unísono (fronteras personales)')
    guardar(fig, 's08_recorrido_deltaf', ancho=7.2, alto=3.2)


# ----------------------------------------------------------------------
# Figura 2: coincidencia de parciales — 5ª justa vs. tritono
# ----------------------------------------------------------------------
def coincidencia_parciales():
    f0 = 220.0                               # fundamental de la nota grave
    n_parciales = 6
    bc = 100.0                               # ancho de banda crítica (~Hz)

    def peine(ax, r_num, r_den, titulo, roza_esperado):
        """Dibuja los parciales de la nota grave (f0) y la aguda (f0·r)."""
        fa = f0 * r_num / r_den              # fundamental de la aguda
        graves = f0 * np.arange(1, n_parciales + 1)
        agudos = fa * np.arange(1, n_parciales + 1)

        for g in graves:
            ax.plot([g, g], [0, 1], color=COLORES['azul'], lw=1.8)
        for a in agudos:
            ax.plot([a, a], [0, -1], color=COLORES['acento'], lw=1.8)

        # Marcar pares que ROZAN (0 < |g-a| < banda crítica)
        for g in graves:
            for a in agudos:
                d = abs(g - a)
                if 0 < d < bc * 0.6:         # dentro de banda crítica → roza
                    x = (g + a) / 2
                    ax.plot(x, 0, marker='x', ms=9, mew=2.0,
                            color=COLORES['tinta'], zorder=5)
                elif d < 1.0:                # coincidencia (no roza)
                    ax.plot(g, 0, marker='o', ms=6,
                            mfc=COLORES['papel'], mec=COLORES['tinta'],
                            mew=1.3, zorder=5)

        ax.set_title(titulo, fontsize=10)
        ax.set_xlim(150, 1500)
        ax.set_ylim(-1.4, 1.4)
        ax.set_yticks([0.5, -0.5])
        ax.set_yticklabels(['grave', 'aguda'], fontsize=9)
        ax.axhline(0, color=COLORES['gris'], lw=0.6)
        for lado in ('left',):
            ax.spines[lado].set_visible(False)

    fig, ejes = plt.subplots(2, 1, sharex=True)
    peine(ejes[0], 3, 2, 'Quinta justa 3:2 — parciales coinciden (○)', False)
    peine(ejes[1], 45, 32, 'Tritono ~45:32 — parciales rozan (×)', True)

    ejes[1].set_xlabel('frecuencia (Hz)')

    # Leyenda de símbolos
    ejes[0].plot([], [], 'o', mfc=COLORES['papel'], mec=COLORES['tinta'],
                 mew=1.3, label='coinciden (sin aspereza)')
    ejes[0].plot([], [], 'x', color=COLORES['tinta'], mew=2.0,
                 label='dentro de banda crítica (rozan)')
    ejes[0].legend(loc='upper right', fontsize=8.5)

    fig.suptitle('La consonancia como coincidencia de parciales',
                 fontsize=11.5, fontweight='bold')
    guardar(fig, 's08_coincidencia_parciales', ancho=7.0, alto=4.4)


if __name__ == '__main__':
    recorrido_deltaf()
    coincidencia_parciales()
