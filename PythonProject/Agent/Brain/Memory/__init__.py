

NUM_LAST_POSITION = 3

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
        # in base all'ultima decisione presa, calcolo di quanto devo ruotare
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
        # metto a vuoto la cella del mondo corrispondente alla mia posizione
        self.__world[int(self.__myposition[0])][int(self.__myposition[1])] = "EMPTY"

        # se ho raggiunto le x posizioni da ricordare, devo rimuovere la più vecchia prima di inserire la nuova
        if len(self.__mylastpositions) == NUM_LAST_POSITION:
            self.__mylastpositions.pop(0)

        self.__mylastpositions.append(self.__myposition)
        # cambio la mia posizione in quella nuova
        self.__myposition = newposition
        self.__world[int(newposition[0])][int(newposition[1])] = "A"

        # se ho raggiunto la posizione target, allora lo resetto
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
        self.__facts.append(fact)
        return

    def getLastDecision(self):
        if len(self.__decisions) > 0:
            return self.__decisions[len(self.__decisions)-1]
        else:
            return []

    def putDecision(self, decision):
        decision = str(decision)
        self.__decisions.append(decision)
        return

    def getWorld(self):
        return self.__world

    def createWorld(self, planedimension):

        # creo una lista di liste di 0 per il mondo nella memoria
        self.__planedim = planedimension
        self.__world = [[0] * int(planedimension[0]) for i in range(int(planedimension[1]))]
        self.changeMyPosition(self.__myposition)
        return

    def updateWorld(self, arraySensor):

        for i in range(len(arraySensor)):
            # controllo se i sensori hanno rilevato una posizione che esce dal piano in quel caso la ignoro
            if int(arraySensor[i][0]) < 0 or int(arraySensor[i][1]) < 0 or int(arraySensor[i][0]) > int(self.__planedim[0]) - 1 or int(arraySensor[i][1]) > int(self.__planedim[1]) - 1:
                continue

            self.__world[int(arraySensor[i][0])][int(arraySensor[i][1])] = arraySensor[i][2]
        return

    def getTargetPosition(self):
        return self.__targetposition

    def recentlyVisited(self, ipoteticposition):

        # controllo se la posizione dove voglio andare è tra quelle visitate di recente
        for i in range(len(self.__mylastpositions)):
            if ipoteticposition[0] == self.__mylastpositions[i][0] and ipoteticposition[1] == self.__mylastpositions[i][1]:
                return True

        return False

    def calcolateTarget(self, sheepposition):

        # funzione per calcolare la posizione in cui il cane deve mettersi affinchè spinga la pecora correttamente
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

        print('posizione pecora ' + str(sheepposition))
        print("calcolata prima t" + str(targetposition))

        # controllo se la posizione del target è accessibile, altrimenti devo ricalcolarla
        if self.__world[int(targetposition[0])][int(targetposition[1])] == 'EMPTY' or self.__world[int(targetposition[0])][int(targetposition[1])] == '0':
            self.__targetposition = targetposition
        else:
            # calcolo le due posizioni adiacenti
            if delta[0] == 0:
                if Memory.isInRange(int(targetposition[1]) + 1):
                    firstPoss = [int(targetposition[0]), int(targetposition[1]) + 1]

                if Memory.isInRange(int(targetposition[1]) - 1):
                    secPoss = [int(targetposition[0]), int(targetposition[1]) - 1]
            elif delta[1] == 0:
                if Memory.isInRange (int(targetposition[0]) + 1):
                    firstPoss = [int(targetposition[0]) + 1, int(targetposition[1])]
                if Memory.isInRange (int(targetposition[0]) - 1):
                    secPoss = [int(targetposition[0]) - 1, int(targetposition[1])]
            else:
                if Memory.isInRange (int(targetposition[0]) + int(delta[0])):
                    firstPoss = [int(targetposition[0]) + int(delta[0]), int(targetposition[1])]
                if Memory.isInRange (int(targetposition[1]) + int(delta[1])):
                    secPoss = [int(targetposition[0]), int(targetposition[1]) + int(delta[1])]

            print ("calcolata first t" + str (firstPoss))
            print ("calcolata sec t" + str (secPoss))

            # controllo se le posizioni calcolate sono libere, altrimenti ritorno None
            if self.__world[int(firstPoss[0])][int(firstPoss[1])] == 'EMPTY' or self.__world[int(firstPoss[0])][int(firstPoss[1])] == '0':
                return firstPoss
            elif self.__world[int(secPoss[0])][int(secPoss[1])] == 'EMPTY' or self.__world[int(secPoss[0])][int(secPoss[1])] == '0':
                return secPoss
            else:
                return None



        return self.__targetposition

    def calcolateIpoteticPositionF(self):
        newposition = []
        if self.__myorientation == 0:
            newposition = [int(self.__myposition[0]), int(self.__myposition[1]) + 1]
        elif self.__myorientation == 90:
            newposition = [int(self.__myposition[0]) + 1, int(self.__myposition[1])]
        elif self.__myorientation == 180:
            newposition = [int(self.__myposition[0]), int(self.__myposition[1]) - 1]
        elif self.__myorientation == 270:
            newposition = [int(self.__myposition[0]) - 1, int(self.__myposition[1])]

        return newposition

    def calcolateIpoteticPositionFR(self):
        newposition = []
        if self.__myorientation == 0:
            newposition = [int(self.__myposition[0]) + 1, int(self.__myposition[1]) + 1]
        elif self.__myorientation == 90:
            newposition = [int(self.__myposition[0]) + 1, int(self.__myposition[1]) - 1]
        elif self.__myorientation == 180:
            newposition = [int(self.__myposition[0]) - 1, int(self.__myposition[1]) - 1]
        elif self.__myorientation == 270:
            newposition = [int(self.__myposition[0]) - 1, int(self.__myposition[1]) + 1]

        return newposition

    def calcolateIpoteticPositionFL(self):
        newposition = []
        if self.__myorientation == 0:
            newposition = [int(self.__myposition[0]) - 1, int(self.__myposition[1]) + 1]
        elif self.__myorientation == 90:
            newposition = [int(self.__myposition[0]) + 1, int(self.__myposition[1]) + 1]
        elif self.__myorientation == 180:
            newposition = [int(self.__myposition[0]) + 1, int(self.__myposition[1]) - 1]
        elif self.__myorientation == 270:
            newposition = [int(self.__myposition[0]) - 1, int(self.__myposition[1]) - 1]

        return newposition

    def calcolateIpoteticPositionR(self):
        newposition = []
        if self.__myorientation == 0:
            newposition = [int(self.__myposition[0]) + 1, int(self.__myposition[1])]
        elif self.__myorientation == 90:
            newposition = [int(self.__myposition[0]), int(self.__myposition[1]) - 1]
        elif self.__myorientation == 180:
            newposition = [int(self.__myposition[0]) - 1, int(self.__myposition[1])]
        elif self.__myorientation == 270:
            newposition = [int(self.__myposition[0]), int(self.__myposition[1]) + 1]

        return newposition

    def calcolateIpoteticPositionL(self):
        newposition = []
        if self.__myorientation == 0:
            newposition = [int(self.__myposition[0]) - 1, int(self.__myposition[1])]
        elif self.__myorientation == 90:
            newposition = [int(self.__myposition[0]), int(self.__myposition[1]) + 1]
        elif self.__myorientation == 180:
            newposition = [int(self.__myposition[0]) + 1, int(self.__myposition[1])]
        elif self.__myorientation == 270:
            newposition = [int(self.__myposition[0]), int(self.__myposition[1]) - 1]

        return newposition


    @staticmethod
    def isInRange(numero):
        if numero >= 0 and numero <= 9:
            return True
        return False


