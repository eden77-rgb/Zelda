import pygame
import pytmx
import pyscroll

class MapLoader:
    def __init__(self, data_pos, screen, camera):
        self.data_pos = data_pos["map"]
        self.screen = screen
        self.camera_rect = camera

        self.x = 0
        self.y = 0
        self.zoom = data_pos["zoom"]

    
    def load_map(self):
        self.tmx_data = pytmx.util_pygame.load_pygame(self.data_pos)
        self.map_data = pyscroll.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(self.map_data, self.screen.get_size(), clamp_camera=False)
        self.map_layer.zoom = round(self.zoom, 1)

        self.collision_objects = self.get_collision_objects()
        self.switchmap_objects = self.get_switchmap_objects()
        self.grass_objects = self.get_grass_objects()
        self.pot_objects = self.get_pot_objects()


    def add_group(self):
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer)


    def draw_map(self):
        self.map_layer.zoom = round(self.zoom, 1)
        self.map_layer.center(self.camera_rect.center)
        self.group.draw(self.screen)


    def get_collision_objects(self):
        collision_objects = []

        for layer  in self.tmx_data.layers:
            if hasattr(layer, "name") and layer.name == "collision":
                for obj in layer:

                    rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    collision_objects.append(rect)

        return collision_objects
    

    def get_switchmap_objects(self):
        switchmap_objects = {}

        for layer in self.tmx_data.layers:
            if layer.name == "switchmap":
                for obj in layer:

                    rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    switchmap_objects[obj.type] = rect

        return switchmap_objects


    def get_grass_objects(self):
        grass_objects = []

        for layer in self.tmx_data.layers:
            if layer.name == "herbes":
                for obj in layer:

                    rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    grass_objects.append(rect)

        return grass_objects
    

    def get_pot_objects(self):
        pot_objects = []

        for layer in self.tmx_data.layers:
            if layer.name == "pot":
                for obj in layer:

                    rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    pot_objects.append(rect)

        return pot_objects
