import pygame

class Health_bar():
    def __init__(self):
        self.back_rect = pygame.rect.Rect(0, 0, 200, 56)
        self.back_rect_color = (100, 100, 100)

        self.health_rect = pygame.rect.Rect(0, 0, 200, 56)
        self.health_rect_color = (255, 0, 0)

        self.font = pygame.font.Font(None, 50)
    
    def update(self, health):
        self.health_rect.width = health

