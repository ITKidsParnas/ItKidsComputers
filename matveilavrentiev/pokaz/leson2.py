import time
import tkinter as tk

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000,update_clock)
    
root = tk. Tk()
root.title("Часы")

label = tk.Label(root, font=("Segoe Script", 50), fg="red",bg="black")
label.pack(pady=10, padx=10)
update_clock()
root.mainloop()