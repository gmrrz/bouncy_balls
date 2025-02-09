# Player.py

import pygame

class Player:
    def __init__(self, color, size, x, y, speed):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, keys):
    # Updates the players position based on key 
        if keys[pygame.K_LEFT]: # Move left
            self.x -= self.speed
        if keys[pygame.K_RIGHT]: # Move right
            self.x += self.speed
        if keys[pygame.K_UP]: # Move up
            self.y -= self.speed
        if keys[pygame.K_DOWN]: # Move down
            self.y += self.speed

    def draw(self, screen):
        # Draw the player on screen
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))