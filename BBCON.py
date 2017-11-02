class BBCON():

    behaviors = [] #a list of all the behavior objects used by the bbcon
    active_behaviors = [] #a list of all behaviors that are currently active.
    sensobs = [] #a list of all sensory objects used by the bbcon
    motobs = [] #a list of all motor objects used by the bbcon
    arbitrator = None #the arbitrator object that will resolve actuator requests produced by the behaviors.

    #Other instance variables, such as the current timestep, the inactive behaviors, and the controlled agent/robot
    #may also prove useful in your implementation.

    #test
    #test2
    #HEI HENRIK
    #HEI SINDRE

    def add_behavior(self): #append a newly-created behavior onto the behaviors list.
        return True

    def add_sensob(self): #append a newly-created sensob onto the sensobs list.
        return True

    def activate_behavior(self): #add an existing behavior onto the active-behaviors list.
        return True

    def deactive_behavior(self): #remove an existing behavior from the active behaviors list.
        return True


    def run_one_timestep(self):
        #1. Update all sensobs - These updates will involve querying the relevant sensors
        # for their values, along with any pre-processing of those values (as described below)

        #2. Update all behaviors - These updates involve reading relevant sensob values and
        #  producing a motorrecommendation.

        #3. Invoke the arbitrator by calling arbitrator.choose action, which will choose
        #  a winning behavior andreturn that behavior’s motor recommendations and halt request flag.

        #4. Update the motobs based on these motor recommendations. The motobs will then update
        #  the settings of all motors.

        #5. Wait - This pause (in code execution) will allow the motor settings to remain active
        #  for a short period of time, e.g., one half second, thus producing activity in the robot, such as moving forward or turning.

        #6. Reset the sensobs - Each sensob may need to reset itself, or its associated sensor(s), in some way

        return True
