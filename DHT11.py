from machine import Pin
import dht
import utime

dht11 = dht.DHT11(Pin(18))

while True:
    dht11.measure()
    t = dht11.temperature()
    h = dht11.humidity()
    print('T = ', t, 'H = ', h)
    utime.sleep(1)