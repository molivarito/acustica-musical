# -*- coding: utf-8 -*-
"""Figuras de la sesión 09 — Escalas y temperamentos.

Genera:
  s09_coma_pitagorica.svg   — 12 quintas justas vs. 7 octavas en cents; la
                              escalera no cierra por ~23,5 cents
  s09_desviaciones.svg      — desviación (cents) de quinta y tercera mayor
                              en justa / pitagórica / temperamento igual

Ejecutar desde figuras/:  python3 gen_s09.py

Valores (Benade 1990 cap. 15–16; C&G cap. 4): quinta justa 3:2 = 701,955
cents; octava = 1200; coma pitagórica = 12·701,955 − 7·1200 ≈ 23,46 cents.
Tercera mayor: justa 5:4 = 386,3; pitagórica 81:64 = 407,8; igual = 400.
"""
import numpy as np
import matplotlib.pyplot as plt

from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()

QUINTA_JUSTA = 1200 * np.log2(3 / 2)         # 701,955 cents
OCTAVA = 1200.0


# ----------------------------------------------------------------------
# Figura 1: la coma pitagórica como dos escaleras que no cierran
# ----------------------------------------------------------------------
def coma_pitagorica():
    fig, ax = plt.subplots()

    # Escalera de 12 quintas justas (acumulando cents)
    pasos_q = np.arange(0, 13)
    cents_q = pasos_q * QUINTA_JUSTA
    ax.step(pasos_q, cents_q, where='post', color=COLORES['acento'], lw=1.8,
            label='12 quintas justas (×3/2)')
    ax.plot(pasos_q, cents_q, 'o', ms=3.5, color=COLORES['acento'])

    # Escalera de 7 octavas (mismo eje x reescalado a 12 pasos para comparar
    # el punto final: 7 octavas = mismo "Do" nominal)
    pasos_o = np.linspace(0, 12, 8)
    cents_o = np.arange(0, 8) * OCTAVA
    ax.step(pasos_o, cents_o, where='post', color=COLORES['azul'], lw=1.8,
            label='7 octavas (×2)')
    ax.plot(pasos_o, cents_o, 's', ms=3.5, color=COLORES['azul'])

    # El sobrante: la coma pitagórica
    top_q = cents_q[-1]
    top_o = cents_o[-1]
    ax.annotate('', xy=(12, top_q), xytext=(12, top_o),
                arrowprops=dict(arrowstyle='<->', lw=1.3,
                                color=COLORES['tinta']))
    coma = top_q - top_o
    ax.text(12.15, (top_q + top_o) / 2,
            f'coma pitagórica\n≈ {coma:.1f} cents\n(¼ de semitono)',
            fontsize=9.5, color=COLORES['tinta'], va='center')

    ax.text(0.3, 8850, r'$12\times702 = 8424$ cents', fontsize=9.5,
            color=COLORES['acento'])
    ax.text(0.3, 8300, r'$7\times1200 = 8400$ cents', fontsize=9.5,
            color=COLORES['azul'])

    ax.set_xlabel('quintas apiladas (o su octava equivalente)')
    ax.set_ylabel('intervalo acumulado (cents)')
    ax.set_xlim(0, 15.2)
    ax.set_ylim(-300, 9700)
    ax.set_xticks(range(0, 13, 2))
    ax.legend(loc='lower right')
    ax.set_title('Doce quintas justas no cierran con siete octavas')
    guardar(fig, 's09_coma_pitagorica', ancho=7.0, alto=4.4)


# ----------------------------------------------------------------------
# Figura 2: desviaciones de quinta y tercera en tres sistemas
# ----------------------------------------------------------------------
def desviaciones():
    # Desviación respecto de la razón JUSTA correspondiente (en cents).
    # Quinta: justa 701,955 (ref). Tercera mayor: justa 386,314 (ref).
    quinta_justa = 1200 * np.log2(3 / 2)
    tercera_justa = 1200 * np.log2(5 / 4)

    sistemas = ['Entonación\njusta', 'Pitagórica', 'Temperamento\nigual']
    # Quinta en cada sistema
    quintas = [quinta_justa, quinta_justa, 700.0]
    # Tercera mayor en cada sistema
    terceras = [tercera_justa, 1200 * np.log2(81 / 64), 400.0]

    dev_quinta = [q - quinta_justa for q in quintas]
    dev_tercera = [t - tercera_justa for t in terceras]

    fig, ax = plt.subplots()
    x = np.arange(len(sistemas))
    ancho = 0.36

    b1 = ax.bar(x - ancho / 2, dev_quinta, ancho, color=COLORES['azul'],
                label='quinta (5ª)')
    b2 = ax.bar(x + ancho / 2, dev_tercera, ancho, color=COLORES['acento'],
                label='tercera mayor (3ª M)')

    ax.axhline(0, color=COLORES['tinta'], lw=1.0)
    ax.text(-0.35, 2.0, 'justo (0 cents)', fontsize=8.5,
            color=COLORES['gris'], ha='left')

    # Etiquetas numéricas sobre cada barra
    for barras in (b1, b2):
        for b in barras:
            h = b.get_height()
            va = 'bottom' if h >= 0 else 'top'
            off = 0.4 if h >= 0 else -0.4
            ax.text(b.get_x() + b.get_width() / 2, h + off,
                    f'{h:+.0f}', ha='center', va=va, fontsize=8.5,
                    color=COLORES['tinta'])

    ax.set_xticks(x)
    ax.set_xticklabels(sistemas)
    ax.set_ylabel('desviación respecto al justo (cents)')
    ax.set_ylim(-16, 27)
    ax.legend(loc='lower left')
    ax.set_title('Qué sacrifica cada temperamento (quinta vs. tercera mayor)')
    guardar(fig, 's09_desviaciones', ancho=7.0, alto=4.2)


if __name__ == '__main__':
    coma_pitagorica()
    desviaciones()
