import tkinter as tk
from src.simplex import Simplex

class SimplexGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simplex Solver")

        self.target_function_label = tk.Label(master, text="Função alvo (separada por vírgulas):")
        self.target_function_entry = tk.Entry(master)

        self.number_of_constraints_label = tk.Label(master, text="Número de restrições:")
        self.number_of_constraints_entry = tk.Entry(master)

        self.constraints_label = tk.Label(master, text="Restrições (uma por linha, separadas por vírgulas e tipo):")
        self.constraints_entry = tk.Text(master, height=5, width=50)

        self.solve_button = tk.Button(master, text="Resolver", command=self.solve)

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.config(state=tk.DISABLED)

        self.target_function_label.pack()
        self.target_function_entry.pack()
        self.number_of_constraints_label.pack()
        self.number_of_constraints_entry.pack()
        self.constraints_label.pack()
        self.constraints_entry.pack()
        self.solve_button.pack()
        self.result_text.pack()

    def get_user_input(self):
        target_function = [float(x) for x in self.target_function_entry.get().replace(' ', '').split(',')]
        number_of_constraints = int(self.number_of_constraints_entry.get())
        constraints_text = self.constraints_entry.get("1.0", tk.END)
        constraints_lines = constraints_text.splitlines()
        constraints = [line.split(',')[:-1] + [float(line.split(',')[-1])] if line.split(',')[-1].replace('.', '', 1).isdigit() else line.split(',') for line in constraints_lines]

        return target_function, number_of_constraints, constraints

    def show_results(self, shadow_prices, great_values, great_profit):
        result_str = "Resultados:\n"
        for key in shadow_prices:
            result_str += f'PREÇO SOMBRA DE {key}: {shadow_prices[key]}\n'

        for key in great_values:
            result_str += f'VALOR ÓTIMO DE {key}: {great_values[key]}\n'

        result_str += f'LUCRO ÓTIMO: {great_profit}\n'

        # Atualiza o widget de texto com os resultados
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result_str)
        self.result_text.config(state=tk.DISABLED)

    def solve(self):
        target_function, number_of_constraints, constraints = self.get_user_input()

        ppl = Simplex()

        ppl.setTargetFunction(target_function, 'max')
        ppl.setNumberOfConstraints(number_of_constraints)
        ppl.formatTargetFunction()
        ppl.setTableLabels()
        ppl.setConstraints(constraints)
        simplexTable = ppl.setSimplexTable()

        try_again = True

        while try_again:
            largest_negative, pivot_column_index = ppl.findLargestNegativeValueInZ(simplexTable)
            pivot_line_index = ppl.findPivotLine(simplexTable, pivot_column_index)
            pivot_item = ppl.findPivotItem(simplexTable, pivot_line_index, pivot_column_index)
            reference_line, simplexTable = ppl.setReferenceLine(simplexTable, pivot_line_index, pivot_item)
            simplexTable = ppl.updateRows(simplexTable, pivot_line_index, pivot_column_index, reference_line)
            try_again, great_profit, shadow_prices, great_values = ppl.checkIfThereIsNegativeNumberInTargetFunction()

        self.show_results(shadow_prices, great_values, great_profit)


def main():
    root = tk.Tk()
    simplex_gui = SimplexGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
