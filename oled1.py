from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

oled.text("HOLA", 0, 0, 1)
oled.text("Raspberry", 0, 15, 1)
oled.text("Pi Pico", 0, 30, 1)
oled.show()

while True:
    pass