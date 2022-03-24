const int  sensorPin1 = 2;
const int  sensorPin2 = 3;
const int  sensorPin3 = 4;
const int  sensorPin4 = 5;
const int  sensorPin5 = 12;
const int  relayPin1 = 11;
const int  relayPin2 = 10;
const int  relayPin3 = 9;
const int  relayPin4 = 8;

int sensorState1 = 0;
int sensorState2 = 0;
int sensorState3 = 0;
int sensorState4 = 0;
int sensorState5 = 0;
int lastsensorState1 = 0;
int lastsensorState2 = 0;
int lastsensorState3 = 0;
int lastsensorState4 = 0;

void setup() {
  pinMode(sensorPin1, INPUT);
  pinMode(sensorPin2, INPUT);
  pinMode(sensorPin3, INPUT);
  pinMode(sensorPin4, INPUT);
  pinMode(sensorPin5, INPUT);
  pinMode(relayPin1, OUTPUT);
  pinMode(relayPin2, OUTPUT);
  pinMode(relayPin3, OUTPUT);
  pinMode(relayPin4, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  sensorState1 = digitalRead(sensorPin1);
  sensorState2 = digitalRead(sensorPin2);
  sensorState3 = digitalRead(sensorPin3);
  sensorState4 = digitalRead(sensorPin4);
  sensorState5 = digitalRead(sensorPin5);

  if (sensorState1 != lastsensorState1) {
    if (sensorState1 == LOW) {
      Serial.println("count1");
    }
    delay(50);
  }
  lastsensorState1 = sensorState1;

  
  if (sensorState2 != lastsensorState2) {
    if (sensorState2 == LOW) {
      Serial.println("count2");
    }
    delay(50);
  }
  lastsensorState2 = sensorState2;

  
  if (sensorState3 != lastsensorState3) {
    if (sensorState3 == LOW) {
      Serial.println("count3");
    }
    delay(50);
  }
  lastsensorState3 = sensorState3;

  
  if (sensorState4 != lastsensorState4) {
    if (sensorState4 == LOW) {
      Serial.println("count4");
    }
    delay(50);
  }
  lastsensorState4 = sensorState4;

  if (sensorState5 == LOW) {
    // turn LED on:
    digitalWrite(relayPin1, HIGH);
    digitalWrite(relayPin2, HIGH);
    digitalWrite(relayPin3, HIGH);
    digitalWrite(relayPin4, HIGH);
  } else if(sensorState5 == HIGH){
    // turn LED off:
    digitalWrite(relayPin1, LOW);
    digitalWrite(relayPin2, LOW);
    digitalWrite(relayPin3, LOW);
    digitalWrite(relayPin4, LOW);
  }
}
