import random
from colorama import Fore, Style, init

# Инициализация colorama для красивого вывода в консоль
init(autoreset=True)

# Функция для вывода приветствия и описания игры
def intro():
    print(Fore.CYAN + Style.BRIGHT + "Добро пожаловать в игру 'Поход в кишечник'!")
    print(Fore.GREEN + "Вы - микроб, который путешествует по кишечнику.")
    print(Fore.YELLOW + "Ваша цель - выжить, найти выход и победить Главного Босса!")
    print(Fore.MAGENTA + "-" * 50)

# Функция для выбора способности игроком
def choose_ability():
    abilities = {
        "1": ("Восстановление", "Восстанавливает 20 здоровья.", 20),
        "2": ("Уклонение", "Позволяет избежать одного негативного события.", 0),
        "3": ("Усиление", "Увеличивает ваши очки на 10 после каждого события.", 10),
        "4": ("Ярость", "Увеличивает силу атаки на 10, но снижает защиту на 5.", 0)  # Новая способность
    }
    print(Fore.YELLOW + "Выберите способность:")
    for key, (name, description, _) in abilities.items():
        print(Fore.CYAN + f"{key}. {name} - {description}")

    while True:
        choice = input(Fore.WHITE + "Ваш выбор (1-4): ").strip()
        if choice in abilities:
            return abilities[choice]
        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")

# Функция, описывающая случайное событие в локации
def encounter(location, ability_used, has_artifact, has_weapon):  # Добавлены параметры для артефакта и оружия
    events = {
        "начало": [("Вы встретили полезные бактерии! Они помогают вам.", 10), ("Вы столкнулись с токсинами! Вам нужно отступить.", -20)],
        "еда": [("Вы нашли еду! Ваши силы восстановлены.", 15), ("Вы попали в ловушку! Вам нужно выбраться.", -10)],
        "токсичное место": [("Вы нашли антидот! Он поможет вам в будущем.", 0, "антидот"), ("Вы столкнулись с токсинами! Вам нужно отступить.", -30)],
        "пустота": [("Вы нашли безопасное место для отдыха.", 5), ("Вы потеряли время и силы, но ничего не нашли.", -5)],
        "заброшенный участок": [("Вы нашли старый запас еды!", 20), ("Вы столкнулись с опасным патогеном! Вам нужно бежать.", -25)],
        "колония бактерий": [("Вы присоединились к колонии бактерий! Ваши силы увеличены.", 20), ("Вы столкнулись с конкурентами! Вам нужно бежать.", -15)],
        "пещера": [("Вы нашли редкий минерал! Он поможет вам в будущем.", 0, "минерал"), ("Вы попали в ловушку! Вам нужно выбраться.", -20)],
        "заброшенная лаборатория": [("Вы нашли старые образцы! Они могут быть полезны.", 10, "образец"), ("Вы столкнулись с охранной системой! Вам нужно бежать.", -30)],
        "микробная ферма": [("Вы нашли источник пищи! Ваши силы восстановлены.", 25), ("Вы столкнулись с агрессивными бактериями! Вам нужно бежать.", -15)],
        "кишечный лабиринт": [("Вы нашли выход из лабиринта! Ваши очки увеличены.", 30), ("Вы заблудились и потеряли силы.", -10)],
        "заброшенный склад": [("Вы нашли полезные ресурсы!", 15), ("Вы столкнулись с опасными химикатами! Вам нужно бежать.", -25)],
        "потерянный мир": [("Вы нашли древние артефакты! Они могут помочь вам.", 0, "артефакт"), ("Вы столкнулись с древними патогенами! Вам нужно бежать.", -40)],
        "кишечный рынок": [("Вы нашли торговца! Он предлагает вам полезные вещи.", 0, "торговец"), ("Вы столкнулись с ворами! Вам нужно бежать.", -20)],
        "оазис": [("Вы нашли колодец с целебной водой! Восстанавливает много здоровья.", 40), ("Вы столкнулись с песчаной бурей! Потеря сил.", -15)], #Новая локация
        "канализация":[("Вы нашли чертежи от оружия", 0, "чертеж"),("Вы провалились в люк", -30)], #Новая локация
        "древний храм":[("Вы нашли легендарное оружие", 0, "оружие"), ("Храм обвалился на вас", -50)] #Новая локация
    }

    event = random.choice(events[location])

    if event[1] < 0 and not ability_used:
        print(Fore.YELLOW + "Вы используете способность 'Уклонение'!")
        return ("Вы избежали негативного события!", 10)

    if location == "древний храм" and has_artifact:
        print(Fore.GREEN + "Артефакт помог найти вам сокровище")
        return ("Вы нашли легендарный артефакт", 50) #Если есть артефакт увеличивает шанс на выйгрыш

    return event

# Функция для выбора локации игроком
def choose_location(has_blueprint): #Добавлена проверка на чертеж
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
    print(Fore.CYAN + "14. Оазис")
    print(Fore.CYAN + "15. Канализация") #Новые локации
    if has_blueprint:
      print(Fore.CYAN + "16. Древний Храм") #Новые локации

    print(Fore.MAGENTA + "-" * 50)

    while True:
        choice = input(Fore.WHITE + "Ваш выбор (1-16): ").strip()
        locations = [
                "начало", "еда", "токсичное место", "пустота", "заброшенный участок",
                "колония бактерий", "пещера", "заброшенная лаборатория", "микробная ферма",
                "кишечный лабиринт", "заброшенный склад", "потерянный мир", "кишечный рынок", "оазис", "канализация"
            ]
        if has_blueprint:
            locations.append("древний храм")
        if choice in [str(i) for i in range(1, len(locations)+1)]:
            return locations[int(choice) -   1]
        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")

# Функция для использования предмета из инвентаря
def use_item(inventory, has_weapon):
    if not inventory:
        print(Fore.RED + "Ваш инвентарь пуст!")
        return 0

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
            elif item == "оружие" and has_weapon == False:
                print(Fore.GREEN + "Вы экипировали оружие!")
                return "оружие"
            else:
                print(Fore.RED + "Этот предмет не может быть использован.")
                return 0
        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")

# Функция для отдыха (восстановления здоровья)
def rest(health):
    print(Fore.GREEN + "Вы отдыхаете и восстанавливаете 20 здоровья.")
    return min(health + 20, 100)

# Функция для атаки
def attack(ability_name, has_weapon): #Добавлена проверка на оружие
    success = random.choice([True, False])
    attack_power = 20
    if ability_name == "Ярость":
        attack_power += 10
    if has_weapon:
        attack_power += 15
    if success:
        print(Fore.GREEN + "Вы успешно атаковали врага и получили 20 очков!")
        return attack_power
    else:
        print(Fore.RED + "Атака не удалась! Вы потеряли 10 здоровья.")
        return -10

# Функция для битвы с боссом
def boss_battle(health, score, ability_name, has_weapon):
    print(Fore.RED + Style.BRIGHT + "\nВНИМАНИЕ! ВЫ ВСТУПИЛИ В БИТВУ С ГЛАВНЫМ БОССОМ!")
    boss_health = 150
    print(Fore.RED + f"Здоровье босса: {boss_health}")
    global inventory
    while health > 0 and boss_health > 0:
        print(Fore.YELLOW + "\nВыберите действие:")
        print(Fore.CYAN + "1. Атаковать")
        print(Fore.CYAN + "2. Использовать антидот (если есть)")
        print(Fore.CYAN + "3. Попытаться сбежать")

        action = input(Fore.WHITE + "Ваш выбор (1-3): ").strip()

        if action == "1":
            damage = attack(ability_name, has_weapon)
            if damage > 0:
                boss_health -= damage
                print(Fore.GREEN + f"Вы нанесли боссу {damage} урона!")
            else:
                health -= 10
                print(Fore.RED + "Босс контратаковал!")

        elif action == "2":
            if "антидот" in inventory:
                inventory.remove("антидот")
                health = min(health + 50, 100)
                print(Fore.GREEN + "Вы использовали антидот и восстановили 50 здоровья!")
            else:
                print(Fore.RED + "У вас нет антидота!")

        elif action == "3":
            if random.random() < 0.3:  # 30% шанс на побег
                print(Fore.GREEN + "Вам удалось сбежать!")
                return health, score, False  # Возвращаем False, чтобы указать, что битва не выиграна
            else:
                health -= 20
                print(Fore.RED + "Попытка побега не удалась! Босс нанес вам урон.")

        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")

        print(Fore.BLUE + f"Ваше здоровье: {health}")
        print(Fore.RED + f"Здоровье босса: {boss_health}")

    if health <= 0:
        print(Fore.RED + "Вы проиграли в битве с боссом.")
        return health, score, False
    else:
        print(Fore.GREEN + Style.BRIGHT + "ПОБЕДА! Вы победили Главного Босса!")
        score += 100
        return health, score, True  # Возвращаем True, чтобы указать, что битва выиграна


# Функция, определяющая концовку игры
def ending(score, health, inventory, boss_defeated): #Добавлена проверка на победу над боссом
    if health <= 0:
        print(Fore.RED + "Вы потеряли все силы и не смогли продолжить путь. Игра окончена!")
    elif boss_defeated:
        print(Fore.GREEN + Style.BRIGHT + "Поздравляем! Вы победили Главного Босса и стали героем кишечника!")
    elif score >= 150 and "антидот" in inventory and "артефакт" in inventory:
        print(Fore.GREEN + "Поздравляем! Вы стали легендой кишечника и нашли выход с помощью антидота и артефакта!")
    elif score >= 100 and "антидот" in inventory:
        print(Fore.YELLOW + "Вы успешно выжили, но не смогли найти выход. У вас есть антидот, который может помочь в будущем!")
    elif score >= 50:
        print(Fore.MAGENTA + "Вы потерялись в кишечнике и не смогли найти выход. Но вы все еще микроб!")
    else:
        print(Fore.RED + "Вы не смогли выжить в кишечнике. Игра окончена!")

# Основная функция игры
def main():
    global inventory
    intro()
    ability = choose_ability()
    ability_name, ability_description, ability_effect = ability
    ability_used = False

    health = 100
    score = 0
    inventory = []
    location = "начало"
    has_blueprint = False
    has_artifact = False
    has_weapon = False
    boss_defeated = False

    print(Fore.GREEN + f"Вы выбрали способность: {ability_name} - {ability_description}")

    while health > 0 and not boss_defeated: #Добавлена проверка на поражение босса
        print(Fore.BLUE + Style.BRIGHT + f"\nВы находитесь в локации: {location}")
        print(Fore.YELLOW + "Выберите действие:")
        print(Fore.CYAN + "1. Исследовать")
        print(Fore.CYAN + "2. Проверить инвентарь")
        print(Fore.CYAN + "3. Выбрать новую локацию")
        print(Fore.CYAN + "4. Использовать предмет")
        print(Fore.CYAN + "5. Отдохнуть")
        print(Fore.CYAN + "6. Атаковать")
        print(Fore.CYAN + "7. Встретиться с Главным Боссом (Только в Кишечном Лабиринте)")
        print(Fore.CYAN + "8. Выйти")
        print(Fore.MAGENTA + "-" * 50)

        action = input(Fore.WHITE + "Ваш выбор (1-8): ").strip()

        if action == "1":
            event = encounter(location, ability_used, has_artifact, has_weapon)
            print(Fore.GREEN + event[0])
            if event[1] >= 0:
                score += event[1] + (ability_effect if ability_name == "Усиление" else 0)
                health += event[1] if event[1] > 0 else 0
            else:
                health += event[1]

            if len(event) > 2:
                item = event[2]
                inventory.append(item)
                print(Fore.GREEN + f"Вы получили предмет: {item}")
                if item == "артефакт":
                    has_artifact = True
                if item == "чертеж":
                  has_blueprint = True
                if item == "оружие":
                  has_weapon = True


            if ability_name == "Уклонение":
                ability_used = True

        elif action == "2":
            if not inventory:
                print(Fore.RED + "Ваш инвентарь пуст!")
            else:
                print(Fore.YELLOW + "В вашем инвентаре:")
                for item in inventory:
                    print(Fore.CYAN + f"- {item}")

        elif action == "3":
            location = choose_location(has_blueprint)
            ability_used = False  # Сбрасываем использование способности при смене локации

        elif action == "4":
            health_change = use_item(inventory, has_weapon)
            if health_change == "оружие":
                has_weapon = True
            elif isinstance(health_change, int):
                health += health_change

        elif action == "5":
            health = rest(health)

        elif action == "6":
            health_change = attack(ability_name, has_weapon)
            score += health_change if health_change > 0 else 0
            health += health_change if health_change < 0 else 0
            if ability_name == "Ярость":
              health -= 5

        elif action == "7" and location == "кишечный лабиринт":
            health, score, boss_defeated = boss_battle(health, score, ability_name, has_weapon)
            if boss_defeated:
                break

        elif action == "8":
            print(Fore.YELLOW + "Вы вышли из игры.")
            break

        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")

        print(Fore.BLUE + f"Здоровье: {health}")
        print(Fore.GREEN + f"Очки: {score}")
        print(Fore.MAGENTA + "-" * 50)

    ending(score, health, inventory, boss_defeated)


if __name__ == "__main__":
    main()
