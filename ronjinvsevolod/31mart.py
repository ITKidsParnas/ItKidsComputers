import tkinter as tk
from tkinter import messagebox
import random

class ClickGame:
    def __init__(self, root):
        self.root=root
        self.root.title("Таба-плейс")
        self.root.geometry("600x400")

        self.score=0
        self.time_left=1000000000

        self.score_label=tk.Label(root, text=f"Ваш счёт: {self.score}", font=("Arial", 16))
        self.score_label.pack()

        self.timer_label=tk.Label(root, text=f"Осталось: {self.time_left}",font=("Arial", 16))
        self.timer_label.pack()

        self.button = tk.Button(root, text="Тап!", width=200, height=180, bg="red", command=self.on_click)
        self.button.place(x=250, y=150)
        
        self.update_timer()

    def on_click(self):
        self.score += 1
        self.score_label.config(text=f"Ваш счёт: {self.score}")
        self.move_button()

    def move_button(self):
        x =random.randint(0, 540)
        y =random.randint(0, 340)
        self.button.place(x=x, y=y)

    def update_timer(self):
        if self.time_left>0:
            self.time_left-=1
            self.timer_label.config(text=f'Время:{self.time_left}')
            self.root.after(1000,self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.button.config(state="disabled")
        self.timer_label.config(text="Время вышло")
        messagebox.showinfo("Конец игры",f'ВАШ СЧЁТ:{self.score}')

if __name__=="__main__":
    root=tk.Tk()
    game=ClickGame(root)
    root.mainloop()