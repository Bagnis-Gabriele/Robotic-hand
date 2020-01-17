#include<Servo.h>

//variables to transform the string into numbers
String msg;    //message sent from python
int number[5]; //vector for storing servo data
int power;     //exponentiation to calculate servo data
int k;         //counter
int pos;       //position to store the servo data

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

void setup() {
  //select the servo pin
  m1.attach(s1);
  m2.attach(s2);
  m3.attach(s3);
  m4.attach(s4);
  m5.attach(s5);
  
  //initialize the serial port
  Serial.begin(9600);
  
  //servo reset
  m1.write(180);
  m2.write(180);
  m3.write(180);
  m4.write(180);
  m5.write(180);
}

void loop(){
  
  //if there is data avaible read it
  if(Serial.available()){
    
    //read message
    msg = Serial.readString();

    //vector reset
    for (k=0;k<5;k++){
      number[k]=0;
    }

    //Servo data calculation
    for (k=0; k<15; k++){
      //position setting
      switch (k){
        case 0: case 1: case 2: pos=0; break;
        case 3: case 4: case 5: pos=1; break;
        case 6: case 7: case 8: pos=2; break;
        case 9: case 10: case 11: pos=3; break;
        case 12: case 13: case 14: pos=4; break;
      }
      //pow setting
      switch (k){
        case 0: case 3: case 6: case 9: case 12: power=100; break;
        case 1: case 4: case 7: case 10: case 13: power=10; break;
        case 2: case 5: case 8: case 11: case 14: power=1; break;
      }
      //sum of the number
      number[pos]+=(((int)msg.charAt(k))-48)*power;
    }

    m1.write(number[0]);
    m2.write(number[1]);
    m3.write(number[2]);
    m4.write(number[3]);
    m5.write(number[4]);

    Serial.print("1");
  }
  
}
