import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
import numpy as np


class Plot_manager:
    def __init__(self, anchor_list, room_size = [0,0,6,6]):
        self.room_size = room_size
        self.anchor_list = anchor_list

    def animate(self, i):
        data = pd.read_csv('src/data.csv')
        x = data['index']
        y1 = data['posX']
        y2 = data['posY']
        y3 = data["posZ"]
        plt.cla()
        plt.plot(y1, y2, label='movement', linestyle="--", alpha=0.1)
        plt.axhline(self.room_size[0], color = "#01BFDA") #on y axis (horizontal)
        plt.axhline(self.room_size[2], color = "#01BFDA") #on y axis (horizontal)
        plt.axvline(self.room_size[1], color = "#01BFDA") #on x axis (vertical)
        plt.axvline(self.room_size[3], color = "#01BFDA") #on x axis (vertical)
        # plt.axhspan(0, 6, alpha=0.2) #does not work with lists
        # plt.axvspan(self.room_size[2], self.room_size[3], alpha=0.2) #does not work with lists
        self.add_anchors(self.anchor_list)
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

    def add_anchors(self, anchor_list):
        if any(isinstance(i, list) for i in anchor_list):
            for anchor in anchor_list:
                plt.scatter(anchor[0], anchor[1], color="red")
                plt.text(anchor[0], anchor[1], anchor[2])
        else:
            plt.scatter(anchor_list[0], anchor_list[1], color="red")
            plt.text(anchor_list[0], anchor_list[1], anchor_list[2])

    def run(self):
        ani = FuncAnimation(plt.gcf(), self.animate, interval=100)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    anchors = [[0, 0, "anchor1"], [6, 6, "anchor2"], [6,0, "anchor3"]]
    room_size = [0,0,7,7]#x1, y1, x2, y2
    test = Plot_manager(anchors)
    test.run()
