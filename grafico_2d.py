import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random



x = {}
y = {}
z = {}

contador = 0

countadores = []


def grafico(data):
    print(data)
    # Single Points
    ax = plt.axes()
    x_data = data["x"]
    y_data = data["y"]
    z_data = data["z"]
    ax.scatter(x_data,y_data,z_data)
    plt.show()

def graf2d(data,team,colores):
    global contador
    contador += 1    
    plt.clf()
    ax = plt.axes()
    print(data)
    data = data[team]
    countadores.append(contador)
    for i in data:
        color = colores[i]
        if contador <= 1:
            x[i] = []
            y[i] = []
            z[i] = []
        x_values = []
        y_values = []
        z_values = []
        x[i].append(data[i]["x"])
        y[i].append(data[i]["y"])
        z[i].append(data[i]["z"])
        x_values.append(data[i]["x"])
        y_values.append(data[i]["y"])
        z_values.append(data[i]["z"])
        diccionario = {"x":x,"y":y,"z":z}
        #ax.scatter(x_values,y_values,z_values, color="black")
        ax.plot(countadores,diccionario["z"][i],color,label=i)
        plt.legend()
    plt.pause(0.001)

def graf_dearriba(data,team,colores):
    global contador
    contador += 1    
    plt.clf()
    ax = plt.axes()
    print(data)
    data = data[team]
    countadores.append(contador)
    for i in data:
        color = colores[i]
        if contador <= 1:
            x[i] = []
            y[i] = []
            z[i] = []
        x_values = []
        y_values = []
        z_values = []
        x[i].append(data[i]["x"])
        y[i].append(data[i]["y"])
        z[i].append(data[i]["z"])
        x_values.append(data[i]["x"])
        y_values.append(data[i]["y"])
        z_values.append(data[i]["z"])
        diccionario = {"x":x,"y":y,"z":z}
        #ax.scatter(x_values,y_values,z_values, color="black")
        ax.plot(diccionario["x"][i],diccionario["y"][i],color,label=i)
        plt.legend()
    plt.pause(0.001)    