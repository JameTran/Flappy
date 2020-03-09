import pygame
from pygame.locals import *
import sys

def ball_animation():
    global ball_speed_x, ball_speed_y

    # Moves the ball by one multiple of the ball speed
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Keeps the ball in the boundaries
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Correct speed (direction) for collisions
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangles
ball = pygame.Rect(int(screen_width/2 - 15), int(screen_height/2 - 15), 30, 30)
player = pygame.Rect(screen_width - 20, int(screen_height/2 - 70), 10, 140)
opponent = pygame.Rect(10, int(screen_height/2 - 70), 10, 140)

# Colours for objects and background
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

#Defining the beginning speed of the ball
ball_speed_x = 7
ball_speed_y = 7

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            sys.exit()
    
    # Call ball_animation
    ball_animation()
    
    # Visuals; drawn from top to bottom
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    
    # Updating the window: redraws the screen in each iteration
    pygame.display.flip()
    clock.tick(60)