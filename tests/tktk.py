import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data1 = {'country': ['A', 'B', 'C', 'D', 'E'],
         'gdp_per_capita': [45000, 42000, 52000, 49000, 47000]
         }
df1 = pd.DataFrame(data1)

data2 = {'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
         }  
df2 = pd.DataFrame(data2)

data3 = {'interest_rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
         'index_price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
         }
df3 = pd.DataFrame(data3)


x = {}
y = {}
z = {}
x_val = []
y_val = []
z_val = []

contador = 0


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

class Aplicacion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.etiqueta_temp_celsius = ttk.Label(
            parent, text="Temperatura en ºC:")
        self.etiqueta_temp_celsius.place(x=20, y=20)
        self.caja_temp_celsius = ttk.Entry(parent)
        self.caja_temp_celsius.place(x=140, y=20, width=60)
        self.boton_convertir = ttk.Button(
            parent, text="Convertir", command=self.convertir_temp)
        self.boton_convertir.place(x=20, y=60)
        self.etiqueta_temp_kelvin = ttk.Label(
            parent, text="Temperatura en K: n/a")
        self.etiqueta_temp_kelvin.place(x=20, y=120)
        self.etiqueta_temp_fahrenheit = ttk.Label(
            parent, text="Temperatura en ºF: n/a")
        self.etiqueta_temp_fahrenheit.place(x=20, y=160)
    def convertir_temp(self):
        temp_celsius = float(self.caja_temp_celsius.get())
        temp_kelvin = temp_celsius + 273.15
        temp_fahrenheit = temp_celsius*1.8 + 32
        self.etiqueta_temp_kelvin.config(
            text=f"Temperatura en K: {temp_kelvin}")
        self.etiqueta_temp_fahrenheit.config(
            text=f"Temperatura en ºF: {temp_fahrenheit}")
ventana = tk.Tk()
figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, ventana)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['country', 'gdp_per_capita']].groupby('country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, ventana)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['year', 'unemployment_rate']].groupby('year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')

figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['interest_rate'], df3['index_price'], color='g')
scatter3 = FigureCanvasTkAgg(figure3, ventana)
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['index_price'])
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Index Price')

ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)
app = Aplicacion(ventana)
ventana.mainloop()