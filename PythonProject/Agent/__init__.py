import Agent.Brain
import Agent.Sensor

CONST_QUERY_FACT_CLASS = "takeDecision(X)"
FACT_GOAL_TRUE = "goal('True')"


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

        sensorArray = self.__sensor.whatIsee(array)  # compongo l'array con le coordinate e il contenuto di ogni sensore
        self.__brain.useMemory().updateWorld(sensorArray)  # in base a ciò che rilevo, aggiorno il mondo nella mia memoria
        decision = self.__brain.react(sensorArray, CONST_QUERY_FACT_CLASS)

        return decision

    def goalFound(self, position):

        if self.useBrain().useMemory().getGoalPosition() == None:

            self.useBrain().useMemory().setGoalPosition(position)
            fact = FACT_GOAL_TRUE
            self.useBrain().useMemory().putFact(fact)
            self.useBrain().useLearning().learnNewFact(fact)

        return