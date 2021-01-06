class Memory:

    __decisions = None
    __facts = None
    __goalposition = None
    __world = None
    __myposition = None

    def __init__(self, myposition, planedimension):
        self.__myposition = myposition
        self.createWorld(planedimension)

    def getMyPosition(self):
        return self.__myposition

    def getGoalPosition(self):
        return self.__goalposition

    def setGoalPosition(self, position):
        self.__goalposition = position
        array = Memory.splitStringPosition(position)
        self.__world[array[0]][array[1]] = 'G'

    def putDecision(self, decision):
        decision = str(decision)
        self.__decisions.put(decision)

    def putFact(self, fact):
        fact = str(fact)
        self.__decisions.put(fact)

    def getAllDecisions(self):
        return self.__decisions

    def createWorld(self, planedimension):
        array = Memory.splitStringPosition(planedimension)
        self.__world = [[0] * array[0] for i in range(array[1])]
        self.changeMyPosition(self.__myposition)

    def getWorld(self):
        return self.__world

    def changeMyPosition(self, newposition):
        array = Memory.splitStringPosition(self.__myposition)
        self.__world[array[0]][array[1]] = "0"
        array = Memory.splitStringPosition(newposition)
        self.__world[array[0]][array[1]] = "A"
        self.__myposition = newposition

    def updateWorld(self, arraySensor):
        cellsSensor = arraySensor.split("-")
        positionarray = None

        for i in cellsSensor:
            singlePosition = cellsSensor[i].split(",")
            self.__world[singlePosition[0]][singlePosition[1]] = singlePosition[2]
            positionarray[i] = singlePosition

        return positionarray


    @staticmethod
    def splitStringPosition(position):
        array = position.split(",", 2)
        arrayint = [int(array[0]), int(array[1])]
        return arrayint
