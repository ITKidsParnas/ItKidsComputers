import pyautogui   
import time
import random

while True:
    x = random.randint(0, pyautogui.size().width)
    y = random.randint(0, pyautogui.size().height)
    pyautogui.moveTo(x,y, duration=0.5)
    time.sleep(1)