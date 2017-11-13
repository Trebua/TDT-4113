from Sensob import Sensob
from camera import Camera
from PIL import Image

#Camera sensorobjekt
class Camera_sensob(Sensob):

    def __init__(self):
        Sensob.__init__(self)
        self.img_width = 128
        self.img_height = 96
        self.camera = Camera(img_width=self.img_width,img_height=self.img_height)
        self.value = None #0-1
        self.image = None
        self.min_green = 150 # Thresholds for the color testing
        self.max_red = 150 #Change these as needed
        self.max_blue = 150
        self.recommendation = None
        self.amount = None

    #Oppdaterer image og self.value
    def update(self):
        self.image = self.camera.update()
        x,self.amount = self.find_green()
        self.compute_value(x)
        self.compute_recommendation(x)
        return

    #Finner gjennomsnittlig x verdi for grønn og finner mengden
    def find_green(self):
        amount = 0
        total_width = 0
        for width in range(self.img_width):
            for height in range(self.img_height):
                if self.check_pixel(self.image.getpixel((width,height))):
                    total_width+=width
                    amount += 1
        if amount == 0:
            return 0,0
        return total_width/amount,amount #gjennomsnitt, mengde

    #Sjekker en piksel og ser om den er innenfor grønn-toleransen vår
    def check_pixel(self,pixel):
        return(pixel[0] < self.max_red and pixel[1] > self.min_green and pixel[2] < self.max_blue)

    #Ser på hvor mye fra midten det grønne befinner seg, og finner value (prioritet) mellom 0-1 basert på det
    #Kanskje ta hensyn til hvor mye grønt det er -> sette value til 0 hvis den er for liten
    #Må kanskje justere img_width hvis den er feil
    def compute_value(self,x):
        middle = self.img_width/2
        if self.amount < 150:
            self.value = 0
            return
        if x < middle:
            self.value = (abs(middle-x))/middle
        else:
            self.value = (abs(x-middle))/middle
        return

    #Finner recommendation basert på hvilken side av kamera det er mest grønt
    def compute_recommendation(self,x):
        middle = self.img_width/2
        turn_degree = abs(middle-x)/2 #maks vinkel som kan svinges er da 64 grader, hvis x er i midten vil grader bli 0
        if turn_degree*2 < 4: #Kjører bare rett frem hvis turn degree'en er for lav
            self.recommendation = (("L",0),True)
        elif x < middle:
            self.recommendation = (("L",turn_degree),False)
        else:
            self.recommendation = (("R",turn_degree),False)
        return
