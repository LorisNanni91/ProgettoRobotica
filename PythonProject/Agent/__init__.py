import Agent.Brain
import Agent.Actions
import Agent.Sensor

CONST_FACT_CLASS = "takeDecision(X)"


class Agent:

    __brain = None
    __sensor = None
    __act = None

    def __init__(self, myposition, planedimension):
        self.__brain = Brain.Brain(myposition, planedimension)
        self.__act = Actions.Action()
        self.__sensor = Sensor.Sensor()

    def useBrain(self):
        return self.__brain

    def useSensor(self):
        return self.__sensor

    def useAction(self):
        return self.__act

    def reaction(self, array):
        sensorArray = self.__sensor.whatIsee(array)
        self.__brain.useMemory().updateWorld(sensorArray)
        decision = self.__brain.react(sensorArray, CONST_FACT_CLASS)
        if decision != "Error":
            self.__brain.useMemory().setMyOrientation(self.useAction().calculateRotation(decision))
        return decision

    def goalFound(self, position):
        if self.useBrain().useMemory().getGoalPosition()!= None:
            self.useBrain().useMemory().setGoalPosition(position)
            self.useBrain().useLearning().learnNewFact("goal('True')")
        return