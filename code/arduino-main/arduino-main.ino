//=============================================================================
// Track Bitcoin prices automatically with an ESP32 and an OLED display
// Created on 19 August 2024
// Created by Lucas Fernando (https://www.youtube.com/@lucasfernandochannel)
// You are free to use this code the way you want
//=============================================================================

#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7789.h>
#include <SPI.h>

// Replace with your network credentials
const char* ssid = "";
const char* password = "";

// Replace with your CoinAPI key
const char* api_key = "";
const char* api_url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD";

// Define the waiting time between the API calls
const int waiting_time = 900000; // Wait for 15 minutes

// Define the pins
#define TFT_CS 5
#define TFT_RST 4
#define TFT_DC 2

// Initialize the ST7789 display
Adafruit_ST7789 tft = Adafruit_ST7789(TFT_CS, TFT_DC, TFT_RST);

void setup() {
  // Initialize serial communication
  Serial.begin(115200);

  // Initialize the display
  tft.init(135, 240);
  tft.setRotation(3);
  tft.fillScreen(ST77XX_BLACK);

  // Connect to Wi-Fi
  connectToWiFi();

  // Make API call and display the result
  displayBitcoinPrice();
}

void loop() {
  delay(waiting_time);
  displayBitcoinPrice();  
}

void connectToWiFi() {
  tft.setCursor(10, 10);
  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(2);
  tft.print("Connecting to Wi-Fi");  

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");  
  }

  Serial.println("Connected to Wi-Fi");
  tft.fillScreen(ST77XX_BLACK);
}

String formatTime(String time) {
  // Extract date and time components
  String date = time.substring(0, 10);
  String timeOfDay = time.substring(11, 16);

  // Convert date components
  String year = date.substring(0, 4);  // Year
  String month = date.substring(5, 7);  // Month
  String day = date.substring(8, 10);  // Day

  // Convert the month number to the month name
  String monthNames[] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
  int monthIndex = month.toInt() - 1;
  String monthName = monthNames[monthIndex];

  // Convert time from 24-hour to 12-hour format
  int hour = timeOfDay.substring(0, 2).toInt();
  String minute = timeOfDay.substring(3, 5);  // Minute
  String period = "AM";

  if (hour >= 12) {
    period = "PM";
    if (hour > 12) hour -= 12;
  } else if (hour == 0) {
    hour = 12; // Midnight case
  }

  String formattedTime = monthName + " " + day + ", " + year + ", ";
  formattedTime += String(hour) + ":" + minute + " " + period + " UTC";

  return formattedTime;
}


void displayBitcoinPrice() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(api_url);
    http.addHeader("X-CoinAPI-Key", api_key);

    int httpCode = http.GET(); // Make the request

    if (httpCode > 0) {
      String payload = http.getString();
      Serial.println(payload);
      
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, payload);

      float price = doc["rate"];
      String date = doc["time"];

      // Display the price on the OLED
      tft.fillScreen(ST77XX_BLACK);
      tft.setTextColor(ST77XX_WHITE);
      tft.setCursor(0, 0);
      tft.setTextSize(3);
      tft.print("Bitcoin Price");
      tft.setCursor(0, 30);
      tft.print("USD ");
      tft.setCursor(70, 30);
      tft.print(price, 2);

      String formatted_date = formatTime(date);

      tft.setTextSize(1);
      tft.setCursor(0, 115);
      tft.print(formatted_date);
      tft.setCursor(0, 125);
      tft.print("Update every 15 minutes");
    } else {
      Serial.println("Error on HTTP request");  
    }
    http.end(); // End the request
  }  
}
