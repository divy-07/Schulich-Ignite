import os
import pygame
import random
from enemy import Enemy

bison_1_location = os.path.join("stuff", "bison_1.png")
bison_2_location = os.path.join("stuff", "bison_2.png")
bison_3_location = os.path.join("stuff", "bison_3.png")

class Bison(Enemy):
    bison_1 = pygame.image.load(bison_1_location).convert_alpha()
    bison_1 = pygame.transform.scale(bison_1, (100, 100))
    bison_1_flip = pygame.transform.flip(bison_1, True, False)
    bison_1_pair = (bison_1, bison_1_flip)

    bison_2 = pygame.image.load(bison_2_location).convert_alpha()
    bison_2 = pygame.transform.scale(bison_2, (100, 100))
    bison_2_flip = pygame.transform.flip(bison_2, True, False)
    bison_2_pair = (bison_2, bison_2_flip)

    bison_3 = pygame.image.load(bison_3_location).convert_alpha()
    bison_3 = pygame.transform.scale(bison_3, (100, 100))
    bison_3_flip = pygame.transform.flip(bison_3, True, False)
    bison_3_pair = (bison_3, bison_3_flip)

    def __init__(self, level):
        super().__init__(level)
        self.image_pair = self.bison_1_pair
        self.image = self.image_pair[0]
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice([0,1000]) if self.level > 3 else 1000, random.randint(110, 550))

        self.move_speed = 1
        self.health = 20
        self.hit_damage = 20
        self.kill_points = 3
    

    def update(self, level, player = None):
        if self.health <= 0:
            self.kill()
        
        time = pygame.time.get_ticks()
        if time % 4000 < 1000:
            self.image_pair = self.bison_1_pair
        elif time % 4000 < 2000:
            self.image_pair = self.bison_2_pair
        elif time % 4000 < 3000:
            self.image_pair = self.bison_3_pair
        else:
            self.image_pair = self.bison_2_pair
        
        if level <= 3 and self.rect.x + self.rect.width <= 0:
            self.kill()

        if player is not None:
            if player.rect.x < self.rect.x:
                self.move_speed = abs(self.move_speed)
                self.image = self.image_pair[0]
            else:
                self.move_speed = -abs(self.move_speed)
                self.image = self.image_pair[1]
            
            if player.rect.y < self.rect.y:
                self.rect.y -= abs(self.move_speed)
            else:
                self.rect.y += abs(self.move_speed)
        else:
            self.image = self.image_pair[0]

        self.rect.x -= self.move_speed

