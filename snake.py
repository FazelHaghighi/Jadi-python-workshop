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
    if snake[0][0] < 0 or snake[0][0] > width:
        return True
    elif snake[0][1] < 0 or snake[0][1] > height:
        return True
    return False


def increase_snake(snake):
    # increase the size of the snake by five blocks
    for i in range(5):
        snake.append((snake[-1][0], snake[-1][1]))
        
    return snake


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
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == "d":
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direction == "r":
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direction == "l":
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen, "white", (snake[0][0], snake[0][1], 10, 10))
    pygame.draw.rect(screen, "green", (food[0], food[1], 10, 10))

    # print(snake[0][0], snake[0][1], food[0], food[1])
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        increase_snake(snake)
        print("ate food")
        food = food_position()
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()
