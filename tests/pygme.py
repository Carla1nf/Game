import tkinter as tk
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main_client import Climber
import math
from main_client import avance_x
from main_client import avance_y
from main_client import is_it_secure
from main_client import escalar
from communication.client.client import MountainClient
import time

def main():
    print("hola")
    x = {}
    y = {}
    z = {}
    x_2 = {}
    y_2 = {}
    z_2 = {}
    colores = {}

    contador = 0
    contador2 = 0
    contadores = []

    team1 = "racing"
    climber_1 = Climber("leo messi",((3*math.pi)/4),"royalblue",1)
    climber_2 = Climber("dibu martinez",((5*math.pi)/4),"mediumseagreen",1)
    climber_3 = Climber("lautaro martinez",((7*math.pi)/4),"navy",2)
    climber_4 = Climber("enzo fernandez",(5*(math.pi)/4),"crimson",3)
    equipo = [climber_1,climber_2,climber_3,climber_4]
    nombres = [climber_1.name,climber_2.name,climber_3.name,climber_4.name]
    color = {}
    for climber in equipo:
        color[climber.name] = climber.color
    point_color = {}
    for climber in equipo:
        point_color[climber.name] = climber.point_color

    c = MountainClient()
    c.add_team(team1,nombres)
    team2 = "martin"
    c.finish_registration()

    def main_graf(dataT,team1,colores,point_color):
            x_values = []
            y_values = []
            z_values = []
            nonlocal contador
            ax1.cla()  # Limpiar el gráfico antes de dibujar el siguiente fotograma
            contador += 1
            dataT = dataT[team1]
            for i in dataT:
                color = colores[i]
                if contador <= 1:
                    x[i] = []
                    y[i] = []
                    z[i] = []
                x_values.append(dataT[i]["x"])
                y_values.append(dataT[i]["y"])
                z_values.append(dataT[i]["z"])
                x[i].append(dataT[i]["x"])
                y[i].append(dataT[i]["y"])
                z[i].append(dataT[i]["z"])
                ax1.scatter(x_values, y_values, z_values, color=point_color)
                ax1.plot(x[i], y[i], z[i], color=color, label=i)
    def graph_2d(dataT,team1,colores,point_color):
            x_values = []
            y_values = []
            z_values = []
            nonlocal contador2
            ax2.cla()  # Limpiar el gráfico antes de dibujar el siguiente fotograma
            ax3.cla()
            contador2 += 1
            dataT = dataT[team1]
            contadores.append(contador2)
            for i in dataT:
                color = colores[i]
                if contador2 <= 1:
                    x_2[i] = []
                    y_2[i] = []
                    z_2[i] = []
                x_values.append(dataT[i]["x"])
                y_values.append(dataT[i]["y"])
                x_2[i].append(dataT[i]["x"])
                y_2[i].append(dataT[i]["y"])
                z_2[i].append(dataT[i]["z"])
                ax2.plot(x_2[i], y_2[i], color=color, label=i)
                ax2.scatter(x_values, y_values, color=point_color,s=2.5)
                ax2.scatter(-23000, 0,s=0)
                ax2.scatter(23000, 0,s=0)
                ax2.scatter(0, -23000,s=0)
                ax2.scatter(0, 23000,s=0)
                cc = plt.Circle(( 0, 0 ), 23000 , alpha=0.1,color="black") 
                ax2.set_aspect( 1 ) 
                ax2.add_artist( cc ) 
                #ax2.scatter( 0 , 0 , s = 23000,facecolors='none',edgecolors='black') 
                ax3.plot(contadores,z_2[i],color=color, label=i)
        
    def update_graph(frame):
        for climber in equipo:
            cimas = c.get_data()[team1][climber.name]["cima"]
            if cimas == True:
                cima = True
        direcciones = {climber_1.name:climber_1.main_climb(team1,c),climber_2.name:climber_2.main_climb(team1,c),climber_3.name:climber_3.main_climb(team1,c),climber_4.name:climber_4.main_climb(team1,c)}
        c.next_iteration(team1,direcciones)
        data = c.get_data()
        data2 = c.get_data()[team1][climber_1.name]
        main_graf(data,team1,color,climber.point_color)
        graph_2d(data,team1,color,climber.point_color)
        plt.legend()
        time.sleep(0.1)


        

        # Actualizar los widgets de lienzo
        canvas1.draw()
        canvas2.draw()

    # Crear la ventana
    window = tk.Tk()
    window.title("Gráficos 3D")
    window.geometry("1600x900")

    # Crear figura y ejes 3D para el gráfico 3D 1
    fig1 = plt.figure()
    ax1 = plt.axes(projection='3d')

    # Crear figura y ejes 3D para el gráfico 3D 2
    fig2, (ax2, ax3) = plt.subplots(1, 2)

    # Crear los widgets de lienzo para los gráficos 3D
    canvas1 = FigureCanvasTkAgg(fig1, master=window)
    canvas2 = FigureCanvasTkAgg(fig2, master=window)

    # Colocar los widgets de lienzo en la ventana
    canvas1.get_tk_widget().pack(fill="both")
    canvas2.get_tk_widget().pack(fill="both")

    # Crear animación para actualizar los gráficos
    animation = FuncAnimation(fig1, update_graph, frames=np.arange(0, 100), interval=100)
    # Iniciar el bucle de la ventana
    window.mainloop()
