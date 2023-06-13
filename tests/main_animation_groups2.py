import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.linear_model import LinearRegression
import random

reg = LinearRegression()

x = {}
y = {}
z = {}

contador = 0


def grafico(data):
    print(data)
    # Single Points
    ax = plt.axes(projection="3d")
    x_data = data["x"]
    y_data = data["y"]
    z_data = data["z"]
    ax.scatter(x_data,y_data,z_data)
    plt.show()

def main_graf(data,colores):
    global contador
    contador += 1
    plt.clf()
    ax = plt.axes(projection="3d")
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
        ax.scatter(x_values,y_values,z_values, color="black")
        ax.plot(diccionario["x"][i],diccionario["y"][i],diccionario["z"][i],color)
    plt.pause(0.001)

def test():
    values = [0] * 50

    for i in range(50):
        values[i] = random.randint(0,100)
        plt.xlim(0,50)
        plt.ylim(0,100)
        plt.bar(list(range(50)), values)
        plt.pause(0.0001)
    plt.show()