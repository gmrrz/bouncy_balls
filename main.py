import pygame
import sys
import time
import random

from player import Player
from enemy import Enemy
from config import Config

def main():
    # Initialize Pygame
    pygame.init()

    # Setting screen size
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    pygame.display.set_caption("Bouncy Ballz")

    # Load sounds
    jump_sound = pygame.mixer.Sound("sounds/player/jump_sound2.wav")
    jump_sound2 = pygame.mixer.Sound("sounds/player/jump_sound.wav")
    smash_sound = pygame.mixer.Sound("sounds/player/smash.wav")

    # Creating the player
    player = Player(color=(255, 248, 194), size=50, x=375, y=275, speed=0.5, gravity=0.0015, jump_strength=0.9, dash_strength=5, dash_duration=0.2, jump_sound=jump_sound, jump_sound2=jump_sound2, smash_sound=smash_sound)

    # Dash cooldown variables
    last_dash_time = -Config.DASH_COOLDOWN  # Initialize to allow immediate dash

    # Font for displaying cooldown time
    font = pygame.font.SysFont(None, 36)

    # List to store enemies
    enemies = []
    enemy_spawn_time = time.time()

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
                last_dash_time = handle_keydown(event, player, current_time, keys, last_dash_time)

        # Move the player
        player.move(keys)

        # Spawn enemies at random intervals
        if current_time - enemy_spawn_time > Config.ENEMY_SPAWN_INTERVAL:
            spawn_enemy(enemies)
            enemy_spawn_time = current_time

        # BG color
        screen.fill((255, 232, 85))

        # Move and draw enemies
        for enemy in enemies:
            enemy.move()
            enemy.draw(screen)

        # Draw the player
        player.draw(screen)

        # Display dash cooldown
        display_dash_cooldown(screen, font, current_time, last_dash_time)

        # Check for collisions
        if check_collisions(player, enemies):
            print("Game Over!")
            running = False

        # Update the display
        pygame.display.update()

    # Quit the game
    pygame.quit()
    sys.exit()

def handle_keydown(event, player, current_time, keys, last_dash_time):
    if event.key == pygame.K_x:
        player.smash()
    if event.key == pygame.K_z:
        player.jump()
    if event.key == pygame.K_SPACE:
        if current_time - last_dash_time >= Config.DASH_COOLDOWN:
            if keys[pygame.K_LEFT]:
                player.start_dash(-1)  # Start dash to the left
                last_dash_time = current_time
            elif keys[pygame.K_RIGHT]:
                player.start_dash(1)  # Start dash to the right
                last_dash_time = current_time
    return last_dash_time

def display_dash_cooldown(screen, font, current_time, last_dash_time):
    cooldown_time_left = max(0, Config.DASH_COOLDOWN - (current_time - last_dash_time))
    cooldown_text = font.render(f"Dash Cooldown: {cooldown_time_left:.1f}s", True, (0, 0, 0))
    screen.blit(cooldown_text, (Config.SCREEN_WIDTH - cooldown_text.get_width() - 10, Config.SCREEN_HEIGHT - cooldown_text.get_height() - 10))

def spawn_enemy(enemies):
    # Spawn enemy only from the right wall
    x = Config.SCREEN_WIDTH
    y = random.randint(0, Config.SCREEN_HEIGHT)
    enemy = Enemy(x, y, Config.ENEMY_SPEED)
    enemies.append(enemy)

def check_collisions(player, enemies):
    player_rect = pygame.Rect(player.x, player.y, player.size, player.size)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
        if player_rect.colliderect(enemy_rect):
            return True
    return False

if __name__ == "__main__":
    main()