import os
import pygame

class Weapons(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.speed
        self.kill_offscreen()

    def kill_offscreen(self):
        if self.rect.x + self.rect.width < 0 or self.rect.x > 1000:
            self.kill()