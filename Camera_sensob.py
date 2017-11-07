import Sensob.py
from basic_robot import camera
from PIL import Image

class Camera_sensob(Sensob):
    
    def __init__(self):
        Sensob.__init__(Sensob)
        self.img_width = 128
        self.img_height = 96
        self.camera = camera.Camera(img_width=self.img_width,img_height=self.img_height)
        self.value = None
        self.image = None
        self.min_green = 150 # Thresholds for the color testing
        self.max_red = 150 #Change these as needed
        self.max_blue = 150

    def update(self):
        self.image = self.camera.update()
        self.value = self.find_green()
        return self.value

    def find_green(self):
        amount = 0
        total_width = 0
        for width in range(self.img_width):
            for height in range(self.img_height):
                if self.check_pixel(self.image.getpixel((width,height))):
                    total_width+=width
                    amount += 1
        return total_width/amount

    def check_pixel(self,pixel):
        return(pixel[0] < self.max_red and pixel[1] > self.min_green and pixel[2] < self.max_blue)
