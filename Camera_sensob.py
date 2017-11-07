import Sensob.py
from basic_robot import camera

class Camera_sensob(Sensob):
    def __init__(self):
        Sensob.__init__(Sensob)
        self.img_width = 128
        self.img_height = 96
        self.camera = camera.Camera(img_width=self.img_width,img_height=self.img_height)
        self.value = None
        self.min_green = 150 # Thresholds for the color testing
        self.max_red = 150 #Change these as needed
        self.max_blue = 150

    def update(self):
        self.value = self.camera.update()
        return self.value

    def find_green(self):
