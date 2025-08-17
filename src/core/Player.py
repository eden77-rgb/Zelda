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


ATTACK_UP = [
    (1, 141, 16, 24),
    (18, 140, 16, 25),
    (52, 136, 16, 29),
    (69, 139, 16, 26),
    (86, 141, 16, 24),
    (104, 141, 16, 24)
]

ATTACK_LEFT = [
    (19, 85, 17, 23),
    (37, 86, 19, 22),
    (57, 86, 23, 22),
    (81, 86, 19, 22),
    (101, 85, 16, 23)
]

ATTACK_DOWN = [
    (1, 32, 16, 24),
    (18, 33, 16, 23),
    (35, 34, 16, 22),
    (52, 37, 16, 19),
    (69, 34, 16, 22),
    (86, 33, 16, 23)
]

ATTACK_RIGHT = [
    (1, 85, 17, 23),
    (19, 85, 17, 23),
    (57, 86, 23, 22),
    (81, 86, 19, 22),
    (101, 85, 16, 23)
]


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, map, camera, data_switchmap):
        super().__init__()

        self.x = x
        self.y = y
        self.map = map
        self.camera = camera
        self.data_switchmap = data_switchmap

        self.sprite_sheet = pygame.image.load("../assets/sprites/Link.png")
        self.image = pygame.Surface((16, 24))
        self.rect = self.image.get_rect()

        self.animations = {
            "up": Animation(self.sprite_sheet, WALK_UP, 0.10),
            "left": Animation(self.sprite_sheet, WALK_LEFT, 0.10, True),
            "down": Animation(self.sprite_sheet, WALK_DOWN, 0.10),
            "right": Animation(self.sprite_sheet, WALK_RIGHT, 0.10),

            "attack_up": Animation(self.sprite_sheet, ATTACK_UP, 0.20), # 0.10
            "attack_left": Animation(self.sprite_sheet, ATTACK_LEFT, 0.20, True),
            "attack_down": Animation(self.sprite_sheet, ATTACK_DOWN, 0.20),
            "attack_right": Animation(self.sprite_sheet, ATTACK_RIGHT, 0.20)
        }
        
        self.last_direction = "down"
        self.current_animation = self.last_direction

        self.is_attacking = False
        self.time = 0
        self.cooldown = 0.010

        self.sword = Sword(self)

        self.rect.topleft = (self.x, self.y)
    

    def check_collision(self, dx, dy):
        future_x = self.x + dx
        future_y = self.y + dy
        future_rect = pygame.Rect(future_x, future_y, self.rect.width, self.rect.height)

        for obj in self.map.collision_objects:
            if future_rect.colliderect(obj):
                return False
            
        return True
    

    def check_switchmap(self, dx, dy):
        future_x = self.x + dx
        future_y = self.y + dy
        future_rect = pygame.Rect(future_x, future_y, self.rect.width, self.rect.height)

        for cle, valeur in self.map.switchmap_objects.items():
            if future_rect.colliderect(valeur):
                return [True, cle]
            
        return [False, cle]


    def move(self, dx, dy):
        if self.check_collision(dx, dy):
            self.x += dx
            self.y += dy
            self.rect.topleft = (self.x, self.y)

        if self.check_switchmap(dx, dy)[0]:
            cle = self.check_switchmap(dx, dy)[1]
            map = self.data_switchmap["switchmap"][int(cle)]["to_map"]
            pos = self.data_switchmap["switchmap"][int(cle)]["top_pos"]

            self.camera.switch_camera(map, False)

            self.x = pos[0]
            self.y = pos[1]
            self.rect.topleft = (pos[0], pos[1])


    def update(self):
        keys = pygame.key.get_pressed()
        moving = False

        current_time = pygame.time.get_ticks() / 1000

        self.attack_input()

        if self.is_attacking:
            anim = self.animations[self.current_animation]
            self.image = anim.update(loop=False)

            if anim.is_finished():
                self.is_attacking = False
                self.current_animation = self.last_direction

                anim.reset()
                self.sword.current_animation.reset()
                self.time = current_time

            return
        

        if keys[pygame.K_z]:
            self.move(0, -1)
            
            self.last_direction = "up"
            self.current_animation = self.last_direction
            moving = True

        if keys[pygame.K_q]:
            self.move(-1, 0)
            
            self.last_direction = "left"
            self.current_animation = self.last_direction
            moving = True

        if keys[pygame.K_s]:
            self.move(0, 1)
            
            self.last_direction = "down"
            self.current_animation = self.last_direction
            moving = True

        if keys[pygame.K_d]:
            self.move(1, 0)
            
            self.last_direction = "right"
            self.current_animation = self.last_direction
            moving = True


        if keys[pygame.K_SPACE] and not self.is_attacking:
            if current_time - self.time >= self.cooldown:
                self.is_attacking = True

                self.sword.set_direction(self.last_direction)

                self.current_animation = "attack_" + self.last_direction
                self.image = self.animations[self.current_animation].update()

                return


        if moving:
            self.image = self.animations[self.current_animation].update(True)

        else:
            self.image = self.animations[self.current_animation].reset()


        #print("X: ", self.x, "Y: ", self.y)
    

    def attack_input(self):
        for group in self.groups():
            if self.is_attacking:
                if self.sword not in group:
                    layer = self.sword.get_current_layer()
                    group.add(self.sword, layer=layer)

                else:
                    current_layer = self.sword.get_current_layer()
                    group.change_layer(self.sword, current_layer)

            else:
                if self.sword in group:
                    group.remove(self.sword)
    