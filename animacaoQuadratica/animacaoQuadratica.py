import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.animation import FuncAnimation

def lerpPoint(P0, P1, t):
    x = (1 - t) * P0[0] + t * P1[0]
    y = (1 - t) * P0[1] + t * P1[1]
    return x, y

x = [-2, 0, 2]
y = [-1, 3, -1]

P = np.array([[-2, -1], [0, 3], [2, -1]])

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
ax.set_facecolor('none')
fig.set_facecolor("green")
ax.grid(color='white', linewidth=0.5, alpha=0.3)

# Remove the axes
ax.set_axis_off()

ax.plot([x[0], x[1]], [y[0], y[1]], color="#7085FF", lw=2, solid_capstyle='round', zorder=0)
ax.plot([x[1], x[2]], [y[1], y[2]], color="#7085FF", lw=2, solid_capstyle='round', zorder=0)

ax.scatter(x, y, facecolors="#B4BFFF", edgecolors="#7085FF", linewidths=2, s=400, zorder=1)

# Save the figure before displaying
plt.savefig("animacaoQuadratica/points_no_axes.png", transparent=True)

moving_point_1, = ax.plot([], [], 'o', color='red',  markerfacecolor='#B4BFFF', markeredgecolor='#7085FF', markersize=15, markeredgewidth=3, zorder=2)
moving_point_2, = ax.plot([], [], 'o', color='blue',  markerfacecolor='#B4BFFF', markeredgecolor='#7085FF', markersize=15, markeredgewidth=3, zorder=2)
bezier_point, = ax.plot([], [], 'o', color='blue',  markerfacecolor='#FFDAF4', markeredgecolor='#FF70C6', markersize=15, markeredgewidth=3, zorder=4)

line_1, = ax.plot([], [], color='#7085FF', lw=2, zorder=0)

def update(t):
    x1, y1 = lerpPoint(P[0], P[1], t)
    x2, y2 = lerpPoint(P[1], P[2], t)
    x3, y3 = lerpPoint([x1, y1], [x2, y2], t)

    moving_point_1.set_data([x1], [y1])
    moving_point_2.set_data([x2], [y2])
    bezier_point.set_data([x3], [y3])

    line_1.set_data([x1, x2], [y1, y2])

    return moving_point_1, moving_point_2, bezier_point, line_1

ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 500), blit=True, interval=30)

ani.save("animacaoQuadratica/bezierPonto_Quadratica.mp4", writer="ffmpeg")

# Inicializar a linha da curva de Bézier
bezier_curve, = ax.plot([], [], color='#FF70C6', lw=5, solid_capstyle='round', zorder=3)

# Armazenar as coordenadas da curva
bezier_x = []
bezier_y = []

def bezier(t):
    global bezier_x_data, bezier_y_data
    
    # Reinicializar as coordenadas da curva quando a animação recomeça
    if t == 0:
        bezier_x_data = []
        bezier_y_data = []

    x1, y1 = lerpPoint(P[0], P[1], t)
    x2, y2 = lerpPoint(P[1], P[2], t)
    x3, y3 = lerpPoint([x1, y1], [x2, y2], t)
    
    moving_point_1.set_data([x1], [y1])
    moving_point_2.set_data([x2], [y2])
    bezier_point.set_data([x3], [y3])

    line_1.set_data([x1, x2], [y1, y2])

    bezier_x.append(x3)
    bezier_y.append(y3)
    bezier_curve.set_data(bezier_x, bezier_y)

    return moving_point_1, moving_point_2, bezier_point, line_1, bezier_curve

bezier_anim = FuncAnimation(fig, bezier, frames=np.linspace(0, 1, 500), blit=True, interval=30)

bezier_anim.save("animacaoQuadratica/bezier.mp4", writer="ffmpeg")


plt.show()