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
def plot_first_derivative(P_prime):
    t_values = np.linspace(0, 1, 100)
    first_derivative_x = []
    first_derivative_y = []

    for t in t_values:
        x, y = quadratic_bezier(P_prime[0], P_prime[1], P_prime[2], t)
        first_derivative_x.append(x)
        first_derivative_y.append(y)

    ax1.plot(first_derivative_x, first_derivative_y, color='#A6FF70', lw=4, solid_capstyle='round')

# Static plot for the second derivative Bézier curve
def plot_second_derivative(P_double_prime):
    t_values = np.linspace(0, 1, 100)
    second_derivative_x = []
    second_derivative_y = []

    for t in t_values:
        x, y = lerpPoint(P_double_prime[0], P_double_prime[1], t)
        second_derivative_x.append(x)
        second_derivative_y.append(y)

    ax2.plot(second_derivative_x, second_derivative_y, color='#5CE1E6', lw=4, solid_capstyle='round')

# Initialize the figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.grid(True)
ax2.grid(True)

# Set axis labels and titles
ax1.set_title("First Derivative Bézier Curve")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax2.set_title("Second Derivative Bézier Curve")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

# Define control points for the original Bézier curve
P = np.array([[-3, -3.5], [3.5, -2], [3, 4], [-2, 3]])

# Compute control points for the first and second derivative Bézier curves
P_prime = first_derivative_control_points(P)
P_double_prime = second_derivative_control_points(P_prime)

# Initialize quivers (arrows) for both plots
arrow_first_derivative = ax1.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='#A6FF70', width=0.01)
arrow_second_derivative = ax2.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='#5CE1E6', width=0.01)

# Set fixed axis limits to ensure the arrows stay within the visible range
ax1.set_xlim(-20, 20)  # Adjust these values based on your Bézier curve range
ax1.set_ylim(-20, 20)
ax2.set_xlim(-50, 50)
ax2.set_ylim(-50, 50)

P_prime = first_derivative_control_points(P)
P_double_prime = second_derivative_control_points(P_prime)

# Plot the first derivative Bézier curve
plot_first_derivative(P_prime)

# Plot the second derivative Bézier curve
plot_second_derivative(P_double_prime)

# Function to update the arrow positions in the animation
def update(t):
    # First derivative Bézier point (quadratic Bézier)
    x_prime, y_prime = quadratic_bezier(P_prime[0], P_prime[1], P_prime[2], t)

    # Update first derivative arrow
    arrow_first_derivative.set_UVC(x_prime, y_prime)

    # Second derivative Bézier point (linear Bézier)
    x_double_prime, y_double_prime = lerpPoint(P_double_prime[0], P_double_prime[1], t)

    # Update second derivative arrow
    arrow_second_derivative.set_UVC(x_double_prime, y_double_prime)

    return arrow_first_derivative, arrow_second_derivative

# Create the animation
anim = FuncAnimation(fig, update, frames=np.linspace(0, 1, 200), interval=50, blit=True)

# Show the animation
plt.show()
