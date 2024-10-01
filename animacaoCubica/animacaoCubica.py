import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.animation import FuncAnimation

def lerpPoint(P0, P1, t):
    x = (1 - t) * P0[0] + t * P1[0]
    y = (1 - t) * P0[1] + t * P1[1]
    return x, y

P = np.array([[-8, -2], [-3, 2], [3, 2], [8, -2]])

fig, ax = plt.subplots(figsize=(10, 5), dpi=500)
ax.set_facecolor('green')
fig.set_facecolor("green")
ax.grid(color='white', linewidth=0.5, alpha=0.3)

# Remove the axes
ax.set_axis_off()

ax.plot([P[0,0], P[1,0]], [P[0,1], P[1,1]], color="#7085FF", lw=2, solid_capstyle='round', zorder=0)
ax.plot([P[1,0], P[2,0]], [P[1,1], P[2,1]], color="#7085FF", lw=2, solid_capstyle='round', zorder=0)
ax.plot([P[2,0], P[3,0]], [P[2,1], P[3,1]], color="#7085FF", lw=2, solid_capstyle='round', zorder=0)

ax.scatter(P[:, 0], P[:, 1], facecolors="#B4BFFF", edgecolors="#7085FF", linewidths=2, s=400, zorder=1)

# Save the figure before displaying
plt.savefig("animacaoCubica/points_no_axes.png", transparent=True)

moving_point_1, = ax.plot([], [], 'o', markerfacecolor='#B4BFFF', markeredgecolor='#7085FF', markersize=15, markeredgewidth=3, zorder=1)
moving_point_2, = ax.plot([], [], 'o', markerfacecolor='#B4BFFF', markeredgecolor='#7085FF', markersize=15, markeredgewidth=3, zorder=1)
moving_point_3, = ax.plot([], [], 'o', markerfacecolor='#B4BFFF', markeredgecolor='#7085FF', markersize=15, markeredgewidth=3, zorder=1)
moving_point_4, = ax.plot([], [], 'o', markerfacecolor='#B4BFFF', markeredgecolor='#7085FF', markersize=15, markeredgewidth=3, zorder=1)
moving_point_5, = ax.plot([], [], 'o', markerfacecolor='#B4BFFF', markeredgecolor='#7085FF', markersize=15, markeredgewidth=3, zorder=1)
bezier_point, = ax.plot([], [], 'o',  markerfacecolor='#FFDAF4', markeredgecolor='#FF70C6', markersize=15, markeredgewidth=3, zorder=5)

line_1, = ax.plot([], [], color='#7085FF', lw=2, zorder=0)
line_2, = ax.plot([], [], color='#7085FF', lw=2, zorder=0)
line_3, = ax.plot([], [], color='#7085FF', lw=2, zorder=0)

# Inicializar a linha da curva de Bézier
bezier_curve, = ax.plot([], [], color='#FF70C6', lw=5, solid_capstyle='round', zorder=4)

# Armazenar as coordenadas da curva
bezier_x = []
bezier_y = []

def bezier(t):
    global bezier_x, bezier_y
    
    # Reinicializar as coordenadas da curva quando a animação recomeça
    if t == 0:
        bezier_x = []
        bezier_y = []

    x1, y1 = lerpPoint(P[0], P[1], t)
    x2, y2 = lerpPoint(P[1], P[2], t)
    x3, y3 = lerpPoint(P[2], P[3], t)
    x4, y4 = lerpPoint([x1, y1], [x2, y2], t)
    x5, y5 = lerpPoint([x2, y2], [x3, y3], t)
    x6, y6 = lerpPoint([x4, y4], [x5, y5], t)
    
    moving_point_1.set_data([x1], [y1])
    moving_point_2.set_data([x2], [y2])
    moving_point_3.set_data([x3], [y3])
    moving_point_4.set_data([x4], [y4])
    moving_point_5.set_data([x5], [y5])
    bezier_point.set_data([x6], [y6])

    line_1.set_data([x1, x2], [y1, y2])
    line_2.set_data([x2, x3], [y2, y3])
    line_3.set_data([x4, x5], [y4, y5])

    bezier_x.append(x6)
    bezier_y.append(y6)
    bezier_curve.set_data(bezier_x, bezier_y)

    return moving_point_1, moving_point_2, moving_point_3, moving_point_4, moving_point_5, bezier_point, line_1, line_2, line_3, bezier_curve

bezier_anim = FuncAnimation(fig, bezier, frames=np.linspace(0, 1, 200), blit=True, interval=30)

bezier_anim.save("animacaoCubica/bezierCubica.mp4", writer="ffmpeg")


plt.show()