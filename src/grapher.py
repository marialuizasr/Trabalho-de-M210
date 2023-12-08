import time
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np

class Grapher:

    def __init__(self):
        pass

    def plot_2d(self, formated_restrictions, target_function=None, config=None):

        # Translate formated_restrictions into restrictions
        restrictions = []
        for restriction in formated_restrictions:
            formatted_restriction = {
                'x1': float(restriction[0]),
                'x2': float(restriction[1]),
                'y': float(restriction[-1])
            }

            # Find the index of the non-zero value after 'x2'
            type_index = next((i for i, x in enumerate(restriction[2:-1], 2) if x != 0), None)
            if type_index is not None:
                formatted_restriction['type'] = 'less' if restriction[type_index] == 1 else 'more'
            else:
                formatted_restriction['type'] = 'less'  # or 'more', depending on your default

            restrictions.append(formatted_restriction)

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
            color = 'red' if restriction['type'] == 'less' else 'green' if restriction['type'] == 'more' else 'blue'
            ax.plot(restriction['x'], restriction['y'], color='black', alpha=0.8, linewidth=0.8)
            
            if restriction['type'] == 'more':
                poly_points = [
                    (restriction['x'][0], restriction['y'][0]),
                    (restriction['x'][1], restriction['y'][1]),
                    (restriction['x'][1], ax.get_ylim()[1]),
                    (ax.get_xlim()[1], ax.get_ylim()[1]),
                    (ax.get_xlim()[1], restriction['y'][0])
                ]
                poly = Polygon(poly_points, closed=False, color=color, alpha=0.05)
                ax.add_patch(poly)
            else:
                ax.fill_between(restriction['x'], restriction['y'], color=color, alpha=0.05)

        # ! to fix later
        # # Calculate the optimal point
        # if target_function is not None:
        #     c = [-float(x) for x in target_function[:2]]
        #     A = [[float(r['x1']), float(r['x2'])] for r in restrictions]
        #     b = [float(r['y']) for r in restrictions]
        #     bounds = [(0, None) for _ in range(2)]
        #     res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
        #     if res.success:
        #         ax.plot(res.x[0], res.x[1], 'bo')  # Plot the optimal point

        # Set labels from config
        ax.set_title('Método Gráfico')
        ax.set_xlabel(config['x'])
        ax.set_ylabel(config['y'])

        # Shows the graph
        plt.show(block=False)