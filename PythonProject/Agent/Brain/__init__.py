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
                    if int(positionArray[i][0]) == targetposition[0] \
                            and int(positionArray[i][1]) == targetposition[1]:
                        if positionArray[i][2] == 'EMPTY':
                            positionArray[i][2] = 'TARGET'
                        break

        # compongo e imparo nuovo fatto
        fact = Brain.composeFact(positionArray)
        self.__memory.putFact(fact)
        self.__learning.learnNewFact(fact)

        # consulto il prolog
        decisionarray = self.__behaviour.takeDecision(factClass)

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

        myposition = self.__memory.getMyPosition()
        ipoteticposition = None

        copydecision = list(arraydecision)
        print("lunghezza " + str(len(copydecision)))
        while len(copydecision) > 0:
            decision = copydecision.pop(random.randint(0, len(copydecision) - 1))

            if self.__memory.getLastDecision() != None:
                if decision.split("-")[0] == "Rotate" and self.__memory.getLastDecision().split("-")[0] == "Rotate":
                    continue
            if decision.split("-")[0] == "Rotate" and self.useMemory().getSheepViewed() and self.useMemory().getGoalPosition() != None:
                continue

            if decision == "Forward":
                ipoteticposition = self.__memory.calcolateIpoteticPositionF( )
            elif decision == "Left":
                ipoteticposition = self.__memory.calcolateIpoteticPositionL( )
            elif decision == "Right":
                ipoteticposition = self.__memory.calcolateIpoteticPositionR( )
            elif decision == "Forward-Left":
                ipoteticposition = self.__memory.calcolateIpoteticPositionFL( )
            elif decision == "Forward-Right":
                ipoteticposition = self.__memory.calcolateIpoteticPositionFR( )

            if self.useMemory().getGoalPosition() != None:
                # ho trovato il goal
                targetposition = self.useMemory().getTargetPosition()

                if decision.split ("-")[0] != "Rotate":
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
                    indicequadranteattuale = self.useMemory().calcolateQuadrante(self.useMemory().getMyPosition())
                    indicequadrante = self.useMemory().calcolateQuadrante(ipoteticposition)
                    quadranti = self.useMemory().getQuadrante()
                    if indicequadrante != indicequadranteattuale:
                        # se i punti da esplorare nella mia zona sono meno della soglia, e a l altra zona ha più punti inesplorati, ritorno la decisione
                        if quadranti[indicequadranteattuale] <= self.useMemory().getSoglia() and quadranti[indicequadrante] > quadranti[indicequadranteattuale]:
                            return decision

                    elif quadranti[indicequadranteattuale] > self.useMemory().getSoglia():
                        # se è lo stesso quadrante e non l'ho esplorato a sufficienza ritorno la decisione
                        return decision

                    elif self.useMemory().nearInesplorate(ipoteticposition):
                        return decision

                    # if self.useMemory().getQuadrante()[indicequadrante]
                    # # if self.isConvenient(ipoteticposition, myposition, self.useMemory().getQuadrante(ipoteticposition))
                    # if not self.__memory.recentlyVisited(ipoteticposition):
                    #     # if self.__memory.getWorld()[ipoteticposition[0]][ipoteticposition[1]] != 'V':
                    #     return decision

        # nessuna scelta sembra essere valida, scegliamo a caso
        return arraydecision[random.randint(0, len(arraydecision) - 1)]

    def isConvenient(self, ipoteticposition, myposition, targetposition=None):

        if targetposition is None:
            sheepposition = self.findNearestSheep(myposition)
            if sheepposition != NOT_FOUND:
                currentdiffx = abs(int(sheepposition[0]) - int(myposition[0]))
                currentdiffy = abs(int(sheepposition[1]) - int(myposition[1]))
                ipoteticdiffx = abs(int(sheepposition[0]) - int(ipoteticposition[0]))
                ipoteticdiffy = abs(int(sheepposition[1]) - int(ipoteticposition[1]))
            else:
                return False
        else:
            currentdiffx = abs(int(targetposition[0]) - int(myposition[0]))
            currentdiffy = abs(int(targetposition[1]) - int(myposition[1]))
            ipoteticdiffx = abs(int(targetposition[0]) - int(ipoteticposition[0]))
            ipoteticdiffy = abs(int(targetposition[1]) - int(ipoteticposition[1]))

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

                y = Brain.indexOf(self.__memory.getWorld()[i], 'SHEEP', ymin, ymax)

                if y != NOT_FOUND:
                    sheepposition.append(i)
                    sheepposition.append(y)
                    return sheepposition

            if xmin == 0 and xmax == (int(self.__memory.getPlaneSize()[0]) - 1) and ymin == 0 and ymax == (
                    int(self.__memory.getPlaneSize()[1]) - 1):
                return NOT_FOUND

            raggio += 1

    
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
