import time
import tkinter as tk

def click():
    global clicks, smart_time
    clicks +=1
    label.config(text=f"Clicks: {clicks}")
 #   if time.time() - smart_time >= 10:
    #    label.config(text=f"Время вышло! Кликов: {clicks}")

clicks=0
smart_time=time.time()


root = tk.Tk()
root.title("Clicker-game")

label = tk.Label(root, text ="Clicker", font=("Helvetica", 200))
label.pack(pady=20)
button = tk.Button(root, text = "Жми или проиграй!", command=click )
button.pack(pady=20)

root.mainloop()