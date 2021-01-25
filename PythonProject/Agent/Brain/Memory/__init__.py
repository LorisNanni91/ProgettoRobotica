import random
import sys

class Memory:

    __decisions = None
    __facts = None
    __goalposition = None
    __world = None
    __myposition = None
    __myorientation = None
    __planedim = None

    def __init__(self, myposition, planedimension):
        self.__decisions = []
        self.__facts = []
        self.__myposition = myposition
        self.__myorientation = 0
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

    def getLastFact(self):
        return self.__facts[len(self.__facts)-1]

    def getLastDecision(self):
        return self.__decisions[len(self.__decisions)-1]

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
        self.__myposition = newposition
        arraynewposition = Memory.splitStringPosition(newposition)
        self.__world[array[0]][array[1]] = "0"
        self.__world[arraynewposition[0]][arraynewposition[1]] = "A"

    def changeMyRotation(self):
        decision = self.getLastDecision()
        if decision == "Rotate-Right":
            self.__myorientation += 90
        elif decision == "Rotate-Back":
            self.__myorientation += 180
        elif decision == "Rotate-Left":
            self.__myorientation += 270
        self.__myorientation = self.__myorientation % 360

    def updateWorld(self, arraySensor):
        cellsSensor = arraySensor.split(":")
        positionarray = []

        for i in range(len(cellsSensor)):
            singlePosition = cellsSensor[i].split(",")
            positionarray.append(singlePosition)
            if ( int(singlePosition[0]) < 0 or int(singlePosition[1]) < 0 or int(singlePosition[0]) > self.__planedim[0] - 1 or int(singlePosition[1]) > self.__planedim[1] - 1):
                continue
            self.__world[int(singlePosition[0])][int(singlePosition[1])] = singlePosition[2]

        print( self.__world)
        return positionarray

    def evaluateDecision(self, positionArray, arraydecision):

        if self.__goalposition != None:
            elem = "SHEEP"
            if elem not in positionArray:
                for i in range(len(arraydecision)):
                    if arraydecision[i] == "Forward":
                        ipoteticposition = self.calcolateIpoteticPositionF()
                    elif arraydecision[i] == "Left":
                        ipoteticposition = self.calcolateIpoteticPositionL()
                    elif arraydecision[i] == "Right":
                        ipoteticposition = self.calcolateIpoteticPositionR()
                    elif arraydecision[i] == "Forward-Left":
                        ipoteticposition = self.calcolateIpoteticPositionFL()
                    elif arraydecision[i] == "Forward-Right":
                        ipoteticposition = self.calcolateIpoteticPositionFR()

                    if self.isConvenient(ipoteticposition):
                        return arraydecision[i]
            else:
                return arraydecision[0] #da rivedere

        return arraydecision[random.randint(0, len(arraydecision)-1)]

    def isConvenient(self, ipoteticposition):
        myposition = Memory.splitStringPosition(self.__myposition)
        sheepposition = self.findNearestSheep()
        currentdiffx = abs(sheepposition[0] - myposition[0])
        currentdiffy = abs(sheepposition[1] - myposition[1])
        ipoteticdiffx = abs(sheepposition[0] - ipoteticposition[0])
        ipoteticdiffy = abs(sheepposition[1] - ipoteticposition[1])
        if ipoteticdiffx <= currentdiffx and ipoteticdiffy <= currentdiffy:
            return True
        else:
            return False

    def findNearestSheep(self):
        myposition = Memory.splitStringPosition()
        sheepposition = []
        raggio = 2
        print(self.__world.index("SHEEP"))
        while sheepposition == []:

            xmin = myposition[0] - raggio if myposition[0] - raggio >= 0  and myposition[0] - raggio < self.__planedim[0] else myposition[0]
            xmax = myposition[0] + raggio if myposition[0] + raggio >= 0  and myposition[0] + raggio < self.__planedim[0] else myposition[0]
            ymin = myposition[1] - raggio if myposition[1] - raggio >= 0  and myposition[1] - raggio < self.__planedim[1] else myposition[1]
            ymax = myposition[1] + raggio if myposition[1] + raggio >= 0  and myposition[1] + raggio < self.__planedim[1] else myposition[1]

            for i in range(xmin, xmax+1):

                y = Memory.indexOf(self.__world[i], "SHEEP", ymin, ymax)

                if y != "Non trovato":

                    sheepposition.append(i)
                    sheepposition.append(y)

        return sheepposition

    def calcolateIpoteticPositionL(self):
        newposition = []
        myposition = Memory.splitStringPosition(self.__myposition)
        if self.__myorientation == 0:
            newposition = [myposition[0]-1, myposition[1]]
        elif self.__myorientation == 90:
            newposition = [myposition[0], myposition[1]+1]
        elif self.__myorientation == 180:
            newposition = [myposition[0]+1, myposition[1]]
        elif self.__myorientation == 270:
            newposition = [myposition[0], myposition[1]-1]

        return newposition

    def calcolateIpoteticPositionR(self):
        newposition = []
        myposition = Memory.splitStringPosition (self.__myposition)
        if self.__myorientation == 0:
            newposition = [myposition[0]+1, myposition[1]]
        elif self.__myorientation == 90:
            newposition = [myposition[0], myposition[1]-1]
        elif self.__myorientation == 180:
            newposition = [myposition[0]-1, myposition[1]]
        elif self.__myorientation == 270:
            newposition = [myposition[0], myposition[1]+1]

        return newposition

    def calcolateIpoteticPositionFL(self):
        newposition = []
        myposition = Memory.splitStringPosition (self.__myposition)
        if self.__myorientation == 0:
            newposition = [myposition[0]-1, myposition[1]+1]
        elif self.__myorientation == 90:
            newposition = [myposition[0]+1, myposition[1]+1]
        elif self.__myorientation == 180:
            newposition = [myposition[0]+1, myposition[1]-1]
        elif self.__myorientation == 270:
            newposition = [myposition[0]-1, myposition[1]-1]

        return newposition

    def calcolateIpoteticPositionFR(self):
        newposition = []
        myposition = Memory.splitStringPosition (self.__myposition)
        if self.__myorientation == 0:
            newposition = [myposition[0]+1, myposition[1]+1]
        elif self.__myorientation == 90:
            newposition = [myposition[0]+1, myposition[1]-1]
        elif self.__myorientation == 180:
            newposition = [myposition[0]-1, myposition[1]-1]
        elif self.__myorientation == 270:
            newposition = [myposition[0]-1, myposition[1]+1]

        return newposition

    def calcolateIpoteticPositionF(self):
        newposition = []
        myposition = Memory.splitStringPosition (self.__myposition)
        if self.__myorientation == 0:
            newposition = [myposition[0], myposition[1]+1]
        elif self.__myorientation == 90:
            newposition = [myposition[0]+1, myposition[1]]
        elif self.__myorientation == 180:
            newposition = [myposition[0], myposition[1]-1]
        elif self.__myorientation == 270:
            newposition = [myposition[0]-1, myposition[1]]

        return newposition

    @staticmethod
    def splitStringPosition(position):
        array = position.split(",", 2)
        arrayint = [int(array[0]), int(array[1])]
        return arrayint

    @staticmethod
    def indexOf(list, element, ymin, ymax):
        for i in range(ymin, ymax):
            if list[i] == element:
                return i

        return "Non trovato"