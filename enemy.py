import os
import pygame
import random

class Enemy(pygame.sprite.Sprite):

    def __init__(self, level):
        super().__init__()
        self.level = level
        self.health = 0

    def hit(self, damage, distruct = False):
        if not distruct:
            self.health -= damage
        else:
            self.health = 0
