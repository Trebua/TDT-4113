from abc import abstractmethod

class Sensob:

    def __init__(self, sensors):
        self.value = None
        return

    @abstractmethod
    def update(self):
        return


