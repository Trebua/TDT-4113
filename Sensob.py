from abc import abstractmethod

#Superklasse for sensorobjekter
class Sensob:

    #Alle sensorer har en verdi mellom 0-1 som behandles i behaviour + arbitrator
    def __init__(self, sensors):
        self.value = None
        self.sensors = []
        return

    #Metode alle sensobs skal ha, som oppdaterer sensorverdiene og finner ut ny self.value
    @abstractmethod
    def update(self):
        return
