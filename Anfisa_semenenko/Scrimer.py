import pygame
import sys

pygame.init()

# Запускаем окно в полноэкранном режиме
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Скример")

# Получаем текущий размер экрана
screen_width, screen_height = screen.get_size()

# Загружаем изображение
scream_image = pygame.image.load("screamer.jpg")

# Масштабируем изображение под размер экрана
scream_image = pygame.transform.scale(scream_image, (screen_width, screen_height))

# Загружаем и проигрываем звук
scream_sound = pygame.mixer.Sound("scream.wav")

# Отображаем изображение и проигрываем звук
screen.blit(scream_image, (0, 0))
pygame.display.flip()
scream_sound.play()

# Ждём немного (например, 3 секунды)
pygame.time.wait(1000)

pygame.quit()
sys.exit()