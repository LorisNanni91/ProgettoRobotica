import Agent.Brain


class Agent:

    __brain = None
    __position = None

    def __init__(self, myposition, larg, lung):
        self.__brain = Brain.Brain(myposition, larg, lung)

    def getPosition(self):
        return self.__position

    def useBrain(self):
        return self.__brain
