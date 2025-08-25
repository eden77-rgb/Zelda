import pygame
from maps.ObjectManager import DestructibleObject

SLASHING_BUSH = [
    (8, 17, 29, 43),
    (38, 17, 29, 43),
    (68, 17, 29, 43),
    (98, 17, 29, 43),
    (128, 17, 29, 43),
    (158, 17, 29, 43),
    (188, 17, 29, 43),
    (218, 17, 29, 43)
]

class Grass(DestructibleObject):
    def __init__(self, player, grass_rect):
        super().__init__(player)
        self.grass_rect = grass_rect


    def on_collision(self, sprite_sheet, animation, rect):
        if self.player.sword.rect.colliderect(self.grass_rect) and not self.destroyed:
            self.destroy(sprite_sheet, animation, rect)


class GrassManager():
    def __init__(self, grass_objects, player, screen, pyscroll_group):
        self.grass_objects = grass_objects
        self.player = player
        self.screen = screen
        self.pyscroll_group = pyscroll_group

        self.grass_group = []
        for rect in self.grass_objects:
            self.grass_group.append(Grass(self.player, rect))

        self.sprite_sheet = pygame.image.load("../assets/sprites/Destructible-Object.png")
        self.image_destroyed = pygame.Surface((16, 16), pygame.SRCALPHA)
        self.image_destroyed.blit(self.sprite_sheet, (0, 0), pygame.Rect(1, 1, 16, 16))

        self.sfx_sprite_sheet = pygame.image.load("../assets/sfx/Bush-Pot-SFX.png")


    def update(self):
        for grass in self.grass_group:
            if not grass.destroyed:
                grass.on_collision(self.sfx_sprite_sheet, SLASHING_BUSH, grass.grass_rect)

            if grass.destroyed and not hasattr(grass, 'static_sprite_added'):
                    destroyed_sprite = pygame.sprite.Sprite()
                    destroyed_sprite.image = self.image_destroyed
                    
                    destroyed_sprite.rect = pygame.Rect(
                        grass.grass_rect.x, 
                        grass.grass_rect.y, 
                        self.image_destroyed.get_width(), 
                        self.image_destroyed.get_height()
                    )
                    
                    self.pyscroll_group.add(destroyed_sprite, layer=4)
                    grass.static_sprite_added = True

            if grass.destroyed:
                grass.update(self.pyscroll_group, layer=5)