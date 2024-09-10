import pyautogui, time

def main():
    time.sleep(10)
    while True:
        try:
            x, y = pyautogui.position()
            pyautogui.click(x, y)
            time.sleep(0.1)
        except KeyboardInterrupt:
            return

if __name__ == "__main__":
    main()