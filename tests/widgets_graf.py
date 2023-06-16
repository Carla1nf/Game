import tkinter as tk
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

x = {}
y = {}
z = {}
x_val = []
y_val = []
z_val = []

contador = 0


def main_solo(data):
    plt.clf()
    global contador
    x_values = []
    y_values = []
    z_values = []
    contador += 1

    ax = plt.axes(projection="3d")
    x_values.append(data["x"])
    y_values.append(data["y"])
    z_values.append(data["z"])
    x_val.append(data["x"])
    y_val.append(data["y"])
    z_val.append(data["z"])

    if contador%2 == 0:
        ax.scatter(x_values,y_values,z_values)
        ax.plot(x_val,y_val,z_val)
        plt.pause(0.001)


def main_graf(dataT,team,colores):
    for i in dataT:
        if i == "x":
            return main_solo(dataT)
    global contador
    contador += 1
    plt.clf()
    ax = plt.axes(projection="3d")
    dataT = dataT[team]
    for i in dataT:
        color = colores[i]
        if contador <= 1:
            x[i] = []
            y[i] = []
            z[i] = []
        x_values = []
        y_values = []
        z_values = []
        x[i].append(dataT[i]["x"])
        y[i].append(dataT[i]["y"])
        z[i].append(dataT[i]["z"])
        x_values.append(dataT[i]["x"])
        y_values.append(dataT[i]["y"])
        z_values.append(dataT[i]["z"])
        diccionario = {"x":x,"y":y,"z":z}
        ax.scatter(x_values,y_values,z_values, color="black")
        ax.plot(diccionario["x"][i],diccionario["y"][i],diccionario["z"][i],color,label=i)
        plt.legend()
    plt.pause(0.001)

def update_graph(frame,dataT,team,colores):
    ax1.cla()  # Limpiar el gráfico antes de dibujar el siguiente fotograma
    ax2.cla()

    for i in dataT:
        if i == "x":
            return main_solo(dataT)
    global contador
    contador += 1
    dataT = dataT[team]
    for i in dataT:
        color = colores[i]
        if contador <= 1:
            x[i] = []
            y[i] = []
            z[i] = []
        x_values = []
        y_values = []
        z_values = []
        x[i].append(dataT[i]["x"])
        y[i].append(dataT[i]["y"])
        z[i].append(dataT[i]["z"])
        x_values.append(dataT[i]["x"])
        y_values.append(dataT[i]["y"])
        z_values.append(dataT[i]["z"])
        diccionario = {"x":x,"y":y,"z":z}
        ax1.scatter(x_values,y_values,z_values, color="black")
        ax1.plot(diccionario["x"][i],diccionario["y"][i],diccionario["z"][i],color,label=i)
        plt.legend()
    plt.pause(0.001)

    # Calcular nuevos datos para el gráfico 3D 1
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2 + frame/10.0))

    # Graficar el gráfico 3D 1
    # ax1.plot_surface(X, Y, Z, cmap='viridis')

    # Calcular nuevos datos para el gráfico 3D 2
    Z = np.cos(np.sqrt(X**2 + Y**2 + frame/10.0))

    # Graficar el gráfico 3D 2
    ax2.plot_surface(X, Y, Z, cmap='plasma')

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
