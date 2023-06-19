"""import pandas as pd
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
    
class Graph(tk.Frame):
    def _init_(self, master=None, title="", *args, **kwargs):
        super()._init_(master, *args, **kwargs)
        self.fig = Figure(figsize=(4, 3))
        ax = self.fig.add_subplot(111)
        df = pd.DataFrame({"values": np.random.randint(0, 50, 10)}) #dummy data
        df.plot(ax=ax)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        tk.Label(self, text=f"Graph {title}").grid(row=0)
        self.canvas.get_tk_widget().grid(row=1, sticky="nesw")
        toolbar_frame = tk.Frame(self)
        toolbar_frame.grid(row=2, sticky="ew")
        NavigationToolbar2Tk(self.canvas, toolbar_frame)
    
root = tk.Tk()

for num, i in enumerate(list("123")):
    Graph(root, title=i, width=200).grid(row=num//2, column=num%2)

text_box = tk.Text(root, width=50, height=10, wrap=tk.WORD)
text_box.grid(row=1, column=1, sticky="nesw")
text_box.delete(0.0, "end")
text_box.insert(0.0, 'Altura maxima alcanzada: ')

root.mainloop()
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import ipywidgets
from sklearn.linear_model import LinearRegression
import random
from matplotlib import style
from tkinter import *

reg = LinearRegression()

x = {}
y = {}
z = {}
x_val = []
y_val = []
z_val = []

contador = 0

def plot_graf(data):
    graf = main_graf(n_data=data)

def main_graf(dataT,team,colores,point_color):
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
        point_color_ = point_color[i]
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
        ax.scatter(x_values,y_values,z_values, color=point_color_)
        ax.plot(diccionario["x"][i],diccionario["y"][i],diccionario["z"][i],color,label=i)
        plt.legend()
    thismanager = plt.get_current_fig_manager()
    thismanager.set_window_title("Grafico 3d")
    #if contador%5 == 0:
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