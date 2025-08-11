import pygame
import pytmx
import pyscroll
pygame.init()

WIDTH = 256
HEIGHT = 224
SCALE = 2

screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))

tmx_data = pytmx.util_pygame.load_pygame("../maps/main.tmx")
map_data = pyscroll.TiledMapData(tmx_data)
map_layer = pyscroll.BufferedRenderer(map_data, screen.get_size(), clamp_camera=False)

group = pyscroll.PyscrollGroup(map_layer=map_layer)
group.draw(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
