rom lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

lcd.clear()

lcd.set_cursor_pos(1, 4)
lcd.print(dog)

lcd.set_cursor_mode(CursorMode.LINE)