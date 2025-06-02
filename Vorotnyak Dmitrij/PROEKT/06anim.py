import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)  # Полноэкранный режим

# Определяем цвета
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]  # Разные цвета

# Класс для шара
class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = random.choice(colors)
        self.speed_x = random.choice([-4, 4])
        self.speed_y = random.choice([-4, 4])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Проверка на столкновение с краями экрана
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.speed_x *= -1  # Изменяем направление по оси X
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.speed_y *= -1  # Изменяем направление по оси Y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Класс для квадрата
class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = random.choice(colors)
        self.speed_x = random.choice([-4, 4])
        self.speed_y = random.choice([-4, 4])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Проверка на столкновение с краями экрана
        if self.x <= 0 or self.x + self.size >= width:
            self.speed_x *= -1  # Изменяем направление по оси X
        if self.y <= 0 or self.y + self.size >= height:
            self.speed_y *= -1  # Изменяем направление по оси Y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# Класс для треугольника
class Triangle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = random.choice(colors)
        self.speed_x = random.choice([-4, 4])
        self.speed_y = random.choice([-4, 4])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Проверка на столкновение с краями экрана
        if self.x <= 0 or self.x + self.size >= width:
            self.speed_x *= -1  # Изменяем направление по оси X
        if self.y <= 0 or self.y + self.size >= height:
            self.speed_y *= -1  # Изменяем направление по оси Y

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [
            (self.x, self.y + self.size),
            (self.x + self.size / 2, self.y),
            (self.x + self.size, self.y + self.size),
        ])

# Создаем список фигур: 20 шаров, 20 квадратов и 20 треугольников
shapes = [Ball(random.randint(50, width - 50), random.randint(50, height - 50), random.randint(10, 40)) for _ in range(70)] + \
         [Square(random.randint(50, width - 50), random.randint(50, height - 50), random.randint(20, 80)) for _ in range(70)] + \
         [Triangle(random.randint(50, width - 50), random.randint(50, height - 50), random.randint(20, 60)) for _ in range(70)]

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()  # Выход из программы по нажатию ESC

    # Заливаем экран белым цветом
    screen.fill((255, 255, 255))

    # Обновляем и рисуем фигуры
    for shape in shapes:
        shape.move()
        shape.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение кадров
    pygame.time.Clock().tick(60)