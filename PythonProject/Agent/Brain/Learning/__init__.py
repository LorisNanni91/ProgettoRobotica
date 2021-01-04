class Learning:

    __prolog = None

    def __init__(self, prolog):
        self.__prolog = prolog

    def LearnNewFact(self,fact):
        self.__prolog.assertz(fact)

    def LearnFromFile(self, filepath):
        assert isinstance(filepath, str), "La path deve essere una stringa"
        self.__prolog.consult(filepath)
