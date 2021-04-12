import os
import pygame
from weapons import Weapons

class Mine(Weapons):
    def __init__(self, center):

        image_location = os.path.join("stuff", "mine.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()

        self.rect.center = center

        self.damage = 30
        self.speed = 0

        super().__init__(self.rect.x, self.rect.y)
