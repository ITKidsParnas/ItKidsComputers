import time
import random
import pyautogui

while True:
    x = random.randint(0, pyautogui.size().width)
    y = random.randint(0, pyautogui.size().height)
    pyautogui.moveTo(x, y, 0.5)
    time.sleep(0.5)
    