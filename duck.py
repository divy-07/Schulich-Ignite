import os
import pygame
import random
from enemy import Enemy

duck_location = os.path.join("stuff", "duck.png")

class Duck(Enemy):
    duck_image = pygame.image.load(duck_location).convert_alpha()
    duck_image = pygame.transform.scale(duck_image, (61, 61))
    duck_image_flip = pygame.transform.flip(duck_image, True, False)
    duck_image_pair = (duck_image_flip, duck_image)

    def __init__(self, level):
        super().__init__(level)
        self.image_pair = self.duck_image_pair
        self.image = self.image_pair[0]
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice([0,1000]), random.randint(110, 550))

        self.x_move_speed = 3
        self.y_move_speed = 1
        self.health = 1
        self.hit_damage = 1
        self.kill_points = 1
    

    def update(self, level, player = None):
        if self.health <= 0:
            self.kill()
        
        if player is not None:
            if player.rect.center[0] < self.rect.center[0]:
                self.x_move_speed = abs(self.x_move_speed)
                self.image = self.image_pair[0]
            else:
                self.x_move_speed = -abs(self.x_move_speed)
                self.image = self.image_pair[1]
            
            if player.rect.center[1] < self.rect.center[1]:
                self.rect.y -= abs(self.y_move_speed)
            else:
                self.rect.y += abs(self.y_move_speed)
        else:
            self.image = self.image_pair[0]

        self.rect.x -= self.x_move_speed

