import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Платформер с подвижной камерой")

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.velocity_y = 0
        self.on_ground = False

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Проверка на столкновение с землей
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.on_ground = True
            self.velocity_y = 0
        else:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.velocity_y = -15

# Класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

# Создание группы спрайтов
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Создание игрока
player = Player()
all_sprites.add(player)

# Создание платформ
for i in range(1300):
    width = random.randint(100, 300)
    height = 20
    x = random.randint(0, 100000 - width)
    y = random.randint(100, 500)
    platform = Platform(x, y, width, height)
    all_sprites.add(platform)
    platforms.add(platform)

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

# Параметры камеры
camera_x, camera_y = 0, 0
camera_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    if player.rect.y == 550:
         running = False   

    # Управление движением
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5
    if keys[pygame.K_SPACE]:
        player.rect.y -= 15

    # Проверка столкновений с платформами
    player.on_ground = False
    for platform in platforms:
        if player.rect.colliderect(platform.rect) and player.velocity_y >= 0:
            player.rect.bottom = platform.rect.top
            player.on_ground = True
            player.velocity_y = 0

    # Обновление спрайтов
    all_sprites.update()

    # Камера следует за игроком
    camera_x = player.rect.centerx - WIDTH // 2
    camera_y = player.rect.centery - HEIGHT // 2

    # Ограничиваем камеру по границам
    camera_x = max(0, min(camera_x, 10000000000000 - WIDTH))
    camera_y = max(0, min(camera_y, 600 - HEIGHT))

    # Отрисовка
    screen.fill(WHITE)

    # Сдвигаем все спрайты в соответствии с позицией камеры
    for sprite in all_sprites:
        screen.blit(sprite.image, (sprite.rect.x - camera_x, sprite.rect.y - camera_y))

    pygame.display.flip()

    # Ограничение FPS
    clock.tick(FPS)

pygame.quit()
