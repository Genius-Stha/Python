import pygame
import time
import random
import os

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

highscore_file = "highscore.txt"
if not os.path.exists(highscore_file):
    with open(highscore_file, 'w') as f:
        f.write("0")

def get_highscore():
    with open(highscore_file, 'r') as f:
        return int(f.read())

def set_highscore(score):
    if score > get_highscore():
        with open(highscore_file, 'w') as f:
            f.write(str(score))

def Your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def High_score():
    value = score_font.render("High Score: " + str(get_highscore()), True, yellow)
    dis.blit(value, [350, 0])

def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        color = red if i == len(snake_list) - 1 else black
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

def pause_menu():
    paused = True
    while paused:
        dis.fill(blue)
        msg = font_style.render("Game Paused. Press R to Resume or Q to Quit", True, white)
        dis.blit(msg, [dis_width / 6, dis_height / 2])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def end_menu():
    selecting = True
    while selecting:
        dis.fill(blue)
        msg1 = font_style.render("You Lost!", True, red)
        msg2 = font_style.render("1. Play Again", True, white)
        msg3 = font_style.render("2. Return to Main Menu", True, white)
        dis.blit(msg1, [dis_width / 2 - 50, 100])
        dis.blit(msg2, [dis_width / 2 - 80, 150])
        dis.blit(msg3, [dis_width / 2 - 110, 190])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    gameLoop()
                elif event.key == pygame.K_2:
                    game_menu()

def game_menu():
    menu = True
    while menu:
        dis.fill(blue)
        title = score_font.render("Snake Game", True, yellow)
        play = font_style.render("1. Play", True, white)
        difficulty = font_style.render("2. Select Difficulty", True, white)
        color_opt = font_style.render("3. Change Snake Color", True, white)
        quit_game = font_style.render("Q. Quit", True, white)

        dis.blit(title, [200, 50])
        dis.blit(play, [200, 120])
        dis.blit(difficulty, [200, 160])
        dis.blit(color_opt, [200, 200])
        dis.blit(quit_game, [200, 240])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    gameLoop()
                elif event.key == pygame.K_2:
                    select_difficulty()
                elif event.key == pygame.K_3:
                    change_color()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def select_difficulty():
    global snake_speed
    selecting = True
    while selecting:
        dis.fill(blue)
        easy = font_style.render("1. Easy (10)", True, white)
        medium = font_style.render("2. Medium (15)", True, white)
        hard = font_style.render("3. Hard (25)", True, white)
        dis.blit(easy, [200, 120])
        dis.blit(medium, [200, 160])
        dis.blit(hard, [200, 200])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snake_speed = 10
                    selecting = False
                elif event.key == pygame.K_2:
                    snake_speed = 15
                    selecting = False
                elif event.key == pygame.K_3:
                    snake_speed = 25
                    selecting = False

def change_color():
    global red, black
    changing = True
    while changing:
        dis.fill(blue)
        opt1 = font_style.render("1. Red Head, Black Body", True, white)
        opt2 = font_style.render("2. Green Head, Yellow Body", True, white)
        dis.blit(opt1, [150, 150])
        dis.blit(opt2, [150, 190])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    red = (213, 50, 80)
                    black = (0, 0, 0)
                    changing = False
                elif event.key == pygame.K_2:
                    red = (0, 255, 0)
                    black = (255, 255, 102)
                    changing = False

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    direction = "RIGHT"

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    x1_change = -snake_block
                    y1_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    x1_change = snake_block
                    y1_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    y1_change = -snake_block
                    x1_change = 0
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    y1_change = snake_block
                    x1_change = 0
                    direction = "DOWN"

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 570 <= mouse[0] <= 590 and 10 <= mouse[1] <= 30:
            pygame.draw.rect(dis, yellow, [570, 10, 20, 20])
            if click[0] == 1:
                pause_menu()

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        High_score()

        pygame.draw.rect(dis, yellow, [570, 10, 20, 20])
        pause_text = font_style.render("||", True, black)
        dis.blit(pause_text, (573, 10))

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

        if game_close:
            set_highscore(Length_of_snake - 1)
            end_menu()

# Default speed
snake_speed = 15

game_menu()