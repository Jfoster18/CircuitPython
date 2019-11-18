import board
from digitalio import DigitalInOut, Direction, Pull
import time

class RGB(): #makes class "rgb"

    def __init__(self, r, g, b):

        self.r = DigitalInOut(r)
        self.r.direction = Direction.OUTPUT

        self.g = DigitalInOut(g)
        self.g.direction = Direction.OUTPUT

        self.b = DigitalInOut(b)
        self.b.direction = Direction.OUTPUT

    def red(self): #defines red and says what is neeeded for rgb led to become red
        self.r.value = False #maks rgb led red
        self.b.value = True
        self.g.value = True

    def green(self): #defines green and says what is needed for rgb led to become green
        self.r.value = True
        self.g.value = False #makes rgb led green
        self.b.value = True

    def blue(self): #defines blue and says what is needed for rgb led to become blue
        self.r.value = True
        self.g.value = True
        self.b.value = False #makes rgb led blue

    def cyan(self): #defines cyan and says what colors need to be on to make cyan
        self.r.value = True
        self.g.value = False #green and blue make cyan
        self.b.value = False

    def magenta(self): #defines magents and says what colors are needed to make magenta
        self.r.value = False
        self.g.value = True
        self.b.value = False #blue and red make magents

    def yellow(self): #defines yellow and says what colors are needed to make yellow
        self.r.value = False
        self.g.value = False #green and red make yellow
        self.b.value = True

    #def off(self):
        #self.r.value = True
        #self.g.value = True
        # self.b.value = True