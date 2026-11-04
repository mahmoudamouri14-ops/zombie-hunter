import pygame
import random
import sys

# تهيئة بايثون واللعبة
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Hunter")

# الألوان
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
BLACK = (20, 20, 20)

clock = pygame.time.Clock()

# اللاعب
player_x = WIDTH // 2
player_y = HEIGHT - 60
player_speed = 7

bullets = []
zombies = []

SPAWN_ZOMBIE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ZOMBIE, 1000)

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == SPAWN_ZOMBIE:
            z_x = random.randint(50, WIDTH - 50)
            zombies.append({'x': z_x, 'y': -50, 'speed': random.randint(2, 4)})
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append({'x': player_x + 20, 'y': player_y})

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    for bullet in bullets[:]:
        bullet['y'] -= 10
        if bullet['y'] < 0:
            bullets.remove(bullet)

    for zombie in zombies[:]:
        zombie['y'] += zombie['speed']
        
        for bullet in bullets[:]:
            if abs(bullet['x'] - zombie['x']) < 30 and abs(bullet['y'] - zombie['y']) < 30:
                if bullet in bullets: bullets.remove(bullet)
                if zombie in zombies: zombies.append(None)
                zombies.remove(zombie)
                score += 1
                break
                
        if zombie in zombies and zombie['y'] > HEIGHT:
            print("Game Over! Score:", score)
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, BLUE, (player_x, player_y, 40, 40))
    
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet['x'], bullet['y'], 5, 10))
        
    for zombie in zombies:
        pygame.draw.rect(screen, GREEN, (zombie['x'], zombie['y'], 40, 40))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
