import pygame
from pygame.locals import *
import random

WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10

def collision(pos1, pos2):
    return pos1 == pos2

def off_limits(pos):
    return not (0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1])

def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0] // PIXEL_SIZE - 1) * PIXEL_SIZE
    y = random.randint(0, WINDOW_SIZE[1] // PIXEL_SIZE - 1) * PIXEL_SIZE
    return x, y

def restart_game():
    global snake_pos, apple_pos, snake_direction, score
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()
    score = 0  # Reinicia o placar

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Snake Game")

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((255, 255, 255))
snake_direction = K_LEFT

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()

# Configuração do placar
font = pygame.font.Font(None, 36)
score = 0

while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(apple_surface, apple_pos)

    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))  # Aumenta o tamanho da cobra
        apple_pos = random_on_grid()
        score += 1  # Incrementa o placar

    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    for i in range(len(snake_pos)-1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            restart_game()
        snake_pos[i] = snake_pos[i-1]

    if off_limits(snake_pos[0]):
        restart_game()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    # Renderiza o placar no canto superior esquerdo
    score_text = font.render(f"Maçãs: {score}", True, (255, 255, 255))

    screen.blit(score_text, (5, 5))

    pygame.display.update()
