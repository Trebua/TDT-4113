import random

class Arbitrator():

<<<<<<< HEAD

    def __init__(self, bbcon, stochastic):

    #BBCon.active_behaviours gir behaviours
    #Behaviour.priority gir vekt
    def __init__(self, bbcon, stochastic):

        self.bbcon = bbcon
=======
    #BBCon.active_behaviours gir behaviours
    #Behaviour.priority gir vekt
    def __init__(self, bbcon,stochastic):
        self.bbcon = bbcon #Oppdaterer denne seg?
>>>>>>> ca71a1fd5fd3f46a9ddb58d789e37de6f8613867
        self.stochastic = stochastic

    #Velger hvordan man skal finne en vinner basert på hva init
    def choose_action(self):
<<<<<<< HEAD
        return True
=======
        if self.stochastic:
            return self.stochastic_choice()
        else: return self.deterministic_choice()
>>>>>>> ca71a1fd5fd3f46a9ddb58d789e37de6f8613867

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

    #Velger den med størst prioritet
    def deterministic_choice(self):
        max = self.bbcon.active_behaviors[0].priority
        winner = self.bbcon.active_behaviors[0]
        for behave in self.bbcon.active_behaviors:
            if behave.priority > max:
                max = behave.priority
                winner = behave
        return winner
