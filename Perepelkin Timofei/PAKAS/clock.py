import tkinter as tk
from datetime import datetime
import pytz

# Устанавливаем временную зону для Москвы
moscow_tz = pytz.timezone('Europe/Moscow')

def update_time():
    # Получаем текущее время в Москве
    moscow_time = datetime.now(moscow_tz).strftime("%H:%M:%S")
    label.config(text=moscow_time)  # Обновляем текст метки
    label.after(1000, update_time)  # Запускаем обновление каждую секунду

# Создаем главное окно
root = tk.Tk()
root.title("Часы по Московскому Времени")

# Создаем метку для отображения времени
label = tk.Label(root, font=("Helvetica", 48), fg="black")
label.pack(pady=20)  # Добавляем отступ

# Запускаем обновление времени
update_time()

# Запускаем главный цикл
root.mainloop()
