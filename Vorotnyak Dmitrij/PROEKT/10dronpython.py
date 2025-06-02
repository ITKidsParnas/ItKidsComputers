import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
DRONE_SPEED = 5
WHEAT_COUNT = 10
CARROT_COUNT = 10
TREE_COUNT = 10

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 128, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Управление дроном")

# Создаем поверхности для объектов
drone_image = pygame.Surface((50, 50))
drone_image.fill(BLUE)

wheat_image = pygame.Surface((20, 20))
wheat_image.fill(YELLOW)

carrot_image = pygame.Surface((20, 20))
carrot_image.fill(ORANGE)

tree_image = pygame.Surface((30, 30))
tree_image.fill(GREEN)

# Функция для генерации случайных позиций
def generate_positions(count):
    return [(random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20)) for _ in range(count)]

# Изначальные позиции пшеницы — сразу заполняем полностью
wheat_positions = generate_positions(WHEAT_COUNT)
carrot_positions = []
tree_positions = []

# Счетчики собранного урожая/объектов
wheat_collected=0
carrots_collected=0
trees_collected=0

# Таймеры спавна для остальных объектов
last_carrot_spawn_time=pygame.time.get_ticks()
last_tree_spawn_time=pygame.time.get_ticks()

clock=pygame.time.Clock()

# Позиция дрона
drone_rect=drone_image.get_rect(center=(WIDTH//2 ,HEIGHT//2 ))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление дроном стрелками
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        drone_rect.x -= DRONE_SPEED
    if keys[pygame.K_RIGHT]:
        drone_rect.x += DRONE_SPEED
    if keys[pygame.K_UP]:
        drone_rect.y -= DRONE_SPEED
    if keys[pygame.K_DOWN]:
        drone_rect.y += DRONE_SPEED

    # Ограничение по границам экрана
    drone_rect.clamp_ip(screen.get_rect())

    # Проверка столкновений с пшеницей
    for pos in wheat_positions[:]:
        wheat_rect=wheat_image.get_rect(topleft=pos)
        if drone_rect.colliderect(wheat_rect):
            wheat_positions.remove(pos)
            wheat_collected+=1

    # Проверка столкновений с морковками
    for pos in carrot_positions[:]:
        carrot_rect=carrot_image.get_rect(topleft=pos)
        if drone_rect.colliderect(carrot_rect):
            carrot_positions.remove(pos)
            carrots_collected+=1

    # Проверка столкновений с деревьями
    for pos in tree_positions[:]:
        tree_rect=tree_image.get_rect(topleft=pos)
        if drone_rect.colliderect(tree_rect):
            tree_positions.remove(pos)
            trees_collected+=1

    current_time=pygame.time.get_ticks()

    # Условие появления морковок: после сбора >=10 пшениц
    if wheat_collected >=10:
        # Спавн морковок через интервал времени и если их меньше чем CARROT_COUNT
        if current_time - last_carrot_spawn_time >3000:
            needed_carrots= CARROT_COUNT - len(carrot_positions)
            if needed_carrots >0:
                new_pos_list= generate_positions(needed_carrots)
                carrot_positions.extend(new_pos_list)
            last_carrot_spawn_time= current_time

        # Условие появления деревьев: после сбора >=10 морковок
        if carrots_collected >=10:
            # Спавн деревьев через интервал времени и если их меньше чем TREE_COUNT
            if current_time - last_tree_spawn_time >5000:
                needed_trees= TREE_COUNT - len(tree_positions)
                if needed_trees >0:
                    new_pos_list= generate_positions(needed_trees)
                    tree_positions.extend(new_pos_list)
                last_tree_spawn_time= current_time

    # Отрисовка всего на экране
    screen.fill(WHITE)

    # Рисуем дрона
    screen.blit(drone_image, drone_rect)

    # Рисуем объекты на сцене
    for pos in wheat_positions:
        screen.blit(wheat_image, pos)

    for pos in carrot_positions:
        screen.blit(carrot_image, pos)

    for pos in tree_positions:
        screen.blit(tree_image, pos)

    # Текст счетчиков собранного урожая/объектов
    font=pygame.font.Font(None ,36 )
    
    text_wheat= font.render(f'Собрано пшеницы: {wheat_collected}', True , (0 ,0 ,0))
    text_carrots= font.render(f'Собрано морковки: {carrots_collected}', True , (0 ,0 ,0))
    text_trees= font.render(f'Собрано деревьев: {trees_collected}', True , (0 ,0 ,0))

    screen.blit(text_wheat,(10 ,10))
    screen.blit(text_carrots,(10 ,40))
    screen.blit(text_trees,(10 ,70))

    
    pygame.display.flip()
    
    clock.tick(60)