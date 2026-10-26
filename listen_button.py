import serial
import serial.tools.list_ports
import time
import sys

# --- Configuration ---
BAUD_RATE = 9600

def list_serial_ports():
    """Lists all available serial ports and returns them."""
    ports = serial.tools.list_ports.comports()
    return sorted(ports)

def select_port():
    """Prompts the user to select a serial port from the available list."""
    print("--- Available Serial Ports ---")
    ports = list_serial_ports()
    
    if not ports:
        print("No serial ports detected. Please connect your Arduino.")
        sys.exit(1)
        
    for i, port in enumerate(ports):
        print(f"[{i}] {port.device} - {port.description}")
        
    while True:
        try:
            selection = input(f"\nSelect a port index (0-{len(ports)-1}): ")
            index = int(selection)
            if 0 <= index < len(ports):
                return ports[index].device
            else:
                print(f"Error: Please enter a number between 0 and {len(ports)-1}.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

def main():
    # 1. Interactive port selection
    selected_device = select_port()
    
    try:
        # 2. Initialize Serial Connection
        print(f"\nConnecting to {selected_device} at {BAUD_RATE} baud...")
        ser = serial.Serial(selected_device, BAUD_RATE, timeout=1)
        
        # Wait for Arduino to reset (common on Nano/Uno when opening serial)
        time.sleep(2) 
        print("Connected! Waiting for button presses (Ctrl+C to stop)...")

        while True:
            if ser.in_waiting > 0:
                # Read line from serial, decode and strip whitespace
                try:
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if line == "BUTTON_PRESSED":
                        print(f"[{time.strftime('%H:%M:%S')}] Button pressed detected!")
                except Exception as e:
                    print(f"Read Error: {e}")
            
            time.sleep(0.01) # Small sleep to reduce CPU usage

    except serial.SerialException as e:
        print(f"\nError: Could not open serial port {selected_device}.")
        print(f"Details: {e}")
        print("\nTIP: Make sure the Serial Monitor in Arduino IDE is CLOSED.")
    except KeyboardInterrupt:
        print("\nExiting script...")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

if __name__ == "__main__":
    main()
