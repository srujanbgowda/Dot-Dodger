import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dot Dodger")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player
player_size = 40
player = pygame.Rect(WIDTH//2 - player_size//2, HEIGHT - 60, player_size, player_size)
player_speed = 5

# Enemy block
enemy_size = 40
enemy = pygame.Rect(random.randint(0, WIDTH - enemy_size), 0, enemy_size, enemy_size)
enemy_speed = 5

# Clock
clock = pygame.time.Clock()

# Main game loop
run = True
while run:
    clock.tick(60)
    win.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Move enemy
    enemy.y += enemy_speed
    if enemy.y > HEIGHT:
        enemy.y = 0
        enemy.x = random.randint(0, WIDTH - enemy_size)

    # Check collision
    if player.colliderect(enemy):
        print("Game Over!")
        run = False

    # Draw
    pygame.draw.rect(win, GREEN, player)
    pygame.draw.rect(win, RED, enemy)
    pygame.display.update()

pygame.quit()