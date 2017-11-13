
class Behavior:

    #Mangler halt request, men trenger vi enkli det?
    def __init__(self, bbcon, priority = 0):
        self.bbcon = bbcon  # pointer to the controller that uses this behavior.
        self.sensob = None   #a list of all sensobs that this behavior uses
        self.motor_recommendation = None #list of motor recommendations for arbitrator
        self.active_flag = False    #active/inactive behavior
        self.priority = priority #Initial priority
        self.weight = 0 #match_degree*priority
        self.match_degree = 0
        self.name = None


    def set_priority(self,priority):
        self.priority = priority

    def set_name(self,name):
        self.name = name

    def sense_and_act(self):
        self.add_motor_recommendation(self.sensob.recommendation)

    def compute_match_degree(self):
        self.weight = self.sensob.value*self.priority

    def update(self):
        self.sensob.update()
        self.compute_match_degree()
        self.sense_and_act()
        print(self.name + " sin vekt: ", self.weight)


    def add_sensob(self,sensob):
        self.sensob = sensob

    def add_motor_recommendation(self,motor_recommendation):
        self.motor_recommendation = motor_recommendation
