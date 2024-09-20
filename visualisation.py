import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

class Visualizer:
    def __init__(self, dataset):
        self.dataset = dataset

    def Barplot(self, dataset, x, y):
        plt.bar(dataset[x], dataset[y], color = 'pink')
        plt.title('Happiness')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

    def Line(self, dataset, x, y):
        plt.plot(dataset[x], dataset[y], color = 'orange')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'Зависит ли {y} от {x}?')
        plt.show()

    def Scatterplot_3d(self, dataset, x, y, z):
        fig = plt.figure()
        fig_3d = fig.add_subplot(111, projection = '3d')
        fig_3d.set_xlabel(x)
        fig_3d.set_ylabel(y)
        fig_3d.set_zlabel(z)
        plt.show()

    def Scatterplot(self, dataset, x, y):
        plt.scatter(dataset[x], dataset[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()