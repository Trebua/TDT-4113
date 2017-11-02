class Arbitrator():


    def __init__(self, bbcon):
        self.bbcon = bbcon


    def choose_action(self):
        active_behaviours = self.bbcon.activate_behavior()
        return True

    def stochastic_choice(self):
        return True

    def deterministic_choice(self):
        return True

