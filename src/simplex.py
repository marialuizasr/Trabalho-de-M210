infinity = 1000000000000000000

class Simplex():
    def __init__(self) -> None:
        pass

    def setTargetFunction(self, targetFunction, target):
        self.targetFunction = targetFunction
        self.target = target

    def setConstraints(self, constraints):
        self.constraints = constraints
    
    def setSimplexTable(self):
        simplexTable = self.constraints
        simplexTable.insert(0, self.targetFunction)
        self.simplexTable = simplexTable

    def findLargestNegativeValueInZ(self):
        largestNegative = None
        largestNegativeIndex = None
        for index, item in enumerate(self.simplexTable[0]):
            if item < 0 and (largestNegative is None or item < largestNegative):
                largestNegative = item
                largestNegativeIndex = index

        self.largestNegative = largestNegative
        self.pivotColumnIndex = largestNegativeIndex
        return largestNegative

    def findPivotLine(self):
        relations = []
        smallestRelation = None
        smallestRelationIndex = None

        for item in enumerate(self.simplexTable):
            rightSide = item[1][-1]
            valueInPivotColumn = item[1][self.pivotColumnIndex]
            if(valueInPivotColumn != 0):
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
    
    def findPivotItem(self):
        pivotItem = self.simplexTable[self.pivotLineIndex][self.pivotColumnIndex]
        self.pivotItem = pivotItem

    def setNewPivotLine(self):
        auxPivotLine = self.simplexTable[self.pivotLineIndex]
        newPivotLine = []

        for value in auxPivotLine:
            newValueInPivotLine = value/self.pivotItem
            newPivotLine.append(newValueInPivotLine)

        self.simplexTable[self.pivotLineIndex] = newPivotLine
        self.referenceLine = newPivotLine
    
    def updateRows(self):
        auxSimplexTable = self.simplexTable
        for index, row in enumerate(auxSimplexTable):
            if(index != self.pivotLineIndex):
                newLine = []
                for position, element in enumerate(row):
                    newElement = element + auxSimplexTable[index][self.pivotColumnIndex]*self.referenceLine[position]*(-1)
                    newLine.append(newElement)
                self.simplexTable[index] = newLine


    def checkIfThereIsNegativeNumberInTargetFunction(self):
        for value in self.simplexTable[0]:
            if value < 0:
                return [True, 0]
        return [False, self.simplexTable[0][-1]]



        
        

