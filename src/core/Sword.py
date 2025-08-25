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
        (9, 8),
        (6, -8),
        (-1, -10),
        (-5, -7),
        (-13, 0),
        (-1, -5)
    ],
    "flip": [
        False,
        True,
        False,
        True,
        True,
        False
    ],
    "rotation": [
        0,
        -90,
        0,
        0,
        0,
        0
    ],
    "layers": [
        6,
        6,
        6,
        6,
        6
    ]
}

SWORD_LEFT = {
    "frames": [
        (28, 269, 16, 16),
        (62, 277, 16, 8),
        (79, 277, 16, 8),
        (28, 269, 16, 16),
        (45, 269, 16, 16)
    ],
    "position": [
        (-8, -1),
        (-10, 7),
        (-12, 10),
        (-10, 10),
        (-7, 15)
    ],
    "flip": [
        True,
        True,
        True,
        True,
        True
    ],
    "rotation": [
        0,
        0,
        0,
        90,
        90
    ],
    "layers": [
        6,
        6,
        6,
        6,
        7
    ]
}

SWORD_DOWN = {
    "frames": [
        (79, 277, 16, 8),
        (28, 269, 16, 16),
        (62, 277, 16, 8),
        (10, 269, 8, 16),
        (28, 269, 16, 16),
        (45, 269, 16, 16)
    ],
    "position": [
        (-9, 10),
        (-5, 12),
        (6, 15),
        (8, 18),
        (8, 14),
        (13, 11)
    ],
    "flip": [
        True,
        True,
        True,
        False,
        True,
        True,        
    ],
    "rotation": [
        0,
        90,
        90,
        180,
        180,
        180
    ],
    "layers": [
        7,
        7,
        7,
        7,
        7,
        7
    ]
}

SWORD_RIGHT = {
    "frames": [
        (19, 269, 8, 16),
        (45, 269, 16, 16),
        (79, 277, 16, 8,),
        (19, 269, 8, 16),
        (45, 269, 16, 16)
    ],
    "position": [
        (11, -2),
        (12, -1),
        (19, 10),
        (15, 13),
        (7, 15)
    ],
    "flip": [
        False,
        False,
        False,
        False,
        False
    ],
    "rotation": [
        0,
        0,
        0,
        -90,
        -90
    ],
    "layers": [
        6,
        6,
        6,
        6,
        7
    ]
}


class Sword(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        self.player = player
        self.sprite_sheet = pygame.image.load("../assets/sprites/Link.png")

        self.animations = {
            "up": Animation(self.sprite_sheet, SWORD_UP["frames"], 0.20, flip_list=SWORD_UP["flip"], rotation_list=SWORD_UP["rotation"]),
            "left": Animation(self.sprite_sheet, SWORD_LEFT["frames"], 0.20, flip_list=SWORD_LEFT["flip"], rotation_list=SWORD_LEFT["rotation"]),
            "down": Animation(self.sprite_sheet, SWORD_DOWN["frames"], 0.20, flip_list=SWORD_DOWN["flip"], rotation_list=SWORD_DOWN["rotation"]),
            "right": Animation(self.sprite_sheet, SWORD_RIGHT["frames"], 0.20, flip_list=SWORD_RIGHT["flip"], rotation_list=SWORD_RIGHT["rotation"])
        }

        self.sword_data = {
            "up": SWORD_UP,
            "left": SWORD_LEFT,
            "down": SWORD_DOWN,
            "right": SWORD_RIGHT
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

    def get_current_layer(self):
        frame_index = min(int(self.current_animation.frame_index), len(self.current_positions) - 1)
        layers = self.sword_data[self.current_direction]["layers"]

        return layers[frame_index] if frame_index < len(layers) else 0