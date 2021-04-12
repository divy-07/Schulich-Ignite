import pygame

class Points():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 50)
    
    def update(self, add_points):
        self.score += add_points