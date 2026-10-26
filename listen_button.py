import serial
import time

# --- Configuration ---
# Change '/dev/ttyACM0' to your Arduino's port (e.g., 'COM3' on Windows)
SERIAL_PORT = '/dev/ttyACM0' 
BAUD_RATE = 9600

def main():
    try:
        # Initialize Serial Connection
        print(f"Connecting to {SERIAL_PORT}...")
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for Arduino to reset/initialize
        print("Connected! Waiting for button presses...")

        while True:
            if ser.in_waiting > 0:
                # Read line from serial, decode and strip whitespace
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                
                if line == "BUTTON_PRESSED":
                    print(f"[{time.strftime('%H:%M:%S')}] Button pressed detected!")
                    # Add your custom logic here (e.g., trigger an action)
            
            time.sleep(0.01) # Small sleep to reduce CPU usage

    except serial.SerialException as e:
        print(f"Error: Could not open serial port {SERIAL_PORT}. {e}")
    except KeyboardInterrupt:
        print("\nExiting script...")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

if __name__ == "__main__":
    main()
