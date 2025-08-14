import pygame

class Sword(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        self.player = player

        self.sprite_sheet = pygame.image.load("../assets/sprites/Link.png")
        self.image = self.get_image()
        self.rect = self.image.get_rect()


    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey(image.get_at((0,0)))
        return image
    

    def update(self):
        self.rect.x = self.player.rect.x + 20
        self.rect.y = self.player.rect.y + 10