import Sensob.py
import random
from basic_robot import ultrasonic.py

#Tar inn ultrasonic-wrapper og oppdaterer distansen samt regner ut prioriteringen.
class Ultrasonic_sensob(Sensob):

    #Instansierer ultrasonic_sensor som en subklasse av Sensob
    def __init__(self):
        Sensob.__init__(self)
        self.ultrasonic = ultrasonic.Ultrasonic()
        self.distance = 0

    #Oppdaterer self.distance med sensorens utregnede avstand
    def update(self):
        self.distance = self.ultrasonic.compute_distance() #distanse i cm
        self.compute_value()
        self.compute_recommendation()

    #Hvis distansen er større enn 10 cm så bryr vi oss ikke om det, ellers blir det viktigere jo nærmere vi kommer
    def compute_value(self):
        if self.distance >= 10:
            self.value = 0
        else:
            self.value = (1-(self.distance/10))

    #Ber roboten svinge til høyre eller venstre (tilfeldig) 90 grader.
    def compute_recommendation(self):
        self.recommendation = (["L","R"][random.randint(0,1)],90)
