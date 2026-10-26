/**
 * @file Button.ino
 * @brief Detects button presses on pin 2 and sends a signal via Serial.
 * 
 * Circuit:
 * - Button connected between digital pin 2 and GND.
 * - Internal pull-up resistor is used (pin 2 is HIGH when open, LOW when pressed).
 */

// --- Constants ---
const uint8_t BUTTON_PIN = 2;           // Pin connected to the button
const unsigned long DEBOUNCE_DELAY = 50; // Debounce time in milliseconds

// --- State Variables ---
int lastSteadyState = HIGH;       // The previous steady state from the input pin
int lastFlickerableState = HIGH;  // The previous flickerable state from the input pin
unsigned long lastDebounceTime = 0;  // The last time the output pin was toggled

void setup() {
  // Initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
  // Configure the button pin with internal pull-up resistor:
  // This avoids the need for an external resistor.
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  
  // Optional: Send a boot message to confirm serial is working
  // Serial.println("Arduino Ready. Waiting for button press...");
}

void loop() {
  // Read the state of the button:
  int currentState = digitalRead(BUTTON_PIN);

  // Check if the button state has changed (due to noise or pressing)
  if (currentState != lastFlickerableState) {
    // Reset the debouncing timer
    lastDebounceTime = millis();
    // Save the flickerable state
    lastFlickerableState = currentState;
  }

  // If the state has been stable for longer than the debounce delay,
  // it's a valid change
  if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
    
    // If the button state has changed to a steady state
    if (lastSteadyState == HIGH && currentState == LOW) {
      // Transition from HIGH (idle) to LOW (pressed) detected:
      Serial.println("BUTTON_PRESSED");
    }
    
    // Save the steady state
    lastSteadyState = currentState;
  }
}
