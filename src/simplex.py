infinity = 1000000000000000000

class Simplex():
    def __init__(self) -> None:
        pass

    def setTargetFunction(self, targetFunction, target):
        self.iteration = 0
        self.targetFunction = targetFunction
        self.target = target

    def setConstraints(self, constraints):
        self.constraints = constraints
    
    def setSimplexTable(self):
        simplexTable = self.constraints
        simplexTable.insert(0, self.targetFunction)
        self.simplexTable = simplexTable
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
                return [True, 0]
        return [False, self.simplexTable[0][-1]]



        
        

