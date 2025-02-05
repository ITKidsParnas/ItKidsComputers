import pygame
import random

# Настройки игры
WIDTH, HEIGHT = 800, 600
FPS = 30
HAMSTER_SIZE = 50
BULLET_SIZE = 10

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Классы игры
class Hamster:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, HAMSTER_SIZE, HAMSTER_SIZE)
        self.color = color
        self.health = 100

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # Удерживаем хамстера в границах экрана
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - HAMSTER_SIZE:
            self.rect.x = WIDTH - HAMSTER_SIZE
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT - HAMSTER_SIZE:
            self.rect.y = HEIGHT - HAMSTER_SIZE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Главная функция игры
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    hamster1 = Hamster(100, 100, RED)
    hamster2 = Hamster(600, 100, GREEN)
    bullets = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            hamster1.move(-5, 0)
        if keys[pygame.K_d]:
            hamster1.move(5, 0)
        if keys[pygame.K_w]:
            hamster1.move(0, -5)
        if keys[pygame.K_s]:
            hamster1.move(0, 5)
        if keys[pygame.K_SPACE]:
            bullets.append([hamster1.rect.centerx, hamster1.rect.centery])

        if keys[pygame.K_LEFT]:
            hamster2.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            hamster2.move(5, 0)
        if keys[pygame.K_UP]:
            hamster2.move(0, -5)
        if keys[pygame.K_DOWN]:
            hamster2.move(0, 5)
        if keys[pygame.K_RETURN]:
            bullets.append([hamster2.rect.centerx, hamster2.rect.centery])

        screen.fill(WHITE)

        for bullet in bullets:
            bullet[1] -= 10  # bullets move upward
            pygame.draw.rect(screen, (0, 0, 0), (bullet[0], bullet[1], BULLET_SIZE, BULLET_SIZE))
            if bullet[1] < 0:
                bullets.remove(bullet)

        hamster1.draw(screen)
        hamster2.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()