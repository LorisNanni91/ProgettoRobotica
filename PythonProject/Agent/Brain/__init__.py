from pyswip import Prolog
import Agent.Brain.Behaviour
import Agent.Brain.Learning
import Agent.Brain.Memory
import random


class Brain:

    __learning = None
    __memory = None
    __behaviour = None
    __prolog = None

    def __init__(self, myposition, planedimension):
        self.__prolog = Prolog()
        self.__behaviour = Behaviour.Behaviour(self.__prolog)
        self.__learning = Learning.Learning(self.__prolog)
        self.__memory = Memory.Memory(myposition, planedimension)

    def useLearning(self):
        return self.__learning

    def useMemory(self):
        return self.__memory

    def useBehaviour(self):
        return self.__behaviour

    def react(self, positionArray, factClass):

        if self.__memory.getGoalPosition() != None:
            targetposition = self.useMemory().getTargetPosition()

            if targetposition == None:
                for i in range(len(positionArray)):
                    if positionArray[i][2] == "SHEEP":
                        targetposition = self.useMemory().calcolateTarget(positionArray[i])
                        break
            if targetposition == None:
                targetposition = self.useMemory().calcolateTarget(self.findNearestSheep(self.__memory.getMyPosition()))

            #ho trovato il goal 1a fase, nell array c è pecora? se si punto quella pecora altrimenti dalla mia posizione cerco la pecora più vicina che ricordo, se non ne ricordo nessuna esploro
            for i in range(len(positionArray)):
                if positionArray[i][0] == targetposition[0] and positionArray[i][1] == targetposition[1]:
                    positionArray[i][2] = "TARGET"
        fact = Brain.composeFact(positionArray)
        self.__memory.putFact(fact)
        self.__learning.learnNewFact(fact)
        decisionarray = (self.__behaviour.takeDecision(factClass))
        if len(decisionarray) > 0 and decisionarray != "Error":
            decision = self.evaluateDecision(positionArray, decisionarray)
            # decision = decisionarray[0]
            print("questa è la decisione " + str(decisionarray))
            self.__memory.putDecision(decision)
            #self.__memory.changeMyRotation()
            return decision
        else:
            return "Error"

    def evaluateDecision(self, positionArray, arraydecision):
        myposition = self.useMemory().getMyPosition()
        myorientation = self.useMemory().getMyOrientation()
        ipoteticposition = None
        for i in range(len(arraydecision)):
            if arraydecision[i] == "Forward":
                ipoteticposition = self.calcolateIpoteticPositionF(myposition, myorientation)
            elif arraydecision[i] == "Left":
                ipoteticposition = self.calcolateIpoteticPositionL(myposition, myorientation)
            elif arraydecision[i] == "Right":
                ipoteticposition = self.calcolateIpoteticPositionR(myposition, myorientation)
            elif arraydecision[i] == "Forward-Left":
                ipoteticposition = self.calcolateIpoteticPositionFL(myposition, myorientation)
            elif arraydecision[i] == "Forward-Right":
                ipoteticposition = self.calcolateIpoteticPositionFR(myposition, myorientation)

            if self.useMemory().getGoalPosition() != None:
                elem = "SHEEP"
                if elem not in positionArray:
                    if self.isConvenient(ipoteticposition, myposition):
                            return arraydecision[i]
                else:
                    return arraydecision[0]  # da rivedere
            else:
                if self.__memory.getWorld()[ipoteticposition[0]][ipoteticposition[1]] == '0':
                    return arraydecision[i]

        return arraydecision[random.randint(0, len(arraydecision) - 1)]
        # myposition = self.useMemory().getMyPosition()
        # myorientation = self.useMemory().getMyOrientation()
        #
        # if self.useMemory().getGoalPosition() != None:
        #     elem = "SHEEP"
        #     if elem not in positionArray:
        #         for i in range(len(arraydecision)):
        #             if arraydecision[i] == "Forward":
        #                 ipoteticposition = self.calcolateIpoteticPositionF(myposition, myorientation)
        #             elif arraydecision[i] == "Left":
        #                 ipoteticposition = self.calcolateIpoteticPositionL(myposition, myorientation)
        #             elif arraydecision[i] == "Right":
        #                 ipoteticposition = self.calcolateIpoteticPositionR(myposition, myorientation)
        #             elif arraydecision[i] == "Forward-Left":
        #                 ipoteticposition = self.calcolateIpoteticPositionFL(myposition, myorientation)
        #             elif arraydecision[i] == "Forward-Right":
        #                 ipoteticposition = self.calcolateIpoteticPositionFR(myposition, myorientation)
        #
        #             if self.isConvenient(ipoteticposition, myposition):
        #                 return arraydecision[i]
        #     else:
        #         return arraydecision[0] #da rivedere
        #
        # return arraydecision[random.randint(0, len(arraydecision)-1)]

    def isConvenient(self, ipoteticposition, myposition):
        sheepposition = self.findNearestSheep(myposition)
        currentdiffx = abs(int(sheepposition[0]) - int(myposition[0]))
        currentdiffy = abs(int(sheepposition[1]) - int(myposition[1]))
        ipoteticdiffx = abs(int(sheepposition[0]) - ipoteticposition[0])
        ipoteticdiffy = abs(int(sheepposition[1]) - ipoteticposition[1])
        if ipoteticdiffx <= currentdiffx + 1 and ipoteticdiffy <= currentdiffy +1:
            return True
        else:
            return False

    def findNearestSheep(self, myposition):
        sheepposition = []
        raggio = 2
        #print(self.__world.index("SHEEP"))
        while sheepposition == []:

            xmin = int(myposition[0]) - raggio if int(myposition[0]) - raggio >= 0  and int(myposition[0]) - raggio < self.__memory.getMyOrientation()[0] else int(myposition[0])
            xmax = int(myposition[0]) + raggio if int(myposition[0]) + raggio >= 0  and int(myposition[0]) + raggio < self.__memory.getMyOrientation()[0] else int(myposition[0])
            ymin = int(myposition[1]) - raggio if int(myposition[1]) - raggio >= 0  and int(myposition[1]) - raggio < self.__memory.getMyOrientation()[1] else int(myposition[1])
            ymax = int(myposition[1]) + raggio if int(myposition[1]) + raggio >= 0  and int(myposition[1]) + raggio < self.__memory.getMyOrientation()[1] else int(myposition[1])

            for i in range(xmin, xmax+1):

                y = Brain.indexOf(self.__memory.getWorld()[i], "SHEEP", ymin, ymax)

                if y != "Non trovato":

                    sheepposition.append(i)
                    sheepposition.append(y)

        return sheepposition

    def calcolateIpoteticPositionF(self, myposition, myorientation):
        newposition = []
        if myorientation == 0:
            newposition = [int(myposition[0]), int(myposition[1]) + 1]
        elif myorientation == 90:
            newposition = [int(myposition[0]) + 1, int(myposition[1])]
        elif myorientation == 180:
            newposition = [int(myposition[0]), int(myposition[1]) - 1]
        elif myorientation == 270:
            newposition = [int(myposition[0]) - 1, int(myposition[1])]

        return newposition
    
    def calcolateIpoteticPositionFR(self, myposition, myorientation):
        newposition = []
        if myorientation == 0:
            newposition = [int(myposition[0])+1, int(myposition[1])+1]
        elif myorientation == 90:
            newposition = [int(myposition[0])+1, int(myposition[1])-1]
        elif myorientation == 180:
            newposition = [int(myposition[0])-1, int(myposition[1])-1]
        elif myorientation == 270:
            newposition = [int(myposition[0])-1, int(myposition[1])+1]

        return newposition
    
    def calcolateIpoteticPositionFL(self, myposition, myorientation):
        newposition = []
        if myorientation == 0:
            newposition = [int(myposition[0])-1, int(myposition[1])+1]
        elif myorientation == 90:
            newposition = [int(myposition[0])+1, int(myposition[1])+1]
        elif myorientation == 180:
            newposition = [int(myposition[0])+1, int(myposition[1])-1]
        elif myorientation == 270:
            newposition = [int(myposition[0])-1, int(myposition[1])-1]

        return newposition
    
    def calcolateIpoteticPositionR(self, myposition, myorientation):
        newposition = []
        if myorientation == 0:
            newposition = [int(myposition[0])+1, int(myposition[1])]
        elif myorientation == 90:
            newposition = [int(myposition[0]), int(myposition[1])-1]
        elif myorientation == 180:
            newposition = [int(myposition[0])-1, int(myposition[1])]
        elif myorientation == 270:
            newposition = [int(myposition[0]), int(myposition[1])+1]

        return newposition
    
    def calcolateIpoteticPositionL(self, myposition, myorientation):
        newposition = []
        if myorientation == 0:
            newposition = [int(myposition[0])-1, int(myposition[1])]
        elif myorientation == 90:
            newposition = [int(myposition[0]), int(myposition[1])+1]
        elif myorientation == 180:
            newposition = [int(myposition[0])+1, int(myposition[1])]
        elif myorientation == 270:
            newposition = [int(myposition[0]), int(myposition[1])-1]

        return newposition

    @staticmethod
    def indexOf(list, element, ymin, ymax):
        for i in range (ymin, ymax):
            if list[i] == element:
                return i

        return "Non trovato"

    @staticmethod
    def composeFact(positionArray):

        fact = "perception("
        for i in range(len(positionArray)):
            fact = fact + "'" + positionArray[i][2] + "',"
        fact = fact[:-1]
        fact = fact + ")"
        return fact