import Agent.Brain
import Agent.Sensor

CONST_QUERY_FACT_CLASS = "takeDecision(X)"


class Agent:

    __brain = None
    __sensor = None

    def __init__(self, myposition, planedimension):
        self.__brain = Brain.Brain(myposition, planedimension)
        self.__sensor = Sensor.Sensor()
        self.__brain.useLearning().learnFromFile("prolog.pl")

    def useBrain(self):
        return self.__brain

    def useSensor(self):
        return self.__sensor

    def reaction(self, array):

        sensorArray = self.__sensor.whatIsee(array)
        self.__brain.useMemory().updateWorld(sensorArray)
        decision = self.__brain.react(sensorArray, CONST_QUERY_FACT_CLASS)

        return decision

    def goalFound(self, position):

        if self.useBrain().useMemory().getGoalPosition() == None:

            self.useBrain().useMemory().setGoalPosition(position)
            self.useBrain().useLearning().learnNewFact("goal('True')")

        return