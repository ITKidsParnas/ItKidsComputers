import pyautogui
import random
import time
while True:
    X=random.randint(0,pyautogui.size().width)
    y=random.randint(0,pyautogui.size().height)
    pyautogui.moveTo(X,y,duration=0.)
    time.sleep(1)