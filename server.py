import network
import utime
import usocket

ssid = 'Totalplay-D3AB'
passwd = 'D3ABB2BB9PssBWP6'

wf = network.WLAN(network.STA_IF)
wf.active(True)
wf.connect(ssid, passwd)

while not wf.isconnected():
    pass
print('Connected!')

net = wf.ifconfig()
ip = net[0]
print(ip)
s = usocket.socket()
s.bind((ip, 2023))
s.listen(10)
print('Socket creado, esperando conexion...')
(sc, addr) = s.accept()
print('Cliente conectado, IP: ', addr)
continuar = True
while continuar:
    data = sc.recv(32).decode()
    print(data)
    if(data == 'z'):
        continuar = False
print('Fin de programa')
sc.close()
s.close()
