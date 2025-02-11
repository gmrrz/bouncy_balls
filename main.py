import pygame 
import sys
import time

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

# Load the smash sound
smash_sound = pygame.mixer.Sound("sounds/player/smash.wav")

# Creating the player
player = Player(color = (255, 248, 194), size=50, x=375, y=275, speed=.5, gravity=.0015, jump_strength=.9, dash_strength= 15, dash_duration = .05, jump_sound=jump_sound, jump_sound2=jump_sound2, smash_sound=smash_sound)

# Variable to track double-tap for dashing
last_left_press_time = 0
last_right_press_time = 0
double_tap_threshold = 0.3 # Time in seconds to register a double tap

# Dash cooldown var
dash_cooldown = 2
last_dash_time = -dash_cooldown

# Font for displaying cooldown time
font = pygame.font.SysFont(None, 36)

# Game Loop
running = True
while running:
    # Event handling
    current_time = time.time()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                player.smash()
            if event.key == pygame.K_z:
                # Just pressed key for up
                player.jump()
            if event.key == pygame.K_LEFT:
                if current_time - last_left_press_time < double_tap_threshold and current_time - last_dash_time >= dash_cooldown:
                    player.start_dash(-1)
                    last_dash_time = current_time
                last_left_press_time = current_time
            if event.key == pygame.K_RIGHT:
                if current_time - last_right_press_time < double_tap_threshold and current_time - last_dash_time >= dash_cooldown:
                    player.start_dash(1)
                    last_dash_time = current_time
                last_right_press_time = current_time
    # Move the player
    player.move(keys)

    # BG colorr
    screen.fill((255, 232, 85))

    # Draw the player
    player.draw(screen)

    # Displaying dash cooldown
    cooldown_time_left = max (0, dash_cooldown - (current_time - last_dash_time))
    cooldown_text = font.render(f"Dash Cooldown: {cooldown_time_left:.1f}s", True, (255, 255, 255))
    screen.blit(cooldown_text, (screen_width - cooldown_text.get_width() - 10, screen_height - cooldown_text.get_height() - 10))


    # Update the display
    pygame.display.update()


# Quits Game
pygame.quit()
sys.exit()