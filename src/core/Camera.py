import pygame

class Camera:
    def __init__(self, data_pos, screen):
        self.data_pos = data_pos
        self.screen = screen

        self.x = 0
        self.y = 0


    def create_camera(self, id):
        self.current_id = id
        self.start_x = self.data_pos["cameras"][id]["start_x"]
        self.start_y = self.data_pos["cameras"][id]["start_y"]

        self.end_x = self.data_pos["cameras"][id]["end_x"]
        self.end_y = self.data_pos["cameras"][id]["end_y"]

        self.x = self.start_x
        self.y = self.start_y

        print(f"create_camera: {self.current_id} - {self.start_x} - {self.start_y}")
        self.camera_rect = pygame.Rect(self.start_x, self.start_y, *self.screen.get_size())
        return self.camera_rect
    

    def switch_camera(self, new_id, reset_pos=True):
        self.current_id = new_id
        self.start_x = self.data_pos["cameras"][new_id]["start_x"]
        self.start_y = self.data_pos["cameras"][new_id]["start_y"]

        self.end_x = self.data_pos["cameras"][new_id]["end_x"]
        self.end_y = self.data_pos["cameras"][new_id]["end_y"]

        if reset_pos:
            self.x = self.start_x
            self.y = self.start_y

        print(f"switch_camera: {self.current_id} - {self.start_x} - {self.start_y}")
        self.camera_rect.topleft = (self.x, self.y)


    def center(self, player):
        center_x = player.x - self.screen.get_width() // 2
        center_y = player.y - self.screen.get_height() // 2

        self.x = max(self.start_x, min(center_x, self.end_x))
        self.y = max(self.start_y, min(center_y, self.end_y))

        self.camera_rect.topleft = (self.x, self.y)


    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if self.y > self.start_y:
                self.y -= 1

        if keys[pygame.K_LEFT]:
            if self.x > self.start_x:
                self.x -= 1

        if keys[pygame.K_DOWN]:
            if self.y < self.end_y:
                self.y += 1

        if keys[pygame.K_RIGHT]:
            if self.x < self.end_x:
                self.x += 1

        self.camera_rect.topleft = (self.x, self.y)
