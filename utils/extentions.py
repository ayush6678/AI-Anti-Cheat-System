import os
import json
import platform

def get_chrome_extensions():
    # Determine the Chrome user data directory based on the operating system
    if platform.system() == "Windows":
        path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Extensions")
    elif platform.system() == "Darwin":  # macOS
        path = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/Extensions")
    elif platform.system() == "Linux":
        path = os.path.expanduser("~/.config/google-chrome/Default/Extensions")
    else:
        return "Unsupported operating system"

    extensions = []

    # Check if the directory exists
    if not os.path.isdir(path):
        return "Chrome user data directory not found"

    # Iterate through the extensions
    for ext_id in os.listdir(path):
        ext_path = os.path.join(path, ext_id)
        if os.path.isdir(ext_path):
            # Find the newest version directory
            versions = os.listdir(ext_path)
            if versions:
                newest_version = max(versions)
                manifest_path = os.path.join(ext_path, newest_version, "manifest.json")
                if os.path.exists(manifest_path):
                    with open(manifest_path, "r", encoding="utf-8") as f:
                        manifest = json.load(f)
                        extensions.append({
                            "name": manifest.get("name", "Unknown"),
                        })

    return extensions
