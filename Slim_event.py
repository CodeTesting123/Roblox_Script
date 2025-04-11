
import pyautogui
import time

def press_keys(keys, duration):
    for key in keys:
        pyautogui.keyDown(key)
    time.sleep(duration)
    for key in keys:
        pyautogui.keyUp(key)
        
# Helper for single key press
def press_key(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

print("Starting in 5 seconds... Switch to your Roblox window!")
time.sleep(5)

cycle = 1
while True:
    print(f"\n--- Cycle {cycle} ---")

    print("Moving to BLUE chest...")
    press_keys(['w', 'a'], 2.5)
    pyautogui.press('e')

    print("Returning from BLUE chest...")
    press_keys(['s', 'd'], 2)

    print("Moving to PURPLE chest...")
    press_keys(['w', 'd'], 2.5)
    pyautogui.press('e')

    print("Returning from PURPLE chest...")
    press_keys(['a', 's'], 2)
    
    print("Small movement: Step back and forward...")
    press_key('s', 2)
    press_key('w', 2)

    print("Cycle complete. Waiting 1:59 before starting next cycle...")
    time.sleep(119)

    cycle += 1
