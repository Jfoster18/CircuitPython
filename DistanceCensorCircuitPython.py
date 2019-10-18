import time
import board
import neopixel
from adafruit_hcsr04 import HCSR04
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D1, echo_pin=board.D7)
pixel_pin = board.NEOPIXEL
num_pixels=1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels,brightness = 0.1)

red = (255,0,0)
pink =(255,0,180)
cyan = (0,255,255)
purple = (180,0,255)
blue = (0,0,255)
green = (0,255,0)


while True:
    try:
        distance = sonar.distance
        print((sonar.distance))
        if distance>0 and distance< 7:
            pixels.fill(red)
            pixels.show()
        if distance>7 and distance< 10:
            pixels.fill(pink)
            pixels.show()
        if distance>10 and distance< 17:
            pixels.fill(purple)
            pixels.show()
        if distance>17 and distance<20:
            pixels.fill(blue)
            pixels.show()
        if distance> 22 and distance<25:
            pixels.fill(cyan)
            pixels.show()
        if distance>25 and distance<35:
            pixels.fill(green)
            pixels.show()



    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.1)