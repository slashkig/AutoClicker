import pyautogui, time
from pynput import keyboard

auto = True

def main():
    global auto
    time.sleep(10)
    while auto:
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        time.sleep(0.1)

def on_press(key):
    global auto
    if key == keyboard.Key.esc:
        auto = False
        return False

if __name__ == "__main__":
    print("Running autoclicker")
    listener = keyboard.Listener(on_press = on_press)
    listener.start()
    main()
    listener.join()
    print("Stopping autoclicker\n")