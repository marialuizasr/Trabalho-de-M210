import numpy as np
import matplotlib.pyplot as plt

class Grapher:

    def __init__(self):
        pass

    def plot_2d(self, restrictions, target_function=None, config=None):

        # Transform restrictions into a list of coordinates where it crosses the x and y axis on the graph
        restrictions = [{'x': (restriction['y']/restriction['x1'] if restriction['x1'] != 0 else 0, 0), 
                         'y': (0, restriction['y']/restriction['x2'] if restriction['x2'] != 0 else 0), 
                         'type': restriction['type']} for restriction in restrictions]

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
            ax.plot(restriction['x'], restriction['y'], color='black', alpha=0.8, linewidth=0.8)
            ax.fill_between(restriction['x'], restriction['y'], color=color, alpha=0.05)

        # Plots the target function
        # ax.plot(target_function[0], target_function[1], color='black')

        # Set labels from config
        ax.set_title('Método Gráfico')
        ax.set_xlabel(config['x'])
        ax.set_ylabel(config['y'])

        # Shows the graph
        plt.show(block=False)


    def plot_3d(self, restrictions, target_function=None, config=None):
        
        # Transform restrictions into a list of coordinates where it crosses the x and y axis on the graph
        restrictions = [{'x': (restriction['y']/restriction['x1'] if restriction['x1'] != 0 else 0, 0, 0), 
                         'y': (0, restriction['y']/restriction['x2'] if restriction['x2'] != 0 else 0, 0), 
                         'z': (0, 0, restriction['y']/restriction['x3'] if restriction['x3'] != 0 else 0),
                         'type': restriction['type']} for restriction in restrictions]
        
        # Calculate min and max values from restrictions
        max_x = max(restriction['x'][0] for restriction in restrictions)
        max_y = max(restriction['y'][1] for restriction in restrictions)
        max_z = max(restriction['z'][2] for restriction in restrictions)
        diff_x = max_x*0.1
        diff_y = max_y*0.1
        diff_z = max_z*0.1

        # Creates the graph
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(0 - diff_x, max_x + diff_x)
        ax.set_ylim(0 - diff_y, max_y + diff_y)
        ax.set_zlim(0 - diff_z, max_z + diff_z)
        ax.grid(True, which='both')

        # Plots the restrictions as planes on the graph
        for restriction in restrictions:
            color = 'red' if restriction['type'] == 'less' else 'blue' if restriction['type'] == 'equal' else 'green'
            ax.plot_trisurf(restriction['x'], restriction['y'], restriction['z'], color=color, alpha=0.333)

            # Create a grid for the base surface
            x = np.linspace(min(restriction['x']), max(restriction['x']), len(restriction['x']))
            y = np.linspace(min(restriction['y']), max(restriction['y']), len(restriction['y']))
            X, Y = np.meshgrid(x, y)
            Z = np.zeros_like(X)

            # Plot the base surface
            ax.plot_surface(X, Y, Z, color=color, alpha=0.05)

        # Set labels from config
        ax.set_title('Método Gráfico')
        ax.set_xlabel(config['x'])
        ax.set_ylabel(config['y'])
        ax.set_zlabel(config['z'])

        # Shows the graph
        plt.show(block=False)

    # Meybe???
    def plot_4d(self, restrictions, target_function=None, config=None):
        pass



if __name__ == '__main__':

    restrictions_2d = [{'x1':2, 'x2':4, 'y':16, 'type':'less'}, {'x1':3, 'x2':2, 'y':12, 'type':'less'}]
    restrictions_3d = [{'x1':1, 'x2':2, 'x3':3, 'y':30, 'type':'less'}, {'x1':2, 'x2':1, 'x3':1, 'y':20, 'type':'more'}, {'x1':1, 'x2':1, 'x3':2, 'y':24, 'type':'less'}]
    config = {'x':'eixo X', 'y':'eixo Y', 'z':'eixo Z'}

    grapher = Grapher()
    # grapher.plot_2d(restrictions_2d, config=config)
    grapher.plot_3d(restrictions_3d, config=config)