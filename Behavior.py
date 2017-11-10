
class Behavior:

    #Mangler halt request, men trenger vi enkli det?
    def __init__(self, bbcon, priority = 0):
        self.bbcon = bbcon  # pointer to the controller that uses this behavior.
        self.sensobs = []   #a list of all sensobs that this behavior uses
        self.motor_recommendations = [] #list of motor recommendations for arbitrator
        self.active_flag = False    #active/inactive behavior
        self.priority = priority #Initial priority
        self.weight = 0 #match_degree*priority
        self.match_degree = 0
        self.name = None


    def set_priority(self,priority):
        self.priority = priority

    def set_name(self,name):
        self.name = name

    def consider_deactivation(self):
        if self.active_flag:
            if self in self.bbcon.active_behaviors:
                self.bbcon.deactive_behavior(self)

    def consider_activation(self):
        if not self.active_flag:
            if self not in self.bbcon.active_behaviors:
                self.bbcon.activate_behavior(self)

    def sense_and_act(self):
        if self.active_flag:
            dict = {}
            #Skal vi legge til flere motor_recommendations eller bare den med størst prioritet?
            for sensor in self.sensobs:
                dict[sensor] = sensor.value
            v=list(dict.values())
            k=list(dict.keys())
            self.add_motor_recommendation(k[v.index(max(v))].recommendation)

    def compute_match_degree(self):
        match = 0
        for sensor in self.sensobs:
            match += sensor.value
        match = match/len(self.sensobs)
        self.match_degree = match
        self.weight = self.match_degree*self.priority

    def compute_active_flag(self):
        if self.weight < 0.2:
            self.active_flag = False
        else:
            self.active_flag = True

    def update(self):
        for sensor in self.sensobs:
            sensor.update()
        self.compute_match_degree() #setter match til summen av match fra sensorer
        self.compute_active_flag()
        self.consider_activation()
        self.consider_deactivation()
        self.sense_and_act()


    def add_sensob(self,sensob):
        self.sensobs.append(sensob)

    def add_motor_recommendation(self,motor_recommendation):
        self.motor_recommendations.append(motor_recommendation)
