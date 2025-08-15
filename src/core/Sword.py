import pygame

SWORD_UP = {
    "frames": [
        (1, 269, 8, 16),
        (10, 269, 8, 16),
        (19, 269, 8, 16),
        (28, 269, 16, 16),
        (45, 269, 16, 16),
        (62, 277, 16, 8),
        (79, 277, 16, 8)
    ],
    "position": [
        (20, 10),
        (20, 10),
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
        self.image = self.get_image(*SWORD_UP["frames"][0])
        self.rect = self.image.get_rect()


    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey(image.get_at((0,0)))
        return image
    

    def update(self):
        self.rect.x = self.player.rect.topleft[0] + SWORD_UP["position"][0][0]
        self.rect.y = self.player.rect.topleft[1] + SWORD_UP["position"][0][1]