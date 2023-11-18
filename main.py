from src.ppl import LinearProgrammingModels

ppl = LinearProgrammingModels()

tryAgain = True
lucro = None

targetFunction = [-5, -7, -8, 0, 0, 0]
constraints = [
    [1, 1, 2, 1, 0, 1190],
    [3, 4.5, 1, 0, 1, 4000],
    # [0.25, 0.5, 0, 0, 1, 50],
]

ppl.setTargetFunction(targetFunction, 'max')
ppl.setConstraints(constraints)
ppl.setSimplexTable()

while (tryAgain):
    ppl.findLargestNegativeValueInZ()
    ppl.findPivotLine()
    ppl.findPivotItem()
    ppl.setNewPivotLine()
    ppl.updateRows()
    [tryAgain, lucro] = ppl.checkIfThereIsNegativeNumberInTargetFunction()

print('Lucro:', lucro)