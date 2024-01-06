from machine import Pin
from utime import sleep

pin = Pin(25, Pin.OUT)

print('Led starts flashing')
while True:
    pin.value(1)
    sleep(0.5)  # on for half a second
    pin.value(0)
    sleep(0.5)  # off for half a second</s>
