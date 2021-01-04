from pyswip import Prolog
import Agent.Brain.Behaviour
import Agent.Brain.Learning
import Agent.Brain.Memory


class Brain:

    __learning = None
    __memory = None
    __behaviour = None
    __prolog = None

    def __init__(self, myposition, larg, lung):
        self.__prolog = Prolog ()
        self.__behaviour = Behaviour.Behaviour(self.__prolog)
        self.__learning = Learning.Learning(self.__prolog)
        self.__memory = Memory.Memory(myposition, larg, lung)

    def useLearning(self):
        return self.__learning

    def useMemory(self):
        return self.__memory

    def useBehaviour(self):
        return self.__behaviour
