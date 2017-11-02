import Sensob.py
from basic_robot import camera

class Camera_sensob(Sensob):
    def __init__(self):
        Sensob.__init__(Sensob)
        self.camera = camera.Camera()
        self.value = None

    def update(self):
        self.value = self.camera.update()
        return self.value


