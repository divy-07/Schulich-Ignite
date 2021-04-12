import os
import sys
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = os.path.join("stuff", "player.png")
        self.walking_right_image = pygame.image.load(image_location).convert_alpha()
        self.walking_right_image = pygame.transform.scale(self.walking_right_image, (100, 100))
        self.walking_left_image = pygame.transform.flip(self.walking_right_image, True, False)
        self.image = self.walking_right_image
        self.rect = self.image.get_rect()

        self.rect.center = (100, 300)
        self.facing = "right"

        self.move_speed = 5

        self.health = 100
        self.bullet_reload_available = True
        self.mine_reload_available = True

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

        if x_change > 0:
            self.facing = "right"
            self.image = self.walking_right_image
        elif x_change < 0:
            self.facing = "left"
            self.image = self.walking_left_image

    def hit(self, damage):
        self.health -= damage

