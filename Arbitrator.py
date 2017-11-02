import random

class Arbitrator():


    def __init__(self, bbcon, stochastic):

    #BBCon.active_behaviours gir behaviours
    #Behaviour.priority gir vekt
    def __init__(self, bbcon, stochastic):

        self.bbcon = bbcon
        self.stochastic = stochastic

    def choose_action(self):
        return True

    #Velger en tilfeldig behaviour
    def stochastic_choice(self):
        sum_priority = 0
        behaviour_dict = {}

        #Går igjennom alle behaviours og lager en dictionary med intervaller
        for behave in self.bbcon.active_behaviors:
            behaviour_dict[behave] = [sum_priority,sum_priority+behave.priority]
            sum_priority+= behave.priority

        #Plukker et random tall innenfor intervallet
        rand = random.uniform(0,sum_priority)
        winner = None

        #Finner riktig vinner
        for key,value in behaviour_dict.items():
            if value[1] < rand:
                winner = key
        return winner

    def deterministic_choice(self):
        return True

