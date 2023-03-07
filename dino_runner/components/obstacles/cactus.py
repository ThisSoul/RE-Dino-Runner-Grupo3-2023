import random
from dino_runner.components.obstacles.obstacles import Obstacle

class Cactus (Obstacle):
    def __init__(self, image, cactus_pos_y):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = cactus_pos_y
        
#self.rect.y = 325

    
