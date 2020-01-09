#include<Servo.h>
int pos = 0;
Servo motore;
void setup() {
  // put your setup code here, to run once:
  motore.attach(12);
  motore.write(0);
  delay(500);
  Serial.begin(9600);
}

void loop(){
  int k;
  int pos = 0;
 for(k = 0; k<180; k++){
  pos++;
  motore.write(pos);
  Serial.println(pos);
  delay(10);
 }
 
 for(k = 0; k<180; k++){
  pos--;
  motore.write(pos);
  Serial.println(pos);
  delay(10);
 }
}
