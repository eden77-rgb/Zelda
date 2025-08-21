import pygame
from core.HUDElement import HUDElement

class Hearth(HUDElement):
    def __init__(self, x, y, scale, life, max_life):
        super().__init__(x, y, scale)
        self.life = life
        self.max_life = max_life

        # Cœur plein
        full_surface = pygame.Surface((7, 7), pygame.SRCALPHA)
        full_surface.blit(self.sprite_sheet, (0, 0), (259, 56, 7, 7))
        self.full_heart = pygame.transform.scale(full_surface, (7 * self.scale, 7 * self.scale))
        self.full_heart.set_colorkey((63, 72, 204))

        # Demi-cœur
        half_surface = pygame.Surface((7, 7), pygame.SRCALPHA)
        half_surface.blit(self.sprite_sheet, (0, 0), (275, 56, 7, 7))
        self.half_heart = pygame.transform.scale(half_surface, (7 * self.scale, 7 * self.scale))
        self.half_heart.set_colorkey((63, 72, 204))

        # Cœur vide (tu devras ajuster les coordonnées selon ton sprite sheet)
        empty_surface = pygame.Surface((7, 7), pygame.SRCALPHA)
        empty_surface.blit(self.sprite_sheet, (0, 0), (291, 56, 7, 7))  # Coordonnées à ajuster
        self.empty_heart = pygame.transform.scale(empty_surface, (7 * self.scale, 7 * self.scale))
        self.empty_heart.set_colorkey((63, 72, 204))


    def update(self, new_life, new_max_life=None):
        self.life = new_life
        if new_max_life is not None:
            self.max_life = new_max_life


    def draw(self, screen):
        if self.visible:
            heart_w = self.full_heart.get_width()
            heart_h = self.full_heart.get_height()
            spacing = 1 * self.scale

            full_hearts = int(self.life)
            has_half = (self.life % 1) != 0
            total_hearts_needed = int(self.max_life) + (1 if self.max_life % 1 != 0 else 0)

            for i in range(total_hearts_needed):
                col = i % 10
                row = i // 10
                x = self.x + col * (heart_w + spacing)
                y = self.y + row * (heart_h + spacing)

                if i < full_hearts:
                    screen.blit(self.full_heart, (x, y))

                elif i == full_hearts and has_half:
                    screen.blit(self.half_heart, (x, y))

                else:
                    screen.blit(self.empty_heart, (x, y))