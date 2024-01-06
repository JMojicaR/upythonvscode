from machine import ADC, Pin
import utime

led1 = Pin(18, Pin.OUT)
led2 = Pin(19, Pin.OUT)
led3 = Pin(20, Pin.OUT)
led4 = Pin(21, Pin.OUT)
adc = ADC(2)

gp = [led1, led2, led3, led4]

while True:
    for k in gp:
        tiempo = int(50 + (adc.read_u16()/327))
        k.value(1)
        utime.sleep_ms(tiempo)  # 50 ms delay between LED
        k.value(0)