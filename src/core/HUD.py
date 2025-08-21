import pygame

from elements.Hearth import Hearth

class HUD:
    def __init__(self, screen, player, scale):
        self.screen = screen
        self.player = player
        self.scale = scale

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        
        self.sprite_sheet = pygame.image.load("../assets/hud/HUD.png").convert_alpha()
        
        surface = pygame.Surface((256, 224), pygame.SRCALPHA)
        surface.blit(self.sprite_sheet, (0, 0), (0, 0, 256, 224))

        colors = [(63, 72, 204), (255, 0, 255)]
        surface_alpha = self.set_colors_key(surface, colors)

        self.hearth = Hearth(161, 24, self.scale, 3.67, 5)
        
        self.image = pygame.transform.scale(surface_alpha, (256 * self.scale, 224 * self.scale))

        self.visible = True


    def draw(self):
        if self.visible:
            self.screen.blit(self.image, (0, 0))
            self.hearth.draw(self.screen)


    def set_colors_key(self, surface, colors):
        for x in range(surface.get_width()):
            for y in range(surface.get_height()):
                color = surface.get_at((x, y))

                if (color.r, color.g, color.b) in colors:
                    surface.set_at((x, y), (0, 0, 0, 0))

        return surface
