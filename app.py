import pygame
import random
pygame.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10

font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block , snake_list):
    for x in snake_list:
        pygame.draw.rect(dis , white , [x[0] , x[1] , snake_block , snake_block])

def message(msg , color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg , [10,dis_height-50])

def losing_message(msg , game_close):
    while game_close == True:
        message(msg, red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_close = False
                    pygame.quit()
                if event.key == pygame.K_c:
                    game_loop()

def game_loop():
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0       
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # generating food on random coordinates
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    # checking the direction of the snake
    direction = ""
    reverse = False

    game_over = False
    while not game_over:
        # moving the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                    if direction == "right":
                        reverse = True
                    else:
                        reverse = False
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                    if direction == "left":
                        reverse = True
                    else:
                        reverse = False
                    direction = "right"
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                    if direction == "down":
                        reverse = True
                    else:
                        reverse = False
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
                    if direction == "up":
                        reverse = True
                    else:
                        reverse = False
                    direction = "down"
        
        # if snake is touches the borders then the game is over
        # if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        #     losing_message("You Lost! You went out of bounds. Press C-Play Again or Q-Quit", True)

        # making sure the snake is always on the screen and not going out of bounds
        x1 = (x1+x1_change) % dis_width
        y1 = (y1+y1_change) % dis_height

        dis.fill(black)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # if snake touches itself then the game is over
        for x in snake_list[:-1]:
            if x == snake_Head and reverse == False:
                pygame.display.update()
                losing_message("You Lost! Your snake touched itself. Press C-Play Again or Q-Quit", True)

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        pygame.display.update()

        # the food is eaten and the snake grows
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

game_loop()