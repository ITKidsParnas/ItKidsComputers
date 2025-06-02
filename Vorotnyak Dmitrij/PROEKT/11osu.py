import pygame
import random
import sys

# Инициализация Pygame
pygame.init()
pygame.mixer.music.load('hit_sound.wav')

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Test")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Основные параметры
target_radius = 30
score = 0
misses = 0  # Количество промахов
time_limit = 30  # Время игры в секундах
font = pygame.font.Font(None, 36)

# Загрузка звуков
hit_sound = pygame.mixer.Sound("hit_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.mp3")

# Функция для создания новой цели
def new_target():
    return (random.randint(target_radius, WIDTH - target_radius), random.randint(target_radius, HEIGHT - target_radius))

target_pos = new_target()
start_ticks = pygame.time.get_ticks()  # Начальное время

# Основной игровой цикл
while True:
    # Вычисляем оставшееся время
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Время в секундах
    if seconds > time_limit:
        # Игра окончена
        screen.fill(WHITE)
        accuracy = (score / (score + misses) * 100) if (score + misses) > 0 else 0  # Вычисляем точность
        result_text = font.render(f'Game Over! Your Score: {score}', True, BLACK)
        accuracy_text = font.render(f'Accuracy: {accuracy:.2f}%', True, BLACK)
        screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 2 - 20))
        screen.blit(accuracy_text, (WIDTH // 2 - accuracy_text.get_width() // 2, HEIGHT // 2 + 20))
        pygame.display.flip()
        pygame.time.delay(3000)  # Задержка перед выходом
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (target_pos[0] - target_radius < mouse_pos[0] < target_pos[0] + target_radius) and \
               (target_pos[1] - target_radius < mouse_pos[1] < target_pos[1] + target_radius):
                score += 1  # Увеличиваем счет при попадании
                hit_sound.play()  # Воспроизводим звук попадания
                target_pos = new_target()
            else:
                misses += 1  # Увеличиваем счет промахов
                miss_sound.play()  # Воспроизводим звук промаха

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, target_pos, target_radius)
    
    # Отображение счета, оставшегося времени и точности
    score_text = font.render(f'Score: {score}', True, BLACK)
    time_text = font.render(f'Time Left: {time_limit - int(seconds)}', True, BLACK)
    accuracy = (score / (score + misses) * 100) if (score + misses) > 0 else 0  # Вычисляем точность
    accuracy_text = font.render(f'Accuracy: {accuracy:.2f}%', True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))
    screen.blit(accuracy_text, (10, 90))

    pygame.display.flip()
    pygame.time.delay(100)
