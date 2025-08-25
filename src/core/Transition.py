import pygame
import math
from enum import Enum

from maps.MapLoader import MapLoader
from maps.ObjectManager import GrassManager

class TransitionState(Enum):
    NONE = 0
    CLOSING = 1
    CHANGING = 2
    OPENING = 3

class Transition:
    def __init__(self, game, screen, clock):
        self.game = game
        self.screen = screen
        self.clock = clock
        
        self.transition_state = TransitionState.NONE
        self.transition_timer = 0
        self.transition_duration = 40
        
        self.circle_radius = 0
        self.screen_center = (screen.get_width() // 2, screen.get_height() // 2)
        self.max_radius = math.sqrt(screen.get_width()**2 + screen.get_height()**2)
        
        self.pending_map = None
        self.pending_pos = None
        self.player_ref = None
        self.camera_ref = None
        

    def start_transition(self, player, camera, target_map, target_pos):
        """Démarre la transition vers une nouvelle position/carte"""
        if self.transition_state != TransitionState.NONE:
            return
            
        self.transition_state = TransitionState.CLOSING
        self.transition_timer = 0
        self.circle_radius = 0
        
        self.player_ref = player
        self.camera_ref = camera
        self.pending_map = target_map
        self.pending_pos = target_pos
        

    def update(self):
        """Met à jour la transition"""
        if self.transition_state == TransitionState.NONE:
            return False
            
        self.transition_timer += 1
        progress = self.transition_timer / self.transition_duration
        
        if self.transition_state == TransitionState.CLOSING:
            self.circle_radius = progress * self.max_radius
            
            if self.transition_timer >= self.transition_duration:
                self.transition_state = TransitionState.CHANGING
                self.transition_timer = 0
                
        elif self.transition_state == TransitionState.CHANGING:
            if self.transition_timer == 1:
                self.camera_ref.switch_camera(self.pending_map, False)

                new_map = MapLoader(self.camera_ref.data_pos["cameras"][self.camera_ref.current_id], self.screen, self.camera_ref.camera_rect)
                new_map.load_map()
                new_map.add_group()

                self.game.map = new_map
                self.player_ref.map = self.game.map

                self.player_ref.x = self.pending_pos[0]
                self.player_ref.y = self.pending_pos[1]
                self.player_ref.rect.topleft = (self.pending_pos[0], self.pending_pos[1])

                self.game.map.group.add(self.player_ref, layer=10)
                
                self.camera_ref.center(self.player_ref)

                self.game.grass_manager = GrassManager(self.game.map.grass_objects, self.player_ref, self.screen, new_map.group)
            
            if self.transition_timer >= self.transition_duration:
                self.transition_state = TransitionState.OPENING
                self.transition_timer = 0
                
        elif self.transition_state == TransitionState.OPENING:
            self.circle_radius = (1 - progress) * self.max_radius
            
            if self.transition_timer >= self.transition_duration:
                self.transition_state = TransitionState.NONE
                self.circle_radius = 0
                return False
                
        return True
        

    def draw(self):
        """Dessine l'effet de transition par-dessus l'écran"""
        if self.transition_state == TransitionState.NONE:
            return
            
        if self.transition_state == TransitionState.CHANGING:
            overlay = pygame.Surface(self.screen.get_size())
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))

        else:
            overlay = pygame.Surface(self.screen.get_size())
            overlay.fill((0, 0, 0))
            
            if self.transition_state == TransitionState.CLOSING:
                hole_radius = self.max_radius - self.circle_radius

                if hole_radius > 0:
                    pygame.draw.circle(overlay, (255, 255, 255), 
                                     self.screen_center, int(hole_radius))
                    overlay.set_colorkey((255, 255, 255))

            else:
                hole_radius = self.max_radius - self.circle_radius

                if hole_radius > 0:
                    pygame.draw.circle(overlay, (255, 255, 255), 
                                     self.screen_center, int(hole_radius))
                    overlay.set_colorkey((255, 255, 255))
            
            self.screen.blit(overlay, (0, 0))
            
    def is_active(self):
        """Retourne True si une transition est en cours"""
        return self.transition_state != TransitionState.NONE
