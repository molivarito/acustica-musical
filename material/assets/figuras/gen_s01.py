"""Figuras de la sesión 01 — Del golpe al tono.

Genera:
  s01_pulsos_ritmo_tono.svg : un mismo pulso repetido a tres tasas
      (ritmo -> zona de transición -> tono), sobre un eje de tiempo común.
  s01_frecuencia_periodo.svg : una oscilación periódica con el período T
      marcado y la relación T = 1/f.

Ejecutar desde figuras/:  python3 gen_s01.py
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()


def pulso(t, t0, ancho=0.004):
    """Un click idéntico centrado en t0: breve seno amortiguado (forma fija)."""
    env = np.exp(-((t - t0) ** 2) / (2 * ancho ** 2))
    osc = np.sin(2 * np.pi * 600 * (t - t0))
    return env * osc


def tren(t, tasa):
    """Tren de pulsos idénticos a 'tasa' pulsos por segundo sobre el eje t."""
    y = np.zeros_like(t)
    dt = 1.0 / tasa
    for k in range(int(t[-1] / dt) + 2):
        y += pulso(t, k * dt)
    return y


def fig_pulsos():
    dur = 0.35                       # ventana temporal común, en segundos
    t = np.linspace(0, dur, 8000)
    tasas = [10, 28, 120]            # pulsos/s: ritmo, zona gris, tono
    rotulos = [
        '10 pulsos/s — se oyen golpes separados (ritmo)',
        '≈ 28 pulsos/s — zona de transición (ni ritmo ni tono claro)',
        '120 pulsos/s — el oído funde los golpes en un tono',
    ]
    fig, axes = plt.subplots(3, 1, sharex=True)
    for ax, tasa, rot in zip(axes, tasas, rotulos):
        ax.plot(t * 1000, tren(t, tasa), color=COLORES['acento'], lw=1.0)
        ax.set_ylim(-1.25, 1.25)
        ax.set_yticks([])
        ax.text(0.012, 0.90, rot, transform=ax.transAxes, va='top',
                fontsize=9.5, style='italic', color=COLORES['tinta'])
    axes[1].set_ylabel('presión (u.a.)')
    axes[-1].set_xlabel('tiempo (ms)')
    axes[-1].set_xlim(0, dur * 1000)
    guardar(fig, 's01_pulsos_ritmo_tono', ancho=7.0, alto=4.4)


def fig_frecuencia_periodo():
    f = 200.0                        # Hz (elegido para que se lean ~3 ciclos)
    T = 1.0 / f                       # período en segundos
    t = np.linspace(0, 3.2 * T, 2000)
    y = np.sin(2 * np.pi * f * t)

    fig, ax = plt.subplots()
    ax.plot(t * 1000, y, color=COLORES['acento'])
    ax.axhline(0, color=COLORES['gris'], lw=0.8)

    # Marcar un período entre dos crestas sucesivas (en t = T/4 y t = T/4 + T)
    x0 = 0.25 * T
    x1 = x0 + T
    ax.annotate('', xy=(x1 * 1000, 1.18), xytext=(x0 * 1000, 1.18),
                arrowprops=dict(arrowstyle='<->', color=COLORES['tinta'], lw=1.2))
    ax.text((x0 + T / 2) * 1000, 1.30, 'período $T$', ha='center',
            va='bottom', color=COLORES['tinta'])
    for xx in (x0, x1):
        ax.plot([xx * 1000, xx * 1000], [np.sin(2 * np.pi * f * xx), 1.18],
                color=COLORES['tinta'], lw=0.7, ls=':')

    ax.text(0.98, 0.04,
            r'$T = \dfrac{1}{f}$   ·   aquí $f = 200$ Hz $\Rightarrow$ $T = 5$ ms',
            transform=ax.transAxes, ha='right', va='bottom', fontsize=10.5)
    ax.set_xlabel('tiempo (ms)')
    ax.set_ylabel('presión (u.a.)')
    ax.set_ylim(-1.35, 1.6)
    ax.set_yticks([-1, 0, 1])
    guardar(fig, 's01_frecuencia_periodo', ancho=7.0, alto=3.6)


if __name__ == '__main__':
    fig_pulsos()
    fig_frecuencia_periodo()
