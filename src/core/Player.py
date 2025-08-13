import pygame

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
        self.image = self.get_image(IDLE[0], IDLE[1], IDLE[2], IDLE[3])
        self.rect = self.image.get_rect()

        self.animation_up = self.get_animation_up()
        self.animation_left = self.get_animation_left()
        self.animation_down = self.get_animation_down()
        self.animation_right = self.get_animation_right()

        self.frame_index = 0
        self.animation_speed = 0.15
        self.last_direction = "down"
        self.last_direction_idle = {
            "up": self.animation_up[0],
            "left": self.animation_left[0],
            "down": self.animation_down[0],
            "right": self.animation_right[0]
        }

        self.rect.topleft = (self.x, self.y)


    def get_image(self, x, y, width, height):
        image = pygame.Surface((16, 24))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey(image.get_at((0,0)))
        return image
    

    def get_animation_up(self):
        images = []
        for elt in WALK_UP:
            images.append(self.get_image(elt[0], elt[1], elt[2], elt[3]))

        return images
    

    def get_animation_left(self):
        images = []
        for elt in WALK_LEFT:
            images.append(pygame.transform.flip(self.get_image(elt[0], elt[1], elt[2], elt[3]), True, False))

        return images
    

    def get_animation_down(self):
        images = []
        for elt in WALK_DOWN:
            images.append(self.get_image(elt[0], elt[1], elt[2], elt[3]))

        return images
    

    def get_animation_right(self):
        images = []
        for elt in WALK_RIGHT:
            images.append(self.get_image(elt[0], elt[1], elt[2], elt[3]))

        return images
    

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

        if keys[pygame.K_z]:
            self.move(0, -1)
            
            self.last_direction = "up"
            moving = True

            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.animation_up):
                self.frame_index = 0

            self.image = self.animation_up[int(self.frame_index)]


        if keys[pygame.K_q]:
            self.move(-1, 0)
            
            self.last_direction = "left"
            moving = True

            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.animation_left):
                self.frame_index = 0

            self.image = self.animation_left[int(self.frame_index)]


        if keys[pygame.K_s]:
            self.move(0, 1)
            
            self.last_direction = "down"
            moving = True

            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.animation_down):
                self.frame_index = 0

            self.image = self.animation_down[int(self.frame_index)]


        if keys[pygame.K_d]:
            self.move(1, 0)
            
            self.last_direction = "right"
            moving = True

            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.animation_right):
                self.frame_index = 0

            self.image = self.animation_right[int(self.frame_index)]


        if not moving:
            self.frame_index = 0
            self.image = self.last_direction_idle[self.last_direction]


        print("X: ", self.x, "Y: ", self.y)
    