import pygame

from core.Camera import Camera
from core.Transition import Transition
from core.SoundManager import SoundManager
from entities.Player import Player
from entities.NPC import NPCManager
from hud.HUD import HUD
from items.Item import ItemManager
from maps.MapLoader import MapLoader
from maps.Grass import GrassManager
from maps.Pot import PotManager
from utils.JsonLoader import JsonLoader

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
        self.camera_rect = self.camera.create_camera(41)

        self.map = MapLoader(self.data_pos["cameras"][self.camera.current_id], self.screen, self.camera_rect)
        self.map.load_map()
        self.map.add_group()

        self.transition = Transition(self, self.screen, self.clock)

        self.npc_manager = NPCManager(self.map.spawn_objects, self.screen, self.map.group)

        self.data_switchmap = JsonLoader("../data/camera_switchmap.json").load_json()
        self.player = Player(311.75, 184, self.map, self.camera, self.data_switchmap, self.transition, self.screen, self.npc_manager.spawn_group)

        self.item_manager = ItemManager(self.player, self.screen, self.map.group)

        self.grass_manager = GrassManager(self.map.grass_objects, self.player, self.screen, self.map.group, self.item_manager)
        self.pot_manager = PotManager(self.map.pot_objects, self.player, self.screen, self.map.group, self.item_manager)

        self.sound_manager = SoundManager()
        self.sound_manager.play_music("../assets/sound/music/Plaine-Hyrule.ogg")

        self.hud = HUD(self.screen, self.player, SCALE)

        self.map.group.add(self.player, layer=100)


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

            self.grass_manager.update()
            self.pot_manager.update()
            self.item_manager.update()

            self.npc_manager.update(self.player)

            self.hud.draw()
            self.hud.hearth.update(self.player.life, self.player.max_life)
            self.hud.rubys.update(self.player.ruby)
            
            self.transition.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    Game().run()