String msg; //message sent from leap motion sensor

int numeri[5];

int k;
int pos;

void setup() {
  Serial.begin(9600);
}

void loop(){
  //if there is data avaible read it
  if(Serial.available()){
    msg = Serial.readString();
    Serial.print(msg);
    for (k=0;k<5;k++){
      numeri[k]=0;
    }
    for (k=0; k<15; k++){
      switch (k){
        case 0: case 1: case 2: pos=0; break;
        case 3: case 4: case 5: pos=1; break;
        case 6: case 7: case 8: pos=2; break;
        case 9: case 10: case 11: pos=3; break;
        case 12: case 13: case 14: pos=4; break;
      }
      numeri[pos]+=(((int)msg.charAt(k))-48)*(pow(10,(2-(k%3))));
    }
    for (k=0;k<5;k++){
      if(numeri[k]<100){
        if(numeri[k]<10){
          Serial.print("00");
        }else{
          Serial.print("0");
        }
      }
      Serial.print(numeri[k]);
    }
  }
}
