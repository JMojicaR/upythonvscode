from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import math

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

x0 = 64
y0 = 32
r = 7

for th in range (361):
    #for r in range(64):        
    x = x0 + int((r) * math.cos(math.radians(4*th)))
    y = y0 - int((r) * math.sin(math.radians(4*th)))
    r = (361/360)*r
    oled.pixel(x , y,  1)
    oled.show()