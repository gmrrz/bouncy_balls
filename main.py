import pygame 
import sys

# Initialize Pygame into code
pygame.init()

# Setting screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clown Invaders")

# Square attributes
square_color = (255, 0, 0) # RED
square_size = 50 # w and h of the square
x, y = 200, 200

# Speed of the square's movement
speed = .5

# Game Loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update position based on arrow keys
    if keys[pygame.K_LEFT]: # Move left
        x -= speed
    if keys[pygame.K_RIGHT]: # Move right
        x += speed
    if keys[pygame.K_UP]: # Move up
        y -= speed
    if keys[pygame.K_DOWN]: # Move down
        y += speed

    # Yellow BG
    screen.fill((255, 232, 85))

    # Draw the sprite
    pygame.draw.rect(screen, square_color, (x, y, square_size, square_size))

    # Update the display
    pygame.display.update()


# Quits Game
pygame.quit()
sys.exit()