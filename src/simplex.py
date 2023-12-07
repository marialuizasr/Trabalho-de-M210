infinity = 1000000000000000000

class Simplex():
    def __init__(self) -> None:
        pass

    def setTargetFunction(self, targetFunction, target):
        self.iteration = 0
        self.targetFunction = targetFunction
        self.target = target
        self.numberofCoeficientsInTargetFunction = len(targetFunction) - 1

    def setNumberOfConstraints(self, numberOfConstraints):
        self.numberOfConstraints = numberOfConstraints

    def formatTargetFunction(self):
        targetFunctionCopy = self.targetFunction
        for index in range(self.numberOfConstraints + 1):
            targetFunctionCopy.append(0)
        self.targetFunction = targetFunctionCopy
        print(self.targetFunction)

    def setTableLabels(self):
        columnsLabels = []
        linesLabels = []
        for index in range(len(self.targetFunction) - 1):
            label = ""
            if(index <= self.numberofCoeficientsInTargetFunction):
                label = f"A{index}"
            else:
                label = f"B{index}"
            columnsLabels.append(label)
        for index in range(-1*self.numberOfConstraints, 0):
            label = columnsLabels[index]
            linesLabels.append(label)

        self.columsLabels = columnsLabels
        self.linesLabels = linesLabels


    def setConstraints(self, constraints):
        formatedConstraints = []
        constraintsLen = len(constraints)
        for constraintIndex, constraint in enumerate(constraints):
            signal = constraint[-1]
            constraint.pop()
            formatedConstraint = constraint
            for index in range(constraintsLen):
                if(constraintIndex == index):
                    if(signal == 'menor'):
                        formatedConstraint.insert(-1, 1)
                    else:
                        formatedConstraint.insert(-1, -1)
                else:
                    formatedConstraint.insert(-1, 0)
            formatedConstraints.append(formatedConstraint)
        print('Formated Constraints', formatedConstraints)
        self.constraints = formatedConstraints
    
    def setSimplexTable(self):
        simplexTable = self.constraints
        simplexTable.insert(0, self.targetFunction)
        self.simplexTable = simplexTable
        print('Simplex Table', self.simplexTable)
        return self.simplexTable

    def findLargestNegativeValueInZ(self, simplexTable):
        largestNegative = None
        largestNegativeIndex = None
        for index, item in enumerate(simplexTable[0]):
            if self.target == 'max' and item < 0 and (largestNegative is None or item < largestNegative):
                largestNegative = item
                largestNegativeIndex = index

            if self.target == 'min' and item > 0 and (largestNegative is None or item > largestNegative):
                largestNegative = item
                largestNegativeIndex = index
        self.largestNegative = largestNegative
        self.pivotColumnIndex = largestNegativeIndex
        return [self.largestNegative, self.pivotColumnIndex]

    def findPivotLine(self, simplexTable, pivotColumnIndex):
        relations = []
        smallestRelation = None
        smallestRelationIndex = None

        for item in enumerate(simplexTable):
            rightSide = item[1][-1]
            valueInPivotColumn = item[1][pivotColumnIndex]
            if(valueInPivotColumn > 0):
                relation = rightSide/valueInPivotColumn
            else:
                relation = infinity
            relations.append(relation)
        for index, relation in enumerate(relations):
            if(index > 0):
                if (smallestRelation is None or relation < smallestRelation):
                    smallestRelation = relation
                    smallestRelationIndex = index
        self.pivotLineIndex = smallestRelationIndex
        copyColumPivotIndex = self.columsLabels[self.pivotColumnIndex]
        copyLinePivotIndex = self.linesLabels[self.pivotLineIndex - 1]

        copyColumnsLabels = self.columsLabels
        copyLinesLabels = self.linesLabels

        copyColumnsLabels[self.pivotColumnIndex] = copyLinePivotIndex
        copyLinesLabels[self.pivotLineIndex - 1] = copyColumPivotIndex

        self.columsLabels = copyColumnsLabels
        self.linesLabels = copyLinesLabels
        return self.pivotLineIndex
    
    def findPivotItem(self, simplexTable, pivotLineIndex, pivotColumnIndex):
        pivotItem = simplexTable[pivotLineIndex][pivotColumnIndex]
        self.pivotItem = pivotItem
        return self.pivotItem

    def setNewPivotLine(self, simplexTable, pivotLineIndex, pivotItem):
        auxPivotLine = simplexTable[pivotLineIndex]
        newPivotLine = []

        for value in auxPivotLine:
            newValueInPivotLine = value/pivotItem
            newPivotLine.append(newValueInPivotLine)

        self.simplexTable[pivotLineIndex] = newPivotLine
        self.referenceLine = newPivotLine
        return [self.referenceLine, self.simplexTable]
    
    def updateRows(self, simplexTable, pivotLineIndex, pivotColumnIndex, referenceLine):
        auxSimplexTable = simplexTable
        for index, row in enumerate(auxSimplexTable):
            if(index != pivotLineIndex):
                newLine = []
                for position, element in enumerate(row):
                    newElement = element + auxSimplexTable[index][pivotColumnIndex]*referenceLine[position]*(-1)
                    newLine.append(newElement)
                simplexTable[index] = newLine
        self.simplexTable = simplexTable
        return simplexTable


    def checkIfThereIsNegativeNumberInTargetFunction(self):
        if(self.target == 'min'):
            return [False, self.simplexTable]
        for value in self.simplexTable[0]:
            if value < 0:
                return [True, 0, 0, 0]
        return [False, self.simplexTable, self.columsLabels, self.linesLabels]



        
        

