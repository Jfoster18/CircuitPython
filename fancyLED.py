import board #pylint: disable-msg=import-error
import time
import digitalio #pylint: disable-msg=import-error

class FancyLED():

    def __init__(self, one, two, three):
        self.one = digitalio.DigitalInOut(one)
        self.two = digitalio.DigitanInOut(two)
        self.three = digitalio.DigitalInOut(three)
        self.one.direction = digitalio.Direction.OUTPUT
        self.two.direction = digitalio.Direction.OUTPUT
        self.three.direction = digitalio.Direction.OUTPUT

    def alternate(self): #defines alternate
        self.one.value = False
        self.two.value = True  #tells which led gets alternate and which dosen't
        self.three.value = True  #pretty much same thing for all of the lighting effects
        time.sleep(.8) # waits a little bit before next rotation starts
        self.one.value = True
        self.two.value = False
        self.three.value = False
        time.sleep(.8)
        self.one.value = True
        self.two.value = True
        self.three.value = False
        time.sleep(.6)

    def blink(self): #defines blink
        self.one.value = True
        self.two.value = True
        self.three.value = False
        time.sleep(.25)
        self.one.value = False
        self.two.value = True
        self.three.value = True
        time.sleep(.25)

    def chase(self): #defines chase
        self.one.value = True
        self.two.value = False
        self.three.value = True
        time.sleep(.15)
        self.one.value = False
        self.two.value = True
        self.three.value = False
        time.sleep(.15)
        self.one.value = True
        self.two.value = True
        self.three.value = False
        time.sleep(.15)

    def sparkle(self): #defines sparkle
        self.one.value = False
        self.two.value = True
        self.three.value = False
        time.sleep(.2)




