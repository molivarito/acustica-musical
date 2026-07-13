# -*- coding: utf-8 -*-
"""Figuras de la sesión 06 — Sonoridad y decibel.

Genera:
  s06_escala_decibel.svg     — regla vertical 0–120 dB SPL con hitos musicales
  s06_suma_fuentes.svg       — nivel al sumar N fuentes iguales (10·log10 N)
  s06_isofonicas_esquema.svg — curvas isofónicas ESQUEMÁTICAS (3 niveles)

Ejecutar desde figuras/:  python3 gen_s06.py
Los valores de los hitos son los típicos citados en el apunte
(Benade 1990 cap. 13; ROS cap. 6): redondeados, no medidos en sala.
"""
import numpy as np
import matplotlib.pyplot as plt

from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()


# ----------------------------------------------------------------------
# Figura 1: la escala del decibel con hitos musicales (regla vertical)
# ----------------------------------------------------------------------
def escala_decibel():
    fig, ax = plt.subplots()

    # Barra vertical de fondo (la "regla")
    ax.axvspan(-0.06, 0.06, color=COLORES['panel'], zorder=0)

    # Zona de la orquesta/banda en fortissimo (banda 95–110 dB)
    ax.fill_between([-0.06, 0.06], 95, 110, color=COLORES['acento'],
                    alpha=0.18, zorder=1)

    # Marcas cada 10 dB
    for nivel in range(0, 121, 10):
        ax.plot([-0.06, 0.06], [nivel, nivel], color=COLORES['gris'],
                lw=0.7, zorder=2)
        ax.text(-0.09, nivel, f'{nivel}', ha='right', va='center',
                fontsize=9.5, color=COLORES['tinta'])

    # Hitos (nivel, etiqueta). Valores típicos redondeados.
    hitos = [
        (0,   'umbral de audición (1000 Hz)'),
        (30,  'susurro'),
        (60,  'conversación'),
        (85,  'criterio NIOSH: 8 h/día máx.'),
        (102, 'orquesta o banda en $ff$ (~95–110)'),
        (120, 'umbral del dolor'),
    ]
    for nivel, texto in hitos:
        ax.plot([-0.06, 0.10], [nivel, nivel], color=COLORES['tinta'],
                lw=1.1, zorder=3)
        ax.plot(0.10, nivel, 'o', ms=4, color=COLORES['acento'], zorder=4)
        ax.text(0.14, nivel, texto, ha='left', va='center', fontsize=10,
                color=COLORES['tinta'])

    # Recordatorio de la gramática del dB, como bloque aparte a la derecha
    ax.annotate('', xy=(0.78, 70), xytext=(0.78, 60),
                arrowprops=dict(arrowstyle='-[, widthB=.4', lw=1.0,
                                color=COLORES['azul']))
    ax.text(0.82, 65, '+10 dB = ×10 en intensidad\n≈ "el doble de fuerte"',
            ha='left', va='center', fontsize=9, color=COLORES['azul'])
    ax.annotate('', xy=(0.78, 33), xytext=(0.78, 30),
                arrowprops=dict(arrowstyle='-[, widthB=.4', lw=1.0,
                                color=COLORES['azul']))
    ax.text(0.82, 31.5, '+3 dB = ×2 en intensidad\n(cambio chico)',
            ha='left', va='center', fontsize=9, color=COLORES['azul'])

    ax.set_xlim(-0.55, 1.75)
    ax.set_ylim(-6, 126)
    ax.set_ylabel('$L_p$ (dB SPL re 20 µPa)')
    ax.set_xticks([])
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_yticks([])
    ax.set_title('La escala del decibel: del umbral al dolor')
    guardar(fig, 's06_escala_decibel', ancho=6.4, alto=5.2)


# ----------------------------------------------------------------------
# Figura 2: suma de fuentes iguales — +3 dB al duplicar
# ----------------------------------------------------------------------
def suma_fuentes():
    fig, ax = plt.subplots()

    n = np.logspace(0, 2, 300)          # de 1 a 100 fuentes
    ax.semilogx(n, 10 * np.log10(n), color=COLORES['gris'], lw=1.2,
                zorder=2, label=r'$\Delta L = 10\,\log_{10} N$')

    # Puntos clave con sus lecturas musicales
    puntos = [
        (1,   0,  '1 fuente\n(referencia)'),
        (2,   3,  '2 fuentes: +3 dB\n(cambio chico)'),
        (4,   6,  '4 fuentes: +6 dB'),
        (10, 10,  '10 fuentes: +10 dB\n≈ el doble de fuerte'),
        (100, 20, '100 fuentes: +20 dB\n≈ el cuádruple'),
    ]
    for x, y, texto in puntos:
        ax.plot(x, y, 'o', ms=6, color=COLORES['acento'], zorder=3)
        despl = (0, 14) if x < 50 else (-52, 6)
        ax.annotate(texto, xy=(x, y), xytext=despl,
                    textcoords='offset points', fontsize=9,
                    color=COLORES['tinta'], ha='left', va='bottom')

    ax.set_xlabel('número de fuentes iguales $N$')
    ax.set_ylabel('aumento de nivel (dB)')
    ax.set_xticks([1, 2, 4, 10, 100])
    ax.set_xticklabels(['1', '2', '4', '10', '100'])
    ax.set_ylim(-1, 26)
    ax.set_title('Duplicar las fuentes suma 3 dB, no el doble de sonoridad')
    guardar(fig, 's06_suma_fuentes', ancho=6.6, alto=4.0)


# ----------------------------------------------------------------------
# Figura 3: curvas isofónicas esquemáticas
# ----------------------------------------------------------------------
def isofonicas():
    """Forma CUALITATIVA de las curvas de igual sonoridad.

    No son datos normalizados: reproducen solo los rasgos que el apunte
    usa (sordera relativa a los graves, que se agrava a nivel bajo, y
    máxima sensibilidad en la zona de 3–4 kHz).
    """
    f = np.logspace(np.log10(20), np.log10(16000), 500)
    d = np.log10(f / 1000.0)

    def curva(fon):
        # Subida al grave: forma fija que crece hacia 20 Hz, escalada por
        # g(fon) para que las curvas queden SEPARADAS a baja frecuencia
        # (a nivel bajo el grave exige mucho más dB extra).
        forma_grave = np.where(d < 0, (d / -1.7)**2, 0.0)   # 0 en 1kHz, 1 en 20Hz
        g = 15.0 + (100.0 - fon) / 80.0 * 40.0              # 55 (20fon) … 15 (100fon)
        dip = -8.0 * np.exp(-((np.log10(f / 3500.0)) / 0.13)**2)  # 3–4 kHz
        agudos = np.where(f > 6000, 45.0 * (np.log10(f / 6000.0))**2, 0.0)
        w = (118.0 - fon) / 100.0
        return fon + g * forma_grave + dip + w * agudos

    fig, ax = plt.subplots()
    niveles = [(20, '20 fon'), (60, '60 fon'), (100, '100 fon')]
    colores = [COLORES['azul'], COLORES['acento'], COLORES['tinta']]
    for (fon, etiqueta), c in zip(niveles, colores):
        y = curva(fon)
        ax.semilogx(f, y, color=c, lw=1.8)
        ax.text(23, y[0] + 3, etiqueta, fontsize=9.5, color=c, va='bottom')
        ax.plot(1000, fon, 'o', ms=5, color=c)   # punto de referencia 1 kHz

    # Referencia: a 1000 Hz cada curva vale su número de fones
    ax.axvline(1000, color=COLORES['gris'], lw=0.7, ls=':')
    ax.text(1050, 2, 'referencia:\n1000 Hz', fontsize=8.5,
            color=COLORES['gris'], ha='left')

    # Anotación pedagógica: el grave exige mucho más nivel a volumen bajo
    ax.annotate('a nivel bajo, un grave\nnecesita mucho más dB\npara oírse igual',
                xy=(40, curva(20)[np.argmin(np.abs(f - 40))]),
                xytext=(260, 96), fontsize=9,
                color=COLORES['azul'], ha='left',
                arrowprops=dict(arrowstyle='->', color=COLORES['azul'],
                                lw=1.0))

    ax.set_xlabel('frecuencia (Hz)')
    ax.set_ylabel('$L_p$ (dB SPL re 20 µPa)')
    ax.set_xticks([20, 50, 100, 200, 500, 1000, 2000, 5000, 10000])
    ax.set_xticklabels(['20', '50', '100', '200', '500', '1k', '2k',
                        '5k', '10k'])
    ax.set_ylim(-8, 125)
    ax.set_title('Curvas de igual sonoridad (esquema cualitativo)')
    guardar(fig, 's06_isofonicas_esquema', ancho=6.8, alto=4.4)


if __name__ == '__main__':
    escala_decibel()
    suma_fuentes()
    isofonicas()
