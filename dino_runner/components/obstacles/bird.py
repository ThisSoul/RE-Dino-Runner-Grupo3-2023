import random
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self,image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(240,310)
        self.index = 0

    def draw(self,screen):
        if self.index >= 10:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1