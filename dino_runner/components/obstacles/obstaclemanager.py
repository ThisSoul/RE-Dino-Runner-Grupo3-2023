import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    def update(self, game):
        if len(self.obstacles) == 0:
           obstacle_type = random.randint(0,2)
           if obstacle_type == 0:
              self.obstacles.append(Cactus(SMALL_CACTUS, 325))
           elif obstacle_type == 1:
              self.obstacles.append(Cactus(LARGE_CACTUS, 300))
           else:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
           obstacle.update(game.game_speed, self.obstacles)
           if game.player.dino_rect.colliderect(obstacle.rect):
              pygame.time.delay(1000)
              game.playing = False
              break 

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []
        