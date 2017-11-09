#from basic_robot.motors import *
import motors

class motob():

    motors = [] # a list of the motors whose settings will be determined by the motob.
    value = None #a holder of the most recent motor recommendation sent to the motob.

    def __init__(self):
        self.motors.append(motors.Motors())
        return

    def update(self,recommendation):# - receive a new motor recommendation, load it into the value slot, and operationalize it.
        self.value = recommendation
        self.operationalize()

    #Vil få verdi som feks ((L,45), True/False)
    #Regner med at motors kun inneholder et motors-objekt
    def operationalize(self):
        if self.value[1]:
            self.motors[0].forward(0.25)
        if not self.value[1]:
            self.motors[0].stop()
        else:
            if self.value[0][0] == "L":
                self.motors[0].setValue([-1,1],1) #Detaljer senere: hvordan få til 45 grader?
            else:
                self.motors[0].setValue([1,-1],1)

