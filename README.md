# Bitcoin Price Monitoring Using ESP32

Track Bitcoin prices automatically with an ESP32 and an OLED display.

![Photo of a project showing an OLED screen connected to an ESP32.](https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/3.jpg)

## THEORY

One of the standout features of the ESP32 board is its robust internet connectivity. This capability allows you to configure the board to make API calls and utilize the responses in various ways. This project leverages that very principle.

In this project, the ESP32 will periodically make API calls to retrieve the current Bitcoin price in US dollars and display this information on an OLED screen.

<div style="display: flex; flex-wrap: wrap;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/1.jpg" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/2.jpg" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/4.jpg" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/5.jpg" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/6.jpg" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/7.jpg" width="400" height="250" style="margin: 10px;">
</div>
</br>

## SET UP

To achieve this, I used CoinAPI, a provider of cryptocurrency APIs. First, you'll need to create an account and obtain a free Market Data API key, which allows you to make up to 100 calls at no cost.

![CoinAPI website - first page.](https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/coin-api-1.png)

![Form to request a free Market Data API key.](https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/coin-api-2.png)

Once you have the API key, download the **boot.py** and **main.py** files and update them with your specific information.

This project is built using MicroPython, and I used Thonny IDE for coding. After downloading the boot.py and main.py files, open them in your preferred IDE.

Let's start with the boot.py file. This file is responsible for configuring your ESP32 board at startup, including connecting it to a Wi-Fi network. Update the **ssid** and **password** variables with your Wi-Fi credentials.

![WI-FI credentials](https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/wifi-credentials.png)

Next, open the main.py file and enter your Market Data API key.

![API key](https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/api-key.png)

Next, you'll need to configure your ESP32 board to work with the OLED screen. In my case, I used a screen with the **ST7789** chip, which, unfortunately, ESP32 doesn't support by default. If you're using the same screen, you'll need to update your board's firmware. I followed the instructions provided in this [repository](https://github.com/russhughes/st7789_mpy/tree/master?tab=readme-ov-file), which includes all the necessary files and step-by-step instructions to make your ESP32 compatible with ST7789 OLED displays.

Once you've completed the setup, upload the boot.py and main.py files to your board. The ESP32 will then request the Bitcoin price from the Market Data API every 15 minutes and display the result on the screen.
