class Memory:

    __decisions = None
    __facts = None
    __goalposition = None
    __world = None
    __myposition = None
    __planedim = None

    def __init__(self, myposition, planedimension):
        self.__decisions = []
        self.__facts = []
        self.__myposition = myposition
        self.createWorld(planedimension)

    def getMyPosition(self):
        return self.__myposition

    def getGoalPosition(self):
        return self.__goalposition

    def setGoalPosition(self, position):
        self.__goalposition = position
        return

    def putDecision(self, decision):
        decision = str(decision)
        self.__decisions.append(decision)
        return

    def putFact(self, fact):
        fact = str(fact)
        self.__decisions.append(fact)
        return

    def getAllDecisions(self):
        return self.__decisions

    def createWorld(self, planedimension):
        array = Memory.splitStringPosition(planedimension)
        self.__planedim = array
        self.__world = [[0] * array[0] for i in range(array[1])]
        self.changeMyPosition(self.__myposition)
        return

    def getWorld(self):
        return self.__world

    def changeMyPosition(self, newposition):
        array = Memory.splitStringPosition(self.__myposition)
        arraynewposition = Memory.splitStringPosition(newposition)
        self.__world[array[0]][array[1]] = "0"
        self.__world[arraynewposition[0]][arraynewposition[1]] = "A"

    def updateWorld(self, arraySensor):
        cellsSensor = arraySensor.split("-")
        positionarray = []

        for i in range(len(cellsSensor)-1):
            singlePosition = cellsSensor[i].split(",")
            if ( int(singlePosition[0]) < 0 or int(singlePosition[1]) < 0 or int(singlePosition[0]) > self.__planedim[0] - 1 or int(singlePosition[1]) > self.__planedim[1] - 1):
                continue
            self.__world[int(singlePosition[0])][int(singlePosition[1])] = singlePosition[2]
            positionarray.append(singlePosition)

        return positionarray


    @staticmethod
    def splitStringPosition(position):
        array = position.split(",", 2)
        arrayint = [int(array[0]), int(array[1])]
        return arrayint
