/*
  Title: Serial Monitor Hello World Loop
  Description: Prints "Hello, World!" to the serial monitor every 2 seconds.
  Used components: Arduino MEGA COM4
  Author: Justin L., Mykhailo I.
  Date: 19.02.2025
  License: CC BY-NC-SA 4.0
*/

void setup() {}

void loop() {
  Serial.begin(9600);
  Serial.println("Hello, World!");
  delay(2000);
}
