bool status = false;
int counter = 0; // this counter is used to check how much alert is already provided

// pins declaration 
const int LED_PIN = 13;
const int BUZZER_PIN = 9;

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    Serial.println(Serial.readString());
    status = !status;
  }
  if (status) {
    playAlert();
    counter ++;
    Serial.println(counter);
  } else {
    counter = 0;
  }
}

void playAlert() {
  digitalWrite(LED_PIN, HIGH);
  if (counter >= 5) {
    digitalWrite(BUZZER_PIN, HIGH);
  }
  delay(500);
  digitalWrite(LED_PIN, LOW);
  digitalWrite(BUZZER_PIN, LOW);
  delay(200);
}
