from machine import PWM, Pin

pwm = PWM(Pin(18))
pwm.freq(50) #20ms
continuar = True


while continuar:
    angulo = input("Digite el valor del angulo: ")
    if(angulo == 'z'):
        pwm.deinit()
        continuar = False
    else:
        dc = int(1638.375 + 36.4*int(angulo))
        pwm.duty_u16(dc)
print('Fin de programa')