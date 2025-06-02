import tkinter as tk
import random
import time
def flash_window(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        color = random.choice(["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "white"])
        root.configure(background=color)
        root.update()
        time.sleep(00.0)


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.update()
    flash_window(5)
    root.destroy()