import subprocess

def check_bluetooth_status():
    try:
        # Run the command to list Bluetooth status
        result = subprocess.run(['bluetoothctl', 'show'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print("Error: Could not run bluetoothctl. Make sure Bluetooth is installed.")
            return

        # Parse the output to check if Bluetooth is powered on
        output = result.stdout
        if "Powered: yes" in output:
            return ("Bluetooth is ON")
        else:
            return ("Bluetooth is OFF")

    except FileNotFoundError:
        print("Error: bluetoothctl is not installed or not found on this system.")


