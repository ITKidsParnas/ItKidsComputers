import tkinter as tk
import random
from datetime import datetime

def update_countdown():
    tracking_date = datetime(datetime.now().year + 1, 1, 1 )
    time_remainting = tracking_date - datetime.now()
    days = time_remainting.days
    hours = time_remainting.seconds // 3600
    minutes = (time_remainting.seconds // 60) % 60
    seconds = time_remainting.seconds % 60

    count_label.config(text = f"{days} Дней, {hours} Часов, {minutes} Минут, {seconds} Секунд")

    window.after(1000, update_countdown)


window = tk.Tk()
window.title("timer")
window.attributes("-fullscreen", True)

window.config(bg="black")

text_label = tk.Label(window, text = "До Нового Года осталось", font =("Helvetica", 48), fg = "yellow", bg = "black")
count_label = tk.Label(window, font =("Helvetica, 48"),fg = "white", bg = "black")


text_label.place(relx = 0.5, rely  = 0.45, anchor="center")
update_countdown()
count_label.place(relx=0.5, rely=0.55, anchor="center")

window.mainloop()
