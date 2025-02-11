import pygame 
import sys

from player import Player

# Initialize Pygame into code
pygame.init()

# Setting screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clown Invaders")

# Creating the player
player = Player(color = (255, 248, 194), size=50, x=375, y=275, speed=.5, gravity=0.1)

# Game Loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Move the player
    player.move(keys)

    # BG colorr
    screen.fill((255, 232, 85))

    # Draw the player
    player.draw(screen)

    # Update the display
    pygame.display.update()


# Quits Game
pygame.quit()
sys.exit()