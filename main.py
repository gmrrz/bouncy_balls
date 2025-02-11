import pygame 
import sys

from player import Player

# Initialize Pygame into code
pygame.init()

# Setting screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncy Ballz")

# Load  the jump sound
jump_sound = pygame.mixer.Sound("sounds/player/jump_sound2.wav")
jump_sound2 = pygame.mixer.Sound("sounds/player/jump_sound.wav")
# Creating the player
player = Player(color = (255, 248, 194), size=50, x=375, y=275, speed=.5, gravity=.007, jump_strength=2, jump_sound=jump_sound, jump_sound2=jump_sound2)

# Game Loop
running = True
while running:
    # Event handling
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                # Just pressed key for up
                player.jump()

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