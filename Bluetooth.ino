#include <SoftwareSerial.h>
SoftwareSerial BTSerial(0,1);

//String command = "helloWorld";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Yo start");
  BTSerial.begin(9600);

}

void loop() {
  //Serial.println("im sending info via bluetooth");
  //delay(1000);
  if (Serial.available()){
    delay(10); // The delay is necessary to get this working!
    BTSerial.write(Serial.read());
  }
}
