
class Action:

    def __init__(self):
        return

    def calculateRotation(self, decision):
        rotation = 0
        if decision == "Rotate-Right":
            rotation = 90
        elif decision == "Rotate-Back":
            rotation = 180
        elif decision == "Rotate-Left":
            rotation = 270
        return rotation