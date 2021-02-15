import server as S
import Agent

NUM_SHEEP = 3

#Message type separators
TYPE_SEPARATOR = "|"
INTERNAL_SEPARATOR = ","

# Message type
PLANE_SIZE = 'PLANE_SIZE'
DOG_POSITION = 'DOG_POSITION'
DOG_SENSOR = 'DOG_SENSOR'
GOAL_REACHED = 'GOAL_REACHED'
GOAL_FOUND = 'GOAL_FOUND'

initialized = False
planedimension = None
dogposition = None

moveCounter = 0

# ho bisogno di inizializzare l'agente prima di incominciare
while not initialized:

    data = S.sock.ReadReceivedData()  # read data

    if data != None:  # if NEW data has been received since last ReadReceivedData function call
        print( "primo ciclo " + data)
        array = data.split(TYPE_SEPARATOR)

        if array[0] == PLANE_SIZE:
            planedimension = array[1].split(INTERNAL_SEPARATOR)

        elif array[0] == DOG_POSITION:
            dogposition = array[1].split(INTERNAL_SEPARATOR)

        if planedimension != None and dogposition != None:
            initialized = True

print("dimensione piano " + str(planedimension) + " posizione cane " + str(dogposition))
# ho ricevuto da Unity i dati necessari quindi creo l'agente
cane = Agent.Agent(dogposition, planedimension)


i = 0
while i < NUM_SHEEP:

    data = S.sock.ReadReceivedData()  # read data
    if data != None:
        print(data)
        array = data.split(TYPE_SEPARATOR)
        if array[0] == DOG_SENSOR:
            decision = cane.reaction(array[1])
            S.sock.SendData(decision)
            if decision != "Errore":
                print("DECISION " + str(moveCounter) + ": " + str(decision) + '\n')
                moveCounter += 1

        elif array[0] == GOAL_REACHED:
            i += 1

        elif array[0] == GOAL_FOUND:
            print("goal trovato")
            cane.goalFound(array[1].split(INTERNAL_SEPARATOR))

        elif array[0] == DOG_POSITION:
            cane.useBrain().useMemory().changeMyPosition(array[1].split(INTERNAL_SEPARATOR))

print("Congratulazioni! La simulazione è terminata in " + int(moveCounter) + " mosse.")