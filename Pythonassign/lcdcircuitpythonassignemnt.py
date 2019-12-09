import board
import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
from analogio import AnalogOut

analog_out=AnalogOut(board.A0)

lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

button_a = digitalio.DigitalInOut(board.D1)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

button_b = digitalio.DigitalInOut(board.D2)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.DOWN

up = 1
number = 0

while True:

    lcd.set_cursor_pos(0,0)
    lcd.print("Switch State: ") #prints out "switch state on lcd screen
    lcd.print(str(up)) #prints out the number that corresponds to the variable "up"
    lcd.set_cursor_pos(1,0)
    lcd.print("presses:") #prints out "presses:" below "switch state"

    if button_a.value:
        number += up #if button a is pressed then it adds 1 to "up"



    if button_b.value:
        up *= -1 #if button a is pressed then it changes what is next to switchstate, either 1 or -1
    lcd.print(str(number))
    lcd.print("     ")