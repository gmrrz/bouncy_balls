import pygame
import sys
import time
import random
import os

from player import Player
from enemy import Enemy
from config import Config

# Game states
MAIN_MENU = 'main_menu'
GAME_MODES = 'game_modes'
EASY = 'easy'
NORMAL = 'normal'
HARD = 'hard'

def main():
    pygame.init()

    # Setting screen size
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    pygame.display.set_caption("Bouncy Ballz")

    # Load sounds
    jump_sound = pygame.mixer.Sound("sounds/player/jump_sound2.wav")
    jump_sound2 = pygame.mixer.Sound("sounds/player/jump_sound.wav")
    smash_sound = pygame.mixer.Sound("sounds/player/smash.mp3")

    # Font for displaying text
    font = pygame.font.SysFont(None, 36)

    # Game state
    game_state = MAIN_MENU

    # Main loop
    while True:
        if game_state == MAIN_MENU:
            game_state = main_menu(screen, font)
        elif game_state == GAME_MODES:
            game_state = game_modes(screen, font)
        elif game_state == EASY:
            run_game(screen, font, jump_sound, jump_sound2, smash_sound, EASY)
            game_state = MAIN_MENU
        elif game_state == NORMAL:
            run_game(screen, font, jump_sound, jump_sound2, smash_sound, NORMAL)
            game_state = MAIN_MENU
        elif game_state == HARD:
            run_game(screen, font, jump_sound, jump_sound2, smash_sound, HARD)
            game_state = MAIN_MENU

def main_menu(screen, font):
    while True:
        screen.fill((0, 0, 0))
        title_text = font.render("Bouncy Ballz", True, (255, 255, 255))
        start_text = font.render("Start Game", True, (255, 255, 255))
        game_modes_text = font.render("Game Modes", True, (255, 255, 255))
        quit_text = font.render("Quit", True, (255, 255, 255))

        screen.blit(title_text, (Config.SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
        screen.blit(start_text, (Config.SCREEN_WIDTH // 2 - start_text.get_width() // 2, 200))
        screen.blit(game_modes_text, (Config.SCREEN_WIDTH // 2 - game_modes_text.get_width() // 2, 300))
        screen.blit(quit_text, (Config.SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 400))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if is_button_clicked(start_text, Config.SCREEN_WIDTH // 2, 200, mouse_x, mouse_y):
                    return EASY
                if is_button_clicked(game_modes_text, Config.SCREEN_WIDTH // 2, 300, mouse_x, mouse_y):
                    return GAME_MODES
                if is_button_clicked(quit_text, Config.SCREEN_WIDTH // 2, 400, mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

def game_modes(screen, font):
    while True:
        screen.fill((0, 0, 0))
        easy_text = font.render("Easy", True, (255, 255, 255))
        normal_text = font.render("Normal", True, (255, 255, 255))
        hard_text = font.render("Hard", True, (255, 255, 255))
        back_text = font.render("Back", True, (255, 255, 255))

        screen.blit(easy_text, (Config.SCREEN_WIDTH // 2 - easy_text.get_width() // 2, 200))
        screen.blit(normal_text, (Config.SCREEN_WIDTH // 2 - normal_text.get_width() // 2, 300))
        screen.blit(hard_text, (Config.SCREEN_WIDTH // 2 - hard_text.get_width() // 2, 400))
        screen.blit(back_text, (Config.SCREEN_WIDTH // 2 - back_text.get_width() // 2, 500))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if is_button_clicked(easy_text, Config.SCREEN_WIDTH // 2, 200, mouse_x, mouse_y):
                    return EASY
                if is_button_clicked(normal_text, Config.SCREEN_WIDTH // 2, 300, mouse_x, mouse_y):
                    return NORMAL
                if is_button_clicked(hard_text, Config.SCREEN_WIDTH // 2, 400, mouse_x, mouse_y):
                    return HARD
                if is_button_clicked(back_text, Config.SCREEN_WIDTH // 2, 500, mouse_x, mouse_y):
                    return MAIN_MENU

def is_button_clicked(text, center_x, y, mouse_x, mouse_y):
    text_rect = text.get_rect(center=(center_x, y))
    return text_rect.collidepoint(mouse_x, mouse_y)

def run_game(screen, font, jump_sound, jump_sound2, smash_sound, mode):
    player = Player(color=(255, 248, 194), size=50, x=375, y=275, speed=0.5, gravity=0.0015, jump_strength=0.9, jump_sound=jump_sound, jump_sound2=jump_sound2, smash_sound=smash_sound)
    enemies = []
    enemy_spawn_time = time.time()
    start_time = time.time()
    score = 0
    high_score = load_high_score(mode)

    running = True
    while running:
        current_time = time.time()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                handle_keydown(event, player)

        player.move(keys)
        if current_time - enemy_spawn_time > Config.ENEMY_SPAWN_INTERVAL:
            spawn_enemy(enemies)
            enemy_spawn_time = current_time

        screen.fill((255, 232, 85))
        for enemy in enemies:
            enemy.move()
            enemy.draw(screen)
        player.draw(screen)

        score = int(current_time - start_time)
        display_score(screen, font, score)

        if check_collisions(player, enemies):
            print("Game Over!")
            running = False

        pygame.display.update()

    if score > high_score:
        save_high_score(mode, score)
        high_score = score

    display_game_over(screen, font, score, high_score)

def handle_keydown(event, player):
    if event.key == pygame.K_x:
        player.smash()
    if event.key == pygame.K_z:
        player.jump()

def display_score(screen, font, score):
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

def display_game_over(screen, font, score, high_score):
    screen.fill((0, 0, 0))
    game_over_text = font.render("Game Over!", True, (255, 0, 0))
    score_text = font.render(f"Your Score: {score}", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
    screen.blit(game_over_text, (Config.SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, Config.SCREEN_HEIGHT // 3))
    screen.blit(score_text, (Config.SCREEN_WIDTH // 2 - score_text.get_width() // 2, Config.SCREEN_HEIGHT // 2))
    screen.blit(high_score_text, (Config.SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, Config.SCREEN_HEIGHT // 2 + 50))
    pygame.display.update()
    time.sleep(3)

def load_high_score(mode):
    file_name = f"high_score_{mode}.txt"
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return int(file.read())
    return 0

def save_high_score(mode, high_score):
    file_name = f"high_score_{mode}.txt"
    with open(file_name, "w") as file:
        file.write(str(high_score))

def spawn_enemy(enemies):
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