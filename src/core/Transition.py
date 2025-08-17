import pygame

class Transition:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock

    def close(self):
        frame = self.screen.copy()
        max_radius = max(self.screen.get_width(), self.screen.get_height()) * 2
        radius, step = 0, 20

        while radius < max_radius:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.screen.blit(frame, (0, 0))
            overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
            pygame.draw.circle(overlay, (0, 0, 0, 255),
                               (self.screen.get_width() // 2, self.screen.get_height() // 2),
                               radius)
            self.screen.blit(overlay, (0, 0))
            pygame.display.flip()
            radius += step
            self.clock.tick(60)
