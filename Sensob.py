#from abc import abstractmethod

#Superklasse for sensorobjekter
class Sensob:

    #Alle sensorer har en verdi mellom 0-1 som behandles i behaviour + arbitrator
    #Recommendation er en motoranbefeling på formen ("L/R", degrees)
    def __init__(self):
        self.value = None
        self.recommendation = None
        self.sensors = []
        return

    #Metode alle sensobs skal ha, som oppdaterer sensorverdiene og finner ut ny self.value
    #@abstractmethod
    def update(self):
        return

    def reset(self):
        self.value = None
        return
