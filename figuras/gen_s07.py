# -*- coding: utf-8 -*-
"""Figuras de la sesión 07 — Batidos.

Genera:
  s07_batido_forma_onda.svg — suma de dos tonos cercanos con su envolvente
  s07_fases_batido.svg      — mecanismo: en fase se refuerzan, en contrafase
                              se cancelan

Ejecutar desde figuras/:  python3 gen_s07.py

Nota física: para que el ciclo rápido sea visible en la página se usan
f1 = 40 Hz y f2 = 43 Hz (la regla f_b = |f2 - f1| = 3 Hz es la misma a
cualquier altura; con 440/443 Hz el trazo sería una mancha).
"""
import numpy as np
import matplotlib.pyplot as plt

from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()


# ----------------------------------------------------------------------
# Figura 1: forma de onda del batido con envolvente
# ----------------------------------------------------------------------
def forma_onda():
    f1, f2 = 40.0, 43.0                      # Hz (bajas para ver el ciclo)
    fb = abs(f2 - f1)                        # 3 batidos por segundo
    t = np.linspace(0, 1.0, 6000)
    y = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    env = 2 * np.cos(2 * np.pi * (f2 - f1) / 2 * t)   # envolvente lenta

    fig, ax = plt.subplots()
    ax.plot(t, y, color=COLORES['azul'], lw=0.8)
    ax.plot(t, np.abs(env), color=COLORES['acento'], lw=1.8)
    ax.plot(t, -np.abs(env), color=COLORES['acento'], lw=1.8)

    # Un batido = de un máximo de la envolvente al siguiente
    t0, t1 = 1 / 3, 2 / 3
    ax.annotate('', xy=(t1, 2.45), xytext=(t0, 2.45),
                arrowprops=dict(arrowstyle='<->', lw=1.1,
                                color=COLORES['tinta']))
    ax.text((t0 + t1) / 2, 2.6,
            r'1 batido: $T_b = 1/f_b \approx 0{,}33$ s',
            ha='center', fontsize=9.5, color=COLORES['tinta'])

    ax.text(0.995, -2.75,
            r'$f_1 = 40$ Hz, $f_2 = 43$ Hz $\rightarrow$ '
            r'$f_b = |f_2 - f_1| = 3$ batidos/s',
            ha='right', fontsize=9.5, color=COLORES['acento'])

    ax.set_xlabel('tiempo (s)')
    ax.set_ylabel('presión (unid. arb.)')
    ax.set_xlim(0, 1)
    ax.set_ylim(-3.1, 3.1)
    ax.set_yticks([-2, 0, 2])
    ax.set_title('Dos tonos cercanos: una sola onda cuya amplitud ondula')
    guardar(fig, 's07_batido_forma_onda', ancho=7.0, alto=3.6)


# ----------------------------------------------------------------------
# Figura 2: el mecanismo — juego de fases
# ----------------------------------------------------------------------
def fases():
    t = np.linspace(0, 3, 600)               # tres ciclos de la onda
    onda = np.sin(2 * np.pi * t)

    fig, ejes = plt.subplots(1, 2, sharey=True)
    casos = [
        (ejes[0], onda, 'en fase: los empujones se suman'),
        (ejes[1], -onda, 'en contrafase: se cancelan'),
    ]
    for ax, onda2, titulo in casos:
        # Las dos ondas componentes (arriba), desplazadas verticalmente
        ax.plot(t, onda + 3.2, color=COLORES['azul'], lw=1.4)
        ax.plot(t, onda2 + 3.2, color=COLORES['gris'], lw=1.4, ls='--')
        # Su suma (abajo)
        ax.plot(t, onda + onda2 - 1.8, color=COLORES['acento'], lw=1.8)
        ax.axhline(-1.8, color=COLORES['gris'], lw=0.5, ls=':')
        ax.set_title(titulo, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel('tiempo')
        for lado in ('left', 'bottom'):
            ax.spines[lado].set_visible(False)

    ejes[0].text(0.05, 4.85, 'onda 1 (—) y onda 2 (- -)', fontsize=9,
                 color=COLORES['tinta'])
    ejes[0].text(0.05, 0.75, 'suma', fontsize=9, color=COLORES['acento'])
    ejes[1].text(0.05, 0.75, 'suma (casi silencio)', fontsize=9,
                 color=COLORES['acento'])
    ejes[0].set_ylim(-4.3, 5.4)

    fig.suptitle('Por qué late: las dos ondas entran y salen de paso',
                 fontsize=11.5, fontweight='bold')
    guardar(fig, 's07_fases_batido', ancho=6.8, alto=3.4)


if __name__ == '__main__':
    forma_onda()
    fases()
