void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT); // GPIO2 (LED or Relay)
  Serial.println("ESP32 Ready. Waiting for serial input...");
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();

    if (cmd == '1') {
      digitalWrite(2, HIGH); // Turn ON
      Serial.println("Action: Light ON");
    }
    else if (cmd == '2') {
      digitalWrite(2, LOW);  // Turn OFF
      Serial.println("Action: Light OFF");
    }
  }
}
