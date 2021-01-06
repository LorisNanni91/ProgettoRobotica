class Behaviour:

    __prolog = None

    def __init__(self, prolog):
        self.__prolog = prolog


    def takeDecision(self, factClass):
        factClass = factClass.replace('"', "'")

        try:
            decisions = list(self.__prolog.query(factClass))
        except:
            decisions = "Error"

        return decisions
