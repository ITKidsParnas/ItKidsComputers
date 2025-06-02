import tkinter as tk

class ClickSpacebarTester:
    def __init__(self, master):
        self.master = master
        self.master.title("Тестер нажатий пробела и кликов мыши за 1 минуту")

        self.spacebar_count = 0
        self.mouse_click_count = 0
        self.is_testing = False

        # Создаем виджеты
        self.label = tk.Label(master, text="Нажмите на кнопку, чтобы начать тестирование.")
        self.label.pack(pady=10)

        self.count_label = tk.Label(master, text="Количество нажатий пробела: 0\nКоличество кликов мыши: 0")
        self.count_label.pack(pady=10)

        self.start_button = tk.Button(master, text="Начать тест", command=self.start_test)
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(master, text="Сбросить", command=self.reset_test)
        self.reset_button.pack(pady=10)

    def start_test(self):
        self.spacebar_count = 0
        self.mouse_click_count = 0
        self.is_testing = True
        self.label.config(text="Нажмите пробел и кликайте мышью как можно больше раз за 1 минуту!")
        self.count_label.config(text="Количество нажатий пробела: 0\nКоличество кликов мыши: 0")
        self.master.after(60000, self.end_test)  # Завершить тест через 60 секунд

    def end_test(self):
        self.is_testing = False
        self.label.config(text="Тест завершен!")
        self.count_label.config(text=f"Количество нажатий пробела: {self.spacebar_count}\nКоличество кликов мыши: {self.mouse_click_count}")

    def reset_test(self):
        self.spacebar_count = 0
        self.mouse_click_count = 0
        self.count_label.config(text="Количество нажатий пробела: 0\nКоличество кликов мыши: 0")
        self.label.config(text="Нажмите на кнопку, чтобы начать тестирование.")

    def count_spacebar(self, event):
        if self.is_testing and event.keysym == 'space':
            self.spacebar_count += 1
            self.count_label.config(text=f"Количество нажатий пробела: {self.spacebar_count}\nКоличество кликов мыши: {self.mouse_click_count}")

    def count_mouse_click(self, event):
        if self.is_testing:
            self.mouse_click_count += 1
            self.count_label.config(text=f"Количество нажатий пробела: {self.spacebar_count}\nКоличество кликов мыши: {self.mouse_click_count}")

# Создание основного окна
root = tk.Tk()
tester = ClickSpacebarTester(root)

# Привязка событий
root.bind("<space>", tester.count_spacebar)
root.bind("<Button-1>", tester.count_mouse_click)  # Левый клик мыши

# Запуск приложения
root.mainloop()
