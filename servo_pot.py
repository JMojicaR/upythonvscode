from machine import PWM, Pin, ADC
import utime

pwm = PWM(Pin(18))
pwm.freq(50)
adc = ADC(2)

while True:
    angulo = int(adc.read_u16()/364)
    dc = 1638.375 + 36.4*angulo
    pwm.duty_u16(int(dc))