
class Behavior:

    def __init__(self, bbcon):
        self.bbcon = bbcon  # pointer to the controller that uses this behavior.
        self.sensobs = []   #a list of all sensobs that this behavior uses
        self.motor_recommendations = [] #list of motor recommendations for arbitrator
        self.active_flag = False    #active/inactive behavior


    def consider_deactivation(self):
        if self.active_flag:
            #consider deactivation
            pass

    def consider_activation(self):
        if not self.active_flag:
            #consider activation
            pass

    def update(self):
        pass


    def add_sensob(self,sensob):
        self.sensobs.append(sensob)

