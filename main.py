from src.simplex import Simplex

ppl = Simplex()

tryAgain = True
lucro = None

targetFunction = [-5, -7, -8]
numberOfConstraints = 2
constraints = [
    [1, 1, 2, 1190, 'menor'],
    [3, 4.5, 1, 4000, 'menor'],
]

# targetFunction = [-5, -7]
# numberOfConstraints = 3
# constraints = [
#     [3, 0, 250, 'menor'],
#     [0, 1.5, 100, 'menor'],
#     [0.25, 0.5, 50, 'menor'],
# ]


# targetFunction = [-25, -50, 0, 0, 0, 0]
# constraints = [
#     [7, 5, 1, 0, 0, 35],
#     [4, 6, 0, 1, 0, 24],
#     [3, 10, 0, 0, 1, 30]
# ]

# targetFunction = [0.06, 0.08, 0, 0, 0, 0]
# constraints = [
#     [8, 6, -1, 0, 0, 48],
#     [1, 2, 0, -1, 0, 12],
#     [1, 2, 0, 0, 1, 20]
# ]

# targetFunction = [12, 7, 0, 0, 0, 0, 0]
# constraints = [
#     [2, 1, -1, 0, 0, 0, 4],
#     [1, 6, 0, -1, 0, 0, 6],
#     [1, 0, 0, 0, 1, 0, 4],
#     [0, 1, 0, 0, 0, 1, 6],
# ]

# ppl.setTargetFunction(targetFunction, 'min')

#### PSEUDO CÓDIGO

# entre com a funcao objetivo (coeficientes)

# entre com o número de restricoes

# entre com as restricoes

ppl.setTargetFunction(targetFunction, 'max')

ppl.setNumberOfConstraints(numberOfConstraints)

ppl.formatTargetFunction()

ppl.setTableLabels()

ppl.setConstraints(constraints)
simplexTable = ppl.setSimplexTable()

while (tryAgain):
    [largestNegative, pivotColumnIndex] = ppl.findLargestNegativeValueInZ(simplexTable)
    pivotLineIndex = ppl.findPivotLine(simplexTable, pivotColumnIndex)
    pivotItem = ppl.findPivotItem(simplexTable, pivotLineIndex, pivotColumnIndex)
    [referenceLine, simplexTable] = ppl.setNewPivotLine(simplexTable, pivotLineIndex, pivotItem)
    simplexTable = ppl.updateRows(simplexTable, pivotLineIndex, pivotColumnIndex, referenceLine)
    [tryAgain, simplex, columsLabels, linesLabels] = ppl.checkIfThereIsNegativeNumberInTargetFunction()

columsLabels.append('LUCRO')
linesLabels.insert(0, 'Z')

print(f'{"":<8}', end='')
for col_label in columsLabels:
    print(f'{col_label:<10}', end='')
print()

for i, row in enumerate(simplex):
    print(f'{linesLabels[i]:<8}', end='')
    for value in row:
        print(f'{value:<10.3f}', end='')
    print()