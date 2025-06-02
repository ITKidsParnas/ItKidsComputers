import itertools
import time


class TextColor:
    RESET = "\033[0m"
    BLUE = "\033[94m"
    PURPLE = "\033[35m"
    GREEN = "\033[92m"  #цвета ansi-коды
    RED = "\033[91m"

def colored_text(text, color):
    return f"{color}{text}{TextColor.RESET}"

def evaluate_password_strength(password):
    length_score = len(password)
    if length_score < 6:
        return 'Слабый'  # Менее 6 символов
    elif length_score < 10:
        return 'Средний'  # 6-9 символов
    else:
        # Более 10 символов
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        

        # Оценка силы пароля
        if has_upper and has_lower and has_digit:
            return 'Сильный'
        else:
            return 'Средний'

def password_cracker(target_password):
    # Определяем возможные символы: буквы и цифры
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password_length = len(target_password)

    # Счетчик для отслеживания количества попыток
    attempt_count = 0

    # Запоминаем время начала процесса подбора
    start_time = time.time()

    # Генерация всех возможных комбинаций символов заданной длины
    for attempt in itertools.product(characters, repeat=password_length):
        attempt = ''.join(attempt)  # Преобразуем кортеж в строку

        # Увеличиваем счетчик каждой итерацией
        attempt_count += 1

        # Выводим каждую 10000-ю попытку
        if attempt_count % 10000 == 0:
            print(colored_text(f"Пробуем пароль: {attempt}", TextColor.GREEN))

        if attempt == target_password:
            # Запоминаем время окончания процесса
            end_time = time.time()
            elapsed_time = end_time - start_time  # Вычисляем время выполнения
            print(colored_text(f"Пароль найден: {attempt}", TextColor.BLUE))
            print(colored_text(f"Время, потраченное на подбор: {elapsed_time:.2f} секунд", TextColor.BLUE))
            return

    print(colored_text("Пароль не найден", TextColor.RED))

# Пример использования
if __name__ == '__main__':
    password_to_crack = input(colored_text("Введите пароль для подбора: ", TextColor.PURPLE))  # Ввод пароля
    password_strength = evaluate_password_strength(password_to_crack)
    print(colored_text(f"Надежность пароля: {password_strength}", TextColor.RED))
    password_cracker(password_to_crack)