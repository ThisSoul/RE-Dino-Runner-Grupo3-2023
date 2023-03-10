# No funciona, no logre acabar el codigo a tiempo
import pygame
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = CLOUD
    
    def update(self, game_speed):
        self.x_pos -= game_speed

        if self.x_pos < -self.image.get_width():
            self.x_pos = pygame.display.get_surface().get_width()

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, self.y_pos))

class Clouds:
    def __init__(self):
        self.clouds = [
           Cloud(500, 100),
           Cloud(800, 200),
           Cloud(1100, 150)
           ]
        
    def update(self):
        for cloud in self.clouds:
            cloud.update(self.game_speed)

    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)
        
