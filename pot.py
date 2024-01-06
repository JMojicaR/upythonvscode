from machine import ADC
import utime

adc = ADC(2)

while True:
    # Read the analog input
    print(adc.read_u16())
    # Wait a bit before taking the next reading</s>
    utime.sleep_ms(200)