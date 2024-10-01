import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Linear interpolation between two points
def lerpPoint(P0, P1, t):
    x = (1 - t) * P0[0] + t * P1[0]
    y = (1 - t) * P0[1] + t * P1[1]
    return x, y

# First derivative of the cubic Bézier curve
def bezierFirstDerivative(P0, P1, P2, P3, t):
    x = -3 * (1 - t)**2 * P0[0] + 3 * ((1 - t)**2 - 2 * (1 - t) * t) * P1[0] + \
        3 * (2 * (1 - t) * t - t**2) * P2[0] + 3 * t**2 * P3[0]
    
    y = -3 * (1 - t)**2 * P0[1] + 3 * ((1 - t)**2 - 2 * (1 - t) * t) * P1[1] + \
        3 * (2 * (1 - t) * t - t**2) * P2[1] + 3 * t**2 * P3[1]

    return x, y

# Second derivative of the cubic Bézier curve
def bezierSecondDerivative(P0, P1, P2, P3, t):
    x = 6 * (1 - t) * P0[0] + 6 * (-2 * (1 - t) + t) * P1[0] + \
        6 * (2 * (1 - t) - 2 * t) * P2[0] + 6 * t * P3[0]
    
    y = 6 * (1 - t) * P0[1] + 6 * (-2 * (1 - t) + t) * P1[1] + \
        6 * (2 * (1 - t) - 2 * t) * P2[1] + 6 * t * P3[1]

    return x, y

# Define control points
P = np.array([[-3, -3.5], [3.5, -2], [3, 4], [-2, 3]])

fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
ax.set_facecolor('green')
fig.set_facecolor("green")
ax.grid(color='white', linewidth=0.5, alpha=0.3)
ax.spines['top'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.tick_params(colors='white')

# Plot control points and lines
ax.plot([P[0,0], P[1,0]], [P[0,1], P[1,1]], color="#7085FF", lw=2, solid_capstyle='round', zorder=0)
ax.plot([P[2,0], P[3,0]], [P[2,1], P[3,1]], color="#7085FF", lw=2, solid_capstyle='round', zorder=0)

ax.scatter(P[:, 0], P[:, 1], facecolors="#B4BFFF", edgecolors="#7085FF", linewidths=2, s=400, zorder=1)

# Bézier point and curve initialization
bezier_point, = ax.plot([], [], 'o', markerfacecolor='#FFDAF4', markeredgecolor='#FF70C6', markersize=15, markeredgewidth=3, zorder=5)
bezier_curve, = ax.plot([], [], color='#FF70C6', lw=5, solid_capstyle='round', zorder=4)

# Initialize Bézier curve coordinates
bezier_x = []
bezier_y = []

# Initialize quivers (arrows)
first_deriv_quiver = None
second_deriv_quiver = None

# Scaling factor for the arrows
arrow_scale = 20  # Adjust this value to control arrow length

def bezier(t):
    global bezier_x, bezier_y, first_deriv_quiver, second_deriv_quiver
    
    # Reset the Bézier curve when animation restarts
    if t == 0:
        bezier_x = []
        bezier_y = []

    # Compute intermediate Bézier points
    x1, y1 = lerpPoint(P[0], P[1], t)
    x2, y2 = lerpPoint(P[1], P[2], t)
    x3, y3 = lerpPoint(P[2], P[3], t)
    x4, y4 = lerpPoint([x1, y1], [x2, y2], t)
    x5, y5 = lerpPoint([x2, y2], [x3, y3], t)
    x6, y6 = lerpPoint([x4, y4], [x5, y5], t)

    # Update Bézier point
    bezier_point.set_data([x6], [y6])

    # Append to the Bézier curve
    bezier_x.append(x6)
    bezier_y.append(y6)
    bezier_curve.set_data(bezier_x, bezier_y)

    # Compute first and second derivatives
    first_derivative = bezierFirstDerivative(P[0], P[1], P[2], P[3], t)
    second_derivative = bezierSecondDerivative(P[0], P[1], P[2], P[3], t)

    # Remove previous quivers
    if first_deriv_quiver:
        first_deriv_quiver.remove()
    if second_deriv_quiver:
        second_deriv_quiver.remove()

    # Draw the quivers (arrows), scaled down by the arrow_scale factor
    first_deriv_quiver = ax.quiver(x6, y6, first_derivative[0] / arrow_scale, first_derivative[1] / arrow_scale,
                                   angles='xy', scale_units='xy', scale=1, color='#A6FF70', zorder=3, width=0.005)
    second_deriv_quiver = ax.quiver(x6, y6, second_derivative[0] / arrow_scale, second_derivative[1] / arrow_scale,
                                    angles='xy', scale_units='xy', scale=1, color='#5CE1E6', zorder=3, width=0.005)

    return bezier_point, bezier_curve, first_deriv_quiver, second_deriv_quiver

# Create animation
bezier_anim = FuncAnimation(fig, bezier, frames=np.linspace(0, 1, 300), blit=True, interval=30)

bezier_anim.save("animacaoDerivs/derivVectors.mp4", writer="ffmpeg")

# Show animation
plt.show()
