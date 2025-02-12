import time
import tkinter as tk

def click():
    global clicks,start_time
    clicks +=1
    label.config(text=f"Твои клики:{clicks}")

    if time.time()-start_time>=60:
        label.config(text=f"Время вышло.Твои клики:{clicks}")

clicks=0
start_time=time.time()







root=tk.Tk()
root.title("Игра-кликер")
label=tk.Label(root,text="хреначь по мышке",font=("Impact",24))
label.pack(pady=20)

button=tk.Button(root,text="Кликать",height=70,width=100,command=click)
button.pack(pady=20)
root.mainloop()