#Costant for message separator
SINGLE_SENSOR = ":"
IN_SENSOR = ","


class Sensor:

    def __init__(self):
        return

    def whatIsee(self, arraySensor):
        cellsSensor = arraySensor.split(SINGLE_SENSOR)
        sensors = []
        for i in range(len(cellsSensor)):
            singlePosition = cellsSensor[i].split(IN_SENSOR)
            sensors.append(singlePosition)
        return sensors
