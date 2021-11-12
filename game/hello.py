import pygame
import sys

pygame.init()
size = width, height = 320,240
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


