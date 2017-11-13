#from basic_robot.motors import *
import motors

class Motob():

    motor = None # a list of the motors whose settings will be determined by the motob.
    value = None #a holder of the most recent motor recommendation sent to the motob.

    def __init__(self):
        self.motor = motors.Motors()
        self.time_per_degree = 3/360 #på 0.5 fart vil 10 grader ta 3/360 * 10 tid
        return

    def update(self,recommendation):# - receive a new motor recommendation, load it into the value slot, and operationalize it.
        self.value = recommendation
        self.operationalize()

    #Vil få verdi som feks ((L,45), True/False)
    def operationalize(self):
        if self.value[1]:
            self.motor.forward(0.3)
        else:
            if self.value[0][0] == "L":
                self.motor.left(0.5, self.time_per_degree * self.value[0][1]) #ny
                #self.motors[0].set_value([0,1])
            else:
                self.motor.right(0.5, self.time_per_degree * self.value[0][1]) #ny
                #gammel: self.motors[0].set_value([1,0])
