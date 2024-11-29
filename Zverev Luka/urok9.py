import webbrowser
import pyautogui
import time

site = "https://www.ravbug.com/bsod/bsod10/"

webbrowser.open(site)
time.sleep(1)
pyautogui.press('F11')
