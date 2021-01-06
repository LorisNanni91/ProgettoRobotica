import Agent.Brain


class Agent:

    __brain = None

    def __init__(self, myposition, planedimension):
        self.__brain = Brain.Brain(myposition, planedimension)

    def useBrain(self):
        return self.__brain
