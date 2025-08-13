import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, collision_layer):
        super().__init__()

        self.x = x
        self.y = y
        self.collision_layer = collision_layer

        self.sprite_sheet = pygame.image.load("../assets/sprites/Link.png")
        self.image = self.get_image(1, 3)
        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x, self.y)


    def get_image(self, x, y):
        image = pygame.Surface((16, 24))
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 24))

        image.set_colorkey(image.get_at((0,0)))
        return image
    

    def check_collision(self, dx, dy):
        future_x = self.x + dx
        future_y = self.y + dy
        future_rect = pygame.Rect(future_x, future_y, self.rect.width, self.rect.height)

        for obj in self.collision_layer:
            if future_rect.colliderect(obj):
                return False
            
        return True


    def move(self, dx, dy):
        if self.check_collision(dx, dy):
            self.x += dx
            self.y += dy
            self.rect.topleft = (self.x, self.y)


    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            self.move(0, -1)

        if keys[pygame.K_q]:
            self.move(-1, 0)

        if keys[pygame.K_s]:
            self.move(0, 1)

        if keys[pygame.K_d]:
            self.move(1, 0)

        print("X: ", self.x, "Y: ", self.y)
    