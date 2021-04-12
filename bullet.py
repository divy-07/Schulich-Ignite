import os
import pygame
from weapons import Weapons

class Bullet(Weapons):
    def __init__(self, x, y, facing):

        image_location = os.path.join("stuff", "bullet.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.damage = 10
        if facing == "right":
            self.speed = 8
        else:
            self.speed = -8

        super().__init__(x, y)
