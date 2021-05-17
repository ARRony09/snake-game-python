import pygame
import time
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
yellow =(255,255,102)
red=(213,50,80)
blue=(0,0,255)
green =(50,153,253)

dis_width = 600
dis_height = 400

snake_block = 10

dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake game by AR Rony")


clock = pygame.time.Clock()

font_style =pygame.font.SysFont("bahnschrift",25)
score_font=pygame.font.SysFont("comicsansms",35)

def message(msg,color):
    mesg = font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width / 6, dis_height / 3])

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])

def yourScore(score):
    value = score_font.render("Your score "+str(score),True,yellow)
    dis.blit(value,[0,0])


def gameLoop():     # creating a function 
    game_over = False
    game_close = False
    x1=dis_width/2
    y1=dis_height/2

    x1_change = 0
    y1_change = 0

    snake_List=[]
    Length_of_snake = 1

    foodx=round(random.randrange(0,dis_width - snake_block)/10.0)*10.0
    foody=round(random.randrange(0,dis_height - snake_block)/10.0)*10.0
    
    while not game_over:
        
        while game_close == True:
            dis.fill(blue)
            message("You lost. Press C to continue or press Q to quit",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1>= dis_width or x1 < 0 or y1>=dis_height or y1<0:
            # if snake crash the bounderies
            game_close=True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis,green,[foodx,foody,10,10])
        snake_Head =[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        # when the length snake excceds , delete the snake_list which will wnd the game

        if len(snake_List)> Length_of_snake:
            del snake_List[0]

        # when snake crash with itself then ends the game
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block,snake_List)
        yourScore(Length_of_snake-1)


        # pygame.draw.rect(dis,black,[x1,y1,snake_block,snake_block])
        pygame.display.update()

        if x1==foodx and y1 == foody:
            foodx =round(random.randrange(0,dis_width - snake_block)/10.0)*10.0
            foody =round(random.randrange(0,dis_height -snake_block)/10.0)*10.0
            Length_of_snake += 1
        clock.tick(21)
    
    pygame.quit()
    quit()

gameLoop()

