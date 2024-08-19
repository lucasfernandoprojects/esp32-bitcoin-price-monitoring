# This code is set up to display information on a SPI OLED screen that uses the st7789 chip
# MicroPython doesn't support this hardware as default. So you need to update your board firmware
# To solve this problem, I used the firmware available on this GitHub repo:
# https://github.com/russhughes/st7789_mpy/tree/master?tab=readme-ov-file
# Information about how to update your board and how to use the st7789 library can be found on this repository README

import urequests as request
import vga1_bold_16x32 as font
import vga1_8x16 as font2
from st7789 import ST7789
from machine import Pin, SPI
from time import sleep

def init_oled_spi(height=135, width=240):
    # Adjust the baudrate according to your screen settings
    spi = SPI(2, baudrate=100000000, polarity=1, sck=Pin(18), mosi=Pin(23))
    display = ST7789(spi, height, width, reset=Pin(4, Pin.OUT), dc=Pin(2, Pin.OUT), backlight=Pin(19, Pin.OUT), cs=Pin(5, Pin.OUT))
    display.init()
    display.on()
    display.fill(0x0000) # Black screen background
    display.rotation(1) # Certify screen is landscape
    return display


def display_text(display, text, font, font2):
    display.text(font, "Bitcoin Price", 0, 0)
    display.text(font, 'USD ' + str(text['rate']), 0, 35)
    display.text(font2, text['time'], 0, 99)
    display.text(font2, 'Update every 15 minutes', 0, 119)
    
    
def convert_date(date):
    # Convert the date to a readable format
    convert_1 = date.split('-')
    convert_2 = convert_1[2][2:]
    convert_1[2] = convert_1[2][:2]
    convert_2 = convert_2.split(':')
    convert_2[0] = convert_2[0][1:]
    
    hours = int(convert_2[0])
    if (hours < 12):
        text = 'AM'
    else:
        text = 'PM'
    
    num = int(convert_1[1])
    if (num == 1):
        month = 'Jan'
    elif (num == 2):
        month = 'Feb'
    elif (num == 3):
        month = 'Mar'
    elif (num == 4):
        month = 'Apr'
    elif (num == 5):
        month = 'May'
    elif (num == 6):
        month = 'Jun'
    elif (num == 7):
        month = 'Jul'
    elif (num == 8):
        month = 'Aug'
    elif (num == 9):
        month = 'Sep'
    elif (num == 10):
        month = 'Oct'
    elif (num == 11):
        month = 'Nov'
    elif (num == 12):
        month = 'Dec'
    else:
        month = 'None'
        
    new_date = month + ' ' + convert_1[2] + ', ' + convert_1[0] + ', ' + convert_2[0] + ':' + convert_2[1] + ' '+ text + ' UTC'
    return new_date
    
    
def bitcoin_price():
    # Get the current Bitcoin price in USD
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    # Add your own key - it uses the CoinAPI service
    headers = {
        'X-CoinAPI-Key': 'API_KEY'
    }
    response = request.get(url, headers=headers)
    response_text = response.text
    
    # Extracting data and converting this to a Python dictionary
    json_start = response_text.find('{')
    json_end = response_text.rfind('}') + 1
    clean_json = response_text[json_start:json_end]
    data = eval(clean_json)
    return data


if __name__ == '__main__':
    wait_time = 900 # 15 minutes
    try:
        while True:
            # Get Bitcoin price in USD right now
            data = bitcoin_price()
            # Convert date
            converted_date = convert_date(data['time'])
            data['time'] = converted_date
            # Print the response
            print(data)
            # Initialize OLED screen
            oled = init_oled_spi()
            # Show the response on OLED screen
            display_text(oled, data, font, font2)
            # Wait for 15 minutes before making another API call
            # CoinAPI limit requests to 100 per day
            # and that's about one call every 15 minutes
            sleep(wait_time)
    except:
        print('Could not get Bitcoin price. Please try again later.')
