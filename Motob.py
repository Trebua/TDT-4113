#from basic_robot.motors import *
import motors

class Motob():

    motors = [] # a list of the motors whose settings will be determined by the motob.
    value = None #a holder of the most recent motor recommendation sent to the motob.

    def __init__(self):
        self.motors.append(motors.Motors())
        self.time_per_degree = 3/360 #på 0.5 fart vil 10 grader ta 3/360 * 10 tid
        return

    def update(self,recommendation):# - receive a new motor recommendation, load it into the value slot, and operationalize it.
        self.value = recommendation
        self.operationalize()

    #Vil få verdi som feks ((L,45), True/False)
    def operationalize(self):
        #forhold = self.value[0][1]/90
        #print("Forhold i motob:", forhold) # Blir alltid 0.011111111112
        if self.value[1]:
            print("Motob: forward")
            self.motors[0].forward(0.3)
            ############Skal vi gi dem en duration for å teste?
        else:
            if self.value[0][0] == "L":
                print("Motob: Left")
                self.motors[0].left(0.5, self.time_per_degree * self.value[0][1]) #ny
                #self.motors[0].set_value([0,1])
            else:
                print("Motob: Right")
                self.motors[0].right(0.5, self.time_per_degree * self.value[0][1]) #ny
                #gammel: self.motors[0].set_value([1,0])
