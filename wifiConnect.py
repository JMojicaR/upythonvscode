import network

ssid = 'Totalplay-D3AB'
passwd = 'D3ABB2BB9PssBWP6'

wf = network.WLAN(network.STA_IF)
wf.active(True)
wf.connect(ssid, passwd)

while not wf.isconnected():
    pass
print('Connected!')
print(wf.ifconfig())