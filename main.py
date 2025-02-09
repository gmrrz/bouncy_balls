import pygame 
import sys

# Initialize Pygame into code
pygame.init()

# Setting screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clown Invaders")

# Game Loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Yellow BG
    screen.fill((255, 232, 85))

    # Update the display
    pygame.display.update()


# Quits Game
pygame.quit()
sys.exit()