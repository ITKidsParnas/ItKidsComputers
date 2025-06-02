import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Установка полноэкранного режима
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()  # Получение текущих размеров экрана
pygame.display.set_caption("Виселица")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Шрифт для текста
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Слова для угадывания
words = [
    "DOG", "CAT", "CAR", "HOUSE", "APARTMENT", "STREET",
    "CHAIR", "TABLE", "WINDOW", "DOOR", "BOOK", "MAGAZINE",
    "NEWSPAPER", "PHONE", "LAMP", "KITCHEN", "FRIDGE",
    "FURNITURE", "CARPET", "PILLOW", "BLANKET", "BED",
    "BATH", "SHOWER", "TOILET", "FOOD", "DRINK",
    "CORN", "BREAD", "FISH", "MEAT", "CUCUMBER",
    "TOMATO", "ONION", "GARLIC", "SALT", "SUGAR",
    "TEA", "COFFEE", "SOUP", "POTATO", "ROLL",
    "SEA", "MOUNTAINS", "FOREST", "LAKE", "PARK",
    "BEACH", "SUN", "RAIN", "SNOW", "WIND",
    "TIME", "DAY", "NIGHT", "MORNING", "EVENING",
    "TRAVEL", "RELAXATION", "NATURE", "WALK", "PICKNIC",
    "MOVIE", "THEATER", "CONCERT", "GAME", "SPORT",
    "FOOTBALL", "BASKETBALL", "TENNIS", "HOCKEY", "GYMNASTICS",
    "DANCE", "RHYTHM", "MUSIC", "PAINTING", "PHOTO",
    "GIFT", "HOLIDAY", "BIRTHDAY", "CELEBRATION", "SAINT",
    "PHONE", "COMPUTER", "INTERNET", "TELEVISION", "COFFEE", 
    "SCHOOL", "STUDENT", "TEACHER", "FRIEND", "FAMILY", 
    "PARTY", "VACATION", "MUSIC", "MOVIE", "BOOK", 
    "GAMES", "SOCCER", "BASKETBALL", "CANDY", "CHOCOLATE", 
    "HAPPY", "SAD", "LOVE", "FRIENDSHIP", "HEALTH", 
    "EXERCISE", "FOOD", "JUNKFOOD", "SNACK", "BREAKFAST", 
    "LUNCH", "DINNER", "DANCE", "SINGING", "TRAVEL", 
    "HOBBY", "ART", "PAINTING", "WRITING", "PHOTOGRAPHY", 
    "WINTER", "SUMMER", "SPRING", "AUTUMN", "HOLIDAY", 
    "CELEBRATION", "BIRTHDAY", "NEWYEAR", "CHRISTMAS", "FRUIT", 
    "VEGETABLE", "PIZZA", "BURGER", "SANDWICH", "PASTA", 
    "ICECREAM", "SODA", "TEA", "SWEETS", "GAME", 
    "BOOKSTORE", "SUBWAY", "TRAIN", "AIRPLANE", "CITY", 
    "COUNTRY", "ROADTRIP", "MUSEUM", "ZOO", "GARDEN", 
    "PARK", "BEACH", "MOUNTAINS", "LAKE", "RIVER", 
    "NATURE", "SPACE", "STARS", "PLANETS", "OCEAN",
    "PYTHON", "PROGRAMMING", "HANGMAN", "DEVELOPER", "COMPUTER", "GAME",
    "ALGORITHMS", "FUNCTION", "VARIABLE", "LISTS", "TUPLE", "DICT", 
    "CIRCULAR", "HEADER", "FIBONACCI", "RECURSION", "DATABASE", "API",
    "EVENTS", "ANIMATION", "THREADING", "MULTITHREADING", "EXCEPTION", 
    "DEBUGGING", "LIBRARY", "FRAMEWORK", "SYNCHRONIZATION", "COMPILATION",
    "INTERPRETER", "CONDITIONS", "LOOPS", "ITERATOR", "GENERATOR",
    "ENCAPSULATION", "POLYMORPHISM", "ABSTRACTION", "COMPOSITION", "INHERITANCE",
    "SOFTWARE", "REGEX", "SCRAPING", "DATA", "MACHINELEARNING", "ARTIFICIALINTELLIGENCE",
    "CLOUDCOMPUTING", "CYBERSECURITY", "DEVOPS", "OPEN_SOURCE", "VERSION_CONTROL"
]

def draw_hangman(attempts):
    pygame.draw.line(screen, BLACK, (500, 100), (500, 150), 5)  # голова
    pygame.draw.line(screen, BLACK, (400, height - 100), (400, 100), 5)  # стойка
    pygame.draw.line(screen, BLACK, (300, height - 100), (500, height - 100), 5)  # основание
    pygame.draw.line(screen, BLACK, (400, 100), (500, 100), 5)  # перекладина
    if attempts == 6:
        pygame.draw.line(screen, BLACK, (500, 270), (530, 320), 5)  # правая нога
        
    if attempts >= 5:
        
        pygame.draw.line(screen, BLACK, (500, 270), (470, 320), 5)  # левая нога
    if attempts >= 4:
        pygame.draw.line(screen, BLACK, (500, 200), (530, 230), 5)  # правая рука

    if attempts >= 3:
        pygame.draw.line(screen, BLACK, (500, 200), (470, 230), 5)  # левая рук
        
    if attempts >= 2:
        pygame.draw.line(screen, BLACK, (500, 170), (500, 270), 5)  # тело
        
    if attempts >= 1:
        pygame.draw.circle(screen, BLACK, (500, 160), 10, 0)  # голова
  
        
        

# Основная логика игры
def main():
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    while True:
        screen.fill(WHITE)
        draw_hangman(attempts)

        # Отображаем часть слова
        word_display = ' '.join(guessed_word)
        text = font.render(word_display, True, BLACK)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 + 50))

        # Отображаем дополнительные сообщения
        message = small_font.render(f"Гаданные буквы: {' '.join(guessed_letters)}", True, BLACK)
        screen.blit(message, (width // 2 - message.get_width() // 2, height // 2 + 150))

        if '_' not in guessed_word:
            win_message = font.render("Вы выиграли!", True, RED)
            screen.blit(win_message, (width // 2 - win_message.get_width() // 2, height // 2 - 50))
            pygame.display.flip()
            pygame.time.wait(2000)
            break

        if attempts <= 0:
            lose_message = font.render(f"Вы проиграли! Загаданное слово: {word}", True, RED)
            screen.blit(lose_message, (width // 2 - lose_message.get_width() // 2, height // 2 - 50))
            pygame.display.flip()
            pygame.time.wait(2000)
            break

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key).upper()
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter in word:
                            for i, char in enumerate(word):
                                if char == letter:
                                    guessed_word[i] = letter
                        else:
                            attempts -= 1

# Запуск игры
if __name__ == "__main__":
    main()