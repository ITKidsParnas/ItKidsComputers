"""
Это игра, где надо кликать по кнопке за отведенное время, кнопка будет убегать
Писать можно прям по порядку и не париться, все норм!
Везде где тексты, пусть редактирую как хотят, ниче страшного, они и сами так делают уже
Все что в тройных кавычках и после хештега - это комментарии для тебя
"""


import tkinter as tk # импортируем библиотеку для работы с приложениями
from tkinter import messagebox # функционал для диалогового окна, типа сообщение и ОК
import random # ну тут понятно

#само приложение
class ClickGame:
    def __init__(self, root):
        self.root = root # создаем главное окно, оно определяется в самом конце как tk.Tk()
        self.root.title("Кликер игра") # название
        self.root.geometry("600x400")  # размеры окна, если что можно менять но тогда нужно будет поменять метод move_button, чтобы по всему приложению скакала кнопка
        
        # переменные счета и времени
        self.score = 0
        self.time_left = 60 # 60 сек таймер, можно по желанию менять
        
        # надписи для счета и таймера
        self.score_label = tk.Label(root, text=f"Счёт: {self.score}", font=("Arial", 16)) # в конце можно будет менять шрифт по желанию и размер. arial соответственно название шрифта, 16 - кегль
        self.score_label.pack()

        self.timer_label = tk.Label(root, text=f"Время: {self.time_left}", font=("Arial", 16))
        self.timer_label.pack()

        # кнопка
        self.button = tk.Button(root, text="Клик!", width=10, height=2, bg="lightblue", command=self.on_click) # bg можно менять на любой цвет теоретически, т.е "black", "pink" и тд, вроде можно и хекс значения, можно чтобы поигрались, когда закончат
        self.button.place(x=250, y=150) # изначальная позиция кнопки

        # каждый раз в лупе апдейтим таймер, эту функцию пропишем дальше
        self.update_timer()


    # методы (фунции внутри класса)
    def on_click(self):
        """увеличиваем счет +меняем текст надписи сверху и перемещаем кнопку по клику"""
        self.score += 1
        self.score_label.config(text=f"Счёт: {self.score}")
        self.move_button() #эту функцию прописываем дальше

    def move_button(self):
        """перемещаем кнопку на случайное место"""
        x = random.randint(0, 540)  # 600 минус ширина кнопки (60)
        y = random.randint(50, 340)  # 400 минус высота кнопки (60) - место для счетчика
        self.button.place(x=x, y=y)

    def update_timer(self):
        """обновляем таймер каждую секунду"""
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Время: {self.time_left}")
            self.root.after(1000, self.update_timer) # через секунду после запуска приложения включается таймер и каждую секу обновляется рекурсивно
        else:
            self.end_game() # если время не больше нуля = конец игры

    def end_game(self):
        """Завершение игры"""
        self.button.config(state="disabled") # делаем кнопку неактивной
        self.timer_label.config(text="Время вышло!") # меняем надпись
        messagebox.showinfo("Конец игры", f"Ваш счёт: {self.score}") # диалоговое окно с конечным счетом

# то что запускает нашу программу, тут и определяем окно и класс игры
if __name__ == "__main__":
    root = tk.Tk()
    game = ClickGame(root)
    root.mainloop()
