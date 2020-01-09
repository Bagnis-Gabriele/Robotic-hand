#include<Servo.h>

#define FINGERS 5
#define MAX_DEGREE 180

//servo pin
int s1 = 5;
int s2 = 6;
int s3 = 7;
int s4 = 8;
int s5 = 9;

//servo objects
Servo m1;
Servo m2;
Servo m3;
Servo m4;
Servo m5;

//servo degree position
int p1 = 0;
int p2 = 0;
int p3 = 0;
int p4 = 0;
int p5 = 0;

void setup() {
  //select the servo pin
  m1.attach(s1);
  m2.attach(s2);
  m3.attach(s3);
  m4.attach(s4);
  m5.attach(s5);
  Serial.begin(9600);
}

void loop(){
  //set the servo degree
  m1.write(p1);
  if(p2 > 30) m2.write(p2);
  if(p3 > 60) m3.write(p3);
  if(p4 > 90) m4.write(p4);
  if(p5 > 120) m5.write(p5);

  Serial.println(p1);
  Serial.println(p2);
  Serial.println(p3);
  Serial.println(p4);
  Serial.println(p5);
  
  //increment the position or reset them if reach 180 degrees
  if(p1 < 180){
    p1++;
  }else{
    p1 = 0;
  }
  if(p2 < 180){
    p2++;
  }else{
    p2 = 0;
  }
  if(p3 < 180){
    p1++;
  }else{
    p3= 0;
  }
  if(p4 < 180){
    p4++;
  }else{
    p4 = 0;
  }
  if(p5 < 180){
    p5++;
  }else{
    p5 = 0;
  } 

  delay(4);
}
