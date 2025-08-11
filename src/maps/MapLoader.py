import pytmx
import pyscroll

class MapLoader:
    def __init__(self, path, screen):
        self.path = path
        self.screen = screen

        self.zoom = 2

    
    def load_map(self):
        self.tmx_data = pytmx.util_pygame.load_pygame(self.path)
        self.map_data = pyscroll.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(self.map_data, self.screen.get_size(), clamp_camera=False)
        self.map_layer.zoom = round(self.zoom, 1)


    def add_group(self):
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer)


    def draw_map(self):
        self.map_layer.zoom = round(self.zoom, 1)
        self.group.draw(self.screen)