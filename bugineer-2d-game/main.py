import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player attributes
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 7

# Enemy attributes
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 0
enemy_speed = 5

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(0, WIDTH - enemy_size)

    # Draw player and enemy
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    # Collision detection
    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(FPS)
