
class ForwardBehavior:

    #Mangler halt request, men trenger vi enkli det?
    def __init__(self, bbcon, priority = 1):
        self.bbcon = bbcon  # pointer to the controller that uses this behavior.
        self.sensobs = []   #a list of all sensobs that this behavior uses
        self.motor_recommendations = [] #list of motor recommendations for arbitrator
        self.active_flag = True    #active/inactive behavior
        self.priority = priority #Initial priority
        self.weight = 0.3 #match_degree*priority
        self.match_degree = 0.3
        self.name = "Forward"


    def set_priority(self,priority):
        self.priority = priority

    def set_name(self,name):
        self.name = name


    def sense_and_act(self):
        self.add_motor_recommendation()

    def update(self):
        self.sense_and_act()

    def add_motor_recommendation(self,motor_recommendation = (("L",0),True)):
        self.motor_recommendation = motor_recommendation
