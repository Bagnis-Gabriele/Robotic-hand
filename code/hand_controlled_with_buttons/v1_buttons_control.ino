#include<Servo.h>

#define FINGERS 5
#define BUTTONS 10
#define MAX_DEGREE 180
#define INC 5 //increment of degrees for servo movement

//FINGER TRIGGERS BUTTON
int fingersButtons[BUTTONS];  //sequence is: mignolo su, mignolo giù, anulare su, anulare giù...
Servo servo_motors[FINGERS];  //create servo object
int servo_degree[FINGERS];

void setup() {
  Serial.begin(9600);
  
  //initialize fingers buttons vector, and set pins to pull up mode
  for(int k=2; k<12; k++){
    fingersButtons[k-2] = k;
    pinMode(fingersButtons[k], INPUT_PULLUP);
  }

  //initialize servo pins
  for(int k=0; k<FINGERS; k++){
    servo_motors[k].attach(k+12);
  }

  //initialize fingers dergees vector
  for(int k=0; k<FINGERS; k++){
    servo_degree[k] = 0;
  }
}

void loop() {
  //check if the user press some buttons
  for(int k=0; k<BUTTONS; k++){
    if(fingersButtons[k] == LOW){
      switch(k){
        case 0: //increment mignolo
        if (servo_degree[0] < MAX_DEGREE) servo_motors[0].write(servo_degree[0] + INC); 
        break;
        
        case 1: //decrement mignolo
        if (servo_degree[0] > MAX_DEGREE) servo_motors[0].write(servo_degree[0] - INC);
        break;
        
        case 2: //incremenet anulare
        if (servo_degree[1] < MAX_DEGREE) servo_motors[1].write(servo_degree[1] + INC);
        break;
        
        case 3: //decrement anulare
        if (servo_degree[1] < MAX_DEGREE) servo_motors[1].write(servo_degree[1] - INC);
        break;
        
        case 4: //increment medio
        if (servo_degree[2] < MAX_DEGREE) servo_motors[2].write(servo_degree[2] + INC);
        break;
        
        case 5: //decrement medio
        if (servo_degree[2] < MAX_DEGREE) servo_motors[2].write(servo_degree[2] - INC);
        break;
        
        case 6: //incremenet indice
        if (servo_degree[3] < MAX_DEGREE) servo_motors[3].write(servo_degree[3] + INC);
        break;
        
        case 7: //decrement indice
        if (servo_degree[3] < MAX_DEGREE) servo_motors[3].write(servo_degree[3] - INC);
        break;

        case 8: //increment pollice
        if (servo_degree[4] < MAX_DEGREE) servo_motors[4].write(servo_degree[4] + INC);
        break;
        
        case 9: //decrement pollice
        if (servo_degree[4] < MAX_DEGREE) servo_motors[4].write(servo_degree[4] - INC);
        break;
        default:
        break;
      }
    }
  }
}
