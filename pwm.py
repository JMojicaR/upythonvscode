from machine import Pin, PWM

pwm = PWM(Pin(18))
pwm.freq(500)
continuar = True

while continuar:
    a = input('Digite un valor de 0 a 100: ')
    if a == 'z':
        continuar = False
    else:
        pwm.duty_u16(int(a)*100)
pwm.deinit()
print('Fin de programa')
