class Behaviour:

    __prolog = None

    def __init__(self, prolog):
        self.__prolog = prolog

    def takeDecision(self, factClass):
        factClass = factClass.replace('"', "'")

        try:
            decisions = list(self.__prolog.query(factClass))
            print("ho deciso")
        except:
            decisions = "Error"

        decisionarray = []

        for i in range(len(decisions)):
            decision = decisions[i]['X']

            if decision not in decisionarray:
                decisionarray.append(decision)

        return decisionarray
