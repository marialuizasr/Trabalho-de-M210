import numpy as np
import matplotlib.pyplot as plt

class Grapher:

    def __init__(self, config):
        self.config = config

    def plot_2d(self, restrictions, target_function=None):

        # Transform restrictions into a list of coordinates where it crosses the x and y axis on the graph
        restrictions = [{'x':(restriction['y']/restriction['x1'], 0), 
                         'y':(0, restriction['y']/restriction['x2']), 
                         'type':restriction['type']} for restriction in restrictions]

        # Calculate min and max values from restrictions
        max_x = max(restriction['x'][0] for restriction in restrictions)
        max_y = max(restriction['y'][1] for restriction in restrictions)
        diff_x = max_x*0.1
        diff_y = max_y*0.1

        # Creates the graph
        _, ax = plt.subplots()
        ax.set_xlim(0 - diff_x, max_x + diff_x)
        ax.set_ylim(0 - diff_y, max_y + diff_y)
        ax.grid(True, which='both')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')

        # Plots the restrictions
        for restriction in restrictions:
            color = 'red' if restriction['type'] == 'less' else 'blue' if restriction['type'] == 'equal' else 'green'
            ax.plot(restriction['x'], restriction['y'], color='black', alpha=0.8, linewidth=0.5)
            ax.fill_between(restriction['x'], restriction['y'], color=color, alpha=0.1)

        # Plots the target function
        # ax.plot(target_function[0], target_function[1], color='black')

        # Set labels from config
        ax.set_title('Método Gráfico')
        ax.set_xlabel(self.config['x'])
        ax.set_ylabel(self.config['y'])

        # Shows the graph
        plt.show()


    def plot_3d(self, restrictions, target_function):
        pass

if __name__ == '__main__':

    restrictions = [{'x1':2, 'x2':4, 'y':16, 'type':'more'}, {'x1':3, 'x2':2, 'y':12, 'type':'less'}]
    config = {'x':'nome do eixo X', 'y':'nome do eixo Y'}

    grapher = Grapher(config)
    grapher.plot_2d(restrictions)