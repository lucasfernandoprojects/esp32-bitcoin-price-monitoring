# Bitcoin Price Monitoring Using ESP32

Track Bitcoin prices automatically with an ESP32 and an OLED display. You can use MicroPython or Arduino to code this project.

*I've recently posted a tutorial about this project on YouTube. You can watch it [here](https://www.youtube.com/@lucasfernandochannel).*

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

This project was developed using both MicroPython and Arduino, so you can choose to work with either Thonny IDE or Arduino IDE. I'll walk you through the setup process for both MicroPython and Arduino.

Once you have the API key, download the ***boot.py*** and ***main.py*** files and update them with your specific information.

After downloading the boot.py and main.py files, open them in your preferred IDE. I highly recommend using Thonny IDE due to its excellent support for MicroPython.

Let's start with the boot.py file. This file is responsible for configuring your ESP32 board at startup, including connecting it to a Wi-Fi network. Update the **ssid** and **password** variables with your Wi-Fi credentials.

![WI-FI credentials](https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/api-key.png)

Next, open the main.py file and enter your Market Data API key.

![API key](https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/wifi-credentials.png)

Next, you'll need to configure your ESP32 board to work with the OLED screen. In my case, I used a screen with the **ST7789** chip, which, unfortunately, ESP32 doesn't support by default. If you're using the same screen, you'll need to update your board's firmware. I followed the instructions provided in this [repository](https://github.com/russhughes/st7789_mpy/tree/master?tab=readme-ov-file), which includes all the necessary files and step-by-step instructions to make your ESP32 compatible with ST7789 OLED displays.

Once you've completed the setup, upload the boot.py and main.py files to your board. The ESP32 will then request the Bitcoin price from the Market Data API every 15 minutes and display the result on the screen.

Ensure you properly attach the OLED screen to the ESP32 board. Since I’m using a 1.14" ST7789 OLED screen, I connected it as follows (adapt the code and connections according to your OLED features):

![Bitcoin price monitoring schematics.](https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/bitcoin-price-monitoring-schematics.png)

If you prefer using the Arduino IDE, I've developed this project within the Arduino ecosystem. Inside the "code" folder, there's another folder named "arduino-main", which contains the ***arduino-main.ino*** file. You can upload this file to your ESP32 using the Arduino IDE — just ensure that all the required libraries are installed. The wiring connections should follow the schematics provided above.

Additionally, there's no need to update the ESP32 firmware for this project. Unlike with MicroPython, the Arduino IDE natively supports the OLED ST7789 display.

<div style="display: flex; flex-wrap: wrap;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/18.jpg" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/19.jpg" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/20.jpg" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/21.jpg" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/22.jpg" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/23.jpg" width="400" height="250" style="margin: 10px;">
</div>
</br>

## CONCLUSION

By following these steps, you’ll successfully configure your ESP32 board to display real-time Bitcoin prices on an OLED screen. Leveraging the power of CoinAPI and the flexibility of MicroPython and Arduino, this project showcases how you can extend the capabilities of your ESP32 with custom firmware and API integrations. With everything set up correctly, your ESP32 will periodically retrieve the latest market data and keep you informed, making this a rewarding project for anyone interested in IoT and cryptocurrency.

If you enjoyed this project, you'll likely appreciate my tutorial on creating an [automated irrigation system using Arduino](https://github.com/lucasfernandoprojects/arduino-soil-moisture-monitoring).
