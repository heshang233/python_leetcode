import pygame
import sys

pygame.init()
size = width, height = 640,480
screen = pygame.display.set_mode(size)
color = (0,0,0)
clock = pygame.time.Clock()

while True:
    
    clock.tick(30)

    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, color, (0,0,width,height))
    pygame.display.flip()


