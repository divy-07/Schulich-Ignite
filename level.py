import pygame

class Level():
    def __init__(self, frame_rate):
        self.current_level = 1
        self.spawn_speed = frame_rate     # 1 spawn speed = 1 second

        self.font = pygame.font.Font(None, 50)
    
    def update(self, seconds):
        if seconds % 10 == 0:
            self.level_up()

    def level_up(self):
        self.current_level += 1
        if self.current_level < 11:
            self.spawn_speed -= 3
        # set enemy speed again after leveling up, Ex:
        # level.level_up()
        # enemy.speed = level.enemy_speed
