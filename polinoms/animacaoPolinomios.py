import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definir as funções p1, p2, p3, p4
def p1(t):
    return -pow(t, 3) + 3 * pow(t, 2) - 3 * t + 1

def p2(t):
    return 3 * pow(t, 3) - 6 * pow(t, 2) + 3 * t

def p3(t):
    return -3 * pow(t, 3) + 3 * pow(t, 2)

def p4(t):
    return pow(t, 3)

# Criar uma série de valores para t (intervalo de 0 a 1)
t_values = np.linspace(0, 1, 5000)

# Calcular os valores das funções p1, p2, p3, p4
p1_values = p1(t_values)
p2_values = p2(t_values)
p3_values = p3(t_values)
p4_values = p4(t_values)

# Configurar o gráfico com fundo preto e grid branco
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
ax.set_facecolor('none')  # Cor de fundo preto
fig.patch.set_alpha(0)  # Cor de fundo preto
ax.grid(color='white', linewidth=0.5, alpha=0.3)  # Grid branco

# Plotar cada função
ax.plot(t_values, p1_values, color='#c9144f', lw=4, solid_capstyle='round')
ax.plot(t_values, p2_values, color='#38c2ff', lw=4, solid_capstyle='round')
ax.plot(t_values, p3_values, color='#18fbb6', lw=4, solid_capstyle='round')
ax.plot(t_values, p4_values, color='#d0c060', lw=4, solid_capstyle='round')

# Inicializar os pontos deslizantes com bordas mais grossas
point_p1, = ax.plot([], [], 'o', markerfacecolor='black', markeredgecolor='#c9144f', markersize=15, markeredgewidth=3)  # Aumentar espessura da borda
point_p2, = ax.plot([], [], 'o', markerfacecolor='black', markeredgecolor='#38c2ff', markersize=15, markeredgewidth=3)  # Aumentar espessura da borda
point_p3, = ax.plot([], [], 'o', markerfacecolor='black', markeredgecolor='#18fbb6', markersize=15, markeredgewidth=3)  # Aumentar espessura da borda
point_p4, = ax.plot([], [], 'o', markerfacecolor='black', markeredgecolor='#d0c060', markersize=15, markeredgewidth=3)  # Aumentar espessura da borda

# Inicializar as linhas verticais "infinitas"
line, = ax.plot([], [], color='white', lw=0.5, linestyle='--')

# Função de atualização da animação
def update(frame):
    # Calcular os valores atuais dos pontos para cada função
    t = t_values[frame]
    point_p1.set_data([t], [p1(t)])
    point_p2.set_data([t], [p2(t)])
    point_p3.set_data([t], [p3(t)])
    point_p4.set_data([t], [p4(t)])

    # Desenhar linhas verticais "infinitas"
    line.set_data([t, t], [ax.get_ylim()[0], ax.get_ylim()[1]])
    
    return point_p1, point_p2, point_p3, point_p4, line

# Criar a animação
ani = FuncAnimation(
    fig, 
    update, 
    frames=5000, 
    blit=True, 
    interval=30
)

ani.save("polinoms.mp4")

# Ajustar as cores dos ticks
ax.tick_params(colors='none')

# Exibir o gráfico
plt.show()
