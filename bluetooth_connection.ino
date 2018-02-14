#include <SoftwareSerial.h>
SoftwareSerial BT(1, 0); 
// creates a "virtual" serial port/UART
// connect BT module TX to D10
// connect BT module RX to D11
// connect BT Vcc to 5V, GND to GND
String data;
//---------------for felx sensor start-------------------------
const int Finger_0 = A0;
const int Finger_1 = A1;
const int Finger_2 = A2;
const int Finger_3 = A3;
const int Finger_4 = A4;

// Pin connected to voltage divider output
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
  
  //---------------for felx sensor start-------------------------
  pinMode(Finger_0, INPUT);
  pinMode(Finger_1, INPUT);
  pinMode(Finger_2, INPUT);
  pinMode(Finger_3, INPUT);
  pinMode(Finger_4, INPUT);
  //delay(50);
  //---------------for felx sensor end-------------------------
 BT.begin(115200);
  // Send test message to other device
  //BT.println("Hello from Arduino");
}
char a; // stores incoming character from other device

void loop() {
  //mesure 5 angles
//      float angle_0 = cal_angle(Finger_0);//拇指
//      float angle_1 = cal_angle(Finger_1);//食指
//      float angle_2 = cal_angle(Finger_2);//中指
//      float angle_3 = cal_angle(Finger_3);
//      float angle_4 = cal_angle(Finger_4);//尾指
      short angle_0 = analogRead(Finger_0);//拇指
      short angle_1 = analogRead(Finger_1);//食指
      short angle_2 = analogRead(Finger_2);//中指
      short angle_3 = analogRead(Finger_3);
      short angle_4 = analogRead(Finger_4);//尾指
      
      
      delay(10); // The delay is necessary to get this working!
      String data_flex_sensor = String(angle_0)+" "+String(angle_1)+" "+String(angle_2)+" "+String(angle_3)+" "+String(angle_4)+" "; //Serial.readString();

      BT.println(data_flex_sensor);
      //delay(10);  
 // }

}
float cal_angle(int finger_number){
      //---------------for felx sensor start-------------------------
  // Read the ADC, and calculate voltage and resistance from it
  int flexADC = analogRead(finger_number);
  float flexV = flexADC * VCC / 1023.0;
  float flexR = R_DIV * (VCC / flexV - 1.0);
  float angle = map(flexR, STRAIGHT_RESISTANCE, BEND_RESISTANCE,0, 90.0);
  return angle;
}

