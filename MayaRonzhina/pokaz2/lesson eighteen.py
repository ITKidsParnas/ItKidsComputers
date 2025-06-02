import time
import tkinter as tk

def kalmar_N230():
    current_time = time.strftime('%H:%M:%S')
    label.config(text = current_time)
    root.after(1000, kalmar_N230)
root = tk.Tk()
root.title("часы")

label = tk.Label(root, font=("Centry Gothic", 200), fg="red", bg="green")
label.pack(pady=10, padx=10)
kalmar_N230()
root.mainloop()