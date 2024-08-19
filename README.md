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

To achieve this, I used CoinAPI, a provider of cryptocurrency APIs. First, you'll need to create an account and obtain a free Market Data API key, which allows you to make up to 100 calls at no cost.

<div style="display: flex; flex-wrap: wrap;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/coin-api-1.png" width="400" height="250" style="margin: 10px;">
    <img src="https://github.com/lucasfernandoprojects/esp32-bitcoin-price-monitoring/blob/main/photos/coin-api-2.png" width="400" height="250" style="margin: 10px;">
</div>
</br>
