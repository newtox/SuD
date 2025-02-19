/*
  Title: Joystick Direction
  Description: Control 4 different LEDs based on the joystick direction.
  Used components: Arduino MEGA COM4, 4 LEDs, 1 Joystick, 4 10k Ohm resistor, ~5mf jumpers, ~10mm jumpers, 1 breadboard
  Authors: Justin L., Mykhailo I.
  Date: 19.02.2025
  License: CC BY-NC-SA 4.0
*/

const int VRX_PIN = A0;
const int VRY_PIN = A1;
const int SW_PIN = 2;

const int LED_UP = 12;
const int LED_RIGHT = 10;
const int LED_DOWN = 11;
const int LED_LEFT = 9;

int xValue;
int yValue;
int centerX = 507;
int threshold = 200;

void setup() {
  pinMode(LED_UP, OUTPUT);
  pinMode(LED_RIGHT, OUTPUT);
  pinMode(LED_DOWN, OUTPUT);
  pinMode(LED_LEFT, OUTPUT);
  pinMode(SW_PIN, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  xValue = analogRead(VRX_PIN);
  yValue = analogRead(VRY_PIN);
  
  Serial.print("X: ");
  Serial.print(xValue);
  Serial.print(" | Y: ");
  Serial.println(yValue);
  
  allLedsOff();
  
  if (xValue < centerX - threshold) {
    digitalWrite(LED_LEFT, HIGH);
  }
  else if (xValue > centerX + threshold) {
    digitalWrite(LED_RIGHT, HIGH);
  }
  
  if (yValue < centerX - threshold) {
    digitalWrite(LED_UP, HIGH);
  }
  else if (yValue > centerX + threshold) {
    digitalWrite(LED_DOWN, HIGH);
  }
  
  delay(50);
}

void allLedsOff() {
  digitalWrite(LED_UP, LOW);
  digitalWrite(LED_RIGHT, LOW);
  digitalWrite(LED_DOWN, LOW);
  digitalWrite(LED_LEFT, LOW);
}
