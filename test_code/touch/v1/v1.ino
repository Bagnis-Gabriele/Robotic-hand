#include<Servo.h>

#define FINGERS 5

//variables to transform the string into numbers
String msg;    //message sent from python
int number[FINGERS]; //vector for storing servo data
int power;     //exponentiation to calculate servo data
int k;         //counter
int pos;       //position to store the servo data

//servo pin
int servos[FINGERS] = {5,6,7,8,9};

//tousch pins
int touch[FINGERS] = {A0,A1,A2,A3,A4};

//vectore that memorize finger's distance
int distances[FINGERS];

//servo objects
Servo motors[FINGERS];

void setup() {
  //associate servo motor to pin
  for(int i=0; i<FINGERS; i++){
    motors[i].attach(servos[i]);
  }
  
  //initialize the serial port
  Serial.begin(9600);
  
  //servo reset
  for(int i=0; i<FINGERS; i++){
    motors[i].write(180);
  }

  //initialize all fingers distances to 0
  for(int i=0; i<FINGERS; i++){
    distances[i] = 0;
  }

  //set photoresistors pins as input
  for(int i=0; i<FINGERS; i++){
    pinMode(touch[i],INPUT);
  }
}

void loop(){
  /*if there is data avaible read it
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

    //print number
    for (k=0;k<5;k++){
      if(number[k]<100){
        if(number[k]<10){
          Serial.print("00");
        }else{
          Serial.print("0");
        }
      }
      Serial.print(number[k]);
    }
  }

  for(int i=0; i<FINGERS; i++){
    distances[i] = analogRead(touch[i])
  }
  */

  //read distacne and memorize it in distances vector
  distances[0] = analogRead(A0);
  Serial.println(distances[0]);

  delay(1000);
  
}
