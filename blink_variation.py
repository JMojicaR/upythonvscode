from machine import ADC, Pin
import utime

led = Pin(18, Pin.OUT)
adc = ADC(2)  # create an instance of the ADC class

while True:
    led.value(1)  # turn off LED to show we're waiting for input
    tiempo = int(50 + (adc.read_u16()/327))
    print("Tiempo de espera:",tiempo,"ms")
    utime.sleep_ms(tiempo)
    led.value(0)  # turn on LED when time is up
    utime.sleep_ms(tiempo)
