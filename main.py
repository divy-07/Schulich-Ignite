import sys
import os
import pygame

pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FRAME_RATE = 60

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

from player import Player
from enemy import Enemy
from health_bar import Health_bar
from points import Points
from level import Level
from bullet import Bullet
from bison import Bison
from weapons import Weapons
from mine import Mine
from duck import Duck

"""
SETUP section - preparing everything before the main loop runs
"""

def main():

    frames = 1

    # player
    player = Player()
    players = pygame.sprite.Group()
    players.add(player)

    # enemy
    enemies = pygame.sprite.Group()

    # health bar
    health_bar = Health_bar()

    # points
    points = Points()

    # level
    level = Level(FRAME_RATE)

    # weapons
    weapons = pygame.sprite.Group()


    while True:
        """
        EVENTS section - how the code reacts when users do things
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                pygame.quit()
                sys.exit()

        if player.health <= 0:
            game_over(points.score, level.current_level)

        # Keyboard events
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and player.rect.top > 60:
            player.move(0, -player.move_speed)
        if keys_pressed[pygame.K_a] and player.rect.left > 0:
            player.move(-player.move_speed, 0)
        if keys_pressed[pygame.K_d] and player.rect.right < SCREEN_WIDTH:
            player.move(player.move_speed, 0)    
        if keys_pressed[pygame.K_s] and player.rect.bottom < SCREEN_HEIGHT:
            player.move(0, player.move_speed)
        if keys_pressed[pygame.K_SPACE] and player.bullet_reload_available:
            if player.facing == "right":
                weapons.add(Bullet(player.rect.center[0], player.rect.center[1], player.facing))
            elif player.facing == "left":
                weapons.add(Bullet(player.rect.center[0], player.rect.center[1], player.facing))
            player.bullet_reload_available = False
        
        if level.current_level > 6 and keys_pressed[pygame.K_LSHIFT] and player.mine_reload_available:
            weapons.add(Mine(player.rect.center))
            player.mine_reload_available = False

        # Mouse events
        mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
        # (x, y) coordinate

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # If left mouse pressed
            pass
        if mouse_buttons[2]:  # If right mouse pressed
            pass

        """
        Timed events
        """
        # enemy spawn

        # bison
        if frames % (5 * level.spawn_speed) == 0:
            enemies.add(Bison(level.current_level))

        # duck
        # if level.current_level > 6 and frames % (3 * level.spawn_speed) == 0:
        if frames % (3 * level.spawn_speed) == 0:
            enemies.add(Duck(level.current_level))

        # weapon spawn
        
        # bullet
        if frames % FRAME_RATE == 0:
            player.bullet_reload_available = True

        # mine
        if frames % (5 * FRAME_RATE) == 0:
            player.mine_reload_available = True

        """
        UPDATE section - manipulate everything on the screen
        """
        # player
        players.update()

        # enemy
        enemies.update(level.current_level, player)

        # health
        health_bar.update(player.health * 2)

        # level
        level.update(frames / 60)

        # weapon
        weapons.update()

        """
        HIT actions - when two rects collide
        """
        hit_enemies = pygame.sprite.spritecollide(player, enemies, False)
        for enemy in hit_enemies:
            points.score += enemy.kill_points
            enemy.health = 0
            player.hit(enemy.hit_damage)
        
        hit_weapon = pygame.sprite.groupcollide(enemies, weapons, False, True)
        for enemy in hit_weapon:
            for weapon in hit_weapon[enemy]:
                enemy.health -= weapon.damage
                if enemy.health <= 0:
                    points.score += enemy.kill_points


        """
        DRAW section - make everything show up on screen
        """
        screen.fill(BLACK)  # Fill the screen with one colour

        # white lines to seperate sections
        pygame.draw.line(screen, WHITE, (0, 57), (SCREEN_WIDTH, 57), 3)

        # player
        players.draw(screen)

        # enemies
        enemies.draw(screen)

        # health bar
        pygame.draw.rect(screen, health_bar.back_rect_color, health_bar.back_rect)
        pygame.draw.rect(screen, health_bar.health_rect_color, health_bar.health_rect)
        screen.blit(health_bar.font.render(str(player.health), True, WHITE), (70, 15))

        # points
        screen.blit(points.font.render("Points: " + str(points.score), True, WHITE), (750, 15))

        # Level
        screen.blit(level.font.render("Level: " + str(level.current_level), True, WHITE), (420, 15))

        # weapon
        weapons.draw(screen)

        frames += 1
        pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
        clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second


def game_over(score, level):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                pygame.quit()
                sys.exit()
        
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RETURN]:
            did_beat = False
            main()
            break

        screen.fill(BLACK)  # Fill the screen with one colour

        gameOverFont = pygame.font.Font(None, 36)
        screen.blit(gameOverFont.render("Game Over!", True, WHITE), (100, 100))
        screen.blit(gameOverFont.render("Your score: " + str(score), True, WHITE), (100, 200))
        screen.blit(gameOverFont.render("Level reached: " + str(level), True, WHITE), (100, 250))
        screen.blit(gameOverFont.render("Press ENTER to play again", True, WHITE), (100, 350))

        pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
        clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second


main()