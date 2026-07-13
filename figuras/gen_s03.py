"""Figuras de la sesión 03 — Modos de vibración.

Genera:
  s03_modos_cuerda.svg : las cuatro primeras formas modales de una cuerda
      fija en ambos extremos (n = 1..4), con nodos marcados y f_n = n f1.
  s03_armonico_vs_inarmonico.svg : espectro armónico (cuerda, 1:2:3:...)
      frente a espectro inarmónico (membrana/placa, razones no enteras).
  s03_decaimiento_multimodo.svg : tres parciales que decaen a distinta tasa
      (el timbre del golpe es una película, no una foto).

Ejecutar desde figuras/:  python3 gen_s03.py
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()


def fig_modos_cuerda():
    L = 1.0
    x = np.linspace(0, L, 400)
    fig, axes = plt.subplots(4, 1, figsize=(6.6, 5.0), sharex=True)
    etiquetas = [r'$n=1$   ($f_1$)', r'$n=2$   ($2f_1$)',
                 r'$n=3$   ($3f_1$)', r'$n=4$   ($4f_1$)']
    for n, (ax, et) in enumerate(zip(axes, etiquetas), start=1):
        y = np.sin(n * np.pi * x / L)
        ax.plot(x, y, color=COLORES['acento'])
        ax.plot(x, -y, color=COLORES['acento'], lw=0.9, ls='--', alpha=0.6)
        ax.fill_between(x, y, -y, color=COLORES['acento'], alpha=0.08)
        ax.axhline(0, color=COLORES['gris'], lw=0.7)
        # nodos: puntos donde sin(n pi x/L) = 0
        nodos = np.arange(0, n + 1) * L / n
        ax.plot(nodos, np.zeros_like(nodos), 'o', color=COLORES['tinta'],
                ms=5, zorder=5)
        ax.set_ylim(-1.4, 1.4)
        ax.set_yticks([])
        ax.set_xlim(-0.02, L + 0.02)
        ax.text(1.015, 0.5, et, transform=ax.transAxes, va='center',
                fontsize=10)
    axes[0].set_title('Modos de una cuerda fija en ambos extremos (nodos ●)')
    axes[-1].set_xlabel('posición a lo largo de la cuerda  $x/L$')
    fig.subplots_adjust(right=0.80)
    guardar(fig, 's03_modos_cuerda', ancho=6.6, alto=5.0)


def fig_armonico_vs_inarmonico():
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8.4, 3.2), sharey=True)

    # Armónico: cuerda ideal, razones enteras 1:2:3:...
    n = np.arange(1, 7)
    amp = 1.0 / n            # amplitudes decrecientes cualitativas
    ax0.stem(n * 1.0, amp, basefmt=' ', linefmt=COLORES['acento'],
             markerfmt='o')
    ax0.set_title('Cuerda: parciales armónicos')
    ax0.set_xlabel(r'frecuencia (en unidades de $f_1$)')
    ax0.set_ylabel('amplitud (rel.)')
    ax0.set_xticks(range(1, 7))
    ax0.text(0.96, 0.92, r'razones $1:2:3:4:\dots$', transform=ax0.transAxes,
             ha='right', va='top', fontsize=9.5, style='italic')

    # Inarmónico: membrana circular ideal (ceros de Bessel), razones no enteras
    razones = [1.00, 1.59, 2.14, 2.30, 2.65, 2.92]
    amp2 = [1.0, 0.7, 0.55, 0.5, 0.4, 0.33]
    ax1.stem(razones, amp2, basefmt=' ', linefmt=COLORES['azul'],
             markerfmt='s')
    ax1.set_title('Membrana / placa: parciales inarmónicos')
    ax1.set_xlabel(r'frecuencia (en unidades del modo más grave)')
    ax1.set_xlim(0.5, 3.2)
    ax1.text(0.96, 0.92, r'razones $1:1{,}59:2{,}14:\dots$',
             transform=ax1.transAxes, ha='right', va='top', fontsize=9.5,
             style='italic')

    fig.tight_layout()
    guardar(fig, 's03_armonico_vs_inarmonico', ancho=8.4, alto=3.2)


def fig_decaimiento():
    t = np.linspace(0, 3.0, 800)
    # tres parciales: el agudo decae más rápido (tau menor)
    datos = [(1, 2.2, COLORES['acento'], 'parcial 1 (grave): decae lento'),
             (3, 1.0, COLORES['azul'],   'parcial 3: intermedio'),
             (6, 0.45, COLORES['gris'],  'parcial 6 (agudo): decae rápido')]
    fig, ax = plt.subplots(figsize=(7.0, 3.6))
    for n, tau, col, lab in datos:
        env = np.exp(-t / tau)
        ax.plot(t, env, color=col, label=lab)
    ax.set_xlabel('tiempo (s)')
    ax.set_ylabel('amplitud del parcial (rel.)')
    ax.set_ylim(0, 1.05)
    ax.set_title('Cada modo decae a su ritmo: el timbre del golpe cambia mientras se apaga')
    ax.legend(loc='upper right')
    guardar(fig, 's03_decaimiento_multimodo', ancho=7.0, alto=3.6)


if __name__ == '__main__':
    fig_modos_cuerda()
    fig_armonico_vs_inarmonico()
    fig_decaimiento()
