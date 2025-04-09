import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 800))
r = pygame.Rect(50, 50, 200, 200)
pygame.draw.rect(screen, (244,234,255), r, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()











