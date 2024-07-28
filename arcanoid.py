import pygame
import sys
import time
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Арканоид")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Параметры ракетки
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10

# Параметры мяча
BALL_SIZE = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = -5

# Параметры кирпичей
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
BRICK_ROWS = 5
BRICK_COLUMNS = 10

# Инициализация объектов игры
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLUMNS):
        bricks.append(pygame.Rect(col * (BRICK_WIDTH + 10) + 35, row * (BRICK_HEIGHT + 10) + 50, BRICK_WIDTH, BRICK_HEIGHT))

# Счетчики
ball_hits = 0
bricks_hit = 0
start_time = time.time()

# Основной цикл игры
running = True
while running:
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Движение ракетки
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and paddle.left > 0:
        paddle.left -= PADDLE_SPEED
    if keys[K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.right += PADDLE_SPEED

    # Движение мяча
    ball.left += BALL_SPEED_X
    ball.top += BALL_SPEED_Y

    # Отражение мяча от стенок
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        BALL_SPEED_X = -BALL_SPEED_X
    if ball.top <= 0:
        BALL_SPEED_Y = -BALL_SPEED_Y
    if ball.colliderect(paddle):
        BALL_SPEED_Y = -BALL_SPEED_Y
        ball_hits += 1

    # Проверка столкновения с кирпичами
    for brick in bricks[:]:
        if ball.colliderect(brick):
            BALL_SPEED_Y = -BALL_SPEED_Y
            bricks.remove(brick)
            bricks_hit += 1

    # Проверка проигрыша
    if ball.top >= SCREEN_HEIGHT:
        print(f"Игра окончена! Вы отразили {ball_hits} мячей и выбили {bricks_hit} кирпичей.")
        running = False

    # Проверка ограничения времени
    elapsed_time = time.time() - start_time
    if elapsed_time >= 60:
        print(f"Время вышло! Вы отразили {ball_hits} мячей и выбили {bricks_hit} кирпичей.")
        running = False

    # Рендеринг объектов
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

    # Обновление экрана
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sys.exit()