import tkinter as tk
import random

def random_choice():
    if not people:
        result_label.config(text="Список людей пуст!")
    else:
        selected_person = random.choice(people)
        result_label.config(text=f"Случайное выбранное слово: {selected_person}")

# Список людей
people = [
    "я",
    "ты",
    "мы",
    "вы",
    "он",
    "она",
    "оно",
    "они",
    "you"
]

# Создание основного окна
root = tk.Tk()
root.title("Случайный выбор человека")

# Кнопка для выбора случайного человека
choose_button = tk.Button(root, text="Выбрать случайное слово", command=random_choice)
choose_button.pack(pady=20)

# Метка для отображения результата
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Запуск основного цикла приложения
root.mainloop()
