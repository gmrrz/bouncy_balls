# Player.py

import pygame

class Player:
    def __init__(self, color, size, x, y, speed, gravity, jump_strength,jump_sound,jump_sound2):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.speed = speed
        self.gravity = gravity
        self.velocity_y = 0
        self.jump_sound = jump_sound
        self.jump_sound2 = jump_sound2
        self.jumps = 0
        self.jump_strength = jump_strength
        self.on_ground = True

    def move(self, keys):
    # Updates the players position based on key 
        if keys[pygame.K_a] or keys[pygame.K_LEFT] : # Move left
            self.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # Move right
            self.x += self.speed



        # This applys gravity
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # prevent the player from falling off the screen and resets jumps
        if self.y + self.size > 600: # Screen height is 600
            self.y = 600 - self.size
            self.velocity_y = 0
            self.jumps = 0
            self.on_ground = True

        # Prevent the player from moving out of bounds horizontally
        if self.x < 0:
            self.x = 0
        if self.x + self.size > 800:
            self.x = 800 - self.size

        # Prevent the player from moving out of bounds vert
        if self.y < 0:
            self.y = 0

    def jump(self):
        # Double Jump logic
        if self.jumps < 2:
            if self.jumps == 0:
                self.jump_sound.play()
            else:
                self.jump_sound2.play()
            self.velocity_y = -self.jump_strength
            self.jumps += 1
            self.on_ground = False

    def draw(self, screen):
        # Draw the player on screen
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))