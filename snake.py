import pygame
import random

# Constants
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 10
FPS = 10
WALL_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (128, 0, 128)  # Purple
SNAKE_COLOR = (255, 255, 255)  # White
FOOD_COLOR = (0, 255, 0)  # Green

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Snake initialization
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = ""
running = True

def get_food_position():
    x = random.randrange(BLOCK_SIZE, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    y = random.randrange(BLOCK_SIZE, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    return x, y

food = get_food_position()

def is_dead(snake):
    x, y = snake[0]
    return not (0 <= x < WIDTH and 0 <= y < HEIGHT)

def draw_walls():
    for i in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.rect(screen, WALL_COLOR, (i, 0, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, WALL_COLOR, (i, HEIGHT - BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    for i in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.rect(screen, WALL_COLOR, (0, i, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, WALL_COLOR, (WIDTH - BLOCK_SIZE, i, BLOCK_SIZE, BLOCK_SIZE))

def increase_snake(snake):
    # Increase the size of the snake by one block
    snake.append(snake[-1])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "d":
        direction = "u"
    if keys[pygame.K_DOWN] and direction != "u":
        direction = "d"
    if keys[pygame.K_RIGHT] and direction != "l":
        direction = "r"
    if keys[pygame.K_LEFT] and direction != "r":
        direction = "l"

    if is_dead(snake):
        running = False

    dx, dy = 0, 0
    if direction == "u":
        dy = -BLOCK_SIZE
    elif direction == "d":
        dy = BLOCK_SIZE
    elif direction == "r":
        dx = BLOCK_SIZE
    elif direction == "l":
        dx = -BLOCK_SIZE

    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    if len(snake) > 1:
        snake.pop()

    screen.fill(BACKGROUND_COLOR)
    for s in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (s[0], s[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    draw_walls()

    if snake[0] == food:
        increase_snake(snake)
        food = get_food_position()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
