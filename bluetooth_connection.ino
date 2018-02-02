#include <SoftwareSerial.h>
SoftwareSerial BT(1, 0); 
// creates a "virtual" serial port/UART
// connect BT module TX to D10
// connect BT module RX to D11
// connect BT Vcc to 5V, GND to GND
String data;
//---------------for felx sensor start-------------------------
const int FLEX_PIN = A0; // Pin connected to voltage divider output
// Measure the voltage at 5V and the actual resistance of your
// 47k resistor, and enter them below:
const float VCC = 4.98; // Measured voltage of Ardunio 5V line
const float R_DIV = 45000.0; // Measured resistance of 3.3k resistor
// Upload the code, then try to adjust these values to more
// accurately calculate bend degree.
const float STRAIGHT_RESISTANCE = 37300.0; // resistance when straight
const float BEND_RESISTANCE = 90000.0; // resistance at 90 deg
//---------------for felx sensor end-------------------------

void setup()  
{
  // set the data rate for the SoftwareSerial port
  //Serial.begin(9600); 
  BT.begin(9600);
  // Send test message to other device
  BT.println("Hello from Arduino");
  //---------------for felx sensor start-------------------------
  pinMode(FLEX_PIN, INPUT);
  //---------------for felx sensor end-------------------------

}
char a; // stores incoming character from other device

void loop() 
{
    //---------------for felx sensor start-------------------------
  // Read the ADC, and calculate voltage and resistance from it
  int flexADC = analogRead(FLEX_PIN);
  float flexV = flexADC * VCC / 1023.0;
  float flexR = R_DIV * (VCC / flexV - 1.0);
  //Serial.println("Resistance: " + String(flexR) + " ohms");
  // Use the calculated resistance to estimate the sensor's
  // bend angle:
  float angle = map(flexR, STRAIGHT_RESISTANCE, BEND_RESISTANCE,0, 90.0);
  //Serial.println();
  //delay(500);
  //---------------for felx sensor end-------------------------
  
  //if(Serial.available()){
      delay(10); // The delay is necessary to get this working!
      data = String(angle); //Serial.readString();
      //Serial.println(data);

      BT.println(angle);
      delay(500);  
 // }

}

