class Learning:

    __prolog = None

    def __init__(self, prolog):
        self.__prolog = prolog

    def learnNewFact(self, fact):
        factClass = fact.split("(")[0] + "(_,_,_,_,_,_,_,_,_,_,_)"
        if factClass == "perception(_,_,_,_,_,_,_,_,_,_,_)":
            self.cleanPerception(factClass)
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
