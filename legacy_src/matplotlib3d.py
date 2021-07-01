
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
import numpy as np
"this is raw version 1.0"
# plt.style.use('fivethirtyeight')

# x_vals = []
# y_vals = []

# index = count()


def animate(i):
    data = pd.read_csv('src/data.csv')
    x = data['index']
    y1 = data['posX']
    y2 = data['posY']
    y3 = data["posZ"]
    
    plt.cla()

    # ax = plt.axes(projection='3d')
    # ax.plot3D(y1, y2,  y3, "green",label = "movement")

    plt.plot(y1, y2, label='movement', linestyle = "--", alpha=0.1)
    # plt.axhline(0, color = "red") #on y axis (horizontal)
    # plt.axhline(6, color = "red") #on y axis (horizontal)
    # plt.axvline(1.3, color = "red") #on x axis (vertical)
    plt.axhspan(0, 6, alpha = 0.2) 
    plt.axvspan(0, 6, alpha = 0.2)
    plt.scatter(0, 0, c="red")
    plt.text(0,0,"anchor")
    
    # plt.annotate(f'({0},{1})', xy=(0, 1))
    try:
        plt.text(data['posX'].iloc[-1], data['posY'].iloc[-1], "you")
        plt.scatter(data['posX'].iloc[-1], data['posY'].iloc[-1], c="g")
    except:
        print("no last value yet")
    
    plt.grid()
    plt.xlabel("Y")
    plt.ylabel("X")
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()