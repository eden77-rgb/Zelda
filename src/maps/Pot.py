import pygame
from maps.ObjectManager import DestructibleObject

SLASHING_POT = [
    (8, 83, 30, 28),
    (39, 83, 30, 28),
    (70, 83, 30, 28),
    (101, 83, 30, 28),
    (132, 83, 30, 28),
    (163, 83, 30, 28),
    (194, 83, 30, 28),
    (225, 83, 30, 28)
]

class Pot(DestructibleObject):
    def __init__(self, player, pot_rect):
        super().__init__(player)
        self.pot_rect = pot_rect


    def on_collision(self, sprite_sheet, animation, rect, item_manager):
        if self.player.sword.rect.colliderect(self.pot_rect) and not self.destroyed:
            self.destroy(sprite_sheet, animation, rect, item_manager)


class PotManager():
    def __init__(self, pot_objects, player, screen, pyscroll_group, item_manager):
        self.pot_objects = pot_objects
        self.player = player
        self.screen = screen
        self.pyscroll_group = pyscroll_group
        self.item_manager = item_manager

        self.pot_group = []
        for rect in self.pot_objects:
            self.pot_group.append(Pot(self.player, rect))

        sprite_sheet = pygame.image.load("../assets/sprites/Destructible-Object.png")
        self.image_destroyed = pygame.Surface((16, 16), pygame.SRCALPHA)
        self.image_destroyed.blit(sprite_sheet, (0, 0), pygame.Rect(69, 1, 16, 16))

        self.sfx_sprite_sheet = pygame.image.load("../assets/sfx/Bush-Pot-SFX.png")


    def update(self):
        for pot in self.pot_group:
            if not pot.destroyed:
                pot.on_collision(self.sfx_sprite_sheet, SLASHING_POT, pot.pot_rect, self.item_manager)

            if pot.destroyed and not hasattr(pot, 'static_sprite_added'):
                    destroyed_sprite = pygame.sprite.Sprite()
                    destroyed_sprite.image = self.image_destroyed
                    
                    destroyed_sprite.rect = pygame.Rect(
                        pot.pot_rect.x, 
                        pot.pot_rect.y, 
                        self.image_destroyed.get_width(), 
                        self.image_destroyed.get_height()
                    )
                    
                    self.pyscroll_group.add(destroyed_sprite, layer=7)
                    pot.static_sprite_added = True

            if pot.destroyed:
                pot.update(self.pyscroll_group, layer=8)