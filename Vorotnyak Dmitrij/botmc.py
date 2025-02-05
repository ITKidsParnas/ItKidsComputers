import itertools
import time
import threading

# Глобальные переменные
found_password = None
lock = threading.Lock()

def attempt_password(attempt, target_password):
    global found_password
    if found_password is not None:  # Если пароль уже найден, завершаем проверку
        return

    if attempt == target_password:
        with lock:
            if found_password is None:  # Проверяем еще раз, чтобы предотвратить дублирование
                found_password = attempt
                print(f'Пароль найден: {attempt}')

def password_cracker(target_password, length, start_char, end_char):
    characters = ''.join(chr(i) for i in range(ord(start_char), ord(end_char) + 1))
    for attempt in itertools.product(characters, repeat=length):
        attempt_str = ''.join(attempt)
        attempt_password(attempt_str, target_password)

def thread_worker(target_password, password_length, start_char, end_char):
    password_cracker(target_password, password_length, start_char, end_char)

if __name__ == '__main__':
    password_to_crack = input("Введите пароль для подбора: ")
    password_length = len(password_to_crack)

    # Создадим несколько потоков для поддержки подбора паролей
    threads = []
    num_threads = 4  # Укажите количество потоков
    chunk_size = 26 // num_threads  # Разделяем диапазон символов на части

    for i in range(num_threads):
        start_char = chr(ord('a') + i * chunk_size)
        end_char = chr(ord('a') + (i + 1) * chunk_size - 1)
        if i == num_threads - 1:  # Для последнего потока добавляем оставшиеся символы
            end_char = 'z'
        thread = threading.Thread(target=thread_worker, args=(password_to_crack, password_length, start_char, end_char))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Ждем завершения всех потоков

    if found_password is None:
        print('Пароль не найден')