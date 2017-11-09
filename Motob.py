#from basic_robot.motors import *
import motors

class Motob():

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
        forhold = self.value[0][1]/90
        if self.value[1]:
            print("Motob: forward")
            self.motors[0].forward()
        if not self.value[1]:
            print("Motob: stop")
            self.motors[0].stop()
        else:
            if self.value[0][0] == "L":
                print("Motob: Left")
                self.motors[0].set_value([-0.25,forhold]) #Detaljer senere: hvordan få til 45 grader?
            else:
                print("Motob: Right")
                self.motors[0].set_value([forhold,-0.25])
