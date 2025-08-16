import pygame

class Animation:
    def __init__(self, sprite_sheet, frames, speed=0.15, flip=False, rotation=0):
        self.sprite_sheet = sprite_sheet
        self.frames = [self.get_image(*f, flip, rotation) for f in frames]
        self.speed = speed

        self.frame_index = 0


    def get_image(self, x, y, width, height, flip=False, rotation=0):
        image = pygame.Surface((width, height))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(image.get_at((0,0)))

        if flip:
            image = pygame.transform.flip(image, True, False)

        elif rotation != 0:
            image = pygame.transform.rotate(image, rotation)

        return image


    def update(self, loop=True):
        print("update")
        self.frame_index += self.speed
        if self.frame_index >= len(self.frames):
            if loop:
                self.frame_index = 0

            else:
                self.frame_index = len(self.frames) - 1

        return self.frames[int(self.frame_index)]
    

    def reset(self):
        self.frame_index  = 0
        return self.frames[0]
    

    def is_finished(self):
        return self.frame_index >= len(self.frames) - 1