import network
import urequests
import time


SSID = 'liangzhiyu'
PASSWORD = '123456789'


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)


while not wlan.isconnected():
    print('is connecting')
    time.sleep(1)

print('wi-fi sucessful')
print('IP adress:', wlan.ifconfig())


api_url = 'http://172.20.10.5:3080'  
try:
    response = urequests.get(api_url)
    print('server respon:', response.text)
    response.close()
except Exception as e:
    print('fail:', e)

