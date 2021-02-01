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
    __targetposition = None
    __mylastpositions = []

    def __init__(self, myposition, planedimension):
        self.__decisions = []
        self.__facts = []
        self.__myposition = myposition
        self.__myorientation = 0
        self.createWorld(planedimension)

    def getMyOrientation(self):
        return self.__myorientation

    def setMyOrientation(self, rotazione):
        self.__myorientation = (self.__myorientation + rotazione) % 360
        return

    def calculateRotation(self):
        decision = self.getLastDecision()
        rotation = 0
        if decision == "Rotate-Right":
            rotation = 90
        elif decision == "Rotate-Back":
            rotation = 180
        elif decision == "Rotate-Left":
            rotation = 270
        return rotation

    def getMyPosition(self):
        return self.__myposition

    def changeMyPosition(self, newposition):
        self.__world[int(self.__myposition[0])][int(self.__myposition[1])] = "EMPTY"
        if len(self.__mylastpositions) == 3:
            self.__mylastpositions.pop(0)
        self.__mylastpositions.append(self.__myposition)
        self.__myposition = newposition
        self.__world[int(newposition[0])][int(newposition[1])] = "A"
        if self.__targetposition != None:
            if int(self.__myposition[0]) == int(self.__targetposition[0]) and int(self.__myposition[1]) == int(self.__targetposition[1]):
                self.__targetposition = None
        return

    def getGoalPosition(self):
        return self.__goalposition

    def setGoalPosition(self, position):
        self.__goalposition = position
        return

    def getPlaneSize(self):
        return self.__planedim

    def getLastFact(self):
        return self.__facts[len(self.__facts)-1]

    def putFact(self, fact):
        fact = str(fact)
        self.__decisions.append(fact)
        return

    def getLastDecision(self):
        return self.__decisions[len(self.__decisions)-1]

    # def getAllDecisions(self):
    #     return self.__decisions

    def putDecision(self, decision):
        decision = str(decision)
        self.__decisions.append(decision)
        return

    def getWorld(self):
        return self.__world

    def createWorld(self, planedimension):
        self.__planedim = planedimension
        self.__world = [[0] * int(planedimension[0]) for i in range(int(planedimension[1]))]
        self.changeMyPosition(self.__myposition)
        return

    def updateWorld(self, arraySensor):
        for i in range(len(arraySensor)):
            if (int(arraySensor[i][0]) < 0 or int(arraySensor[i][1]) < 0 or int(arraySensor[i][0]) > int(self.__planedim[0]) - 1 or int(arraySensor[i][1]) > int(self.__planedim[1]) - 1):
                continue
            self.__world[int(arraySensor[i][0])][int(arraySensor[i][1])] = arraySensor[i][2]
        return

    def calcolateTarget(self, sheepposition):
        deltax = int(sheepposition[0]) - int(self.__goalposition[0])
        deltay = int(sheepposition[1]) - int(self.__goalposition[1])
        delta = []
        if deltax > 0:
            delta.append('1')
        elif deltax < 0:
            delta.append('-1')
        elif deltax == 0:
            delta.append('0')

        if deltay > 0:
            delta.append('1')
        elif deltay < 0:
            delta.append('-1')
        elif deltay == 0:
            delta.append('0')

        targetpositionx = (int(sheepposition[0]) + int(delta[0])) if (int(sheepposition[0]) + int(delta[0])) < int(self.__planedim[0]) else int(sheepposition[0])
        targetpositiony = (int(sheepposition[1]) + int(delta[1])) if (int(sheepposition[1]) + int(delta[1])) < int(self.__planedim[1]) else int(sheepposition[1])
        targetposition = [targetpositionx, targetpositiony]
        if self.__world[int(targetposition[0])][int(targetposition[1])] == 'EMPTY' or self.__world[int(targetposition[0])][int(targetposition[1])] == '0':
            self.__targetposition = targetposition
        else:
            targetposition = 1
            #da vedere

        return self.__targetposition

    def getTargetPosition(self):
        return self.__targetposition

    def recentlyVisited(self, ipoteticposition):
        for i in range(len(self.__mylastpositions)):
            if ipoteticposition[0] == self.__mylastpositions[i][0] and ipoteticposition[1] == self.__mylastpositions[i][1]:
                return True

        return False
