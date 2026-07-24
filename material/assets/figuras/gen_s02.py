"""Figuras de la sesión 02 — Ondas y representación.

Genera:
  s02_tres_retratos.svg : la MISMA señal (tono con varios parciales) en sus
      tres representaciones: forma de onda, espectro y espectrograma.
  s02_propagacion_lambda.svg : onda de presión propagándose en el aire, con
      compresiones/enrarecimientos, la longitud de onda lambda marcada y
      la relación v = lambda f.

Ejecutar desde figuras/:  python3 gen_s02.py
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()

# --- Señal de trabajo: tono compuesto (como una vocal cantada) ---------
F1 = 200.0                       # frecuencia fundamental, Hz
PARCIALES = [1, 2, 3, 4]         # armónicos presentes
AMPL = [1.0, 0.55, 0.35, 0.18]   # amplitudes relativas (decrecientes)
FS = 22050                       # tasa de muestreo para la señal, muestras/s


def senal(t):
    y = np.zeros_like(t)
    for n, a in zip(PARCIALES, AMPL):
        y += a * np.sin(2 * np.pi * n * F1 * t)
    return y


def espectrograma_manual(x, fs, nfft=1024, salto=256):
    """STFT sencilla con ventana de Hann; devuelve (t, f, nivel_dB)."""
    ventana = np.hanning(nfft)
    inicios = range(0, len(x) - nfft, salto)
    cols = []
    for i in inicios:
        seg = x[i:i + nfft] * ventana
        esp = np.abs(np.fft.rfft(seg))
        cols.append(esp)
    S = np.array(cols).T
    S_db = 20 * np.log10(S / S.max() + 1e-6)
    f = np.fft.rfftfreq(nfft, 1 / fs)
    t = (np.array(list(inicios)) + nfft / 2) / fs
    return t, f, S_db


def fig_tres_retratos():
    fig, axes = plt.subplots(1, 3, figsize=(9.4, 3.1))

    # (1) Forma de onda: presión vs tiempo, ~3 períodos
    t = np.linspace(0, 3 / F1, 1200)
    axes[0].plot(t * 1000, senal(t), color=COLORES['acento'])
    axes[0].set_title('Forma de onda')
    axes[0].set_xlabel('tiempo (ms)')
    axes[0].set_ylabel('presión (u.a.)')
    axes[0].axhline(0, color=COLORES['gris'], lw=0.7)

    # (2) Espectro: nivel vs frecuencia (peineta de parciales)
    frecs = [n * F1 for n in PARCIALES]
    niveles_db = 20 * np.log10(np.array(AMPL))
    axes[1].stem(frecs, niveles_db, basefmt=' ',
                 linefmt=COLORES['azul'], markerfmt='o')
    for l in axes[1].get_children():
        pass
    axes[1].set_title('Espectro')
    axes[1].set_xlabel('frecuencia (Hz)')
    axes[1].set_ylabel('nivel (dB rel.)')
    axes[1].set_xlim(0, 5 * F1)
    axes[1].set_ylim(-22, 3)

    # (3) Espectrograma real de la misma señal (con un click inicial)
    dur = 0.5
    tt = np.arange(0, dur, 1 / FS)
    x = senal(tt)
    x[:60] += 3.0 * np.hanning(120)[:60]     # un "golpe" breve al inicio
    tS, fS, S_db = espectrograma_manual(x, FS)
    im = axes[2].pcolormesh(tS, fS, S_db, cmap='magma', vmin=-55, vmax=0,
                            shading='auto', rasterized=True)
    axes[2].set_ylim(0, 1100)
    axes[2].set_title('Espectrograma')
    axes[2].set_xlabel('tiempo (s)')
    axes[2].set_ylabel('frecuencia (Hz)')
    cb = fig.colorbar(im, ax=axes[2], fraction=0.046, pad=0.04)
    cb.set_label('nivel (dB)', fontsize=8.5)
    cb.ax.tick_params(labelsize=8)

    fig.tight_layout()
    guardar(fig, 's02_tres_retratos', ancho=9.4, alto=3.1)


def fig_propagacion():
    L = 2.0                              # tramo de aire mostrado, en metros
    lam = 0.78                           # longitud de onda (La4: 343/440 m)
    x = np.linspace(0, L, 1000)
    p = np.cos(2 * np.pi * x / lam)

    fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True, figsize=(7.2, 4.2),
                                   gridspec_kw={'height_ratios': [1, 1.3]})

    # (arriba) "moléculas de aire": barras cuya DENSIDAD sigue la presión.
    # Densidad local rho(x) = 1 + 0.8 cos(kx); las barras se colocan en los
    # puntos donde la cuenta acumulada N(x) cruza un entero -> más juntas
    # donde la presión (y la densidad de aire) es máxima. Física correcta.
    k = 2 * np.pi / lam
    xf = np.linspace(0, L, 6000)
    Nf = xf + (0.8 / k) * np.sin(k * xf)             # acumulada de rho
    objetivos = np.arange(Nf[0], Nf[-1], L / 130.0)  # ~130 barras
    xpos = np.interp(objetivos, Nf, xf)
    for xp in xpos:
        ax0.plot([xp, xp], [0, 1], color=COLORES['tinta'], lw=0.7, alpha=0.75)
    ax0.set_ylim(0, 1)
    ax0.set_xlim(-0.02, L + 0.02)
    ax0.set_yticks([])
    # etiquetas de compresión (x=0, lam) y enrarecimiento (x=lam/2), con caja
    caja = dict(boxstyle='round,pad=0.15', fc=COLORES['papel'], ec='none', alpha=0.9)
    ax0.text(lam, 0.5, 'compresión', fontsize=8.5, ha='center', va='center',
             color=COLORES['acento'], bbox=caja)
    ax0.text(lam * 0.5, 0.5, 'enrarecimiento', fontsize=8.5, ha='center',
             va='center', color=COLORES['azul'], bbox=caja)
    # flecha de propagación por encima del panel
    ax0.annotate('', xy=(L * 0.62, 1.22), xytext=(L * 0.38, 1.22),
                 annotation_clip=False,
                 arrowprops=dict(arrowstyle='->', color=COLORES['tinta'], lw=1.4))
    ax0.text(L * 0.5, 1.30, r'$v \approx 343$ m/s', ha='center',
             fontsize=9.5, clip_on=False)

    # (abajo) presión vs posición, con lambda marcada entre dos crestas
    ax1.plot(x, p, color=COLORES['acento'])
    ax1.axhline(0, color=COLORES['gris'], lw=0.7)
    ax1.annotate('', xy=(lam, 1.18), xytext=(0, 1.18),
                 arrowprops=dict(arrowstyle='<->', color=COLORES['tinta'], lw=1.2))
    ax1.text(lam / 2, 1.28, r'$\lambda$', ha='center', fontsize=12)
    ax1.set_xlabel('posición (m)')
    ax1.set_ylabel('presión (u.a.)')
    ax1.set_ylim(-1.35, 1.55)
    ax1.set_yticks([-1, 0, 1])
    ax1.text(0.98, 0.06, r'$v = \lambda\, f$', transform=ax1.transAxes,
             ha='right', va='bottom', fontsize=12)

    fig.suptitle('El aire se comprime y se enrarece; lo que viaja es el empujón, no el aire',
                 fontsize=10.5, y=1.00)
    fig.tight_layout()
    guardar(fig, 's02_propagacion_lambda', ancho=7.2, alto=4.2)


if __name__ == '__main__':
    fig_tres_retratos()
    fig_propagacion()
