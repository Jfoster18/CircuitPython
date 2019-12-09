import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")  #serial monitor prints out "make it red"

while True:
     dot.fill((255,0,0))  # the light on board turns on red