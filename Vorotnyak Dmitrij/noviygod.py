import tkinter as tk
import random
from datetime import datetime

def update_countdown():
    tracking_date = datetime(datetime.now().year + 1, 1, 1)
    time_remaning = tracking_date - datetime.now()
    days = time_remaning.days
    hours = time_remaning.seconds // 3600
    minutes = (time_remaning.seconds // 60) % 60
    seconds = time_remaning.seconds % 60

    countdown_label.config(text = f"{days} Дней, {hours} Часоы, {minutes} МИнут, {seconds} секкунд")

    window.after(1000, update_countdown)



window = tk.Tk()
window.title("timer")
window.attributes("-fullscreen", True)

window.config(bg="darkred")

text_label = tk.Label(window, text = "До Нового года jcnfkjcm:", font =("Helvetica", 48), fg = "red", bg = "purple")
countdown_label = tk.Label(window, font=("Helvetica", 48), fg = "blue", bg = "cyan")

text_label.place(relx = 0.5, rely = 0.45, anchor="center")
countdown_label.place(relx = 0.5, rely = 0.55, anchor="center")
update_countdown()
window.mainloop()

