import pygame

from maps.MapLoader import MapLoader
from utils.JsonLoader import JsonLoader
from core.Camera import Camera
from core.Player import Player
from core.Transition import Transition
from core.HUD import HUD

pygame.init()

WIDTH = 256
HEIGHT = 224
SCALE = 2

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
        self.clock = pygame.time.Clock()

        self.data_pos = JsonLoader("../data/camera_pos.json").load_json()
        self.camera = Camera(self.data_pos, self.screen)
        self.camera_rect = self.camera.create_camera(21)

        self.map = MapLoader("../maps/main.tmx", self.screen, self.camera_rect)
        self.map.load_map()
        self.map.add_group()

        self.transition = Transition(self.screen, self.clock)

        self.data_switchmap = JsonLoader("../data/camera_switchmap.json").load_json()
        self.player = Player(2560, 4362, self.map, self.camera, self.data_switchmap, self.transition, self.screen)

        self.hud = HUD(self.screen, self.player, SCALE)

        self.map.group.add(self.player, layer=1)


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            self.transition.update()

            if not self.transition.is_active():
                self.camera.center(self.player)
                self.map.group.update()
                
            elif self.transition.transition_state.name == "CHANGING":
                self.camera.center(self.player)
            
            self.map.draw_map()
            self.hud.draw()
            self.transition.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    Game().run()