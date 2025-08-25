import pygame
from core.Animation import Animation

class DestructibleObject:
    def __init__(self, player):
        self.player = player
        self.destroyed = False

        self.animation = None
        self.animation_sprite = None
        self.animation_finished = False


    def destroy(self, sprite_sheet, animation, rect):
        self.destroyed = True

        self.animation = Animation(sprite_sheet, animation, colorkey="#ff80ff")
        self.animation_sprite = pygame.sprite.Sprite()

        animation_width = animation[0][2]
        animation_height = animation[0][3]

        self.animation_sprite.rect = pygame.Rect(
            rect.x + (rect.width - animation_width) // 2,
            rect.y + (rect.height - animation_height) // 2,
            animation_width,
            animation_height
        )

    
    def update(self, pyscroll_group, layer=5):
        if self.destroyed and self.animation and not self.animation_finished:
            self.animation.update(False)
            
            self.animation_sprite.image = self.animation.update(False)
            
            if self.animation_sprite not in pyscroll_group:
                pyscroll_group.add(self.animation_sprite, layer=layer)
            
            if self.animation.is_finished():
                self.animation_finished = True
                pyscroll_group.remove(self.animation_sprite)
