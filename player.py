# Player.py

import pygame

class Player:
    def __init__(self, color, size, x, y, speed, gravity):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.speed = speed
        self.gravity = gravity
        self.velocity_y = 0

    def move(self, keys):
    # Updates the players position based on key 
        if keys[pygame.K_a]: # Move left
            self.x -= self.speed
        if keys[pygame.K_d]: # Move right
            self.x += self.speed
        if keys[pygame.K_w]: # Move up
            self.y -= self.speed
        if keys[pygame.K_s]: # Move down
            self.y += self.speed

        # This applys gravity
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # prevent the player from falling off the screen
        if self.y + self.size > 600: # Screen height is 600
            self.y = 600 - self.size
            self.velocity_y = 0

    def draw(self, screen):
        # Draw the player on screen
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))