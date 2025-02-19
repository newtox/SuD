/*
  Title: Number Multiplier
  Description: Multiplies the entered number by 2
  Used components: Arduino MEGA COM4
  Author: Justin L., Mykhailo I.
  Date: 19.02.2025
  License: CC BY-NC-SA 4.0
*/

void setup() {
  Serial.begin(9600);

  while (!Serial) {
    continue;
  }

  Serial.println();
  Serial.println("Please enter a number you want to multiply by 2.");
}

void loop() {
  if (Serial.available() > 0) {
    int input = Serial.parseInt();
    Serial.readString();

    int multiplied = input * 2;

    Serial.println(multiplied);


    Serial.println();
    Serial.println("Please enter a number you want to multiply by 2.");
  }
}
