import Sensob.py
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
        #distanse i cm
        self.distance = self.ultrasonic.compute_distance()
        self.compute_value()

    #Hvis distansen er større enn 10 cm så bryr vi oss ikke om det, ellers blir det viktigere jo nærmere vi kommer
    def compute_value(self):
        if self.distance >= 10:
            self.value = 0
        else:
            self.value = (1-(self.distance/10))
