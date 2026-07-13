"""Figuras de la sesión 13 — La voz cantada: fuente y filtro.

Genera:
  s13_fuente_filtro.svg — el modelo fuente-filtro en tres paneles
  s13_mapa_vocales.svg  — el plano F1–F2 con las cinco vocales del español

Ejecutar desde figuras/:  python3 gen_s13.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()

# ----------------------------------------------------------------------
# Figura 1: el modelo fuente-filtro (esquemático, vocal /a/, f0 = 200 Hz)
# ----------------------------------------------------------------------
f0 = 200.0                      # AJUSTAR: fundamental del zumbido glotal (Hz)
n = np.arange(1, 16)            # armónicos hasta 3 kHz
fn = n * f0
amp_fuente = 1.0 / n            # espectro glotal esquemático: cae como 1/n

# filtro del tracto: tres resonancias (formantes) de una /a/ aproximada
F = [(700, 110, 1.0), (1200, 150, 0.85), (2600, 350, 0.55)]  # (Hz, ancho, peso)

def filtro(f):
    """Suma de resonancias tipo campana (esquemático)."""
    H = np.zeros_like(f, dtype=float)
    for Fc, W, A in F:
        H += A / (1 + ((f - Fc) / W) ** 2)
    return H / 1.15

ff = np.linspace(0, 3100, 800)
amp_rad = amp_fuente * filtro(fn)
amp_rad = amp_rad / amp_rad.max()      # normalizado: importa la forma relativa

fig, axs = plt.subplots(1, 3, sharex=True, constrained_layout=True)

# panel 1: la fuente
ax = axs[0]
ax.vlines(fn, 0, amp_fuente, color=COLORES['acento'], lw=1.8)
ax.set_title('1 · fuente: zumbido glotal')
ax.set_ylabel('amplitud (rel.)')
ax.text(f0, 1.04, '$f_0$', ha='center', fontsize=9.5,
        color=COLORES['tinta'])

# panel 2: el filtro
ax = axs[1]
ax.plot(ff, filtro(ff), color=COLORES['azul'])
ax.set_title('2 · filtro: tracto vocal (/a/)')
for (Fc, W, A), et in zip(F, ['$F_1$', '$F_2$', '$F_3$']):
    ax.text(Fc, filtro(np.array([Fc]))[0] + 0.06, et, ha='center',
            fontsize=9.5, color=COLORES['tinta'])

# panel 3: el espectro radiado = fuente × filtro
ax = axs[2]
ax.vlines(fn, 0, amp_rad, color=COLORES['acento'], lw=1.8)
# envolvente punteada: filtro × caída 1/n de la fuente (pasa por las puntas)
sel = ff >= f0
env = filtro(ff[sel]) * f0 / ff[sel]
env = env / env.max()
ax.plot(ff[sel], env, '--', color=COLORES['gris'], lw=1.1)
ax.set_title('3 · espectro radiado')
ax.text(2000, 0.62, 'los armónicos cercanos\na un formante\nsobresalen',
        fontsize=8.5, color=COLORES['tinta'], ha='center')

for ax in axs:
    ax.set_xlim(0, 3100)
    ax.set_ylim(0, 1.15)
    ax.set_xticks([0, 1000, 2000, 3000])
    ax.set_xlabel('$f$ (Hz)')

guardar(fig, 's13_fuente_filtro', ancho=8.2, alto=2.6)

# ----------------------------------------------------------------------
# Figura 2: el mapa F1–F2 de las vocales del español (valores típicos
# aproximados de una voz adulta; los rangos son los del apunte)
# ----------------------------------------------------------------------
vocales = {                     # AJUSTAR: (F1 centro, F2 centro, semiancho F1, semiancho F2)
    '/a/': (750, 1300, 60, 120),
    '/e/': (450, 1950, 60, 170),
    '/i/': (285, 2350, 45, 170),
    '/o/': (450, 900, 60, 120),
    '/u/': (335, 700, 45, 110),
}

fig, ax = plt.subplots(constrained_layout=True)
for et, (f1c, f2c, a1, a2) in vocales.items():
    ax.add_patch(Ellipse((f1c, f2c), 2 * a1, 2 * a2, fc=COLORES['panel'],
                         ec=COLORES['acento'], lw=1.3))
    ax.text(f1c, f2c, et, ha='center', va='center', fontsize=11,
            style='italic', color=COLORES['tinta'])

# las dos reglas del mapa
ax.annotate('', xy=(820, 480), xytext=(330, 480),
            arrowprops=dict(arrowstyle='-|>', color=COLORES['azul'], lw=1.2))
ax.text(575, 420, 'la boca se abre → $F_1$ sube', ha='center', va='top',
        fontsize=9, color=COLORES['azul'])
ax.annotate('', xy=(880, 2450), xytext=(880, 900),
            arrowprops=dict(arrowstyle='-|>', color=COLORES['azul'], lw=1.2))
ax.text(905, 1675, 'la lengua avanza → $F_2$ sube', rotation=90,
        ha='left', va='center', fontsize=9, color=COLORES['azul'])

ax.set_xlim(180, 980)
ax.set_ylim(300, 2750)
ax.set_xlabel('$F_1$ (Hz)')
ax.set_ylabel('$F_2$ (Hz)')

guardar(fig, 's13_mapa_vocales', ancho=5.6, alto=4.4)

print('Listo: figuras de s13.')
