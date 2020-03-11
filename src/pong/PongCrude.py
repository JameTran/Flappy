import pygame
from pygame.locals import *
import sys
import random

# def countdown():
#     intro = True
#     mouse = pygame.mouse.get_pos()
#     while intro:
#         if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
#             pygame.draw.rect(screen, (0,255,0),(150,450,100,50))
#         else:
#             pygame.draw.rect(screen, (0,180,0),(150,450,100,50))
#             pygame.draw.rect(screen, (200,0,0),(550,450,100,50))
#             pygame.display.update()
#             clock.tick(15)

# def paused():
#     global pause
#     pause = True
#     while pause:
#         clock.tick(0.5)
#         pause = False


def ball_animation():
    global ball_speed_x, ball_speed_y

    # Moves the ball by one multiple of the ball speed
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Keeps the ball in the boundaries
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    # Correct speed (direction) for collisions
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if ball_speed_x > 0:
        if opponent.top < ball.y:
            opponent.top += opponent_speed
        if opponent.bottom > ball.y:
            opponent.bottom -= opponent_speed
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= screen_height:
            opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (int(screen_width/2), int(screen_height/2))
    ball_speed_y *= random.choice((1,-1,))
    ball_speed_x *= random.choice((1,-1,))
    clock.tick(3)


pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangles
ball = pygame.Rect(int(screen_width/2 - 15), int(screen_height/2 - 15), 20, 20)
player = pygame.Rect(20, int(screen_height/2 - 70), 15, 140)
opponent = pygame.Rect(screen_width - 35, int(screen_height/2 - 70), 15, 140)

# Colours for objects and background
bg_color = pygame.Color(0,0,100)
light_grey = (200, 200, 200)

#Defining the beginning speed of the ball
ball_speed_x = 6 * random.choice((1,-1,))
ball_speed_y = 6 * random.choice((1,-1,))
player_speed = 0
opponent_speed = 7

# pause = False
# countdown()
while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_DOWN:
                player_speed += 7
            if event.key == K_UP:
                player_speed -= 7
            # if event.key == K_SPACE:
            #     pause = True
            #     paused()
        if event.type == pygame.KEYUP:
            if event.key == K_DOWN:
                player_speed -= 7
            if event.key == K_UP:
                player_speed += 7
        
    
    # Call ball_animation
    ball_animation()
    player_animation()
    opponent_ai()
    
    # Visuals; drawn from top to bottom
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    
    # Updating the window: redraws the screen in each iteration
    pygame.display.flip()
    clock.tick(60)