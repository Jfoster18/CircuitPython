import time
import board
import neopixel
from adafruit_hcsr04 import HCSR04
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D1, echo_pin=board.D7)
pixel_pin = board.NEOPIXEL
num_pixels=1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels,brightness = 0.1)

red = (255,0,0) #tells neopixel what color to be
pink =(255,0,180)
cyan = (0,255,255)
purple = (180,0,255)
blue = (0,0,255)
green = (0,255,0)


while True:
    try:
        distance = sonar.distance #all distance is measured in cm
        print((sonar.distance))
        if distance>0 and distance< 7: #if distance is between 0 and 7cm then the neopixel light turns red
            pixels.fill(red)
            pixels.show()
        if distance>7 and distance< 10: #if distance is between 7 and 10 then neopixel light fades pink
            pixels.fill(pink)
            pixels.show()
        if distance>10 and distance< 17: #if distance is between 10 and 17 then neopixel light fades purple
            pixels.fill(purple)
            pixels.show()
        if distance>17 and distance<20: #if distance is between 17 and 20 then neopixel light fades blue
            pixels.fill(blue)
            pixels.show()
        if distance> 22 and distance<25: #if distance is between 22 and 25 then neopixel light fades cyan
            pixels.fill(cyan)
            pixels.show()
        if distance>25 and distance<35: #if distance is between 25 and 35 then neopixel light fades green
            pixels.fill(green)
            pixels.show()



    except RuntimeError: #if too far away or to close then "Retrying!" gets printed out on serial monitor.
        print("Retrying!")
        pass
    time.sleep(0.1)