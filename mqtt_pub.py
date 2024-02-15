from machine import Pin
from time import sleep
from umqtt.simple  import MQTTClient
import network
from random import *

SSID = "D3AB-5G"
PASSWORD = "D3ABB2BB9PssBWP6"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    pass

print("Connected to Wi-Fi")
print(wlan.ifconfig())

SERVER = 23