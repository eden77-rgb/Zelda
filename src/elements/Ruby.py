import pygame
from core.HUDElement import HUDElement

DISPLAY_NUMBER = {
    0: (259, 13, 7, 7),
    1: (267, 13, 7, 7),
    2: (275, 13, 7, 7),
    3: (283, 13, 7, 7),
    4: (291, 13, 7, 7),
    5: (259, 21, 7, 7),
    6: (267, 21, 7, 7),
    7: (275, 21, 7, 7),
    8: (283, 21, 7, 7),
    9: (291, 21, 7, 7)
}

class Ruby(HUDElement):
    def __init__(self, x, y, scale, ruby_amount):
        super().__init__(x, y, scale)
        self.ruby_amount = str(ruby_amount)
        self.numbers = []

        if len(self.ruby_amount) < 3:
            for _ in range(len(self.ruby_amount), 3):
                self.numbers.append("0")
        
        for elt in self.ruby_amount:
            self.numbers.append(elt)


    def get_image(self, rect):
        surface = pygame.Surface((7, 7), pygame.SRCALPHA)
        surface.blit(self.sprite_sheet, (0, 0), rect)
        image = pygame.transform.scale(surface, (7 * self.scale, 7 * self.scale))
        image.set_colorkey((63, 72, 204))

        return image
    

    def update(self, new_amout):
        self.ruby_amount = str(new_amout)
        self.numbers = []

        if len(self.ruby_amount) < 3:
            for _ in range(len(self.ruby_amount), 3):
                self.numbers.append("0")
        
        for elt in self.ruby_amount:
            self.numbers.append(elt)


    def draw(self, screen):
        x = self.x - 16
        spacing = 2

        for elt in self.numbers:
            x = x + 14 + spacing
            screen.blit(self.get_image(DISPLAY_NUMBER[int(elt)]), (x, self.y))
