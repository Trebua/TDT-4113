from Sensob import Sensob
from reflectance_sensors import ReflectanceSensors

class IR_sensob(Sensob):

    def __init__(self):
        Sensob.__init__(self)
        self.IR = ReflectanceSensors()
        self.value = None
        self.recommendation = None

    def update(self):
        #tar inn 6 verdier i en liste, som er tall mellom 0 og 1, der 0 er mørkt, mens 1 er lyst.
        all_values = self.IR.update()
        self.value = 0
        left_value = sum(all_values[:3])
        right_value = sum(all_values[3:])
        for val in all_values: #oppdaterer self.value med 1/6 (høyest mulig) hvis det er mørkt
            if (val < 0.2):
                self.value += 1/len(all_values)
        if left_value < right_value:
            self.recommendation = ['R', 75]
        elif right_value < left_value:
            self.recommendation = ['L', 75]
