import pygame

class Animation:
    def __init__(self, sprite_sheet, frames, speed=0.15, flip=False, rotation=0, flip_list=None, rotation_list=None, colorkey="#004040"):
        self.sprite_sheet = sprite_sheet
        self.flip_list = flip_list
        self.rotation_list = rotation_list
        self.colorkey = colorkey
        
        if flip_list or rotation_list:
            self.frames = []

            for i, f in enumerate(frames):
                flip_value = flip_list[i] if flip_list and i < len(flip_list) else flip
                rotation_value = rotation_list[i] if rotation_list and i < len(rotation_list) else rotation
                self.frames.append(self.get_image(*f, flip_value, rotation_value))

        else:
            self.frames = [self.get_image(*f, flip, rotation) for f in frames]

        self.speed = speed
        self.frame_index = 0

        self.pause_before_last = 1.0 / speed
        self.pause_counter = 0
        self.animation_completed = False


    def get_image(self, x, y, width, height, flip=False, rotation=0):
        image = pygame.Surface((width, height))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(self.colorkey)

        if flip:
            image = pygame.transform.flip(image, True, False)

        if rotation != 0:
            image = pygame.transform.rotate(image, rotation)

        return image


    def update(self, loop=True):
        if loop:
            self.frame_index += self.speed

            if self.frame_index >= len(self.frames):
                self.frame_index = 0
                self.animation_completed = False

            return self.frames[int(self.frame_index)]
        
        if self.pause_before_last > 0 and int(self.frame_index) == len(self.frames) - 1:
            if self.pause_counter < self.pause_before_last:
                self.pause_counter += 1
                return self.frames[int(self.frame_index)]
            
            else:
                self.animation_completed = True
                return self.frames[int(self.frame_index)]

        self.frame_index += self.speed
        if self.frame_index >= len(self.frames):
            self.frame_index = len(self.frames) - 1

        return self.frames[int(self.frame_index)]
    

    def reset(self):
        self.frame_index  = 0
        self.pause_counter = 0
        self.animation_completed = False

        return self.frames[0]
    

    def is_finished(self):
        return self.animation_completed