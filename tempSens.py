from machine import ADC
import utime

sensor = ADC(4)

while True:
    valor = sensor.read_u16()
    voltaje = valor*3.3/65535
    temp = 27-(voltaje-0.706)/0.001721
    print("Temperatura: {:.2f} C".format(temp))
    utime.sleep_ms(500)