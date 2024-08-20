import subprocess
import re

def get_chrome_windows():
    try:
        # Get all window IDs for Chrome
        output = subprocess.check_output(["xdotool", "search", "--name", "Google Chrome"]).decode().strip()
        return output.split("\n") if output else []
    except subprocess.CalledProcessError:
        print("Error: xdotool not found or unable to search for windows.")
        return []

def get_window_name(window_id):
    try:
        return subprocess.check_output(["xdotool", "getwindowname", window_id]).decode().strip()
    except subprocess.CalledProcessError:
        return ""

def count_chrome_tabs():
    chrome_windows = get_chrome_windows()
    total_tabs = 0

    for window_id in chrome_windows:
        window_name = get_window_name(window_id)
        match = re.search(r'(\d+) tabs? - Google Chrome', window_name)
        if match:
            total_tabs += int(match.group(1))
        elif "Google Chrome" in window_name:
            # If no tab count in title, assume it's 1 tab
            total_tabs += 1

    return (f"Number of open windows in Google Chrome: {total_tabs}")

