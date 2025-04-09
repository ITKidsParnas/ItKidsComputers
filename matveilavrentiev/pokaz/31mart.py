import tkinter as tk
from tkinter import messagebox
import random

class ClickGame:
    def __init__(self,root):
       self.root = root
       self.root.title("тренеровка реакции")
       self.root.geometry("600x400")

       self.score = 0
       self.time_left = 60

       self.score_label = tk.Label(root, text=f"score: {self.score}", font=("Arial", 16))
       self.score_label.pack()

       self.timer_label = tk.Button(root, text=f"time: {self.time_left}", font=("Arial", 16))
       self.timer_label.pack()

       self.butom = tk.Button(root, text="tab", width=10,height=2, bg="lightblue", command=self.on_click)
       self.butom.place(x=250, y=250)

       self.apdaet_timer()
    
    def on_click(self):
        self.score += 1
        self.score_label.config(text=f"ваш счет: {self.score}")
        self.move_button()

    def move_button(self):
        x = random.randint(0, 540)
        y = random.ranbint(0,540)
        self.button.place(x = x, y = y)