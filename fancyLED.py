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

    def alternate(self):
        self.one.value = False 
        self.two.value = True
        self.three.value = True 
        time.sleep(.8)
        self.one.value = True 
        self.two.value = False 
        self.three.value = False 
        time.sleep(.8)
        self.one.value = True 
        self.two.value = True
        self.three.value = False  
        time.sleep(.6) 

    def blink(self):
        self.one.value = True 
        self.two.value = True 
        self.three.value = False 
        time.sleep(.25)
        self.one.value = False 
        self.two.value = True 
        self.three.value = True 
        time.sleep(.25)
    
    def chase(self):
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

    def sparkle(self):
        self.one.value = False 
        self.two.value = True 
        self.three.value = False 
        time.sleep(.2)





