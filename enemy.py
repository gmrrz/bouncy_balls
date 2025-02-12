import pygame
import random

class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.size = 30
        self.color = (255, 0, 0)
        self.speed = speed
        self.direction = 'left'  # Always move left from the right wall

    def move(self):
        if self.direction == 'left':
            self.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))