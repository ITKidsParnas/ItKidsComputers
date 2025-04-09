import time
import tkinter as tk

def click():
   global clicks, start_time
   clicks +=10
   label.config(text=f"кликов: {clicks}")
  # if time.time() - start_time >= 30:
      # label.config(text=f"время вышло Кликов: {clicks}")
clicks=0
start_time=time.time()

root = tk.Tk()
root.title("кликер")
button = tk.Button(root, text = "жми меня",command=click)
label = tk.Label(root, text="жми 100 раз быстро!!!",font=("Helvetica", 24))
label.pack(pady=20)
button.pack(pady=20)

root.mainloop()
