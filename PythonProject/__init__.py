import server as S
import Agent

# Message type
PLANE_SIZE = '0'
DOG_POSITION = '1'
DOG_SENSOR = '2'
GOAL_REACHED = '3'

# Type of object detected by sensor
EMPTY = '0'
SHEEP = '1'
OBSTACLE = '2'
GOAL = '3'

initialized = False
planedimension = None
dogposition = None
while initialized == False:

    data = S.sock.ReadReceivedData()# read data

    if data != None: # if NEW data has been received since last ReadReceivedData function call
        array = data.split("|")
        if array[0] == PLANE_SIZE:
            planedimension = array[1]
        elif array[0] == DOG_POSITION:
            dogposition = array[1]
            #initialized = True

print("dimensione piano " + planedimension + " posizione cane " + dogposition)
cane = Agent.Agent(dogposition, planedimension)
cane.useBrain().useLearning().LearnFromFile("prolog.pl")

i = 0
while i < 5:

    data = S.sock.ReadReceivedData()  # read data
    if data != None:
        array = data.split ("|")
        if array[0] == DOG_SENSOR:
            string= 1
            # dati sensore
        elif array[0] == GOAL_REACHED:
            i += 1




