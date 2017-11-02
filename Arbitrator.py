class Arbitrator():


    def __init__(self, bbcon, stochastic):
        self.bbcon = bbcon
        self.stochastic = stochastic


    def choose_action(self):
        active_behaviours = self.bbcon.active_behaviors

        return True

    def stochastic_choice(self):
        return True

    def deterministic_choice(self):
        return True

