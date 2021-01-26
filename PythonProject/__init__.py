import server as S
import Agent

#Message type separation
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

while initialized == False:

    data = S.sock.ReadReceivedData()# read data

    if data != None: # if NEW data has been received since last ReadReceivedData function call
        print( "primo ciclo " + data)
        array = data.split(TYPE_SEPARATOR)

        if array[0] == PLANE_SIZE:
            planedimension = array[1].split(INTERNAL_SEPARATOR)
        elif array[0] == DOG_POSITION:
            dogposition = array[1].split(INTERNAL_SEPARATOR)
        if planedimension != None and dogposition != None:
            initialized = True

print("dimensione piano " + str(planedimension) + " posizione cane " + str(dogposition))
cane = Agent.Agent(dogposition, planedimension)
cane.useBrain().useLearning().learnFromFile("test.pl")

i = 0
while i < 5:

    data = S.sock.ReadReceivedData()  # read data
    if data != None:
        print(data )
        array = data.split(TYPE_SEPARATOR)
        if array[0] == DOG_SENSOR:
            decision = cane.reaction(array[1])
            S.sock.SendData(decision)
            if decision != "Errore":
                print ("DECISION " + str (moveCounter) + " :" + str (decision) + '\n')
                moveCounter += 1
            # cane.useSensor().whatIsee(array[1])
            # positionArray = cane.useBrain().useMemory().updateWorld(array[1])
            # decision = cane.useBrain().react(positionArray, "takeDecision(X)")


        elif array[0] == GOAL_REACHED:
            i += 1

        elif array[0] == GOAL_FOUND:
            cane.goalFound(array[1])

        elif array[0] == DOG_POSITION:
            cane.useBrain().useMemory().changeMyPosition(array[1].split(INTERNAL_SEPARATOR))
