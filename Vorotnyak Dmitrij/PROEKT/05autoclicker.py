import mouse
import keyboard
import time

# Задержка перед началом работы
time.sleep(5)  # Время в секундах для подготовки

# Настройка количества кликов в секунду
clicks_per_second = 444  # Например, 444 клика в секунду
delay = 1 / clicks_per_second  # Вычисляем задержку между кликами

try:
    print("Автокликер запущен. Нажмите 'Esc' для остановки.")
    while True:
        if keyboard.is_pressed("esc"):  # Проверяем, нажата ли клавиша 'Esc'
            print("Автокликер остановлен.")  # Сообщение об остановке
            break
        mouse.click()  # Выполняем клик
        time.sleep(delay)  # Задержка между кликами
except KeyboardInterrupt:
    print("Автокликер остановлен.")