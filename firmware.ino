#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

const int sensorPin = 2; // Interrupt pin
volatile int count = 0;
LiquidCrystal_I2C lcd(0x27, 16, 2);

void countISR() {
  count++;
}

void setup() {
  Serial.begin(9600);
  pinMode(sensorPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(sensorPin), countISR, FALLING);
  
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Line Active...");
}

void loop() {
  // Send count to Python every 5 seconds
  Serial.println(count);
  
  lcd.setCursor(0,1);
  lcd.print("Count: ");
  lcd.print(count);
  
  delay(5000);
}
