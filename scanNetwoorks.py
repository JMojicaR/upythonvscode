import network

wf = network.WLAN(network.STA_IF)
wf.active(True)
lista = wf.scan()
print("Lista de redes disponibles:")
for i in lista:
    print(i[0])