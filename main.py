import tkinter as tk
from src.simplex import Simplex
from src.grapher import Grapher

class SimplexGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simplex Solver")

        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.label_target_function = tk.Label(self.master, text="Função Objetivo (separe os coeficientes por vírgula):")
        self.label_constraints = tk.Label(self.master, text="Restrições (uma por linha, separe os coeficientes por vírgula):")
        self.label_optimization_type = tk.Label(self.master, text="Tipo de Otimização (max ou min):")

        # Entry Widgets
        self.entry_target_function = tk.Entry(self.master)
        self.entry_constraints = tk.Text(self.master, height=5, width=30)
        self.entry_optimization_type = tk.Entry(self.master)

        # Button
        self.solve_button = tk.Button(self.master, text="Resolver", command=self.solve_simplex)

        # Result Label
        self.result_label = tk.Label(self.master, text="")

        # Layout
        self.label_target_function.pack()
        self.entry_target_function.pack()

        self.label_constraints.pack()
        self.entry_constraints.pack()

        self.label_optimization_type.pack()
        self.entry_optimization_type.pack()

        self.solve_button.pack()
        self.result_label.pack()

    def solve_simplex(self):
        ppl = Simplex()

        try_again = True
        lucro = None

        target_function = [float(x) for x in self.entry_target_function.get().split(',')]

        constraints_text = self.entry_constraints.get("1.0", tk.END).split('\n')[:-1]
        constraints = [list(map(float, line.split(','))) for line in constraints_text]

        num_vars = sum(1 for x in target_function if x != 0)
        restrictions = []
        for constraint in constraints:
            restriction = {
                f'x{i+1}': constraint[i] for i in range(num_vars)
            }
            restriction['y'] = constraint[-1]

            type_index = next((i for i, x in enumerate(constraint[num_vars:-1], num_vars) if x != 0), None)
            restriction['type'] = 'less' if constraint[type_index] == 1 else 'more'

            restrictions.append(restriction)

        config = {'x':'eixo X', 'y':'eixo Y', 'z':'eixo Z'}
        grapher = Grapher()

        if num_vars == 2:
            grapher.plot_2d(restrictions, config=config)
        elif num_vars == 3:
            grapher.plot_3d(restrictions, config=config)

        optimization_type = self.entry_optimization_type.get().lower()

        ppl.setTargetFunction(target_function, optimization_type)
        ppl.setConstraints(constraints)

        simplexTable = ppl.setSimplexTable()


        while try_again:
            [largest_negative, pivot_column_index] = ppl.findLargestNegativeValueInZ(simplexTable)
            pivot_line_index = ppl.findPivotLine(simplexTable, pivot_column_index)
            pivot_item = ppl.findPivotItem(simplexTable, pivot_line_index, pivot_column_index)
            [reference_line, simplexTable] = ppl.setNewPivotLine(simplexTable, pivot_line_index, pivot_item)
            simplexTable = ppl.updateRows(simplexTable, pivot_line_index, pivot_column_index, reference_line)
            [try_again, lucro] = ppl.checkIfThereIsNegativeNumberInTargetFunction()

        self.result_label.config(text=f'Lucro: {lucro}')


if __name__ == "__main__":
    root = tk.Tk()
    app = SimplexGUI(root)
    root.mainloop()

'''
12,7,0,0,0,0,0

2,1,-1,0,0,0,4
1,6,0,-1,0,0,6
1,0,0,0,1,0,4
0,1,0,0,0,1,6
'''
'''
-5,-7,-8,0,0,0

1,1,2,1,0,1190
3,4.5,1,0,1,4000
0.25,0.5,0,0,1,50
'''