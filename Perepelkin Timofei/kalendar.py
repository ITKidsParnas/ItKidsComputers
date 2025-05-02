import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Календарь")

        # Создание календаря
        self.calendar = Calendar(root, selectmode='day')
        self.calendar.pack(pady=20)

        # Кнопка для выбора даты
        self.btn_select_date = tk.Button(root, text="Выбрать дату", command=self.show_selected_date)
        self.btn_select_date.pack(pady=10)

    def show_selected_date(self):
        selected_date = self.calendar.get_date()
        messagebox.showinfo("Выбранная дата", f"Вы выбрали: {selected_date}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()