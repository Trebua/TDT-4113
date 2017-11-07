from abc import abstractmethod

class Sensob:

    def __init__(self, sensors):
        self.value = None
        self.sensors = []
        return

    @abstractmethod
    def update(self):
        return
