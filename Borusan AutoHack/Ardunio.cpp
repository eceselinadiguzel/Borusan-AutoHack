int buzzerPin = 9; // Buzzer'ın bağlı olduğu pin

String incomingData;
float latitude, longitude, acceleration_x, acceleration_y, acceleration_z;

void setup() {
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT); // Buzzer pinini OUTPUT olarak ayarla
}

void loop() {
  if (Serial.available() > 0) {
    incomingData = Serial.readStringUntil('\n');
    parseData();
    if (isSharpManeuver()) {
      Serial.println("Sharp maneuver detected!");
      Serial.print("Location: Lat ");
      Serial.print(latitude, 6);
      Serial.print(" Long ");
      Serial.println(longitude, 6);
    }

    if (incomingData == "ALERT") {
      soundAlarm();
    }
  }
}

void parseData() {
  int firstCommaIndex = incomingData.indexOf(',');
  int secondCommaIndex = incomingData.indexOf(',', firstCommaIndex + 1);
  int thirdCommaIndex = incomingData.indexOf(',', secondCommaIndex + 1);
  int fourthCommaIndex = incomingData.indexOf(',', thirdCommaIndex + 1);

  latitude = incomingData.substring(0, firstCommaIndex).toFloat();
  longitude = incomingData.substring(firstCommaIndex + 1, secondCommaIndex).toFloat();
  acceleration_x = incomingData.substring(secondCommaIndex + 1, thirdCommaIndex).toFloat();
  acceleration_y = incomingData.substring(thirdCommaIndex + 1, fourthCommaIndex).toFloat();
  acceleration_z = incomingData.substring(fourthCommaIndex + 1).toFloat();
}

bool isSharpManeuver() {
  // Makas atma hareketini tespit etmek için ivme verilerini kullan
  return (abs(acceleration_x) > 4.0 || abs(acceleration_y) > 4.0);
}

void soundAlarm() {
  // Sesli uyarı için basit bir alarm sesi
  for (int i = 0; i < 3; i++) {
    digitalWrite(buzzerPin, HIGH);
    delay(500);
    digitalWrite(buzzerPin, LOW);
    delay(500);
  }
}
