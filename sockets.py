import network
from machine import Pin
import usocket

ssid = 'Totalplay-D3AB'
passwd = 'D3ABB2BB9PssBWP6'

wf = network.WLAN(network.STA_IF)
wf.active(True)
wf.connect(ssid, passwd)

while not wf.isconnected():
    pass
print('Connected!')

led = Pin(18, Pin.OUT)
net = wf.ifconfig()
ip = net[0]
print(ip)
s = usocket.socket()
s.bind((ip, 2023))
s.listen(10)
print('Socket creado, esperando conexiones...')
(sc, addr) = s.accept()
print('Cliente conectado, IP: ', addr)
continuar = True
while continuar:
    dato = sc.recv(32).decode()
    print(dato)
    if(dato == 'Z'):
        continuar = False
    elif(dato == "A"):
        led.on()
    elif(dato == "B"):
        led.off()
print('Fin de programa')
sc.close()
s.close()
