import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.linear_model import LinearRegression
import random

reg = LinearRegression()

x = []
y = []
z = []
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

def main_graf(data):
    for i in data:
        plt.clf()
        global contador
        x_values = []
        y_values = []
        z_values = []
        contador += 1

        ax = plt.axes(projection="3d")
        x_values.append(data[i]["x"])
        y_values.append(data[i]["y"])
        z_values.append(data[i]["z"])
        x.append(data[i]["x"])
        y.append(data[i]["y"])
        z.append(data[i]["z"])

        if contador%2 == 0:
            #ax.scatter(x_values,y_values,z_values, color="black")
            ax.scatter(x,y,z, color="black")
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