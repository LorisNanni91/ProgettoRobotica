from pyswip import Prolog
import Agent.Brain.Behaviour
import Agent.Brain.Learning
import Agent.Brain.Memory


class Brain:

    __learning = None
    __memory = None
    __behaviour = None
    __prolog = None

    def __init__(self, myposition, planedimension):
        self.__prolog = Prolog()
        self.__behaviour = Behaviour.Behaviour(self.__prolog)
        self.__learning = Learning.Learning(self.__prolog)
        self.__memory = Memory.Memory(myposition, planedimension)

    def useLearning(self):
        return self.__learning

    def useMemory(self):
        return self.__memory

    def useBehaviour(self):
        return self.__behaviour

    def react(self, positionArray, factClass):
        fact = self.composeFact(positionArray)
        self.__memory.putFact(fact)
        self.__learning.LearnNewFact(fact)
        decision = self.__behaviour.takeDecision(factClass)
        if decision != "Error":
            self.__memory.putDecision(decision)
            return decision
        else:
            return "Error"

    def composeFact(self, positionArray):
        fact = "perception("
        for i in range(len(positionArray)):
            fact = fact + "'" + positionArray[i][2] + "',"
        fact = fact[:-1]
        fact = fact + ")"
        return fact