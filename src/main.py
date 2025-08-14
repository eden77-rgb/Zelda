import pygame

from maps.MapLoader import MapLoader
from utils.JsonLoader import JsonLoader
from core.Camera import Camera
from core.Player import Player

pygame.init()

WIDTH = 256
HEIGHT = 224
SCALE = 2

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
        self.clock = pygame.time.Clock()

        self.data = JsonLoader("../data/camera_pos.json").load_json()
        self.camera = Camera(self.data, self.screen)
        self.camera_rect = self.camera.create_camera(21)

        self.map = MapLoader("../maps/main.tmx", self.screen, self.camera_rect)
        self.map.load_map()
        self.map.add_group()

        self.player = Player(2560, 4362, self.map.collision_objects)

        self.map.group.add(self.player)


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.player.update()

            self.camera.center(self.player)
            # self.camera.update()
            
            self.map.group.update()
            self.map.draw_map()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    Game().run()