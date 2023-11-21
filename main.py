from src.simplex import Simplex

ppl = Simplex()

tryAgain = True
lucro = None

# targetFunction = [-5, -7, -8, 0, 0, 0]
# constraints = [
#     [1, 1, 2, 1, 0, 1190],
#     [3, 4.5, 1, 0, 1, 4000],
#     # [0.25, 0.5, 0, 0, 1, 50],
# ]

# targetFunction = [-5, -7, 0, 0, 0, 0]
# constraints = [
#     [3, 0, 1, 0, 0, 250],
#     [0, 1.5, 0, 1, 0, 100],
#     [0.25, 0.5, 0, 0, 1, 50],
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

targetFunction = [12, 7, 0, 0, 0, 0, 0]
constraints = [
    [2, 1, -1, 0, 0, 0, 4],
    [1, 6, 0, -1, 0, 0, 6],
    [1, 0, 0, 0, 1, 0, 4],
    [0, 1, 0, 0, 0, 1, 6],
]

ppl.setTargetFunction(targetFunction, 'min')
# ppl.setTargetFunction(targetFunction, 'max')

ppl.setConstraints(constraints)
simplexTable = ppl.setSimplexTable()

while (tryAgain):
    [largestNegative, pivotColumnIndex] = ppl.findLargestNegativeValueInZ(simplexTable)
    pivotLineIndex = ppl.findPivotLine(simplexTable, pivotColumnIndex)
    pivotItem = ppl.findPivotItem(simplexTable, pivotLineIndex, pivotColumnIndex)
    [referenceLine, simplexTable] = ppl.setNewPivotLine(simplexTable, pivotLineIndex, pivotItem)
    simplexTable = ppl.updateRows(simplexTable, pivotLineIndex, pivotColumnIndex, referenceLine)
    [tryAgain, lucro] = ppl.checkIfThereIsNegativeNumberInTargetFunction()

print('Lucro:', lucro)