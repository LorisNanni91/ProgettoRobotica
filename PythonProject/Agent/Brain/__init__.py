NOT_FOUND = 'Non trovata'

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
        self.__prolog = Prolog ()
        self.__behaviour = Behaviour.Behaviour (self.__prolog)
        self.__learning = Learning.Learning (self.__prolog)
        self.__memory = Memory.Memory (myposition, planedimension)

    def useLearning(self):
        return self.__learning

    def useMemory(self):
        return self.__memory

    def useBehaviour(self):
        return self.__behaviour

    def react(self, positionArray, factClass):

        if self.__memory.getGoalPosition() is not None:
            targetposition = self.useMemory().getTargetPosition()

            if positionArray[4][2] == 'SHEEP':
                targetposition = self.useMemory().calcolateTarget(positionArray[4])

            if targetposition is not None:
                for i in range(len(positionArray)):
                    if int(positionArray[i][0]) == int(targetposition[0]) \
                            and int(positionArray[i][1]) == int(targetposition[1]):
                        if positionArray[i][2] == 'EMPTY':
                            positionArray[i][2] = "TARGET"
                        break

            # targetposition = self.useMemory().getTargetPosition()
            #
            # if targetposition == None:
            #     for i in range(len(positionArray)):
            #         if positionArray[i][2] == "SHEEP":
            #             print(" sto calcolando il target ")
            #             targetposition = self.useMemory().calcolateTarget(positionArray[i])
            #             break
            # if targetposition == None:
            #     targetposition = self.useMemory().calcolateTarget(self.findNearestSheep(self.__memory.getMyPosition()))
            #
            # print("TARGET POSITION: "+str(targetposition)) #target position
            #
            # if targetposition != None:
            #     for i in range(len(positionArray)):
            #         if int(positionArray[i][0]) == int(targetposition[0]) and int(positionArray[i][1]) == int(targetposition[1]):
            #             positionArray[i][2] = "TARGET"
            #             break

        # compongo e imparo nuovo fatto
        fact = Brain.composeFact(positionArray)
        self.__memory.putFact(fact)
        self.__learning.learnNewFact(fact)

        # consulto il prolog
        decisionarray = self.__behaviour.takeDecision(factClass)

        print("prolog restituisce " + str(decisionarray))

        if decisionarray != "Error":

            # se ho più di una decisione, valuto quale restituire
            if len(decisionarray) > 1:
                decision = self.evaluateDecision(positionArray, decisionarray)
                print("questa sono le decisioni " + str(decisionarray) + "e questa è quella scelta " + decision)

            else:
                decision = decisionarray[0]

            self.__memory.putDecision(decision)
            self.__memory.setMyOrientation(self.__memory.calculateRotation())
            return decision
        else:
            return "Error"

    def evaluateDecision(self, positionArray, arraydecision):

        myposition = self.useMemory().getMyPosition()
        myorientation = self.useMemory().getMyOrientation()
        ipoteticposition = None

        copydecision = arraydecision

        while not copydecision:
            decision = copydecision.pop(random.randint(0, len(copydecision) - 1))

            if decision == "Forward":
                ipoteticposition = self.calcolateIpoteticPositionF(myposition, myorientation)
            elif decision == "Left":
                ipoteticposition = self.calcolateIpoteticPositionL(myposition, myorientation)
            elif decision == "Right":
                ipoteticposition = self.calcolateIpoteticPositionR(myposition, myorientation)
            elif decision == "Forward-Left":
                ipoteticposition = self.calcolateIpoteticPositionFL(myposition, myorientation)
            elif decision == "Forward-Right":
                ipoteticposition = self.calcolateIpoteticPositionFR(myposition, myorientation)

            if self.useMemory().getGoalPosition() != None:
                # ho trovato il goal
                targetposition = self.useMemory().getTargetPosition()

                if targetposition == None:
                    # non ho un target, scelgo la decisione se mi avvicina alla pecora più vicina che ricordo
                    elem = "SHEEP"
                    if not any(elem in x for x in positionArray):
                        if self.isConvenient(ipoteticposition, myposition):
                            return decision
                else:
                    # ho un target, scelgo la decisione se mi avvicina al target
                    elem = "TARGET"
                    if not any(elem in x for x in positionArray):
                        if self.isConvenient(ipoteticposition, myposition, targetposition):
                            return decision
            else:
                # non ho trovato il goal, scelgo la decisione se mi avvicina a una zona non visitata
                if decision.split("-")[0] != "Rotate":
                    print("ci sono arrivato")
                    if not self.__memory.recentlyVisited(ipoteticposition):
                        # if self.__memory.getWorld()[ipoteticposition[0]][ipoteticposition[1]] != 'V':
                        return decision

        # nessuna scelta sembra essere valida, scegliamo a caso
        return arraydecision[random.randint(0, len(arraydecision) - 1)]

        # for i in range(len(arraydecision)):
        #
        #     if arraydecision[i] == "Forward":
        #         ipoteticposition = self.calcolateIpoteticPositionF(myposition, myorientation)
        #     elif arraydecision[i] == "Left":
        #         ipoteticposition = self.calcolateIpoteticPositionL(myposition, myorientation)
        #     elif arraydecision[i] == "Right":
        #         ipoteticposition = self.calcolateIpoteticPositionR(myposition, myorientation)
        #     elif arraydecision[i] == "Forward-Left":
        #         ipoteticposition = self.calcolateIpoteticPositionFL(myposition, myorientation)
        #     elif arraydecision[i] == "Forward-Right":
        #         ipoteticposition = self.calcolateIpoteticPositionFR(myposition, myorientation)
        #
        #     if self.useMemory().getGoalPosition() != None:
        #         elem = "SHEEP"
        #         #se ho trovato il goal, e non vedo una pecora, controllo la mia memoria e vedo se la decisione mi avvicina alla pecora più vicina a me
        #         if not any(elem in x for x in positionArray):
        #             if self.isConvenient(ipoteticposition, myposition):
        #                 return arraydecision[i]
        #
        #     if arraydecision[i].split("-")[0] != "Rotate":
        #         print("ci sono arrivato")
        #         if self.__memory.recentlyVisited(ipoteticposition) == False:
        #             # if self.__memory.getWorld()[ipoteticposition[0]][ipoteticposition[1]] != 'V':
        #             return arraydecision[i]
        #
        # print("decisione casuale")
        # return arraydecision[random.randint(0, len(arraydecision) - 1)]

    def isConvenient(self, ipoteticposition, myposition, targetposition=None):

        if targetposition is None:
            sheepposition = self.findNearestSheep(myposition)
            if sheepposition != NOT_FOUND:
                currentdiffx = abs(int(sheepposition[0]) - int(myposition[0]))
                currentdiffy = abs(int(sheepposition[1]) - int(myposition[1]))
                ipoteticdiffx = abs(int(sheepposition[0]) - ipoteticposition[0])
                ipoteticdiffy = abs(int(sheepposition[1]) - ipoteticposition[1])
            else:
                return False
        else:
            currentdiffx = abs(int(targetposition[0]) - int(myposition[0]))
            currentdiffy = abs(int(targetposition[1]) - int(myposition[1]))
            ipoteticdiffx = abs(int(targetposition[0]) - ipoteticposition[0])
            ipoteticdiffy = abs(int(targetposition[1]) - ipoteticposition[1])

        if ipoteticdiffx <= currentdiffx and ipoteticdiffy <= currentdiffy:
            return True
        else:
            return False

    def findNearestSheep(self, myposition):
        sheepposition = []
        raggio = 2

        # print(self.__world.index("SHEEP"))
        while sheepposition == []:

            xmin = (int(myposition[0]) - raggio) if (int(myposition[0]) - raggio) >= 0 else 0
            xmax = (int(myposition[0]) + raggio) \
                if (int(myposition[0]) + raggio) < int(self.__memory.getPlaneSize()[0]) \
                else (int(self.__memory.getPlaneSize()[0]) - 1)
            ymin = (int(myposition[1]) - raggio) if (int(myposition[1]) - raggio) >= 0 else 0
            ymax = (int(myposition[1]) + raggio) \
                if (int(myposition[1]) + raggio) < int(self.__memory.getPlaneSize()[1]) \
                else (int(self.__memory.getPlaneSize()[1]) - 1)

            for i in range(xmin, xmax + 1):

                y = Brain.indexOf(self.__memory.getWorld()[i], "SHEEP", ymin, ymax)

                if y != NOT_FOUND:
                    sheepposition.append(i)
                    sheepposition.append(y)
                    return sheepposition

            if xmin == 0 and xmax == (int(self.__memory.getPlaneSize()[0]) - 1) and ymin == 0 and ymax == (
                    int(self.__memory.getPlaneSize()[1]) - 1):
                return NOT_FOUND

            raggio += 1

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
            newposition = [int(myposition[0]) + 1, int(myposition[1]) + 1]
        elif myorientation == 90:
            newposition = [int(myposition[0]) + 1, int(myposition[1]) - 1]
        elif myorientation == 180:
            newposition = [int(myposition[0]) - 1, int(myposition[1]) - 1]
        elif myorientation == 270:
            newposition = [int(myposition[0]) - 1, int(myposition[1]) + 1]

        return newposition

    def calcolateIpoteticPositionFL(self, myposition, myorientation):
        newposition = []
        if myorientation == 0:
            newposition = [int(myposition[0]) - 1, int(myposition[1]) + 1]
        elif myorientation == 90:
            newposition = [int(myposition[0]) + 1, int(myposition[1]) + 1]
        elif myorientation == 180:
            newposition = [int(myposition[0]) + 1, int(myposition[1]) - 1]
        elif myorientation == 270:
            newposition = [int(myposition[0]) - 1, int(myposition[1]) - 1]

        return newposition

    def calcolateIpoteticPositionR(self, myposition, myorientation):
        newposition = []
        if myorientation == 0:
            newposition = [int(myposition[0]) + 1, int(myposition[1])]
        elif myorientation == 90:
            newposition = [int(myposition[0]), int(myposition[1]) - 1]
        elif myorientation == 180:
            newposition = [int(myposition[0]) - 1, int(myposition[1])]
        elif myorientation == 270:
            newposition = [int(myposition[0]), int(myposition[1]) + 1]

        return newposition

    def calcolateIpoteticPositionL(self, myposition, myorientation):
        newposition = []
        if myorientation == 0:
            newposition = [int(myposition[0]) - 1, int(myposition[1])]
        elif myorientation == 90:
            newposition = [int(myposition[0]), int(myposition[1]) + 1]
        elif myorientation == 180:
            newposition = [int(myposition[0]) + 1, int(myposition[1])]
        elif myorientation == 270:
            newposition = [int(myposition[0]), int(myposition[1]) - 1]

        return newposition

    @staticmethod
    def indexOf(list, element, ymin, ymax):
        for i in range(ymin, ymax):
            if list[i] == element:
                return i

        return NOT_FOUND

    @staticmethod
    def composeFact(positionArray):

        fact = "perception("
        for i in range(len(positionArray)):
            fact = fact + "'" + positionArray[i][2] + "',"
        fact = fact[:-1]
        fact = fact + ")"
        return fact
