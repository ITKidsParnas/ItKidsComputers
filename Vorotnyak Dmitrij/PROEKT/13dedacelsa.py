import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dead Cells")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Параметры игрока
player_pos = [100, 500]
player_size = 50
player_speed = 5
player_jump_speed = 10
gravity = 0.5
is_jumping = False
jump_count = player_jump_speed

# Параметры врагов
enemy_size = 50
enemies = [[random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT - enemy_size)] for _ in range(5)]
enemy_speed = 2

# Параметры платформ
platforms = [[0, 550, WIDTH, 50], [300, 400, 200, 20], [600, 300, 200, 20]]  # x, y, width, height

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление персонажем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Влево
        player_pos[0] -= player_speed
    if keys[pygame.K_d]:  # Вправо
        player_pos[0] += player_speed
    if not is_jumping:
        if keys[pygame.K_w]:  # Прыжок
            is_jumping = True
    else:
        if jump_count >= -player_jump_speed:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_pos[1] -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = player_jump_speed

    # Гравитация
    if not is_jumping:
        player_pos[1] += gravity

    # Проверка коллизий с платформами
    for platform in platforms:
        if (platform[0] < player_pos[0] < platform[0] + platform[2] or platform[0] < player_pos[0] + player_size < platform[0] + platform[2]) and (platform[1] < player_pos[1] + player_size < platform[1] + platform[3]):
                player_pos[1] = platform[1] - player_size
                is_jumping = False
                jump_count = player_jump_speed

    # Отрисовка
    screen.fill(BLACK)  # Очистка экрана
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))  # Отрисовка персонажа

    # Отрисовка врагов
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))  # Отрисовка врага

    # Отрисовка платформ
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, (platform[0], platform[1], platform[2], platform[3]))  # Отрисовка платформы

    pygame.display.flip()  # Обновление экрана

    # Ограничение кадров в секунду
    pygame.time.Clock().tick(30)