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

        try:
            self.save_data = JsonLoader("../data/save.json").load_json()
            print("Partie chargée")

        except FileNotFoundError:
            print("Nouvelle partie")
            self.save_data = None

        
        if self.save_data:
            player_x = self.save_data["player"]["x"]
            player_y = self.save_data["player"]["y"]
            player_life = self.save_data["player"]["life"]
            player_max_life = self.save_data["player"]["max_life"]
            player_ruby = self.save_data["player"]["ruby"]

            camera_x = self.save_data["camera"]["x"]
            camera_y = self.save_data["camera"]["y"]
            camera_current_id = self.save_data["camera"]["current_id"]

        else:
            player_x = 311.75
            player_y = 184
            player_life = 3
            player_max_life = 3
            player_ruby = 0

            camera_x = 0
            camera_y = 0
            camera_current_id = 41

        self.data_pos = JsonLoader("../data/camera_pos.json").load_json()
        self.camera = Camera(self.data_pos, self.screen)
        self.camera.x = camera_x
        self.camera.y = camera_y
        self.camera_rect = self.camera.create_camera(camera_current_id)

        self.map = MapLoader(self.data_pos["cameras"][self.camera.current_id], self.screen, self.camera_rect)
        self.map.load_map()
        self.map.add_group()

        self.transition = Transition(self, self.screen, self.clock)

        self.npc_manager = NPCManager(self.map.spawn_objects, self.screen, self.map.group)

        self.data_switchmap = JsonLoader("../data/camera_switchmap.json").load_json()
        self.player = Player(player_x, player_y, self.map, self.camera, self.data_switchmap, self.transition, self.screen, self.npc_manager.spawn_group)
        self.player.life = player_life
        self.player.max_life = player_max_life
        self.player.ruby = player_ruby

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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        JsonLoader("../data/save.json").save_json(self.player, self.camera)
                    

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