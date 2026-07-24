"""Figuras de la sesión 11 — Cuerdas frotadas y el cuerpo del instrumento.

Genera:
  s11_helmholtz_esquina.svg  — seis instantáneas del movimiento de Helmholtz
  s11_stick_slip.svg         — el ciclo pegar-soltar visto desde el punto
                               frotado y desde el puente

La cadena cuerda→puente→tapa→aire NO se genera aquí: los documentos de
s11 reutilizan figuras/s10_acoplamiento.svg (generada por gen_s10.py).

Ejecutar desde figuras/:  python3 gen_s11.py
Parámetros ajustables marcados con  # AJUSTAR
"""
import numpy as np
import matplotlib.pyplot as plt

from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()

# ----------------------------------------------------------------------
# Figura 1: movimiento de Helmholtz — la esquina que viaja
# ----------------------------------------------------------------------
L = 1.0          # largo de la cuerda (normalizado)
h = 1.0          # flecha máxima del óvalo (esquemática)
beta = 0.2       # AJUSTAR: posición del arco como fracción de L desde el puente
                 # (exagerada respecto de un violín real, para que se vea)

def envolvente(x):
    """Parábola que la esquina recorre (la silueta que el ojo ve borrosa)."""
    return 4 * h * x * (L - x) / L**2

# Fases del período elegidas para mostrar 2 instantes de deslizamiento
# (esquina en el lado del puente) y 4 de agarre.
fases = [0.05, 0.20, 0.40, 0.60, 0.80, 0.95]

fig, axs = plt.subplots(3, 2, constrained_layout=True)
xx = np.linspace(0, L, 200)

for i, (ax, ph) in enumerate(zip(axs.ravel(), fases)):
    # envolvente (dibujada tenue, como referencia)
    ax.plot(xx, envolvente(xx), ':', color=COLORES['gris'], lw=1.0)
    ax.plot(xx, -envolvente(xx), ':', color=COLORES['gris'], lw=1.0)

    # posición de la esquina: ida por arriba, vuelta por abajo
    if ph <= 0.5:
        xc, signo, dirx = 2 * L * ph, +1, +1
    else:
        xc, signo, dirx = 2 * L * (1 - ph), -1, -1
    yc = signo * envolvente(xc)

    # la cuerda: dos segmentos rectos unidos en la esquina
    ax.plot([0, xc, L], [0, yc, 0], '-', color=COLORES['acento'], lw=2.0,
            solid_capstyle='round')
    ax.plot([xc], [yc], 'o', color=COLORES['tinta'], ms=4)

    # flecha corta: dirección de viaje de la esquina
    ax.annotate('', xy=(xc + 0.09 * dirx, yc), xytext=(xc, yc),
                arrowprops=dict(arrowstyle='-|>', color=COLORES['tinta'],
                                lw=1.0))

    # el punto de contacto con el arco
    xb = beta * L
    yb = np.interp(xb, [0, xc, L], [0, yc, 0]) if xc > 0 else 0.0
    ax.plot([xb], [yb], 'o', color=COLORES['azul'], ms=5, zorder=5)
    ax.plot([xb, xb], [-1.55, -1.25], '-', color=COLORES['azul'], lw=2.5)

    # ¿la cuerda va pegada al arco o deslizando?
    desliza = (ph < beta / 2) or (ph > 1 - beta / 2)
    estado = 'desliza' if desliza else 'pegada al arco'
    color_e = COLORES['acento'] if desliza else COLORES['azul']
    ax.text(0.98, 0.94, estado, transform=ax.transAxes, ha='right',
            va='top', fontsize=9, color=color_e, style='italic')
    ax.text(0.02, 0.94, f'$t = {ph:.2f}\\,T$'.replace('.', ','),
            transform=ax.transAxes, ha='left', va='top', fontsize=9,
            color=COLORES['tinta'])

    # rótulos de extremos y del arco, solo en el primer panel
    if i == 0:
        ax.text(0, -1.75, 'puente', ha='center', va='top', fontsize=8.5,
                color=COLORES['gris'])
        ax.text(L, -1.75, 'dedo', ha='center', va='top', fontsize=8.5,
                color=COLORES['gris'])
        ax.text(xb, -1.62, 'arco', ha='center', va='top', fontsize=8.5,
                color=COLORES['azul'])

    ax.set_xlim(-0.06, L + 0.06)
    ax.set_ylim(-2.4, 1.6)
    ax.axis('off')

guardar(fig, 's11_helmholtz_esquina', ancho=6.6, alto=4.6)

# ----------------------------------------------------------------------
# Figura 2: el ciclo pegar-soltar, visto desde el arco y desde el puente
# ----------------------------------------------------------------------
t = np.linspace(0, 3, 3000)
frac = t % 1.0

# desplazamiento del punto frotado: sube lento pegado al arco una
# fracción (1-beta) del período, cae rápido (desliza) la fracción beta
stick = 1 - beta
despl = np.where(frac < stick,
                 -0.5 + frac / stick,
                 0.5 - (frac - stick) / beta)

# fuerza sobre el puente: diente de sierra; la caída brusca ocurre
# cuando la esquina pasa por el puente (centro de la ventana de
# deslizamiento del punto frotado)
frac_p = (t + beta / 2) % 1.0
fuerza = frac_p - 0.5

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, constrained_layout=True)

ax1.plot(t, despl, color=COLORES['azul'])
ax1.axhline(0, color=COLORES['gris'], lw=0.7, ls=':')
ax1.set_ylabel('despl. del punto\nfrotado (esquem.)')
ax1.set_yticks([])
ax1.annotate('pegada: viaja con el arco\n(pendiente = velocidad del arco)',
             xy=(1.30, 0.05), xytext=(1.52, 0.42), fontsize=8.5,
             color=COLORES['tinta'],
             arrowprops=dict(arrowstyle='->', color=COLORES['gris'], lw=0.9))
ax1.annotate('desliza\n(rápida, en contra)', xy=(0.86, 0.0),
             xytext=(0.16, -0.52), fontsize=8.5, color=COLORES['tinta'],
             arrowprops=dict(arrowstyle='->', color=COLORES['gris'], lw=0.9))
ax1.set_ylim(-0.95, 0.95)

ax2.plot(t, fuerza, color=COLORES['acento'])
ax2.set_ylabel('fuerza sobre el\npuente (esquem.)')
ax2.set_yticks([])
ax2.annotate('la esquina pasa\npor el puente', xy=(1.90, -0.42),
             xytext=(2.12, 0.30), fontsize=8.5, color=COLORES['tinta'],
             arrowprops=dict(arrowstyle='->', color=COLORES['gris'], lw=0.9))
# marca del período entre dos caídas consecutivas
y_T = -0.78
ax2.annotate('', xy=(0.90, y_T), xytext=(1.90, y_T),
             arrowprops=dict(arrowstyle='<->', color=COLORES['tinta'],
                             lw=0.9))
ax2.text(1.40, y_T - 0.06, '$T = 1/f_1$', ha='center', va='top',
         fontsize=9.5, color=COLORES['tinta'])
ax2.set_ylim(-1.05, 0.75)
ax2.set_xlabel('tiempo (en períodos $T = 1/f_1$ de la cuerda)')
ax2.set_xticks([0, 1, 2, 3])

guardar(fig, 's11_stick_slip', ancho=6.6, alto=4.0)

print('Listo: figuras de s11.')
