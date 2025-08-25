import pygame

class DestructibleObject:
    def __init__(self, player):
        self.player = player
        self.destroyed = False


    def destroy(self):
        self.destroyed = True


class Grass(DestructibleObject):
    def __init__(self, player, grass_rect):
        super().__init__(player)
        self.grass_rect = grass_rect


    def on_collision(self):
        if self.player.sword.rect.colliderect(self.grass_rect) and not self.destroyed:
            print("on_collision: ")
            self.destroy()


class GrassManager():
    def __init__(self, grass_objects, player, screen, pyscroll_group):
        self.grass_objects = grass_objects
        self.player = player
        self.screen = screen
        self.pyscroll_group = pyscroll_group

        self.grass_group = []
        for rect in self.grass_objects:
            self.grass_group.append(Grass(self.player, rect))

        self.sprite_sheet = pygame.image.load("../assets/sprites/Destructible-Object.png")
        self.image_destroyed = pygame.Surface((16, 16), pygame.SRCALPHA)
        self.image_destroyed.blit(self.sprite_sheet, (0, 0), pygame.Rect(1, 1, 16, 16))


    def update(self):
        for grass in self.grass_group:
            if not grass.destroyed:
                grass.on_collision()

                if grass.destroyed:
                    destroyed_sprite = pygame.sprite.Sprite()
                    destroyed_sprite.image = self.image_destroyed
                    
                    destroyed_sprite.rect = pygame.Rect(
                        grass.grass_rect.x, 
                        grass.grass_rect.y, 
                        self.image_destroyed.get_width(), 
                        self.image_destroyed.get_height()
                    )
                    
                    self.pyscroll_group.add(destroyed_sprite, layer=5)
