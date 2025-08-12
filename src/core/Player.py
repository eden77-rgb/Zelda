import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.sprite_sheet = pygame.image.load("../assets/sprites/Link.png")
        
        self.image = self.get_image(1, 3)
        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x, self.y)


    def get_image(self, x, y):
        image = pygame.Surface((16, 24))
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 24))

        image.set_colorkey(image.get_at((0,0)))
        return image
    

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            self.y -= 1

        if keys[pygame.K_q]:
            self.x -= 1

        if keys[pygame.K_s]:
            self.y += 1

        if keys[pygame.K_d]:
            self.x += 1

        print("X: ", self.x, "Y: ", self.y)
        self.rect.topleft = (self.x, self.y)
    