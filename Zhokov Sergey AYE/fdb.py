import random
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

def intro():
    print(Fore.CYAN + Style.BRIGHT + "Добро пожаловать в игру 'Поход в кишечник'!")
    print(Fore.GREEN + "Вы - микроб, который путешествует по кишечнику.")
    print(Fore.YELLOW + "Ваша цель - выжить и найти выход!")
    print(Fore.MAGENTA + "-" * 50)

def choose_ability():
    abilities = {
        "1": ("Восстановление", "Восстанавливает 20 здоровья.", 20),
        "2": ("Уклонение", "Позволяет избежать одного негативного события.", 0),
        "3": ("Усиление", "Увеличивает ваши очки на 10 после каждого события.", 10),
    }
    
    print(Fore.YELLOW + "Выберите способность:")
    for key, (name, description, _) in abilities.items():
        print(Fore.CYAN + f"{key}. {name} - {description}")
    
    while True:
        choice = input(Fore.WHITE + "Ваш выбор (1-3): ").strip()
        if choice in abilities:
            return abilities[choice]
        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")

def encounter(location, ability_used):
    events = {
        "начало": [
            ("Вы встретили полезные бактерии! Они помогают вам.", 10),
            ("Вы столкнулись с токсинами! Вам нужно отступить.", -20),
        ],
        "еда": [
            ("Вы нашли еду! Ваши силы восстановлены.", 15),
            ("Вы попали в ловушку! Вам нужно выбраться.", -10),
        ],
        "токсичное место": [
            ("Вы нашли антидот! Он поможет вам в будущем.", 0, "антидот"),
            ("Вы столкнулись с токсинами! Вам нужно отступить.", -30),
        ],
        "пустота": [
            ("Вы нашли безопасное место для отдыха.", 5),
            ("Вы потеряли время и силы, но ничего не нашли.", -5),
        ],
        "заброшенный участок": [
            ("Вы нашли старый запас еды!", 20),
            ("Вы столкнулись с опасным патогеном! Вам нужно бежать.", -25),
        ],
        "колония бактерий": [
            ("Вы присоединились к колонии бактерий! Ваши силы увеличены.", 20),
            ("Вы столкнулись с конкурентами! Вам нужно бежать.", -15),
        ],
        "пещера": [
            ("Вы нашли редкий минерал! Он поможет вам в будущем.", 0, "минерал"),
            ("Вы попали в ловушку! Вам нужно выбраться.", -20),
        ],
        "заброшенная лаборатория": [
            ("Вы нашли старые образцы! Они могут быть полезны.", 10, "образец"),
            ("Вы столкнулись с охранной системой! Вам нужно бежать.", -30),
        ],
        "микробная ферма": [
            ("Вы нашли источник пищи! Ваши силы восстановлены.", 25),
            ("Вы столкнулись с агрессивными бактериями! Вам нужно бежать.", -15),
        ],
        "кишечный лабиринт": [
            ("Вы нашли выход из лабиринта! Ваши очки увеличены.", 30),
            ("Вы заблудились и потеряли силы.", -10),
        ],
        "заброшенный склад": [
            ("Вы нашли полезные ресурсы!", 15),
            ("Вы столкнулись с опасными химикатами! Вам нужно бежать.", -25),
        ],
        "потерянный мир": [
            ("Вы нашли древние артефакты! Они могут помочь вам.", 0, "артефакт"),
            ("Вы столкнулись с древними патогенами! Вам нужно бежать.", -40),
        ],
        "кишечный рынок": [
            ("Вы нашли торговца! Он предлагает вам полезные вещи.", 0, "торговец"),
            ("Вы столкнулись с ворами! Вам нужно бежать.", -20),
        ],
    }
    
    event = random.choice(events[location])
    
    # Если событие негативное и способность уклонения не использована
    if event[1] < 0 and not ability_used:
        print(Fore.YELLOW + "Вы используете способность 'Уклонение'!")
        return ("Вы избежали негативного события!", 0)
    
    return event

def choose_location():
    print(Fore.YELLOW + "Выберите локацию для исследования:")
    print(Fore.CYAN + "1. Начало")
    print(Fore.CYAN + "2. Еда")
    print(Fore.CYAN + "3. Токсичное место")
    print(Fore.CYAN + "4. Пустота")
    print(Fore.CYAN + "5. Заброшенный участок")
    print(Fore.CYAN + "6. Колония бактерий")
    print(Fore.CYAN + "7. Пещера")
    print(Fore.CYAN + "8. Заброшенная лаборатория")
    print(Fore.CYAN + "9. Микробная ферма")
    print(Fore.CYAN + "10. Кишечный лабиринт")
    print(Fore.CYAN + "11. Заброшенный склад")
    print(Fore.CYAN + "12. Потерянный мир")
    print(Fore.CYAN + "13. Кишечный рынок")
    print(Fore.MAGENTA + "-" * 50)

    while True:
        choice = input(Fore.WHITE + "Ваш выбор (1-13): ").strip()
        if choice in [str(i) for i in range(1, 14)]:
            return [
                "начало", "еда", "токсичное место", "пустота", "заброшенный участок",
                "колония бактерий", "пещера", "заброшенная лаборатория", "микробная ферма",
                "кишечный лабиринт", "заброшенный склад", "потерянный мир", "кишечный рынок"
            ][int(choice) - 1]
        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")

def use_item(inventory):
    if not inventory:
        print(Fore.RED + "Ваш инвентарь пуст!")
        return

    print(Fore.YELLOW + "Выберите предмет для использования:")
    for i, item in enumerate(inventory, 1):
        print(Fore.CYAN + f"{i}. {item}")

    while True:
        choice = input(Fore.WHITE + "Ваш выбор: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(inventory):
            item = inventory.pop(int(choice) - 1)
            if item == "антидот":
                print(Fore.GREEN + "Вы использовали антидот и восстановили 30 здоровья!")
                return 30
            elif item == "минерал":
                print(Fore.GREEN + "Вы использовали минерал и получили 10 очков!")
                return 10
            elif item == "артефакт":
                print(Fore.GREEN + "Вы использовали артефакт и получили 50 очков!")
                return 50
            else:
                print(Fore.RED + "Этот предмет не может быть использован.")
                return 0
        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")

def rest(health):
    print(Fore.GREEN + "Вы отдыхаете и восстанавливаете 20 здоровья.")
    return min(health + 20, 100)  # Максимум 100 здоровья

def attack():
    success = random.choice([True, False])
    if success:
        print(Fore.GREEN + "Вы успешно атаковали врага и получили 20 очков!")
        return 20
    else:
        print(Fore.RED + "Атака не удалась! Вы потеряли 10 здоровья.")
        return -10

def ending(score, health, inventory):
    # Условия для концовок
    if health <= 0:
        print(Fore.RED + "Вы потеряли все силы и не смогли продолжить путь. Игра окончена!")
    elif score >= 150 and "антидот" in inventory and "артефакт" in inventory:
        print(Fore.GREEN + "Поздравляем! Вы стали легендой кишечника и нашли выход с помощью антидота и артефакта!")
    elif score >= 100 and "антидот" in inventory:
        print(Fore.YELLOW + "Вы успешно выжили, но не смогли найти выход. У вас есть антидот, который может помочь в будущем!")
    elif score >= 50:
        print(Fore.MAGENTA + "Вы потерялись в кишечнике и не смогли найти выход. Но вы все еще микроб!")
    else:
        print(Fore.RED + "Вы не смогли выжить в кишечнике. Игра окончена!")

def main():
    intro()
    ability = choose_ability()
    ability_name, ability_description, ability_effect = ability
    ability_used = False
    
    health = 100
    score = 0
    inventory = []
    location = "начало"

    print(Fore.GREEN + f"Вы выбрали способность: {ability_name} - {ability_description}")

    while health > 0:
        print(Fore.BLUE + Style.BRIGHT + f"\nВы находитесь в локации: {location}")
        print(Fore.YELLOW + "Выберите действие:")
        print(Fore.CYAN + "1. Исследовать")
        print(Fore.CYAN + "2. Проверить инвентарь")
        print(Fore.CYAN + "3. Выбрать новую локацию")
        print(Fore.CYAN + "4. Использовать предмет")
        print(Fore.CYAN + "5. Отдохнуть")
        print(Fore.CYAN + "6. Атаковать")
        print(Fore.CYAN + "7. Выйти")
        print(Fore.MAGENTA + "-" * 50)

        action = input(Fore.WHITE + "Ваш выбор (1-7): ").strip()

        if action == "1":
            event = encounter(location, ability_used)
            print(Fore.GREEN + event[0])
            if event[1] >= 0:
                score += event[1] + (ability_effect if ability_name == "Усиление" else 0)
                health += event[1] if event[1] > 0 else 0
            else:
                health += event[1]  # Уменьшаем здоровье

            if len(event) > 2:  # Если есть предмет
                inventory.append(event[2])
                print(Fore.GREEN + f"Вы получили предмет: {event[2]}")

            if ability_name == "Уклонение":
                ability_used = True  # Способность использована

        elif action == "2