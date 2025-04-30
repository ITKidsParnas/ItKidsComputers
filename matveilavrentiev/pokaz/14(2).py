import tkinter as tk
import random
import time

def flash_window(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        color = random.choice(["red", "blue", "black"])
        root.configure(background=color)
        root.update()
        time.sleep(0.0)

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    flash_window(10)
    root.destroy()