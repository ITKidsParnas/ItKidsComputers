import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна (только для определения размеров)
WIDTH, HEIGHT = 800, 600

# Полноэкранный режим
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Можно получить текущие размеры экрана
WIDTH, HEIGHT = screen.get_size()

pygame.display.set_caption("Стань жирным")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Игрок
class Player:
    def __init__(self, name):
        self.size = 20
        self.position = [WIDTH // 2, HEIGHT // 2]
        self.name = name

    def grow(self):
        self.size += 1

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.position[0] -= 2
        if keys[pygame.K_RIGHT]:
            self.position[0] += 2
        if keys[pygame.K_UP]:
            self.position[1] -= 2
        if keys[pygame.K_DOWN]:
            self.position[1] += 2

        # Ограничение по границам экрана
        self.position[0] = max(self.size, min(WIDTH - self.size, self.position[0]))
        self.position[1] = max(self.size, min(HEIGHT - self.size, self.position[1]))

    def draw(self):
        pygame.draw.circle(screen, GREEN, (int(self.position[0]), int(self.position[1])), self.size)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.name, True, WHITE)
        screen.blit(text_surface,
                    (self.position[0] - text_surface.get_width() // 2,
                     self.position[1] - text_surface.get_height() // 2))

# Еда
class Food:
    def __init__(self):
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        self.size = 5
        # Случайный цвет для еды
        self.color = random.choice([RED, BLUE, YELLOW, PURPLE])

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (int(self.position[0]), int(self.position[1])), self.size)

# Меню для ввода ника
def menu():
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 -30 ,200 ,40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    
    font = pygame.font.Font(None ,36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active= not active
                else:
                    active= False
                color= color_active if active else color_inactive
            
            if event.type==pygame.KEYDOWN:
                if active:
                    if event.key==pygame.K_RETURN:
                        return text.strip() or "Игрок"
                    elif event.key==pygame.K_BACKSPACE:
                        text= text[:-1]
                    else:
                        text+= event.unicode

        screen.fill(WHITE)
        
        txt_surface= font.render(text ,True ,color)
        width= max(200 , txt_surface.get_width()+10)
        input_box.w= width
        
        screen.blit(txt_surface,(input_box.x+5 , input_box.y+5))
        pygame.draw.rect(screen,color,input_box ,2)

        # Отображение текста "Введите ник"
        title_surface= font.render("Введите ник:", True,(0 ,0 ,0))
        screen.blit(title_surface,(WIDTH //2 - title_surface.get_width()//2 , HEIGHT//2 - title_surface.get_height() -40))
        
        pygame.display.flip()

def main():
    player_name= menu()
    
    player= Player(player_name)
    food_items= [Food() for _ in range(10)]

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.move()

        # Проверка на сбор еды с использованием расстояния для точности столкновения
        for food in food_items[:]:
            dx= player.position[0]- food.position[0]
            dy= player.position[1]- food.position[1]
            distance= (dx**2 + dy**2)**0.5

            if distance< player.size + food.size:
                player.grow()
                food_items.remove(food)
                food_items.append(Food())

        # Отрисовка
        screen.fill(WHITE)

        player.draw()

        for food in food_items:
            food.draw()

        pygame.display.flip()

if __name__=="__main__":
    main()