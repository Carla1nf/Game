import tkinter as tk
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

x = {}
y = {}
z = {}
colores = {}

contador = 0

def main_grafico(dataT, team, colores):
    def update_graph(frame):
        nonlocal dataT, team, colores
        ax1.cla()  # Limpiar el gráfico antes de dibujar el siguiente fotograma
        ax2.cla()

        global contador
        contador += 1
        dataT = dataT[team]
        for i in dataT:
            color = colores[i]
            if contador <= 1:
                x[i] = []
                y[i] = []
                z[i] = []
            x[i].append(dataT[i]["x"])
            y[i].append(dataT[i]["y"])
            z[i].append(dataT[i]["z"])
            ax1.scatter(x[i], y[i], z[i], color=color)
            ax1.plot(x[i], y[i], z[i], color=color, label=i)
            plt.legend()

        # Actualizar los widgets de lienzo
        canvas1.draw()
        canvas2.draw()

    # Crear la ventana
    window = tk.Tk()
    window.title("Gráficos 3D animados con Matplotlib")

    # Crear figura y ejes 3D para el gráfico 3D 1
    fig1 = plt.figure()
    ax1 = plt.axes(projection='3d')

    # Crear figura y ejes 3D para el gráfico 3D 2
    fig2 = plt.figure()
    ax2 = plt.axes(projection='3d')

    # Crear los widgets de lienzo para los gráficos 3D
    canvas1 = FigureCanvasTkAgg(fig1, master=window)
    canvas2 = FigureCanvasTkAgg(fig2, master=window)

    # Colocar los widgets de lienzo en la ventana
    canvas1.get_tk_widget().pack(side=tk.LEFT)
    canvas2.get_tk_widget().pack(side=tk.RIGHT)

    # Crear animación para actualizar los gráficos
    animation = FuncAnimation(fig1, update_graph, frames=np.arange(0, 100), interval=100)

    # Iniciar el bucle de la ventana
    window.mainloop()
