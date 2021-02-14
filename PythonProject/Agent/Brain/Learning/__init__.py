FACT_GOAL_FALSE = "goal('False')"

class Learning:
    __prolog = None

    def __init__(self, prolog):
        self.__prolog = prolog
        # all'inizio la classe goal vale false
        self.learnNewFact(FACT_GOAL_FALSE, True)

    def learnNewFact(self, fact, initialized=False):
        if not initialized:  # se non sto inizializzando, devo svuotare il db prolog
            factClass = fact.split("(")[0]

            if factClass == "perception":
                factClass += "(_,_,_,_,_,_,_,_,_,_,_)"

            elif factClass == "goal":
                factClass += "(_)"

            self.cleanPerception(factClass)

        print("fatto che sta imparando " + str(fact))
        self.__prolog.assertz(str(fact))  # se sto inizializzando devo solo imparare il nuovo fatto
        return

    def learnFromFile(self, filepath):
        assert isinstance(filepath, str), "La path deve essere una stringa"
        self.__prolog.consult(filepath)
        return

    def cleanPerception(self, factClass):
        factClass = str(factClass)
        self.__prolog.retractall(factClass)
        return
