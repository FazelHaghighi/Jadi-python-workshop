# Example file showing a basic pygame "game loop"
import pygame
import random

width = 600
height = 400

snake = [(width / 2, height / 2)]

# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

direction = ""

def food_position():
    food = [random.randrange(10, (width-10), 10), 
            random.randrange(10, (height-10), 10)]
    return food

food = food_position()

def is_dead(snake):
    if snake[0][0] < 0 or snake[0][0] > width - 20:
        return True
    elif snake[0][1] < 0 or snake[0][1] > height - 20:
        return True
    return False

def draw_wall():
    for i in range(0, width, 10):
        pygame.draw.rect(screen, "red", (i, 0, 10, 10))
        pygame.draw.rect(screen, "red", (i, height-10, 10, 10))
    for i in range(0, height, 10):
        pygame.draw.rect(screen, "red", (0, i, 10, 10))
        pygame.draw.rect(screen, "red", (width-10, i, 10, 10))


def increase_snake(snake):
    # increase the size of the snake by five blocks
    for i in range(1):
        snake.append((snake[-1][0], snake[-1][1]))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
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
    
    # move the snake
    if direction == "u":
        snake.insert(0, (snake[0][0], snake[0][1] - 10))
    if direction == "d":
        snake.insert(0, (snake[0][0], snake[0][1] + 10))
    if direction == "r":
        snake.insert(0, (snake[0][0] + 10, snake[0][1]))
    if direction == "l":
        snake.insert(0, (snake[0][0] - 10, snake[0][1]))
    
    if len(snake) > 1:
        snake.pop()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    for s in snake:
        pygame.draw.rect(screen, "white", (s[0], s[1], 10, 10))
    pygame.draw.rect(screen, "green", (food[0], food[1], 10, 10))
    draw_wall()

    # print(snake[0][0], snake[0][1], food[0], food[1])
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        increase_snake(snake)
        food = food_position()
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 10

pygame.quit()
