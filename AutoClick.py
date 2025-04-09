import pyautogui
import time
from pynput import keyboard

clicking = True

def on_press(key):
    global clicking
    try:
        if key.char == 'q':
            clicking = False
            return False  # Stop the listener
    except AttributeError:
        pass

print("Auto clicker will start in 5 seconds... Press 'q' to stop.")
time.sleep(5)

# Start keyboard listener in the background
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Clicking started...")
while clicking:
    pyautogui.click()
    time.sleep(0.01)

print("Clicking stopped.")
