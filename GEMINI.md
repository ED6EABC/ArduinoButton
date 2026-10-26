# Project Instructions: ArduinoButton

## Project Overview
This project is an Arduino sketch workspace intended for button interaction experiments and embedded development.

- **Primary Language / Environment:** C++ / Arduino (`.ino`)
- **Key Files & Structure:**
  - `Button/Button.ino`: Main Arduino sketch containing initialization (`setup()`) and loop execution (`loop()`) logic.

## Building and Running

### Using Arduino IDE
1. Open Arduino IDE.
2. Open `Button/Button.ino`.
3. Select your connected Arduino board and port from the **Tools** menu.
4. Click **Verify** (Compile) or **Upload** to flash the code to your Arduino board.

### Using Arduino CLI (Optional / Headless)
If `arduino-cli` is installed:
- **Compile:**
  ```bash
  arduino-cli compile --fqbn arduino:avr:uno Button
  ```
- **Upload:**
  ```bash
  arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno Button
  ```

## Development Conventions
- **Arduino Standard Structure:** Keep hardware initialization, pin configuration (`pinMode`), and serial setups in `setup()`.
- **Loop Routine:** Keep polling routines, debounce handling, and state machine updates responsive within `loop()`. Avoid excessive blocking delays (`delay()`) when handling button events; prefer non-blocking timing via `millis()` or interrupt routines where applicable.
- **Naming & Formatting:** Follow standard Arduino C++ conventions (CamelCase for functions/variables, descriptive constant names for GPIO pin assignments).
