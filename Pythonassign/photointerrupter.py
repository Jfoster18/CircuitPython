import board
import time
from digitalio import DigitalInOut, Direction, Pull.UP

counter = 0
interupts = 0

photo = DigitalInOut(board.D7)
photo.direction = Direction.INPUT
photo.pull = Pull.UP
initial = time.monotonic()

while True:
    now = time.monotonic()
    if time.monotonic() % 4 == 0:
        print("the number of interupts is ", counter ) #prints out the number of times its been interrupted
    if photo.value and interupts ==0:
        interupts = 1
        counter = counter + 1 # adds one to "counter" for every interrupt


    interupts = photo.value