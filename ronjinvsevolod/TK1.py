import time
import tkinter as tk
def drift_street():
    current_time=time.strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000,drift_street)
root=tk.Tk()
root.title("Часы")
label=tk.Label(root,font=("Impact",120),fg="blue", bg="black")
label.pack(pady=10,padx=10)
drift_street()
root.mainloop()