import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Таймер")

        self.time_left = 0
        self.running = False

        self.label = tk.Label(root, text="Введите время в cекундах:", font=("Helvetica", 70))
        self.label.pack()

        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack()

        self.start_button = tk.Button(root, text="Старт", command=self.start_timer)
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(root, text="Стоп", command=self.stop_timer)
        self.stop_button.pack(side="left")

        self.reset_button = tk.Button(root, text="Сброс", command=self.reset_timer)
        self.reset_button.pack(side="left")

        self.timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
        self.timer_label.pack()

    def start_timer(self):
        if not self.running:
            try:
                self.time_left = int(self.entry.get())
                self.running = True
                self.update_timer()
            except ValueError:
                self.timer_label.config(text="Ошибка ввода")

    def update_timer(self):
        if self.running and self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.timer_label.config(text="Время вышло!")
            self.running = False

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.timer_label.config(text="00:00")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = TimerApp(root)
    root.mainloop()