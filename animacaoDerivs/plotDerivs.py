import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Linear interpolation between two points
def lerpPoint(P0, P1, t):
    x = (1 - t) * P0[0] + t * P1[0]
    y = (1 - t) * P0[1] + t * P1[1]
    return x, y

# Function to compute the control points for the first derivative Bézier curve
def first_derivative_control_points(P):
    P_prime = np.zeros((3, 2))
    P_prime[0] = 3 * (P[1] - P[0])
    P_prime[1] = 3 * (P[2] - P[1])
    P_prime[2] = 3 * (P[3] - P[2])
    return P_prime

# Function to compute the control points for the second derivative Bézier curve
def second_derivative_control_points(P_prime):
    P_double_prime = np.zeros((2, 2))
    P_double_prime[0] = 2 * (P_prime[1] - P_prime[0])
    P_double_prime[1] = 2 * (P_prime[2] - P_prime[1])
    return P_double_prime

# Bézier curve function for quadratic curves
def quadratic_bezier(P0, P1, P2, t):
    x1, y1 = lerpPoint(P0, P1, t)
    x2, y2 = lerpPoint(P1, P2, t)
    x3, y3 = lerpPoint([x1, y1], [x2, y2], t)
    return x3, y3

# Static plot for the first derivative Bézier curve
def plot_first_derivative(P_prime, ax):
    t_values = np.linspace(0, 1, 100)
    first_derivative_x = []
    first_derivative_y = []

    for t in t_values:
        x, y = quadratic_bezier(P_prime[0], P_prime[1], P_prime[2], t)
        first_derivative_x.append(x)
        first_derivative_y.append(y)

    ax.plot(first_derivative_x, first_derivative_y, color='#A6FF70', lw=4, solid_capstyle='round')

# Static plot for the second derivative Bézier curve
def plot_second_derivative(P_double_prime, ax):
    t_values = np.linspace(0, 1, 100)
    second_derivative_x = []
    second_derivative_y = []

    for t in t_values:
        x, y = lerpPoint(P_double_prime[0], P_double_prime[1], t)
        second_derivative_x.append(x)
        second_derivative_y.append(y)

    ax.plot(second_derivative_x, second_derivative_y, color='#5CE1E6', lw=4, solid_capstyle='round')

# Function to animate first derivative Bézier curve
def animate_first_derivative(t, P_prime, ax, arrow):
    # First derivative Bézier point (quadratic Bézier)
    x_prime, y_prime = quadratic_bezier(P_prime[0], P_prime[1], P_prime[2], t)
    arrow.set_UVC(x_prime, y_prime)
    return arrow,

# Function to animate second derivative Bézier curve
def animate_second_derivative(t, P_double_prime, ax, arrow):
    # Second derivative Bézier point (linear Bézier)
    x_double_prime, y_double_prime = lerpPoint(P_double_prime[0], P_double_prime[1], t)
    arrow.set_UVC(x_double_prime, y_double_prime)
    return arrow,

# Prepare and save first derivative animation
def save_first_derivative_animation(P_prime):
    fig, ax1 = plt.subplots(figsize=(6, 6))
    fig.set_facecolor('green')
    ax1.set_facecolor('green')
    ax1.grid(color='white', linewidth=0.5, alpha=0.3)
    ax1.spines['top'].set_color('white')
    ax1.spines['bottom'].set_color('white')
    ax1.spines['left'].set_color('white')
    ax1.spines['right'].set_color('white')
    ax1.tick_params(colors='white')
    ax1.set_xlim(-20, 20)
    ax1.set_ylim(-20, 20)

    plot_first_derivative(P_prime, ax1)

    arrow_first_derivative = ax1.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='#A6FF70', width=0.01)

    anim1 = FuncAnimation(fig, animate_first_derivative, fargs=(P_prime, ax1, arrow_first_derivative), frames=np.linspace(0, 1, 300), interval=30, blit=True)

    anim1.save("animacaoDerivs/first_derivative_animation.mp4", writer='ffmpeg', dpi=300)

# Prepare and save second derivative animation
def save_second_derivative_animation(P_double_prime):
    fig, ax2 = plt.subplots(figsize=(6, 6))
    fig.set_facecolor('green')
    ax2.set_facecolor('green')
    ax2.grid(color='white', linewidth=0.5, alpha=0.3)
    ax2.spines['top'].set_color('white')
    ax2.spines['bottom'].set_color('white')
    ax2.spines['left'].set_color('white')
    ax2.spines['right'].set_color('white')
    ax2.tick_params(colors='white')
    ax2.set_xlim(-50, 50)
    ax2.set_ylim(-50, 50)

    plot_second_derivative(P_double_prime, ax2)

    arrow_second_derivative = ax2.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='#5CE1E6', width=0.01)

    anim2 = FuncAnimation(fig, animate_second_derivative, fargs=(P_double_prime, ax2, arrow_second_derivative), frames=np.linspace(0, 1, 300), interval=30, blit=True)

    anim2.save("animacaoDerivs/second_derivative_animation.mp4", writer='ffmpeg', dpi=300)

# Define control points for the original Bézier curve
P = np.array([[-3, -3.5], [3.5, -2], [3, 4], [-2, 3]])

# Compute control points for the first and second derivative Bézier curves
P_prime = first_derivative_control_points(P)
P_double_prime = second_derivative_control_points(P_prime)

# Save both animations
save_first_derivative_animation(P_prime)
save_second_derivative_animation(P_double_prime)
