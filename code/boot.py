from network import WLAN, STA_IF
from machine import Pin
from time import sleep

# Local network credentials
ssid = 'WIFI_NAME'
password = 'WIFI_PASSWORD'
sleeping_time = 0.2

def connect_wifi(ssid, password):
    # Connect to local network (wi-fi)
    try:
        print("Connecting to wi-fi")
        built_in_led = Pin(2, Pin.OUT)
      
        station = WLAN(STA_IF)
        station.active(True)
        station.connect(ssid, password)
      
        while station.isconnected() == False:
            built_in_led.value(0)
            sleep(sleeping_time)
            built_in_led.value(1)
            sleep(sleeping_time)

        print(f'Board connected to {ssid}')
        return station
    except:
        print(f'Couldn\'t connect to {ssid}')
        return None


# Connect to network
connect_wifi(ssid, password)
