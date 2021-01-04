class Memory:

    __decisions = None
    __goalposition = None
    __world = None
    __myposition = None

    def __init__(self, myposition, larg, lung):
        self.__myposition = myposition
        self.createWorld(larg, lung)


    def setGoalPosition(self, position):
        self.__goalposition = position

    def putDecision(self, decision):
        decision = str(decision)
        self.__decisions.put(decision)

    def getAllDecisions(self):
        return self.__decisions

    def createWorld(self, larghezza, lunghezza):
        self.__world = [[0] * larghezza for i in range(lunghezza)]
        self.changeMyPosition(self.__myposition)

    def getWorld(self):
        return self.__world

    def insertSheepinWorld(self, position):
        array = position.split(",", 2)
        x = int(array[0])
        y = int(array[1])
        print(x, y)
        self.__world[x][y] = "S"

    def changeMyPosition(self, newposition):
        array = newposition.split (",", 2)
        x = int (array[0])
        y = int (array[1])
        self.__world[x][y] = "Agent"
