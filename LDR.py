from machine import ADC
import utime

ldr = ADC(0)

while True:
    ldr_value = ldr.read_u16()
    print("LDR value is {}".format(ldr_value))
    utime.sleep_ms(500)