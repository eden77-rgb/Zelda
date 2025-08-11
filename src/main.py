import pygame
pygame.init()

WIDTH = 256
HEIGHT = 224
SCALE = 2

screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
