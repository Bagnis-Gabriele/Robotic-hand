String msg; //message sent from leap motion sensor

void setup() {
  Serial.begin(9600);
}

void loop(){
  //if there is data avaible read it
  if(Serial.available()){
    msg = Serial.readString();
    Serial.print(msg);
  }
}
