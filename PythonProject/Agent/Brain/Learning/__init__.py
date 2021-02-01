class Learning:

    __prolog = None

    def __init__(self, prolog):
        self.__prolog = prolog
        self.learnNewFact("goal('False')", True)

    def learnNewFact(self, fact, initialized = False):
        if initialized == False:
            factClass = fact.split("(")[0]
            if factClass == "perception":
                factClass += "(_,_,_,_,_,_,_,_,_,_,_)"
            elif factClass == "goal":
                factClass += "(_)"
            self.cleanPerception(factClass)

        print("fatto che sta imparando " + str(fact))
        self.__prolog.assertz(str(fact))
        return

    def learnFromFile(self, filepath):
        assert isinstance(filepath, str), "La path deve essere una stringa"
        self.__prolog.consult(filepath)
        return

    def cleanPerception(self, factClass):
        factClass = str(factClass)
        self.__prolog.retractall(factClass)
        return
