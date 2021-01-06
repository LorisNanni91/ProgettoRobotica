class Learning:

    __prolog = None

    def __init__(self, prolog):
        self.__prolog = prolog

    def LearnNewFact(self, fact):
        self.__prolog.assertz(str(fact))
        return

    def LearnFromFile(self, filepath):
        assert isinstance(filepath, str), "La path deve essere una stringa"
        self.__prolog.consult(filepath)
        return

    def Clean(self, fact):
        fact = str(fact)
        factClass = fact.split('(')[0] + '(_)'
        self.__prologEngine.retractall(factClass)
