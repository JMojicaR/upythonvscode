from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import math
import utime

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

y0 = 32
x0 = 19

for x in range(91):
    y = -int(30*math.sin(4*x*2*math.pi/360))
    oled.pixel(x + x0, y0, 1)
    oled.line(x+x0, y0, x+x0, y+y0, 1)
    oled.show()