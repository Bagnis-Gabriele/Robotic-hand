#include<Servo.h>

#define FINGERS 5
#define MAX_DEGREE 180

//pin of the servos
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

//initialize the servo degree position
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

  m1.write(180);
  m2.write(180);
  m3.write(180);
  m4.write(180);
  m5.write(180);

  delay(2000);
}

void loop(){
  //close
  for(int k=0; k<MAX_DEGREE; k+=5){
    //increment all servos dergees
    p1 += 5;
    p2 += 5;
    p3 += 5;
    p4 += 5;
    p5 += 5;

    //renew servos position
    m1.write(p1);
    m2.write(p2);
    m3.write(p3);
    m4.write(p4);
    m5.write(p5);

    //delay(4);

    Serial.println(p1);
    Serial.println(p2);
    Serial.println(p3);
    Serial.println(p4);
    Serial.println(p5);
  }

  //open
  for(int k=0; k<MAX_DEGREE; k+=5){
    //increment all servos dergees
    p1 -= 5;
    p2 -= 5;
    p3 -= 5;
    p4 -= 5;
    p5 -= 5;

    //renew servos position
    m1.write(p1);
    m2.write(p2);
    m3.write(p3);
    m4.write(p4);
    m5.write(p5);

    //delay(4);

    Serial.println(p1);
    Serial.println(p2);
    Serial.println(p3);
    Serial.println(p4);
    Serial.println(p5);
  }
}
