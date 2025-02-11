import pygame
import time

class Player:
    def __init__(self, color, size, x, y, speed, gravity, jump_strength, dash_strength, dash_duration, jump_sound, jump_sound2, smash_sound):
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
        self.dash_strength = dash_strength
        self.dash_duration = dash_duration
        self.dash_start_time = None
        self.on_ground = True

    def move(self, keys):
        current_time = time.time()
        
        # Apply horizontal velocity and decay it over time
        if self.dash_start_time:
            if current_time - self.dash_start_time < self.dash_duration:
                self.x += self.velocity_x
            else:
                self.velocity_x = 0
                self.dash_start_time = None
        else:
            if keys[pygame.K_LEFT]:  # Move left
                self.x -= self.speed
            if keys[pygame.K_RIGHT]:  # Move right
                self.x += self.speed

        # Apply gravity
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        self.x += self.velocity_x
        self.velocity_x *= 0.9  # Decay factor for smoother stopping

        # Prevent the player from falling off the screen and reset jumps
        if self.y + self.size > 600:  # Screen height is 600
            self.y = 600 - self.size
            self.velocity_y = -self.jump_strength  # Reverse velocity for bounce
            self.jumps = 0
            self.on_ground = True

        # Prevent the player from moving out of bounds horizontally
        if self.x < 0:
            self.x = 0
        if self.x + self.size > 800:
            self.x = 800 - self.size

        # Prevent the player from moving out of bounds vertically
        if self.y < 0:
            self.y = 0

    def jump(self):
        # Double jump logic
        if self.jumps < 2:
            if self.jumps == 0:
                self.jump_sound.play()
            else:
                self.jump_sound2.play()
            self.velocity_y = -self.jump_strength
            self.jumps += 1
            self.on_ground = False

    def smash(self):
        # Smash down logic
        self.velocity_y = self.jump_strength * 2  # Increase velocity for a stronger downward force
        self.smash_sound.play()

    def start_dash(self, direction):
        # Start dash logic
        self.velocity_x = direction * self.dash_strength
        self.dash_start_time = time.time()

    def draw(self, screen):
        # Draw the player on screen
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))