import random

#Returnerer en vinner basert på aktive behaviours i bbcon
class Arbitrator():

    #BBCon.active_behaviours gir behaviours
    #Behaviour.weight gir vekt
    def __init__(self, bbcon,stochastic):
        self.bbcon = bbcon #Oppdaterer denne seg?
        self.stochastic = stochastic

    #Velger hvordan man skal finne en vinner basert på hva init
    def choose_action(self):
        if self.stochastic:
            return self.stochastic_choice()
        else: return self.deterministic_choice()

    #Velger en tilfeldig behaviour
    def stochastic_choice(self):
        sum_weight = 0
        behaviour_dict = {}

        #Går igjennom alle behaviours og lager en dictionary med intervaller
        for behave in self.bbcon.active_behaviors:
            behaviour_dict[behave] = [sum_weight,sum_weight+behave.weight]
            sum_weight+= behave.weight

        #Plukker et random tall innenfor intervallet
        rand = random.uniform(0,sum_weight)
        winner = None

        #Finner riktig vinner
        for key,value in behaviour_dict.items():
            if value[1] < rand:
                winner = key
        return winner

    #Velger den med størst prioritet
    def deterministic_choice(self):
        max = self.bbcon.active_behaviors[0].weight
        winner = self.bbcon.active_behaviors[0]
        for behave in self.bbcon.active_behaviors:
            if behave.weight > max:
                max = behave.weight
                winner = behave
        return winner
