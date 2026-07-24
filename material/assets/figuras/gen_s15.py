"""Figura de la sesión 15 — Cómo defender un proyecto acústico.

Genera:
  s15_cadena_defensa.svg — la columna vertebral de una explicación:
                           fenómeno → modelo → predicción → medición →
                           desviación → explicación

Ejecutar desde figuras/:  python3 gen_s15.py
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from estilo_figuras import aplicar_estilo, COLORES, guardar

aplicar_estilo()

# las seis estaciones de la cadena, con su recordatorio en una línea
estaciones = [
    ('fenómeno', 'qué se oye, con el\nvocabulario del curso'),
    ('modelo', 'cuerda, tubo,\nmembrana, resonador'),
    ('predicción', 'la del hito 1,\ntal como se escribió'),
    ('medición', 'el número, con\nunidades y condiciones'),
    ('desviación', 'cuánto y en\nqué dirección'),
    ('explicación', 'el mecanismo,\nen proporciones'),
]

fig, ax = plt.subplots(constrained_layout=True)
ax.set_xlim(0, 12.4)
ax.set_ylim(0, 2.6)
ax.axis('off')

W, H, paso = 1.78, 1.30, 2.06   # geometría de las cajas
for i, (titulo, sub) in enumerate(estaciones):
    cx = 0.95 + i * paso
    # la desviación y su explicación son el corazón de la defensa:
    # se destacan con el borde en color de acento
    borde = COLORES['acento'] if i >= 4 else COLORES['tinta']
    ax.add_patch(FancyBboxPatch((cx - W / 2, 1.3 - H / 2), W, H,
                                boxstyle='round,pad=0.08',
                                fc=COLORES['panel'], ec=borde, lw=1.2))
    ax.text(cx, 1.62, titulo, ha='center', va='center', fontsize=10,
            fontweight='bold', color=COLORES['tinta'])
    ax.text(cx, 1.08, sub, ha='center', va='center', fontsize=7.3,
            color=COLORES['gris'], linespacing=1.35)
    if i < len(estaciones) - 1:
        ax.annotate('', xy=(cx + paso - W / 2 - 0.10, 1.3),
                    xytext=(cx + W / 2 + 0.10, 1.3),
                    arrowprops=dict(arrowstyle='-|>', lw=1.4,
                                    color=COLORES['tinta']))

guardar(fig, 's15_cadena_defensa', ancho=8.6, alto=1.9)

print('Listo: figura de s15.')
