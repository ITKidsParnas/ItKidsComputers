import tkinter as tk
from tkinter import messagebox
import random

class Hangman:
    def __init__(self, master):
        self.master = master
        self.master.title("Виселица")
        
        self.word_list = ["крокодил", "Гусь", "Мороженое", "Скороговорка", "Капучино", "слово"]
        self.secret_word = random.choice(self.word_list)
        self.guessed_letters = []
        self.max_attempts = 6
        self.attempts = 0
        
        self.label_word = tk.Label(master, text=self.get_display_word(), font=("Arial", 24))
        self.label_word.pack(pady=20)
        
        self.entry_letter = tk.Entry(master, font=("Arial", 24))
        self.entry_letter.pack(pady=20)
        
        self.button_guess = tk.Button(master, text="Угадать", command=self.guess_letter, font=("Arial", 16))
        self.button_guess.pack(pady=20)

        self.label_attempts = tk.Label(master, text=f"Ошибки: {self.attempts}/{self.max_attempts}", font=("Arial", 16))
        self.label_attempts.pack(pady=20)

        self.canvas = tk.Canvas(master, width=200, height=200, bg="white")
        self.canvas.pack(pady=20)

        self.draw_hangman()

    def get_display_word(self):
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        return display_word.strip()

    def guess_letter(self):
        letter = self.entry_letter.get().lower()
        self.entry_letter.delete(0, tk.END)

        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Ошибка", "Введите одну букву.")
            return

        if letter in self.guessed_letters:
            messagebox.showwarning("Ошибка", "Вы уже угадали эту букву.")
            return

        self.guessed_letters.append(letter)

        if letter not in self.secret_word:
            self.attempts += 1
            self.label_attempts.config(text=f"Ошибки: {self.attempts}/{self.max_attempts}")
            self.draw_hangman()

        self.label_word.config(text=self.get_display_word())

        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Игра окончена", f"Вы проиграли! Загаданное слово: {self.secret_word}")
            self.master.destroy()
        elif "_" not in self.get_display_word():
            messagebox.showinfo("Поздравляем!", "Вы угадали слово!")
            self.master.destroy()

    def draw_hangman(self):
        self.canvas.delete("all")
        if self.attempts >= 1:
            self.canvas.create_line(50, 150, 150, 150)  # Ножка
        if self.attempts >= 2:
            self.canvas.create_line(100, 150, 100, 50)  # Столб
        if self.attempts >= 3:
            self.canvas.create_line(100, 50, 150, 50)  # Перекладина
        if self.attempts >= 4:
            self.canvas.create_line(150, 50, 150, 70)  # Голова
            self.canvas.create_oval(135, 70, 165, 100)  # Лицо
        if self.attempts >= 5:
            self.canvas.create_line(150, 100, 130, 130)  # Левая рука
        if self.attempts >= 6:
            self.canvas.create_line(150, 100, 170, 130)  # Правая рука

if __name__ == "__main__":
    root = tk.Tk()
    game = Hangman(root)
    root.mainloop()
