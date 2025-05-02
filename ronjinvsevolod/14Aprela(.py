import tkinter as tk
import random
import time
def flash_window(duration):
    end_time=time.time()+duration
    while time.time()<end_time:
        color=random.choice(["White","blue"])
        root.configure(background=color)
        root.update()
        time.sleep(0.1)

if __name__=="__main__":
    root=tk.Tk()
    root.attributes("-fullscreen",True)
    root.update()
    flash_window(21)
    root.destroy()

