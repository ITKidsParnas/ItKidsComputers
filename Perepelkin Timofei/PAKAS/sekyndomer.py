import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Секундомер")

        self.running = False
        self.time_elapsed = 0  # Время в секундах

        # Метка для отображения времени
        self.label = tk.Label(root, text=self.format_time(self.time_elapsed), font=("Helvetica", 48))
        self.label.pack(pady=20)

        # Кнопки
        self.start_button = tk.Button(root, text="Старт", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Стоп", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Сброс", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.update()  # Запускаем обновление метки времени

    def format_time(self, seconds):
        """Форматирует время в часы, минуты и секунды."""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def update(self):
        """Обновляет время, если секундомер запущен."""
        if self.running:
            self.time_elapsed += 1
            self.label.config(text=self.format_time(self.time_elapsed))
        self.root.after(1000, self.update)  # Обновляем каждую секунду

    def start(self):
        """Запускает секундомер."""
        self.running = True

    def stop(self):
        """Останавливает секундомер."""
        self.running = False

    def reset(self):
        """Сбрасывает секундомер."""
        self.running = False
        self.time_elapsed = 0
        self.label.config(text=self.format_time(self.time_elapsed))

# Создание основного окна
if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
