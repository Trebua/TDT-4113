from Sensob import Sensob
import random
import ultrasonic

#Tar inn ultrasonic-wrapper og oppdaterer distansen samt regner ut prioriteringen.
class Ultrasonic_sensob(Sensob):

    #Instansierer ultrasonic_sensor som en subklasse av Sensob
    def __init__(self):
        Sensob.__init__(self)
        self.ultrasonic = ultrasonic.Ultrasonic()
        self.distance = 0
        self.recommendation = None
        self.value = 0


    #Oppdaterer self.distance med sensorens utregnede avstand
    def update(self):
        self.distance = self.ultrasonic.sensor_get_value() #distanse i cm
        self.compute_value()
        self.compute_recommendation()

    #Hvis distansen er større enn 10 cm så bryr vi oss ikke om det, ellers blir det viktigere jo nærmere vi kommer
    def compute_value(self):
        print("Distanse: ",self.distance)
        if self.distance >= 5:
            self.value = 0
        else:
            self.value = (1-(self.distance/5)) #Kanskje delt på 5 siden den ikke vil være større enn 5

    #Ber roboten svinge til høyre eller venstre (tilfeldig) 90 grader.
    def compute_recommendation(self):
        forward = False
        if self.distance >= 5:
            forward = True
        self.recommendation = ((["L","R"][random.randint(0,1)],90),forward)

