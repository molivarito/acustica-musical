"""Figuras de la sesión 04 — La receta del timbre.

Genera:
  s04_punto_pulsacion.svg : la misma cuerda pulsada en L/2 y en L/10;
      la receta de amplitudes  A_n ~ |sin(n*pi*x0/L)| / n^2.
  s04_sintesis_aditiva.svg : construcción de una onda sumando armónicos
      impares (1, 1+3, 1+3+5): síntesis aditiva.
  s04_envolvente.svg : la envolvente de una nota pulsada y la MISMA nota
      al revés (mismo espectro, otra película -> otro instrumento).

Ejecutar desde figuras/:  python3 gen_s04.py
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()


def receta(x0_rel, nmax=12):
    """Amplitud del modo n para una cuerda ideal pulsada en x0 = x0_rel * L."""
    n = np.arange(1, nmax + 1)
    A = np.abs(np.sin(n * np.pi * x0_rel)) / n ** 2
    return n, A / A.max()


def fig_punto_pulsacion():
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(7.0, 4.4), sharex=True)

    n, A = receta(0.5)               # pulsada en L/2
    ax0.stem(n, A, basefmt=' ', linefmt=COLORES['acento'], markerfmt='o')
    ax0.set_title(r'Pulsada en $L/2$: los parciales pares nacen mudos (sonido hueco)')
    ax0.set_ylabel('amplitud (rel.)')
    ax0.set_ylim(0, 1.08)

    n, A = receta(0.1)               # pulsada en L/10
    ax1.stem(n, A, basefmt=' ', linefmt=COLORES['azul'], markerfmt='o')
    ax1.set_title(r'Pulsada en $L/10$ (cerca del puente): de todo, rica en agudos (brillante)')
    ax1.set_ylabel('amplitud (rel.)')
    ax1.set_xlabel(r'número de parcial $n$   (frecuencia $= n f_1$)')
    ax1.set_xticks(range(1, 13))
    ax1.set_ylim(0, 1.08)

    fig.tight_layout()
    guardar(fig, 's04_punto_pulsacion', ancho=7.0, alto=4.4)


def fig_sintesis_aditiva():
    t = np.linspace(0, 2, 1000)      # dos períodos (t en unidades de período)
    fig, axes = plt.subplots(3, 1, figsize=(6.8, 4.4), sharex=True)

    combos = [
        ([1], 'parcial 1 (seno puro)'),
        ([1, 3], '1 + 3'),
        ([1, 3, 5, 7], '1 + 3 + 5 + 7  →  se acerca a una onda "hueca"'),
    ]
    for ax, (armonicos, lab) in zip(axes, combos):
        y = np.zeros_like(t)
        for k in armonicos:
            y += (1.0 / k) * np.sin(2 * np.pi * k * t)
        ax.plot(t, y, color=COLORES['acento'])
        ax.axhline(0, color=COLORES['gris'], lw=0.7)
        ax.set_ylim(-1.25, 1.25)
        ax.set_yticks([])
        ax.text(0.012, 0.88, lab, transform=ax.transAxes, va='top',
                fontsize=9.5, style='italic')
    axes[0].set_title('Síntesis aditiva: sumar armónicos no agrega notas, tiñe una sola')
    axes[1].set_ylabel('amplitud (u.a.)')
    axes[-1].set_xlabel('tiempo (en períodos de $f_1$)')
    fig.tight_layout()
    guardar(fig, 's04_sintesis_aditiva', ancho=6.8, alto=4.4)


def fig_envolvente():
    t = np.linspace(0, 1.0, 1000)
    # envolvente de pulsación: ataque abrupto + decaimiento
    ataque = np.clip(t / 0.02, 0, 1)
    env = ataque * np.exp(-t / 0.28)
    env = env / env.max()
    env_rev = env[::-1]              # la misma nota al revés

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(7.4, 3.0), sharey=True)
    ax0.plot(t, env, color=COLORES['acento'])
    ax0.fill_between(t, env, color=COLORES['acento'], alpha=0.10)
    ax0.set_title('Nota pulsada: ataque y decaimiento', fontsize=9.5)
    ax0.set_xlabel('tiempo (s)')
    ax0.set_ylabel('amplitud (rel.)')

    ax1.plot(t, env_rev, color=COLORES['azul'])
    ax1.fill_between(t, env_rev, color=COLORES['azul'], alpha=0.10)
    ax1.set_title('La MISMA nota, al revés', fontsize=9.5)
    ax1.set_xlabel('tiempo (s)')

    fig.suptitle('Mismo espectro, distinta envolvente → el oído oye otro instrumento',
                 fontsize=10.5, y=1.02)
    fig.tight_layout()
    guardar(fig, 's04_envolvente', ancho=7.4, alto=3.0)


if __name__ == '__main__':
    fig_punto_pulsacion()
    fig_sintesis_aditiva()
    fig_envolvente()
