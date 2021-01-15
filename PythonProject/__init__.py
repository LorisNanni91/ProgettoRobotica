import server as S
import Agent

# Message type
PLANE_SIZE = 'PLANE_SIZE'
DOG_POSITION = 'DOG_POSITION'
DOG_SENSOR = 'DOG_SENSOR'
GOAL_REACHED = 'GOAL_REACHED'
GOAL_FOUND = 'GOAL_FOUND'

# Type of object detected by sensor
EMPTY = 'EMPTY'
SHEEP = 'SHEEP'
OBSTACLE = 'OBSTACLE'
WALL = 'WALL'
GOAL = 'GOAL'

initialized = False
planedimension = None
dogposition = None
while initialized == False:

    data = S.sock.ReadReceivedData()# read data

    if data != None: # if NEW data has been received since last ReadReceivedData function call
        print( "primo ciclo " + data)
        array = data.split("|")
        if array[0] == PLANE_SIZE:
            planedimension = array[1]
        elif array[0] == DOG_POSITION:
            dogposition = array[1]
        if planedimension != None and dogposition != None:
            initialized = True

print("dimensione piano " + planedimension + " posizione cane " + dogposition)
cane = Agent.Agent(dogposition, planedimension)
cane.useBrain().useLearning().LearnFromFile("prolog.pl")

i = 0
while i < 5:

    data = S.sock.ReadReceivedData()  # read data
    if data != None:
        print(data)
        array = data.split("|")
        if array[0] == DOG_SENSOR:
            positionArray = cane.useBrain().useMemory().updateWorld(array[1])
            decision = cane.useBrain().react(positionArray, "takeDecision(X)")
            print("DECISION: " + str(decision[0]))
            S.sock.SendData(decision[0])
        elif array[0] == GOAL_REACHED:
            i += 1
        elif array[0] == GOAL_FOUND:
            cane.useBrain().useMemory().setGoalPosition(array[1])
        elif array[0] == DOG_POSITION:
            cane.useBrain().useMemory().changeMyPosition(array[1])
