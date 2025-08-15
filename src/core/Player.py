import pygame

from core.Sword import Sword
from core.Animation import Animation

IDLE = (1, 3, 16, 24)

WALK_UP =  [
    (1, 111, 16, 24),
    (19, 111, 16, 24),
    (36, 110, 16, 25),
    (53, 109, 16, 26)
]

WALK_LEFT = [
    (1, 58, 17, 24),
    (20, 57, 17, 25),
    (38, 57, 16, 25),
    (55, 58, 17, 24)
]

WALK_DOWN = [
    (1, 3, 16, 24),
    (19, 3, 16, 24),
    (36, 2, 16, 25),
    (53, 1, 16, 26)
]

WALK_RIGHT = [
    (1, 58, 17, 24),
    (20, 57, 17, 25),
    (38, 57, 16, 25),
    (55, 58, 17, 24)
]


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, collision_layer):
        super().__init__()

        self.x = x
        self.y = y
        self.collision_layer = collision_layer

        self.sprite_sheet = pygame.image.load("../assets/sprites/Link.png")
        self.image = pygame.Surface((16, 24))
        self.rect = self.image.get_rect()

        self.sword = Sword(self)

        self.animations = {
            "up": Animation(self.sprite_sheet, WALK_UP, 0.10),
            "left": Animation(self.sprite_sheet, WALK_LEFT, 0.10, True),
            "down": Animation(self.sprite_sheet, WALK_DOWN, 0.10),
            "right": Animation(self.sprite_sheet, WALK_RIGHT, 0.10)
        }
        
        self.last_direction = "down"
        self.rect.topleft = (self.x, self.y)
    

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
        moving = False

        self.attack_input()

        if keys[pygame.K_z]:
            self.move(0, -1)
            
            self.last_direction = "up"
            moving = True

        if keys[pygame.K_q]:
            self.move(-1, 0)
            
            self.last_direction = "left"
            moving = True

        if keys[pygame.K_s]:
            self.move(0, 1)
            
            self.last_direction = "down"
            moving = True

        if keys[pygame.K_d]:
            self.move(1, 0)
            
            self.last_direction = "right"
            moving = True


        if moving:
            self.image = self.animations[self.last_direction].update()

        else:
            self.image = self.animations[self.last_direction].reset()


        print("X: ", self.x, "Y: ", self.y)
    

    def attack_input(self):
        keys = pygame.key.get_pressed()

        for group in self.groups():
            if keys[pygame.K_SPACE]:
                print("[ESPACE]: préssé")
                if self.sword not in group:
                    group.add(self.sword)

            else:
                if self.sword in group:
                    group.remove(self.sword)
    