import board
from digitalio import DigitalInOut, Direction, Pull
import time

class RGB():

    def __init__(self, r, g, b):

        self.r = DigitalInOut(r)
        self.r.direction = Direction.OUTPUT

        self.g = DigitalInOut(g)
        self.g.direction = Direction.OUTPUT

        self.b = DigitalInOut(b)
        self.b.direction = Direction.OUTPUT

    def red(self):
        self.r.value = False
        self.b.value = True
        self.g.value = True

    def green(self):
        self.r.value = True
        self.g.value = False
        self.b.value = True

    def blue(self):
        self.r.value = True
        self.g.value = True
        self.b.value = False

    def cyan(self):
        self.r.value = True
        self.g.value = False
        self.b.value = False

    def magenta(self):
        self.r.value = False
        self.g.value = True
        self.b.value = False

    def yellow(self):
        self.r.value = False
        self.g.value = False
        self.b.value = True

    #def off(self):
        #self.r.value = True
        #self.g.value = True
        # self.b.value = True