# -*- coding: utf-8 -*-
"""Figuras de la sesión 10 — Resonancia, impedancia y acoplamiento.

Genera:
  s10_curva_resonancia.svg  — respuesta vs. frecuencia de excitación, dos
                              amortiguamientos (pico ancho vs. angosto)
  s10_acoplamiento.svg      — cadena cuerda→puente→tapa→aire (cajas/flechas)
  s10_helmholtz.svg         — esquema de la botella: masa del cuello +
                              resorte del volumen

Ejecutar desde figuras/:  python3 gen_s10.py

Curvas de resonancia ESQUEMÁTICAS (resonador de 2.º orden); ilustran la
relación pico ancho↔poco Q y pico angosto↔alto Q (Benade 1990 cap. 10;
C&G cap. 5). No corresponden a un objeto medido.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse

from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()


# ----------------------------------------------------------------------
# Figura 1: curva de respuesta para dos amortiguamientos
# ----------------------------------------------------------------------
def curva_resonancia():
    f0 = 1.0
    f = np.linspace(0.2, 2.0, 800)

    def respuesta(Q):
        # Amplitud de un resonador de segundo orden forzado (normalizada)
        x = f / f0
        return 1.0 / np.sqrt((1 - x**2)**2 + (x / Q)**2)

    fig, ax = plt.subplots()
    for Q, c, etiqueta in [(3, COLORES['azul'], 'poco Q: pico ancho\n(muy amortiguado)'),
                           (18, COLORES['acento'], 'alto Q: pico angosto\n(poco amortiguado)')]:
        r = respuesta(Q)
        ax.plot(f, r, color=c, lw=1.9, label=etiqueta)

    # Marcar f0
    ax.axvline(f0, color=COLORES['gris'], lw=0.7, ls=':')
    ax.text(f0 + 0.03, 18.8, r'$f_0$', ha='left', va='top', fontsize=12,
            color=COLORES['tinta'])

    # Flecha del ancho a media potencia para el pico angosto
    r18 = respuesta(18)
    pico = r18.max()
    ax.annotate('ancho ↔ amortiguamiento', xy=(1.0, pico * 0.6),
                xytext=(1.25, pico * 0.75), fontsize=9,
                color=COLORES['acento'],
                arrowprops=dict(arrowstyle='->', color=COLORES['acento'],
                                lw=1.0))

    ax.set_xlabel('frecuencia de excitación / $f_0$')
    ax.set_ylabel('amplitud de respuesta (unid. arb.)')
    ax.set_xlim(0.2, 2.0)
    ax.set_ylim(0, 20)
    ax.legend(loc='upper right')
    ax.set_title('La curva de resonancia: el pico y su ancho (esquema)')
    guardar(fig, 's10_curva_resonancia', ancho=6.8, alto=4.2)


# ----------------------------------------------------------------------
# Figura 2: cadena de acoplamiento cuerda→puente→tapa→aire
# ----------------------------------------------------------------------
def acoplamiento():
    fig, ax = plt.subplots()

    cajas = [
        (0.5, 'CUERDA', 'alta impedancia\n(vibra fuerte,\nmueve poco aire)',
         COLORES['azul']),
        (3.2, 'PUENTE', 'transformador\nde impedancia', COLORES['acento']),
        (5.9, 'TAPA / CAJA', 'baja impedancia\n(mueve mucho aire)',
         COLORES['azul']),
        (8.6, 'AIRE', 'sonido\nradiado', COLORES['tinta']),
    ]
    w, h = 1.9, 1.5
    centros = []
    for x, titulo, sub, color in cajas:
        box = FancyBboxPatch((x, 1.0), w, h,
                             boxstyle='round,pad=0.06,rounding_size=0.12',
                             linewidth=1.4, edgecolor=color,
                             facecolor=COLORES['panel'])
        ax.add_patch(box)
        ax.text(x + w / 2, 1.0 + h - 0.42, titulo, ha='center', va='center',
                fontsize=10.5, fontweight='bold', color=color)
        ax.text(x + w / 2, 1.0 + 0.45, sub, ha='center', va='center',
                fontsize=8, color=COLORES['tinta'])
        centros.append(x + w / 2)

    # Flechas de flujo de energía
    for i in range(len(cajas) - 1):
        x0 = cajas[i][0] + w
        x1 = cajas[i + 1][0]
        flecha = FancyArrowPatch((x0, 1.75), (x1, 1.75),
                                 arrowstyle='-|>', mutation_scale=16,
                                 lw=1.6, color=COLORES['tinta'])
        ax.add_patch(flecha)

    ax.text(5.55, 2.95, 'energía de la vibración',
            ha='center', fontsize=9, color=COLORES['tinta'], style='italic')

    # Nota del compromiso
    ax.text(5.55, 0.25,
            'La caja no agrega energía: convierte la vibración de la cuerda '
            'en sonido.\nSonar más fuerte se paga durando menos.',
            ha='center', fontsize=8.5, color=COLORES['acento'])

    ax.set_xlim(0, 11)
    ax.set_ylim(0, 3.4)
    ax.axis('off')
    ax.set_title('Acoplamiento: cómo la energía de la cuerda llega al aire')
    guardar(fig, 's10_acoplamiento', ancho=7.4, alto=2.9)


# ----------------------------------------------------------------------
# Figura 3: resonador de Helmholtz (la botella)
# ----------------------------------------------------------------------
def helmholtz():
    fig, ax = plt.subplots()

    # Silueta de la botella: cuerpo ancho (x 2.2–4.2), hombro y cuello
    # angosto (x 2.85–3.55). Se dibuja como un contorno cerrado.
    xc = 3.2                                  # eje de la botella
    cuello_izq, cuello_der = 2.85, 3.55
    cuerpo_izq, cuerpo_der = 2.2, 4.2
    # Contorno recorrido en sentido horario desde la boca izquierda
    cont_x = [cuello_izq, cuello_izq, cuerpo_izq, cuerpo_izq, 2.5,
              3.9, cuerpo_der, cuerpo_der, cuello_der, cuello_der]
    cont_y = [8.4, 6.8, 6.0, 1.6, 1.0,
              1.0, 1.6, 6.0, 6.8, 8.4]
    ax.plot(cont_x, cont_y, color=COLORES['tinta'], lw=1.6)

    # Volumen de aire (resorte): relleno del cuerpo, respetando el contorno
    ax.fill_between([cuerpo_izq, cuerpo_der], 1.3, 6.0,
                    color=COLORES['panel'], zorder=0)
    ax.fill_between([2.5, 3.9], 1.0, 1.3, color=COLORES['panel'], zorder=0)

    # Masa de aire en el cuello (tapón) — banda sombreada dentro del cuello
    ax.fill_between([cuello_izq, cuello_der], 6.4, 7.7,
                    color=COLORES['acento'], alpha=0.28, zorder=1)
    ax.annotate('masa de aire\n(el "tapón" del cuello)',
                xy=(cuello_der, 7.1), xytext=(4.4, 7.8), fontsize=9.5,
                color=COLORES['acento'],
                arrowprops=dict(arrowstyle='->', color=COLORES['acento'],
                                lw=1.0))
    # Flecha de oscilación del tapón (sube y baja)
    ax.annotate('', xy=(xc, 7.9), xytext=(xc, 6.7),
                arrowprops=dict(arrowstyle='<->', lw=1.4,
                                color=COLORES['acento']))

    # Resorte esquemático dentro del cuerpo
    ys = np.linspace(1.8, 5.6, 200)
    xs = xc + 0.5 * np.sin(2 * np.pi * (ys - 1.8) / 0.65)
    ax.plot(xs, ys, color=COLORES['azul'], lw=1.4)
    ax.annotate('resorte de aire\n(el volumen se comprime)',
                xy=(3.0, 3.6), xytext=(4.5, 3.4), fontsize=9.5,
                color=COLORES['azul'],
                arrowprops=dict(arrowstyle='->', color=COLORES['azul'],
                                lw=1.0))

    # Soplo rasante sobre la boca
    ax.annotate('', xy=(3.75, 8.7), xytext=(2.65, 8.7),
                arrowprops=dict(arrowstyle='-|>', lw=1.4,
                                color=COLORES['gris']))
    ax.text(2.55, 9.0, 'soplo rasante', fontsize=9, color=COLORES['gris'])

    # Fórmula (semicuantitativa, coherente con el recuadro del apunte)
    ax.text(5.2, 1.6,
            r'$f_0 = \dfrac{v}{2\pi}\sqrt{\dfrac{A}{V\,L_{ef}}}$',
            fontsize=12, color=COLORES['tinta'])
    ax.text(5.2, 0.7, 'menos volumen $V$ → $f_0$ más aguda',
            fontsize=8.5, color=COLORES['tinta'])

    ax.set_xlim(1.5, 9.5)
    ax.set_ylim(0, 9.6)
    ax.axis('off')
    ax.set_title('El resonador de Helmholtz: masa del cuello + resorte del volumen')
    guardar(fig, 's10_helmholtz', ancho=7.0, alto=4.6)


if __name__ == '__main__':
    curva_resonancia()
    acoplamiento()
    helmholtz()
