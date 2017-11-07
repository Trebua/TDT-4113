import Sensob
from basic_robot import reflectance_sensors

class IR_sensob(Sensob):

    def __init__(self):
        Sensob.__init__(self)
        self.IR = reflectance_sensors.IRProximitySensor()
        self.value = None
        self.recommendation = None

    def update(self):
        #tar inn 6 verdier i en liste, som er tall mellom 0 og 1, der 0 er mørkt, mens 1 er lyst.
        all_values = self.IR.update()
        self.value = 0
        for val in all_values: #oppdaterer self.value med 1/6 (høyest mulig) hvis det er mørkt
            if (val < 0.2):
                self.value += 1/len(all_values)
            
