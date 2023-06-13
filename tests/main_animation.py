import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import ipywidgets
from sklearn.linear_model import LinearRegression
import random

reg = LinearRegression()

x = {}
y = {}
z = {}
x_val = []
y_val = []
z_val = []

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

def plot_graf(data):
    graf = main_graf(n_data=data)

def main_graf(dataT,team,colores):
    for i in dataT:
        if i == "x":
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
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

def test():
    values = [0] * 50

    for i in range(50):
        values[i] = random.randint(0,100)
        plt.xlim(0,50)
        plt.ylim(0,100)
        plt.bar(list(range(50)), values)
        plt.pause(0.0001)
    plt.show()