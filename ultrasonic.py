from machine import Pin
import utime

trig = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)

while True:
    trig.value(1)
    utime.sleep_us(10)  # send a pulse of at least
    trig.value(0)
    t1 = 0
    t2 = 0
    #t2 = utime.ticks_us()
    while echo.value() == 0:
        #print('value 0')
        t1 = utime.ticks_us()
    while echo.value() == 1:
        #print('value 1')
        t2 = utime.ticks_us()
    t = t2-t1
    d = 17*(t)/1000 
    print(d, ' cm')
    utime.sleep_ms(500)