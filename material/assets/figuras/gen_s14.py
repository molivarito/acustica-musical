"""Figuras de la sesión 14 — La sala como instrumento.

Genera:
  s14_respuesta_impulsiva.svg — directo, reflexiones tempranas y cola
  s14_caida_t60.svg           — la caída de 60 dB y el piso de ruido
  s14_modos_sala.svg          — modos axiales entre dos paredes (la ducha)

Ejecutar desde figuras/:  python3 gen_s14.py
"""
import numpy as np
import matplotlib.pyplot as plt

from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()

# ----------------------------------------------------------------------
# Figura 1: respuesta de una sala a un impulso (esquemática)
# ----------------------------------------------------------------------
rng = np.random.default_rng(11)   # semilla fija: figura reproducible

t_dir = 12.0                                        # llegada del directo (ms)
tempranas = [(45, 0.55), (63, 0.46), (82, 0.37),    # (ms, amplitud)
             (105, 0.30), (130, 0.24)]
t_cola = np.sort(rng.uniform(150, 620, 150))        # cola: llegadas densas
a_cola = 0.50 * np.exp(-(t_cola - 150) / 160) * rng.uniform(0.25, 1, t_cola.size)

fig, ax = plt.subplots(constrained_layout=True)
ax.vlines([t_dir], 0, 1.0, color=COLORES['acento'], lw=2.4)
ax.vlines([t for t, a in tempranas], 0, [a for t, a in tempranas],
          color=COLORES['azul'], lw=1.8)
ax.vlines(t_cola, 0, a_cola, color=COLORES['gris'], lw=0.8)

# envolvente exponencial de la cola
tt = np.linspace(150, 640, 200)
ax.plot(tt, 0.52 * np.exp(-(tt - 150) / 160), '--', color=COLORES['tinta'],
        lw=1.1)
ax.text(430, 0.24, 'decaimiento exponencial\n(la pendiente fija el $T_{60}$)',
        fontsize=8.5, color=COLORES['tinta'])

# separadores y rótulos de las tres zonas
for x in (30, 150):
    ax.axvline(x, color=COLORES['gris'], lw=0.8, ls=':')
ax.text(t_dir, 1.04, 'sonido directo', ha='left', fontsize=9,
        color=COLORES['acento'])
ax.text(90, 0.86, 'reflexiones\ntempranas', ha='center', fontsize=9,
        color=COLORES['azul'])
ax.text(390, 0.86, 'cola reverberante', ha='center', fontsize=9,
        color=COLORES['gris'])

ax.set_xlim(0, 660)
ax.set_ylim(0, 1.14)
ax.set_yticks([])
ax.set_xlabel('tiempo desde el impulso (ms)')
ax.set_ylabel('amplitud (esquem.)')

guardar(fig, 's14_respuesta_impulsiva', ancho=6.8, alto=3.0)

# ----------------------------------------------------------------------
# Figura 2: la caída de 60 dB, el T60 y el piso de ruido
# Números del ejemplo del apunte: sala de clases, T60 ≈ 1,1 s.
# ----------------------------------------------------------------------
t0, L0, T60, piso = 0.2, 90.0, 1.1, 45.0   # AJUSTAR si se quiere otro caso
pend = 60.0 / T60                          # dB/s

t = np.linspace(0, 2.3, 600)
ideal = np.where(t < t0, L0, L0 - pend * (t - t0))
medida = np.maximum(ideal, piso)

fig, ax = plt.subplots(constrained_layout=True)
ax.plot(t, medida, color=COLORES['acento'], label='lo que registra la app')
sel = ideal < piso + 2
ax.plot(t[sel], ideal[sel], '--', color=COLORES['azul'], lw=1.4,
        label='extrapolación de la caída inicial')

# referencias horizontales: nivel inicial y −60 dB
for y in (L0, L0 - 60):
    ax.axhline(y, color=COLORES['gris'], lw=0.8, ls=':')
ax.axvline(t0, color=COLORES['gris'], lw=0.8, ls=':')
ax.text(t0 - 0.03, 92.5, 'la fuente calla', ha='right', fontsize=8.5,
        color=COLORES['tinta'])

# flecha vertical: los 60 dB de caída
xf = 1.72
ax.annotate('', xy=(xf, L0 - 60), xytext=(xf, L0),
            arrowprops=dict(arrowstyle='<->', color=COLORES['tinta'], lw=0.9))
ax.text(xf + 0.04, L0 - 30, '60 dB\n(la intensidad cae\na la millonésima)',
        fontsize=8.5, va='center', color=COLORES['tinta'])

# flecha horizontal: el T60
ax.annotate('', xy=(t0 + T60, 26), xytext=(t0, 26),
            arrowprops=dict(arrowstyle='<->', color=COLORES['tinta'], lw=0.9))
ax.text(t0 + T60 / 2, 24.2, '$T_{60}$', ha='center', va='top', fontsize=10.5,
        color=COLORES['tinta'])

ax.text(1.95, piso + 1.5, 'ruido de fondo', fontsize=8.5,
        color=COLORES['acento'])

ax.set_xlim(0, 2.3)
ax.set_ylim(18, 97)
ax.set_xlabel('tiempo (s)')
ax.set_ylabel('$L_p$ (dB re 20 µPa)')
ax.legend(loc='center right', bbox_to_anchor=(1.0, 0.72))

guardar(fig, 's14_caida_t60', ancho=6.8, alto=3.6)

# ----------------------------------------------------------------------
# Figura 3: modos axiales entre dos paredes paralelas (la ducha, L = 2 m)
# En una pared rígida el aire no puede moverse: la presión es MÁXIMA ahí
# (al revés que en el extremo abierto de un tubo).
# ----------------------------------------------------------------------
Lsala = 2.0
xx = np.linspace(0, Lsala, 300)
frecs = [86, 171, 257]     # ≈ 343·n/(2·2) Hz, redondeadas como en el apunte

fig, axs = plt.subplots(3, 1, sharex=True, constrained_layout=True)
for ax, nmodo, fmodo in zip(axs, (1, 2, 3), frecs):
    p = np.cos(nmodo * np.pi * xx / Lsala)
    ax.fill_between(xx, p, -p, color=COLORES['panel'])
    ax.plot(xx, p, color=COLORES['acento'])
    ax.plot(xx, -p, color=COLORES['acento'], lw=1.0, alpha=0.55)
    # las paredes
    for x in (0, Lsala):
        ax.axvline(x, color=COLORES['tinta'], lw=4.0)
    ax.text(Lsala + 0.06, 0,
            f'$n = {nmodo}$ · $f \\approx {fmodo}$ Hz', va='center',
            fontsize=9.5, color=COLORES['tinta'])
    ax.set_ylim(-1.4, 1.4)
    ax.set_yticks([])
    ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
    ax.spines['bottom'].set_bounds(0, Lsala)
    ax.spines['left'].set_visible(False)

axs[0].annotate('en la pared, la presión\nes máxima (el aire\nno puede moverse)',
                xy=(0.02, 0.95), xytext=(0.28, 1.05), fontsize=8,
                color=COLORES['tinta'], va='center',
                arrowprops=dict(arrowstyle='->', color=COLORES['gris'],
                                lw=0.9))
axs[0].set_title('Dos paredes paralelas separadas $L$ = 2 m (una ducha): '
                 '$f = v\\,n/2L$', fontsize=10.5)
axs[-1].set_xlabel('distancia entre las paredes (m)')
axs[-1].set_xlim(-0.08, 2.75)

guardar(fig, 's14_modos_sala', ancho=6.6, alto=3.8)

print('Listo: figuras de s14.')
