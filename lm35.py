from machine import ADC
import utime

sensor = ADC(4)
lm35 = ADC(1)

while True:
    valor = sensor.read_u16()
    valor_lm35 = lm35.read_u16()
    voltaje = valor*3.3/65535
    voltaje_lm35 = valor_lm35*3.3/65535
    temp = 27-(voltaje-0.706)/0.001721
    temp_lm35 = 100*voltaje_lm35
    print("Temperatura: {:.2f} C".format(temp))
    print("Temperatura LM35: {:.2f} C".format(temp_lm35))
    utime.sleep_ms(500)