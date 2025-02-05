import tkinter as tk
import random
from datetime import datetime

def update_countdown():
    tracking_date = datetime(datetime.now().year + 1, 1, 1)
    time_remaining = tracking_date - datetime.now()
    days = time_remaining.days
    hours = time_remaining.seconds // 3600
    minutes = (time_remaining.seconds // 60) % 60
    seconds = time_remaining.seconds % 60

    countdown_lable.config(text = f"{days} Дней, {hours} Часов, {minutes} Минут, {seconds} Секунд")

    window.after(1000, update_countdown)


window = tk.Tk()
window.title("timer")
window.attributes("-fullscreen", True)
window.config(bg="black")

text_lable = tk.Label(window, text = "До Нового Года =)", font = ("Helvetica", 52),fg = "white", bg = "black")

countdown_lable = tk.Label(window, font=("Helvetica", 52),fg = "white", bg = "black")

text_lable.place(relx = 0.5, rely = 0.45, anchor="center")
countdown_lable.place(relx=0.5,rely=0.55, anchor="center")
update_countdown()
window.mainloop()
