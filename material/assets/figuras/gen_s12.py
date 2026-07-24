"""Figuras de la sesión 12 — Vientos y lutería.

Genera:
  s12_modos_tubos.svg        — modos de presión (y velocidad) de un tubo
                               abierto-abierto vs. cerrado-abierto
  s12_agujero_tubo.svg       — un agujero abierto acorta el tubo efectivo
  s12_correccion_extremo.svg — la columna sobresale del extremo abierto

Ejecutar desde figuras/:  python3 gen_s12.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()

# ----------------------------------------------------------------------
# Figura 1: modos de un tubo abierto-abierto vs. cerrado-abierto
# Se dibuja la AMPLITUD de la onda estacionaria de presión (±envolvente);
# la velocidad (punteada, solo en la primera fila) es complementaria.
# ----------------------------------------------------------------------
L = 1.0
xx = np.linspace(0, L, 300)

fig, axs = plt.subplots(3, 2, sharex=True, constrained_layout=True)

# etiquetas de frecuencia de cada fila
et_abierto = ['$f_1 = v/2L$', '$2f_1$', '$3f_1$']
et_cerrado = ['$f_1 = v/4L$', '$3f_1$', '$5f_1$']

for fila in range(3):
    # --- columna 0: abierto-abierto ------------------------------------
    ax = axs[fila, 0]
    n = fila + 1
    p = np.sin(n * np.pi * xx / L)              # presión: nodo en ambos extremos
    ax.fill_between(xx, p, -p, color=COLORES['panel'])
    ax.plot(xx, p, color=COLORES['acento'])
    ax.plot(xx, -p, color=COLORES['acento'], lw=1.0, alpha=0.55)
    if fila == 0:
        u = np.cos(n * np.pi * xx / L)          # velocidad: máxima en los extremos
        ax.plot(xx, u, '--', color=COLORES['azul'], lw=1.3)
        ax.plot(xx, -u, '--', color=COLORES['azul'], lw=0.9, alpha=0.5)
    ax.text(1.03, 0, et_abierto[fila], fontsize=9.5, va='center',
            color=COLORES['tinta'])

    # paredes del tubo (ambos extremos abiertos: sin tapa)
    for y in (1.25, -1.25):
        ax.plot([0, L], [y, y], color=COLORES['tinta'], lw=2.0)

    # --- columna 1: cerrado-abierto ------------------------------------
    ax = axs[fila, 1]
    m = 2 * fila + 1
    p = np.cos(m * np.pi * xx / (2 * L))        # presión: máxima en el extremo cerrado
    ax.fill_between(xx, p, -p, color=COLORES['panel'])
    ax.plot(xx, p, color=COLORES['acento'])
    ax.plot(xx, -p, color=COLORES['acento'], lw=1.0, alpha=0.55)
    if fila == 0:
        u = np.sin(m * np.pi * xx / (2 * L))    # velocidad: nula en la tapa
        ax.plot(xx, u, '--', color=COLORES['azul'], lw=1.3)
        ax.plot(xx, -u, '--', color=COLORES['azul'], lw=0.9, alpha=0.5)
    ax.text(1.03, 0, et_cerrado[fila], fontsize=9.5, va='center',
            color=COLORES['tinta'])

    for y in (1.25, -1.25):
        ax.plot([0, L], [y, y], color=COLORES['tinta'], lw=2.0)
    ax.plot([0, 0], [-1.25, 1.25], color=COLORES['tinta'], lw=3.0)  # la tapa

    for ax in axs[fila]:
        ax.set_xlim(-0.03, 1.42)
        ax.set_ylim(-1.5, 1.5)
        ax.axis('off')

axs[0, 0].set_title('abierto–abierto (flauta)', fontsize=10.5)
axs[0, 1].set_title('cerrado–abierto (tubo tapado)', fontsize=10.5)

# leyenda única para toda la figura
from matplotlib.lines import Line2D
fig.legend(handles=[
    Line2D([], [], color=COLORES['acento'], label='presión $p$ (amplitud)'),
    Line2D([], [], color=COLORES['azul'], ls='--',
           label='velocidad $u$ (complementaria)')],
    loc='outside lower center', ncol=2, fontsize=9)

guardar(fig, 's12_modos_tubos', ancho=6.8, alto=4.2)

# ----------------------------------------------------------------------
# Figura 2: un agujero abierto acorta el tubo efectivo
# ----------------------------------------------------------------------
LT = 10.0                      # largo del tubo (unidades arbitrarias)
x_ag = [6.5, 7.7, 8.9]         # AJUSTAR: posiciones de los agujeros

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, constrained_layout=True)

def dibuja_tubo(ax, abiertos):
    """Tubo abierto en ambos extremos con agujeros en la pared superior.

    abiertos: lista de índices de agujeros destapados (círculo blanco).
    """
    for y in (0.8, -0.8):
        ax.plot([0, LT], [y, y], color=COLORES['tinta'], lw=2.2)
    for i, xa in enumerate(x_ag):
        fc = COLORES['papel'] if i in abiertos else COLORES['tinta']
        ax.add_patch(Circle((xa, 0.8), 0.22, fc=fc, ec=COLORES['tinta'],
                            lw=1.4, zorder=5))
    ax.set_xlim(-0.4, LT + 0.4)
    ax.set_ylim(-1.9, 1.8)
    ax.axis('off')

# panel 1: todos los agujeros tapados — vibra el tubo entero
dibuja_tubo(ax1, abiertos=[])
xx = np.linspace(0, LT, 300)
p = 0.62 * np.sin(np.pi * xx / LT)
ax1.fill_between(xx, p, -p, color=COLORES['panel'])
ax1.plot(xx, p, color=COLORES['acento'])
ax1.plot(xx, -p, color=COLORES['acento'], lw=1.0, alpha=0.55)
ax1.text(LT / 2, 1.35, 'todos los agujeros tapados: vibra el tubo entero,  '
         '$f_1 = v/2L$', ha='center', fontsize=9.5, color=COLORES['tinta'])
ax1.annotate('', xy=(LT, -1.35), xytext=(0, -1.35),
             arrowprops=dict(arrowstyle='<->', color=COLORES['gris'], lw=0.9))
ax1.text(LT / 2, -1.52, '$L$', ha='center', va='top', fontsize=10,
         color=COLORES['gris'])

# panel 2: primer agujero destapado — el tubo "termina" ahí
dibuja_tubo(ax2, abiertos=[0])
Lef = x_ag[0]
xx2 = np.linspace(0, Lef, 300)
p2 = 0.62 * np.sin(np.pi * xx2 / Lef)
ax2.fill_between(xx2, p2, -p2, color=COLORES['panel'])
ax2.plot(xx2, p2, color=COLORES['acento'])
ax2.plot(xx2, -p2, color=COLORES['acento'], lw=1.0, alpha=0.55)
ax2.annotate('la presión se fuga:\npara la onda, el tubo termina aquí',
             xy=(Lef, 0.95), xytext=(6.9, 1.65), fontsize=8.5,
             color=COLORES['tinta'], va='center',
             arrowprops=dict(arrowstyle='->', color=COLORES['gris'], lw=0.9))
ax2.annotate('', xy=(Lef, -1.35), xytext=(0, -1.35),
             arrowprops=dict(arrowstyle='<->', color=COLORES['gris'], lw=0.9))
ax2.text(Lef / 2, -1.52, '$L_{ef} < L$   →   la nota sube', ha='center',
         va='top', fontsize=10, color=COLORES['tinta'])

guardar(fig, 's12_agujero_tubo', ancho=6.6, alto=3.6)

# ----------------------------------------------------------------------
# Figura 3: corrección de extremo — la columna sobresale del tubo
# ----------------------------------------------------------------------
LT = 10.0
dL = 0.9      # sobresaliente (exagerado para que se vea; real ≈ 0,6 r)

fig, ax = plt.subplots(constrained_layout=True)

# columna de aire que vibra: sombreada, sobresale dL del extremo abierto
# (el borde derecho es el casquete redondeado)
yyc = np.linspace(-1, 1, 200)
ax.fill_betweenx(yyc, 0, LT + dL * np.sqrt(1 - yyc**2),
                 color=COLORES['panel'])

# paredes del tubo (cerrado a la izquierda, abierto a la derecha)
for y in (1.0, -1.0):
    ax.plot([0, LT], [y, y], color=COLORES['tinta'], lw=2.4)
ax.plot([0, 0], [-1.0, 1.0], color=COLORES['tinta'], lw=3.2)   # tapa

# frontera efectiva de la columna (casquete redondeado, punteado)
tt = np.linspace(-np.pi / 2, np.pi / 2, 100)
ax.plot(LT + dL * np.cos(tt), np.sin(tt), ':', color=COLORES['azul'],
        lw=1.6)

# envolvente de presión del modo fundamental, con nodo FUERA del tubo
Lef = LT + dL
xxp = np.linspace(0, Lef, 400)
p = 0.75 * np.cos(np.pi * xxp / (2 * Lef))
ax.plot(xxp, p, color=COLORES['acento'])
ax.plot(xxp, -p, color=COLORES['acento'], lw=1.0, alpha=0.55)
ax.annotate('nodo de presión:\nqueda fuera del tubo', xy=(Lef, 0.06),
            xytext=(10.9, 1.35), fontsize=8.5, color=COLORES['tinta'],
            arrowprops=dict(arrowstyle='->', color=COLORES['gris'], lw=0.9))

# cotas: L (huincha) y L_ef = L + ΔL
ax.annotate('', xy=(LT, -1.35), xytext=(0, -1.35),
            arrowprops=dict(arrowstyle='<->', color=COLORES['gris'], lw=0.9))
ax.text(LT / 2, -1.5, '$L$ (lo que mide la huincha)', ha='center', va='top',
        fontsize=9.5, color=COLORES['gris'])
ax.annotate('', xy=(Lef, -2.05), xytext=(0, -2.05),
            arrowprops=dict(arrowstyle='<->', color=COLORES['tinta'], lw=0.9))
ax.text(Lef / 2, -2.2, '$L_{ef} = L + \\Delta L$  →  '
        '$f_1 = v/4L_{ef}$: más grave que el cálculo ingenuo',
        ha='center', va='top', fontsize=9.5, color=COLORES['tinta'])
ax.annotate('$\\Delta L \\approx 0{,}6\\,r$', xy=(LT + dL / 2, 1.0),
            xytext=(9.0, 1.75), fontsize=9.5, color=COLORES['azul'],
            ha='center',
            arrowprops=dict(arrowstyle='->', color=COLORES['azul'], lw=0.9))

ax.set_xlim(-0.5, 13.6)
ax.set_ylim(-2.9, 2.2)
ax.axis('off')

guardar(fig, 's12_correccion_extremo', ancho=6.6, alto=2.9)

print('Listo: figuras de s12.')
