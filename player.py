import pygame
import time

class Player:
    def __init__(self, color, size, x, y, speed, gravity, jump_strength, jump_sound, jump_sound2, smash_sound):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.speed = speed
        self.gravity = gravity
        self.velocity_y = 0
        self.velocity_x = 0
        self.jump_sound = jump_sound
        self.jump_sound2 = jump_sound2
        self.smash_sound = smash_sound
        self.jumps = 0
        self.jump_strength = jump_strength
        self.on_ground = True

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        self.velocity_y += self.gravity
        self.y += self.velocity_y

        if self.y + self.size > 600:
            self.y = 600 - self.size
            self.velocity_y = -self.jump_strength
            self.jumps = 0
            self.on_ground = True

        if self.x < 0:
            self.x = 0
        if self.x + self.size > 800:
            self.x = 800 - self.size

        if self.y < 0:
            self.y = 0

    def jump(self):
        if self.jumps < 2:
            if self.jumps == 0:
                self.jump_sound.play()
            else:
                self.jump_sound2.play()
            self.velocity_y = -self.jump_strength
            self.jumps += 1
            self.on_ground = False

    def smash(self):
        self.velocity_y = self.jump_strength * 2
        self.smash_sound.play()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))