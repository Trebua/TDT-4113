class BBCON():

    behaviors = [] #a list of all the behavior objects used by the bbcon
    active_behaviors = [] #a list of all behaviors that are currently active.
    sensobs = [] #a list of all sensory objects used by the bbcon
    motobs = [] #a list of all motor objects used by the bbcon
    arbitrator = None #the arbitrator object that will resolve actuator requests produced by the behaviors.

    #Other instance variables, such as the current timestep, the inactive behaviors, and the controlled agent/robot
    #may also prove useful in your implementation.

    def add_behavior(self, behavior): #append a newly-created behavior onto the behaviors list.
        self.behaviors.append(behavior)
        return

    def add_sensob(self,sensob): #append a newly-created sensob onto the sensobs list.
        self.sensobs.append(sensob)
        return

    def activate_behavior(self, behavior): #add an existing behavior onto the active-behaviors list.
        self.activ_behaviors.append(behavior)
        return

    def deactive_behavior(self, behavior): #remove an existing behavior from the active behaviors list.
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
        return

    #Oppdaterer alle behaviors
    def update_behaviors(self):
        for behave in self.behaviors:
            behave.update()

    def update_motobs(self):
        for motob in self.motobs:
            motob.update()

    def update_sensobs(self):
        for sensor in self.sensobs:
            sensor.update()

    def choose_winning_behaviour(self):
        winner = self.arbitrator.choose_action()
        return winner.motor_recommendations[0] #Er det riktig at første recommendation skal velges? eventuelt fjerne denne behaviouren?
        #Skal man ha med noe om activeflag her eller håndteres det i behaviour?


    def run_one_timestep(self):
        #1. Update all sensobs - These updates will involve querying the relevant sensors
        # for their values, along with any pre-processing of those values (as described below)
        self.update_sensobs()


        #2. Update all behaviors - These updates involve reading relevant sensob values and
        #  producing a motorrecommendation.
        self.update_behaviors()
        #3. Invoke the arbitrator by calling arbitrator.choose action, which will choose
        #  a winning behavior andreturn that behavior’s motor recommendations and halt request flag.
        recommendation = self.choose_winning_behaviour()

        #4. Update the motobs based on these motor recommendations. The motobs will then update
        #  the settings of all motors.
        
        #5. Wait - This pause (in code execution) will allow the motor settings to remain active
        #  for a short period of time, e.g., one half second, thus producing activity in the robot, such as moving forward or turning.

        #6. Reset the sensobs - Each sensob may need to reset itself, or its associated sensor(s), in some way

        return True
