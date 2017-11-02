#from basic_robot.motors import *
import basic_robot.motors.py

class motob():

    motors = [] # a list of the motors whose settings will be determined by the motob.
    value = None #a holder of the most recent motor recommendation sent to the motob.

    def __init__(self):
        return

    def update(self,recommendation):# - receive a new motor recommendation, load it into the value slot, and operationalize it.
        return True

    def operationalize(self):
        # convert a motor recommendation into one or more motor settings, which are sent to
        #the corresponding motor(s).
        return True
