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

def main_graf(data):
    global contador
    contador += 1
    for i in data:
        xval = []
        yval = []
        zval = []
        plt.clf()
        x_values = {}
        y_values = {}
        z_values = {}

        ax = plt.axes(projection="3d")
        x_values[i] = data[i]["x"]
        y_values[i] = data[i]["y"]
        z_values[i] = data[i]["z"]
        x[contador] = (data[i]["x"])
        y[contador] = (data[i]["y"])
        z[contador] = (data[i]["z"])

        if contador%2 == 0:
            for value in x.values():
                xval.append(value)
            print(xval)
            for value in y.values():
                yval.append(value)
            for value in z.values():
                zval.append(value)
            #ax.scatter(x_values[i],y_values[i],z_values[i], color="blue")
            ax.plot(xval,yval,zval, color="black")
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