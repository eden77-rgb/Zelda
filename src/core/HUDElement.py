import pygame

class HUDElement:
    def __init__(self, x, y, scale):
        self.x = x * scale
        self.y = y * scale
        self.scale = scale

        self.sprite_sheet = pygame.image.load("../assets/hud/HUD.png").convert_alpha()
        self.visible = True


    def set_position(self, x, y):
        self.x = x
        self.y = y

        
    def draw(self):
        pass


    def update(self):
        pass
