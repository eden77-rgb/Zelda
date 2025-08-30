import pygame

STATIC_KNIGHT_UP = [
    (30, 2, 25, 28)
]

STATIC_KNIGHT_LEFT = [
    (63, 2, 21, 28)
]

STATIC_KNIGHT_DOWN = [
    (1, 1, 25, 30)
]

STATIC_KNIGHT_RIGHT = [
    (89, 2, 21, 28)
]

class NPC(pygame.sprite.Sprite):
    def __init__(self, type, x, y, sprite_sheet, pyscroll_group, layer=4):
        super().__init__()

        self.type = type
        self.x = x
        self.y = y
        self.sprite_sheet = sprite_sheet
        self.pyscroll_group = pyscroll_group
        self.layer = layer

        self.direction = "down"

        rect = pygame.Rect(*STATIC_KNIGHT_UP[0])
        self.image = self.sprite_sheet.subsurface(rect).copy()
        self.image.set_colorkey("#ff90ff")

        self.rect = pygame.Rect(0, 0, rect.width, rect.height)
        self.rect.center = (self.x, self.y)

        self.pyscroll_group.add(self, layer=self.layer)


    def update(self):
        self.rect.center = (self.x, self.y)

        if self.direction == "up":
            rect = pygame.Rect(*STATIC_KNIGHT_UP[0])

        elif self.direction == "down":
            rect = pygame.Rect(*STATIC_KNIGHT_DOWN[0])

        elif self.direction == "left":
            rect = pygame.Rect(*STATIC_KNIGHT_LEFT[0])

        elif self.direction == "right":
            rect = pygame.Rect(*STATIC_KNIGHT_RIGHT[0])

        else:
            rect = pygame.Rect(*STATIC_KNIGHT_DOWN[0])

        self.image = self.sprite_sheet.subsurface(rect).copy()
        self.image.set_colorkey("#ff90ff")


    def look_at_player(self, player):
        dx = player.x - self.x
        dy = player.y - self.y
        # Priorité à l'axe le plus grand
        if abs(dx) > abs(dy):
            if dx > 0:
                self.direction = "right"

            else:
                self.direction = "left"

        else:
            if dy > 0:
                self.direction = "down"

            else:
                self.direction = "up"


class NPCManager:
    def __init__(self, spawn_object, screen, pyscroll_group):
        self.spawn_object = spawn_object
        self.screen = screen
        self.pyscroll_group = pyscroll_group

        self.sprite_sheet = pygame.image.load("../assets/sprites/NPC.png").convert_alpha()

        self.spawn_group = []
        for obj in self.spawn_object:
            npc = NPC(obj["type"], obj["x"], obj["y"], self.sprite_sheet, self.pyscroll_group)
            self.spawn_group.append(npc)

        print("NPCManager", self.spawn_group)


    def update(self, player):
        for npc in self.spawn_group:
            if player is not None:
                npc.look_at_player(player)
            npc.update()