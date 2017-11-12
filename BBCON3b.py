import time
from Motob import Motob
from Behavior import Behavior
from Arbitrator import Arbitrator
from IR_sensob import IR_sensob
from Camera_sensob import Camera_sensob
from Ultrasonic_sensob import Ultrasonic_sensob
from zumo_button import ZumoButton
from ForwardBehavior import ForwardBehavior

#Disse importeres i andre klasser
#from Sensob import Sensob
#import random
#import reflectance_sensors
#import camera
#from PIL import Image
#import motors
#import ultrasonic


class BBCON3b():

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

    def add_motob(self,motob):
        self.motobs.append(motob)
        return

    def set_arbitrator(self,arbitrator):
        self.arbitrator = arbitrator
        return

    def activate_behavior(self, behavior): #add an existing behavior onto the active-behaviors list.
        self.active_behaviors.append(behavior)
        return

    def deactive_behavior(self, behavior): #remove an existing behavior from the active behaviors list.
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
        return

    #Oppdaterer alle behaviors
    def update_behaviors(self):
        for behave in self.behaviors:
            behave.update()

    #Oppdaterer alle motobs med recommendations fra vinnende behaviour
    def update_motobs(self, recommendation):
        for motob in self.motobs:
            motob.update(recommendation)

    #Oppdaterer sensorverdier
    def update_sensobs(self):
        for sensor in self.sensobs:
            sensor.update()

    #Finner vinnende behaviour og returnerer recommendation + active_flag
    def choose_winning_behaviour(self):
        winner = self.arbitrator.choose_action()
        if len(winner.motor_recommendations) == 0:
            return (("L",0),True) #Betyr bare kjør fremover.
        print("Første motor rec: ", winner.motor_recommendations[0])
        print("Siste motor rec: ", winner.motor_recommendations[-1])
        return (winner.motor_recommendations.pop(-1),winner.active_flag) #Er det riktig at første recommendation skal velges? eventuelt fjerne denne behaviouren?
    #pop 0 eller siste?

    #Resetter alle sensobs
    def reset_sensobs(self):
        for sensor in self.sensobs:
            sensor.reset()

    #Kjører alle metodene
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
        self.update_motobs(recommendation)

        #5. Wait - This pause (in code execution) will allow the motor settings to remain active
        #  for a short period of time, e.g., one half second, thus producing activity in the robot, such as moving forward or turning.
        time.sleep(0.5)

        #6. Reset the sensobs - Each sensob may need to reset itself, or its associated sensor(s), in some way
        self.reset_sensobs()

def run():
    #Initierer bbcon
    bbcon = BBCON3b()

    #Initierer sensorer
    ultrasonic = Ultrasonic_sensob()
    camera = Camera_sensob()
    ir = IR_sensob()

    #Initierer behaviour
    avoid_collision = Behavior(bbcon,0.3)
    find_color = Behavior(bbcon,0.9)
    avoid_line = Behavior(bbcon,0.4)
    forward = ForwardBehavior(bbcon,0.2)

    #Setter navn på behaviours
    avoid_collision.set_name("Ultrasonic-behavior")
    find_color.set_name("Kamera-behavior")
    avoid_line.set_name("IR-behavior")


    #Initierer arbitrator
    arbitrator = Arbitrator(bbcon,True) #Må sette true eller false, true = stokastisk, false = deterministisk

    #Initerer motob
    motob = Motob()

    #Legger sensobs i behaviour
    avoid_collision.add_sensob(ultrasonic)
    avoid_line.add_sensob(ir)
    find_color.add_sensob(camera)

    #Legger sensobs i bbcon - for at alle sensorverdiene skal oppdatere seg
    bbcon.add_sensob(ultrasonic)
    bbcon.add_sensob(ir)
    bbcon.add_sensob(camera)

    #Legger behaviours i bbcon
    bbcon.add_behavior(forward)
    bbcon.add_behavior(find_color)
    bbcon.add_behavior(avoid_collision)
    bbcon.add_behavior(avoid_line)

    #Legger motor inn i bbcon
    bbcon.add_motob(motob)

    #Legger til arbitrator
    bbcon.set_arbitrator(arbitrator)

    ZumoButton().wait_for_press()

    while True:
        bbcon.run_one_timestep()
        if len(bbcon.active_behaviors) > 0:
            for behavior in bbcon.active_behaviors:
                print(behavior.name)
