#include<Servo.h>

#define FINGERS 5
#define MAX_DEGREE 180
#define NCHAR 15

String msg = String(NCHAR); //message sent from leap motion sensor
String number = String(3);  //single finger position to convert into int

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
  Serial1.begin(19200);
}

void loop(){
  //if there is data avaible read it
  if(Serial.available()){
    int k = 0;  //message index
    int i = 0;  //single finger position index
    msg = Serial.read();

    //divide the string in 5 numbers and refresh single finger position each time
    for(k=0; k<3; k++){
      i=0;
      number.setCharAt(i,msg.charAt(k));
      i++;
    }
    m1.write(number.toInt()); //THUMB
    Serial1.println(number);
    for(k=3; k<6; k++){
      i=0;
      number.setCharAt(i,msg.charAt(k));
      i++;
    }
    m2.write(number.toInt()); //INDEX
    Serial1.println(number);
    for(k=6; k<9; k++){
      i=0;
      number.setCharAt(i,msg.charAt(k));
      i++;
    }
    m3.write(number.toInt()); //MIDDLE
    Serial1.println(number);
    for(k=9; k<12; k++){
      i=0;
      number.setCharAt(i,msg.charAt(k));
      i++;
    }
    m4.write(number.toInt()); //RING
    Serial1.println(number);
    for(k=12; k<15; k++){
      i=0;
      number.setCharAt(i,msg.charAt(k));
      i++;
    }
    m5.write(number.toInt()); //PINKIE
    Serial1.println(number);
  }
}
