import win32gui
import win32con
import win32api
import time
import os 
from time import sleep

listcoords=()

def find_window_by_title(title):
    hwnd = win32gui.FindWindow(None,title)
    if hwnd == 0:
        raise Exception(f"Окно с название {title} не найдено")
    return hwnd

def click_in_window(hwnd, x, y):
    rect = win32gui. GetWindowRect(hwnd)
    screen_x = rect[0]+x
    screen_y = rect[1]+y

    win32api. SetCursorPos((screen_x, screen_y))

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, screen_x, screen_y, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, screen_x, screen_y, 0, 0)
    sleep(0.05)

hwnd = find_window_by_title("Lively Wallpaper")
cur = 1

path ="log.txt"
try:
    with open(path,"x")as file:
        file.write("1")
except FileExistsError:
    print("файл существует")
while True:
    with open(path, "1") as file:
            cur = file.read()
    if time.localtime().tm_hour == 0 and time. localtime().tm_min == 0 and time.localtime().tm_sec == 0: 
        click_in_window(hwnd, 170, 175)
        with open(path, "wr") as file:
            cur += 1
            if file.read() == "10":
                file.write("1")



