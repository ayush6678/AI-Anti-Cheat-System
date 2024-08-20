import subprocess
import sys
import re

def get_device_names():
    devices = {
        "USB": [],
        "HDMI": [],
    }

    if sys.platform.startswith('win'):
        # Windows
        try:
            # USB devices
            output = subprocess.check_output(['powershell', "Get-PnpDevice -Class USB -FriendlyName '*' | Select-Object FriendlyName"], universal_newlines=True)
            devices['USB'] = [line.strip() for line in output.split('\n') if line.strip() and not line.startswith('FriendlyName')]

            # HDMI devices
            output = subprocess.check_output(['powershell', "Get-PnpDevice -Class Display -FriendlyName '*' | Select-Object FriendlyName"], universal_newlines=True)
            devices['HDMI'] = [line.strip() for line in output.split('\n') if line.strip() and not line.startswith('FriendlyName')]

        except subprocess.CalledProcessError:
            print("Error executing PowerShell commands")

    elif sys.platform.startswith('linux'):
        # Linux
        try:
            # USB devices
            output = subprocess.check_output(['lsusb'], universal_newlines=True)
            devices['USB'] = [re.split(r'\d+:', line, maxsplit=1)[-1].strip() for line in output.split('\n') if line.strip()]

            # HDMI devices (this might not work on all systems)
            output = subprocess.check_output(['xrandr'], universal_newlines=True)
            devices['HDMI'] = [line.split()[0] for line in output.split('\n') if ' connected ' in line]

            
        except subprocess.CalledProcessError:
            print("Error executing shell commands")

    elif sys.platform.startswith('darwin'):
        # macOS
        try:
            # USB devices
            output = subprocess.check_output(['system_profiler', 'SPUSBDataType'], universal_newlines=True)
            devices['USB'] = [line.split(':')[-1].strip() for line in output.split('\n') if line.strip().startswith('Product:')]

            # HDMI devices (this might not work on all systems)
            output = subprocess.check_output(['system_profiler', 'SPDisplaysDataType'], universal_newlines=True)
            devices['HDMI'] = [line.split(':')[-1].strip() for line in output.split('\n') if 'Display Type' in line]


        except subprocess.CalledProcessError:
            print("Error executing shell commands")

    else:
        print("Unsupported operating system")

    return devices


