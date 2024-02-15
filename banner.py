from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
import utime

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, 39, 2, 16)

mensaje = "HOLA MUNDO"

lcd.move_to(2, 1)
lcd.putstr(mensaje)

while  True:
    lcd.move_to(2, 1)
    lcd.putstr(mensaje)
    lcd.show_cursor()
    for i in range(len(mensaje)):
        lcd.move_disp_right()
        utime.sleep(1)
    lcd.clear() 
    