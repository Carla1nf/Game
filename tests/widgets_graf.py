import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.linear_model import LinearRegression
import random
from IPython.display import display

def test(rango_max):
    values = [0] * 50

    for i in range(50):
        values[i] = random.randint(0,rango_max)
        plt.xlim(0,50)
        plt.ylim(0,100)
        plt.bar(list(range(50)), values)
        plt.pause(0.0001)
    plt.show()

def plot_fct(w=1):
    x = np.random.uniform(0,5,size=100)
    y = 2 * x + w * np.random.normal(size=100)
    plt.scatter(x,y)
display(widgets.interact(plot_fct, w=(0,5,0.5)))