NUM_LAST_POSITION = 3
SOGLIA_MIN = 2
EMPTY = 'EMPTY'
SHEEP = 'SHEEP'

import math

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
    # quandranti: 0 [6,6-9,9], 1 [0,6-5,9], 2 [0,0-5,5], 3 [6,0-9,5]
    __quadranti = []
    __valoresoglia = None
    __sheepviewed = False

    def __init__(self, myposition, planedimension):
        self.__decisions = []
        self.__facts = []
        self.__myposition = [int(myposition[0]), int(myposition[1])]
        self.__myorientation = 0
        self.createWorld(planedimension)
        self.initializeQuadranti()

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
        self.__world[self.__myposition[0]][self.__myposition[1]] = EMPTY

        # se ho raggiunto le x posizioni da ricordare, devo rimuovere la più vecchia prima di inserire la nuova
        if len(self.__mylastpositions) == NUM_LAST_POSITION:
            self.__mylastpositions.pop(0)

        self.__mylastpositions.append(self.__myposition)
        # cambio la mia posizione in quella nuova
        self.__myposition = [int(newposition[0]), int(newposition[1])]
        self.__world[int(newposition[0])][int(newposition[1])] = "A"

        # se ho raggiunto la posizione target, allora lo resetto
        if self.__targetposition != None:
            if self.__myposition[0] == int(self.__targetposition[0]) and self.__myposition[1] == int(self.__targetposition[1]):
                self.__targetposition = None

        return

    def getGoalPosition(self):
        return self.__goalposition

    def setGoalPosition(self, position):
        self.__goalposition = [int(position[0]), int(position[1])]
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
            return None

    def putDecision(self, decision):
        decision = str(decision)
        self.__decisions.append(decision)
        return

    def getWorld(self):
        return self.__world

    def createWorld(self, planedimension):

        # creo una lista di liste di 0 per il mondo nella memoria
        self.__planedim = [int(planedimension[0]), int(planedimension[1])]
        self.__world = [[0] * self.__planedim[0] for i in range(self.__planedim[1])]
        self.changeMyPosition(self.__myposition)
        return

    def initializeQuadranti(self):
        # si assume che le dimensioni del piano siano pari
        quadrante = (self.__planedim[0]/2) * (self.__planedim[1]/2)
        for i in range(0, 4):
            self.__quadranti.append(quadrante)
        self.__valoresoglia = quadrante / SOGLIA_MIN
        return

    def updateQuadranti(self, vettore):
        indice = self.calcolateQuadrante(vettore)
        self.__quadranti[indice] -= 1
        return

    def getQuadrante(self):
        return self.__quadranti

    def calcolateQuadrante(self, vettore):
        # da ragionarci?
        if int(vettore[0]) < int(self.__planedim[0]/2) and int(vettore[1]) < int(self.__planedim[1]/2):
            return 2
        elif int(vettore[0]) >= int(self.__planedim[0]/2) and int(vettore[1]) >= int(self.__planedim[1]/2):
            return 0
        elif int(vettore[0]) < int(self.__planedim[0]/2) and int(vettore[1]) >= int(self.__planedim[1]/2):
            return 1
        elif int(vettore[0]) >= int(self.__planedim[0]/2) and int(vettore[1]) < int(self.__planedim[1]/2):
            return 3

    def getSoglia(self):
        return self.__valoresoglia

    def getInesplorateQuadrante(self):
        max = 0
        for i in range(1, len(self.__quadranti)):
            if self.__quadranti[i] > self.__quadranti[max]:
                max = i
        return max

    def nearInesplorate(self, ipoteticposition):
        quandranteinesplorato = self.getInesplorateQuadrante()
        deltaattuale = None
        deltaipotetico = None

        if quandranteinesplorato == 0:
            x = math.pow((self.__planedim[0] - 1) - self.__myposition[0], 2)
            y = math.pow((self.__planedim[0] - 1) - self.__myposition[1], 2)
            deltaattuale = math.sqrt(y + x)

            x = math.pow((self.__planedim[0] - 1) - int(ipoteticposition[0]), 2)
            y = math.pow((self.__planedim[0] - 1) - int(ipoteticposition[1]), 2)
            deltaipotetico = math.sqrt(y + x)

        elif quandranteinesplorato == 1:
            x = math.pow(0 - self.__myposition[0], 2)
            y = math.pow((self.__planedim[0] - 1) - self.__myposition[1], 2)
            deltaattuale = math.sqrt(y + x)

            x = math.pow(0 - int(ipoteticposition[0]), 2)
            y = math.pow((self.__planedim[0] - 1) - int(ipoteticposition[1]), 2)
            deltaipotetico = math.sqrt(y + x)

        elif quandranteinesplorato == 2:
            x = math.pow(0 - self.__myposition[0], 2)
            y = math.pow(0 - self.__myposition[1], 2)
            deltaattuale = math.sqrt(y + x)

            x = math.pow(0 - int(ipoteticposition[0]), 2)
            y = math.pow(0 - int(ipoteticposition[1]), 2)
            deltaipotetico = math.sqrt(y + x)

        elif quandranteinesplorato == 3:
            x = math.pow((self.__planedim[0] - 1) - self.__myposition[0], 2)
            y = math.pow(0 - self.__myposition[1], 2)
            deltaattuale = math.sqrt(y + x)

            x = math.pow((self.__planedim[0] - 1) - int(ipoteticposition[0]), 2)
            y = math.pow(0 - int(ipoteticposition[1]), 2)
            deltaipotetico = math.sqrt(y + x)

        if deltaipotetico <= deltaattuale:
            return True
        else:
            return False


    def updateWorld(self, arraySensor):

        self.__sheepviewed = False

        for i in range(len(arraySensor)):
            # controllo se i sensori hanno rilevato una posizione che esce dal piano in quel caso la ignoro
            if int(arraySensor[i][0]) < 0 or int(arraySensor[i][1]) < 0 or int(arraySensor[i][0]) > self.__planedim[0] - 1 or int(arraySensor[i][1]) > self.__planedim[1] - 1:
                continue
            if self.__world[int(arraySensor[i][0])][int(arraySensor[i][1])] == 0:
                vettore = [int(arraySensor[i][0]), int(arraySensor[i][1])]
                self.updateQuadranti(vettore)
            if arraySensor[i][2] == SHEEP:
                self.__sheepviewed = True
            self.__world[int(arraySensor[i][0])][int(arraySensor[i][1])] = arraySensor[i][2]
        return

    def getTargetPosition(self):
        return self.__targetposition

    def getSheepViewed(self):
        return self.__sheepviewed

    def recentlyVisited(self, ipoteticposition):

        if len(self.__mylastpositions) > 0:
            # controllo se la posizione dove voglio andare è tra quelle visitate di recente
            for i in range(len(self.__mylastpositions)):
                if int(ipoteticposition[0]) == self.__mylastpositions[i][0] and int(ipoteticposition[1]) == self.__mylastpositions[i][1]:
                    return True

        return False

    def calcolateTarget(self, sheepposition):

        # funzione per calcolare la posizione in cui il cane deve mettersi affinchè spinga la pecora correttamente
        deltax = int(sheepposition[0]) - self.__goalposition[0]
        deltay = int(sheepposition[1]) - self.__goalposition[1]
        delta = []

        if deltax > 0:
            delta.append(1)
        elif deltax < 0:
            delta.append(-1)
        elif deltax == 0:
            delta.append(0)

        if deltay > 0:
            delta.append(1)
        elif deltay < 0:
            delta.append(-1)
        elif deltay == 0:
            delta.append(0)

        targetpositionx = (int(sheepposition[0]) + delta[0]) if (int(sheepposition[0]) + delta[0]) < self.__planedim[0] else int(sheepposition[0])
        targetpositiony = (int(sheepposition[1]) + delta[1]) if (int(sheepposition[1]) + delta[1]) < self.__planedim[1] else int(sheepposition[1])
        targetposition = [int(targetpositionx), int(targetpositiony)]

        print('posizione pecora ' + str(sheepposition))
        print("calcolata prima t" + str(targetposition))

        # controllo se la posizione del target è accessibile, altrimenti devo ricalcolarla
        if self.__world[targetposition[0]][targetposition[1]] == EMPTY:
            self.__targetposition = targetposition
        else:
            # calcolo le due posizioni adiacenti
            firstPoss = None
            secPoss = None
            if delta[0] == 0:
                if Memory.isInRange(targetposition[1] + 1):
                    firstPoss = [targetposition[0], targetposition[1] + 1]
                if Memory.isInRange(targetposition[1] - 1):
                    secPoss = [targetposition[0], targetposition[1] - 1]

            elif delta[1] == 0:
                if Memory.isInRange(targetposition[0] + 1):
                    firstPoss = [targetposition[0] + 1, targetposition[1]]
                if Memory.isInRange(targetposition[0] - 1):
                    secPoss = [targetposition[0] - 1, targetposition[1]]

            else:
                if Memory.isInRange(targetposition[0] + delta[0]):
                    firstPoss = [targetposition[0] + delta[0], targetposition[1]]
                if Memory.isInRange(targetposition[1] + delta[1]):
                    secPoss = [targetposition[0], targetposition[1] + delta[1]]

            # print ("calcolata first t" + str (firstPoss))
            # print ("calcolata sec t" + str (secPoss))

            # controllo se le posizioni calcolate sono libere, altrimenti ritorno None
            if firstPoss != None and self.__world[int(firstPoss[0])][int(firstPoss[1])] == EMPTY:
                return firstPoss
            elif secPoss != None and self.__world[int(secPoss[0])][int(secPoss[1])] == EMPTY:
                return secPoss
            else:
                ipoteticposition = self.calcolateIpoteticPositionF()
                if self.__world[int(ipoteticposition[0])][int(ipoteticposition[1])] == EMPTY:
                    return ipoteticposition
                ipoteticposition = self.calcolateIpoteticPositionFL()
                if self.__world[int(ipoteticposition[0])][int(ipoteticposition[1])] == EMPTY:
                    return ipoteticposition
                ipoteticposition = self.calcolateIpoteticPositionFR()
                if self.__world[int(ipoteticposition[0])][int(ipoteticposition[1])] == EMPTY:
                    return ipoteticposition



        return self.__targetposition

    def calcolateIpoteticPositionF(self):
        newposition = []
        if self.__myorientation == 0:
            newposition = [self.__myposition[0], self.__myposition[1] + 1]
        elif self.__myorientation == 90:
            newposition = [self.__myposition[0] + 1, self.__myposition[1]]
        elif self.__myorientation == 180:
            newposition = [self.__myposition[0], self.__myposition[1] - 1]
        elif self.__myorientation == 270:
            newposition = [self.__myposition[0] - 1, self.__myposition[1]]

        return newposition

    def calcolateIpoteticPositionFR(self):
        newposition = []
        if self.__myorientation == 0:
            newposition = [self.__myposition[0] + 1, self.__myposition[1] + 1]
        elif self.__myorientation == 90:
            newposition = [self.__myposition[0] + 1, self.__myposition[1] - 1]
        elif self.__myorientation == 180:
            newposition = [self.__myposition[0] - 1, self.__myposition[1] - 1]
        elif self.__myorientation == 270:
            newposition = [self.__myposition[0] - 1, self.__myposition[1] + 1]

        return newposition

    def calcolateIpoteticPositionFL(self):
        newposition = []
        if self.__myorientation == 0:
            newposition = [self.__myposition[0] - 1, self.__myposition[1] + 1]
        elif self.__myorientation == 90:
            newposition = [self.__myposition[0] + 1, self.__myposition[1] + 1]
        elif self.__myorientation == 180:
            newposition = [self.__myposition[0] + 1, self.__myposition[1] - 1]
        elif self.__myorientation == 270:
            newposition = [self.__myposition[0] - 1, self.__myposition[1] - 1]

        return newposition

    def calcolateIpoteticPositionR(self):
        newposition = []
        if self.__myorientation == 0:
            newposition = [self.__myposition[0] + 1, self.__myposition[1]]
        elif self.__myorientation == 90:
            newposition = [self.__myposition[0], self.__myposition[1] - 1]
        elif self.__myorientation == 180:
            newposition = [self.__myposition[0] - 1, self.__myposition[1]]
        elif self.__myorientation == 270:
            newposition = [self.__myposition[0], self.__myposition[1] + 1]

        return newposition

    def calcolateIpoteticPositionL(self):
        newposition = []
        if self.__myorientation == 0:
            newposition = [self.__myposition[0] - 1, self.__myposition[1]]
        elif self.__myorientation == 90:
            newposition = [self.__myposition[0], self.__myposition[1] + 1]
        elif self.__myorientation == 180:
            newposition = [self.__myposition[0] + 1, self.__myposition[1]]
        elif self.__myorientation == 270:
            newposition = [self.__myposition[0], self.__myposition[1] - 1]

        return newposition


    @staticmethod
    def isInRange(numero):
        if numero >= 0 and numero <= 9:
            return True
        return False


