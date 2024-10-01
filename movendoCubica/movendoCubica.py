import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Linear interpolation between two points
def lerpPoint(P0, P1, t):
    x = (1 - t) * P0[0] + t * P1[0]
    y = (1 - t) * P0[1] + t * P1[1]
    return x, y

def bezierCube(P0, P1, P2, P3, t):
    # Interpolação linear entre P0, P1, P2, P3
    x1, y1 = lerpPoint(P0, P1, t)  # Ponto entre P0 e P1
    x2, y2 = lerpPoint(P1, P2, t)  # Ponto entre P1 e P2
    x3, y3 = lerpPoint(P2, P3, t)  # Ponto entre P2 e P3

    # Interpolação linear entre os pontos intermediários
    x4, y4 = lerpPoint([x1, y1], [x2, y2], t)  # Ponto entre (P0->P1) e (P1->P2)
    x5, y5 = lerpPoint([x2, y2], [x3, y3], t)  # Ponto entre (P1->P2) e (P2->P3)

    # Interpolação final para o ponto da curva
    return lerpPoint([x4, y4], [x5, y5], t)  # Ponto final da curva

# Pontos de controle iniciais
P = np.array([[-8, -2], [-3, 2], [3, 2], [8, -2]])

# Novos pontos de controle para onde os pontos vão se mover
P_mov1 = np.array([[-8, -2], [-3, 2], [1, -3], [8, -2]])
P_mov2 = np.array([[-2, -2], [9, 2], [-9, 2], [2, -2]])

# Função de animação para interpolar entre dois conjuntos de pontos
def animate_movement(P_start, P_end, filename):
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.set_facecolor('none')
    fig.set_facecolor("green")
    ax.grid(color='white', linewidth=0.5, alpha=0.3)

    # Definir os limites dos eixos para garantir que os pontos não saiam da tela
    ax.set_xlim(-10, 10)  # Ajuste conforme necessário
    ax.set_ylim(-4, 3)    # Ajuste conforme necessário

    # Remover os eixos
    ax.set_axis_off()

    # Scatter dos pontos de controle iniciais
    control_points = ax.scatter(P_start[:, 0], P_start[:, 1], facecolors="#B4BFFF", edgecolors="#7085FF", linewidths=2, s=400, zorder=1)

    # Inicializar a linha da curva de Bézier
    bezier_curve, = ax.plot([], [], color='#FF70C6', lw=5, solid_capstyle='round', zorder=4)

    line_1, = ax.plot([], [], color='#7085FF', lw=2, zorder=0)
    line_2, = ax.plot([], [], color='#7085FF', lw=2, zorder=0)

    # Função de atualização para a animação
    def update(frame):
        t = frame / 100  # Para interpolar entre os dois conjuntos de pontos

        # Interpolação dos pontos de controle de P_start para P_end
        P_interp = (1 - t) * P_start + t * P_end

        # Atualizar os dados dos pontos de controle
        control_points.set_offsets(P_interp)

        # Calcular os pontos da curva de Bézier para cada valor de t
        bezier_x = []
        bezier_y = []
        t_values = np.linspace(0, 1, 500)
        for t_b in t_values:
            x, y = bezierCube(P_interp[0], P_interp[1], P_interp[2], P_interp[3], t_b)
            bezier_x.append(x)
            bezier_y.append(y)

        # Atualizar a curva de Bézier
        bezier_curve.set_data(bezier_x, bezier_y)

        line_1.set_data([P_interp[0, 0], P_interp[1, 0]], [P_interp[0, 1], P_interp[1, 1]])
        line_2.set_data([P_interp[2, 0], P_interp[3, 0]], [P_interp[2, 1], P_interp[3, 1]])

        return control_points, bezier_curve, line_1, line_2

    # Criar a animação
    ani = FuncAnimation(fig, update, frames=101, blit=True, interval=30)

    # Salvar a animação como mp4
    ani.save(filename, writer="ffmpeg")

    plt.show()

# Animação de P para P_mov1
animate_movement(P, P_mov1, "movendoCubica/P_to_P_mov1.mp4")

# Animação de P_mov1 para P_mov2
animate_movement(P_mov1, P_mov2, "movendoCubica/P_mov1_to_P_mov2.mp4")

# Animação de P_mov1 para P_mov2
animate_movement(P_mov2, P, "movendoCubica/P_mov2_to_P.mp4")
