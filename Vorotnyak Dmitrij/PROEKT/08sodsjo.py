import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Платформер с монстрами и оружием')

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Загружаем изображения
player_image = pygame.image.load('gratis-png-terraria-super-mario-bros-super-mario-world-sprite-videojuego-sprite.png')  # Замените на путь к вашему изображению
player_image = pygame.transform.scale(player_image, (50, 50))

teleport_image = pygame.image.load('5nDSuce.png')  # Замените на путь к вашему изображению
teleport_image = pygame.transform.scale(teleport_image, (50, 50))

monster_image = pygame.image.load('png-transparent-pixel-alien-illustration-emoji-alien-iphone-monster-space-invaders-purple-violet-text-thumbnail.png')  # Замените на путь к вашему изображению
monster_image = pygame.transform.scale(monster_image, (50, 50))

bullet_image = pygame.image.load('png-klev-club-puen-p-pikselnaya-pulya-png-16.png')  # Замените на путь к вашему изображению
bullet_image = pygame.transform.scale(bullet_image, (30, 15))  # Увеличиваем размер пули в три раза

# Параметры игрока
player_pos = [100, HEIGHT - 70]
player_velocity = 5
is_jumping = False
jump_count = 10

# Время между выстрелами
last_shot_time = 0
shot_delay = 1000  # 1 секунда в миллисекундах

# Получение платформ (все платформы твердые)
def get_platforms():
    return [
        pygame.Rect(0, HEIGHT - 20, WIDTH, 20),  # Земля
        pygame.Rect(200, HEIGHT - 150, 200, 20),  # Платформа 1
        pygame.Rect(500, HEIGHT - 300, 200, 20),  # Платформа 2
        pygame.Rect(350, HEIGHT - 450, 200, 20),  # Платформа 3
    ]

# Проверка платформы
def check_platform_collision(player_rect, platforms):
    player_rect.y += 1  # Проверяем непосредственно под игроком
    for platform in platforms:
        if player_rect.colliderect(platform):
            return platform
    return None

# Класс для пуль
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 15)  # Новый размер пули
        self.velocity = 10

    def move(self):
        self.rect.x += self.velocity

# Класс для монстров
class Monster:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.velocity = random.choice([-2, 2])  # Случайное движение влево или вправо

    def move(self):
        self.rect.x += self.velocity
        if self.rect.left <= 0 or self.rect.right >= WIDTH:  # Столкновение со стенами
            self.velocity *= -1

# Проверка столкновения
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Списки пуль и монстров
bullets = []
monsters = [Monster(600, HEIGHT - 70), Monster(300, HEIGHT - 70)]  # Пример создания двух монстров

# Основной цикл игры
running = True
while running:
    pygame.time.delay(30)  # Задержка для управления FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Движение игрока
    if keys[pygame.K_a] and player_pos[0] > player_velocity:  # Влево
        player_pos[0] -= player_velocity
    if keys[pygame.K_d] and player_pos[0] < WIDTH - 50 - player_velocity:  # Вправо
        player_pos[0] += player_velocity

    # Прыжок
    if not is_jumping:
        if keys[pygame.K_w]:  # Прыжок
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1 if jump_count > 0 else -1
            player_pos[1] -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Проверяем столкновение игрока с платформами
    player_rect = pygame.Rect(player_pos[0], player_pos[1], 50, 50)
    platforms = get_platforms()
    platform_collision = check_platform_collision(player_rect, platforms)

    if platform_collision:
        # Если игрок падает, устанавливаем его сверху платформы
        if player_pos[1] + 50 <= platform_collision.top:  # player_height = 50
            player_pos[1] = platform_collision.top - 50
            is_jumping = False
            jump_count = 10

    # Добавляем стрельбу
    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and len(bullets) == 0 and (current_time - last_shot_time) > shot_delay:
        bullets.append(Bullet(player_pos[0] + 20, player_pos[1] + 20))  # Пуля появляется из середины игрока
        last_shot_time = current_time  # Запоминаем время последнего выстрела

    # Движение пуль
    for bullet in bullets[:]:
        bullet.move()
        if bullet.rect.x > WIDTH:  # Удаляем пулю, если она вышла за границы экрана
            bullets.remove(bullet)

    # Движение монстров
    for monster in monsters:
        monster.move()

    # Проверка столкновений между игроком и монстрами
    for monster in monsters:
        if check_collision(player_rect, monster.rect):
            print("Вы погибли!")  # Логика смерти игрока
            running = False  # Завершаем игру при столкновении

    # Проверка столкновений между пулями и монстрами
    for bullet in bullets[:]:
        for monster in monsters[:]:
            if check_collision(bullet.rect, monster.rect):
                bullets.remove(bullet)  # Удаляем пулю
                monsters.remove(monster)  # Удаляем монстра
                break  # Установить break, чтобы избежать ошибок во время итераций

    # Отрисовка
    screen.fill(BLACK)  # Очистка экрана

    # Рисуем платформы
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    # Рисуем игрока
    screen.blit(player_image, (player_pos[0], player_pos[1]))

    # Рисуем телепорт
    screen.blit(teleport_image, (100, 100))  # Пример позиции

    # Рисуем монстров
    for monster in monsters:
        screen.blit(monster_image, (monster.rect.x, monster.rect.y))

    # Рисуем пули
    for bullet in bullets:
        screen.blit(bullet_image, (bullet.rect.x, bullet.rect.y))

    pygame.display.flip()  # Обновляем экран

# Выход из Pygame
pygame.quit()
sys.exit()