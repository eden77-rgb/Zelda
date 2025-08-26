import pygame
from random import randint
from core.Animation import Animation

GREEN_RUBY = [
    (36, 249, 8, 14),
    (52, 249, 8, 14),
    (68, 249, 8, 14)
]
BLUE_RUBY = [
    (84, 249, 8, 14),
    (100, 249, 8, 14),
    (116, 249, 8, 14)
]

RED_RUBY = [
    (132, 249, 8, 14),
    (148, 249, 8, 14),
    (164, 249, 8, 14)
]

HEARTH = [
    (104, 280, 8, 7),
    (88, 280, 8, 7)
]

ITEMS_TYPES = {
    "heart": HEARTH,
    "green_ruby": GREEN_RUBY,
    "blue_ruby": BLUE_RUBY,
    "red_ruby": RED_RUBY
}


class ItemManager:
    def __init__(self, player, screen, group):
        self.player = player
        self.screen = screen
        self.group = group

        self.sprite_sheet = pygame.image.load("../assets/sprites/Items.png")
        self.items = pygame.sprite.Group()


    def roll(self):
        roll = randint(0, 100)

        if roll <= 50:
            return None

        elif roll <= 70:
            return "heart"

        elif roll <= 85:
            return "green_ruby"

        elif roll <= 95:
            return "blue_ruby"

        else:
            return "red_ruby"


    def spawn(self, position):
        item_type = self.roll()

        if item_type is None:
            return None
        
        item = Item(position, item_type, self.sprite_sheet)
        self.items.add(item)
        self.group.add(item, layer=200)
        return item
    

    def update(self):
        for item in self.items:
            item.update()

            if item.rect.colliderect(self.player.rect):
                self.collect_item(item)


    def collect_item(self, item):
        if item.item_type == "heart":
            self.player.take_heal(1)

        elif item.item_type == "green_ruby":
            self.player.ruby += 1

        elif item.item_type == "blue_ruby":
            self.player.ruby += 5

        elif item.item_type == "red_ruby":
            self.player.ruby += 20

        self.items.remove(item)
        self.group.remove(item)
        item.kill()


class Item(pygame.sprite.Sprite):
    def __init__(self, position, item_type, sprite_sheet):
        super().__init__()
        self.item_type = item_type
        self.sprite_sheet = sprite_sheet

        self.animation = Animation(self.sprite_sheet, ITEMS_TYPES[item_type], speed=0.1, colorkey="#800080")

        self.image = self.animation.update(loop=True)
        self.rect = self.image.get_rect()

        if isinstance(position, (tuple, list)) and len(position) == 2:
            self.rect.centerx = position[0]
            self.rect.centery = position[1]
            self.base_y = position[1] - self.rect.height // 2
        
        elif hasattr(position, 'centerx') and hasattr(position, 'centery'):
            self.rect.centerx = position.centerx
            self.rect.centery = position.centery
            self.base_y = position.centery - self.rect.height // 2

        self.bounce_offset = 0
        self.bounce_speed = 0.05

        print(item_type, position)


    def update(self):
        self.image = self.animation.update(loop=True)
        
        self.bounce_offset += self.bounce_speed
        bounce_y = int(2 * pygame.math.Vector2(0, 1).rotate(self.bounce_offset * 180).y)
        self.rect.y = self.base_y + bounce_y