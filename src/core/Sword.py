import pygame
from core.Animation import Animation

SWORD_UP = {
    "frames": [
        (62, 277, 16, 8),
        (45, 269, 16, 16),
        (10, 269, 8, 16),
        (19, 269, 8, 16),
        (45, 269, 16, 16),
        (19, 269, 8, 16)
    ],
    "position": [
        (5, 10),
        (20, 10),
        (20, 10),
        (20, 10),
        (20, 10),
        (20, 10)
    ]
}


class Sword(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        self.player = player
        self.sprite_sheet = pygame.image.load("../assets/sprites/Link.png")

        self.animations = {
            "up": Animation(self.sprite_sheet, SWORD_UP["frames"], 0.02),
            "left": Animation(self.sprite_sheet, SWORD_UP["frames"], 0.02),
            "down": Animation(self.sprite_sheet, SWORD_UP["frames"], 0.02),
            "right": Animation(self.sprite_sheet, SWORD_UP["frames"], 0.02)
        }

        self.sword_data = {
            "up": SWORD_UP,
            "left": SWORD_UP,
            "down": SWORD_UP,
            "right": SWORD_UP
        }

        self.current_direction = "down"
        self.current_animation = self.animations[self.current_direction]
        self.current_positions = self.sword_data[self.current_direction]["position"]

        self.image = self.current_animation.reset()
        self.rect = self.image.get_rect()


    def set_direction(self, direction):
        if direction in self.animations:
            self.current_direction = direction
            self.current_animation = self.animations[direction]
            self.current_positions = self.sword_data[direction]["position"]

            self.current_animation.frame_index = 0
            self.image = self.current_animation.reset()
    

    def update(self):
        new_image = self.current_animation.update(loop=False)
        if new_image:
            self.image = new_image
        
        frame_index = min(int(self.current_animation.frame_index), len(self.current_positions)-1)
        offset_x, offset_y = self.current_positions[frame_index]
        self.rect.topleft = (self.player.rect.x + offset_x, self.player.rect.y + offset_y)