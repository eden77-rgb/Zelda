import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()

        self.sounds = {}
        self.music_volume = 0.5
        self.sfx_volume = 0.7

    
    def load_sound(self, name, path):
        if not name in self.sounds:
            self.sounds[name] = pygame.mixer.Sound(path)
            self.sounds[name].set_volume(self.sfx_volume)

    
    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()


    def play_music(self, path, loop=-1):
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(loop)


    def stop_music(self):
        pygame.mixer.music.stop()