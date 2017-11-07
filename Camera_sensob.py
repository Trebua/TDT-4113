import Sensob.py
from basic_robot import camera

class Camera_sensob(Sensob):
    def __init__(self):
        Sensob.__init__(Sensob)
        self.img_width = 128
        self.img_height = 96
        self.camera = camera.Camera(img_width=self.img_width,img_height=self.img_height)
        self.value = None

    def update(self):
        self.value = self.camera.update()
        return self.value


