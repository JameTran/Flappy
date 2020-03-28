import sys
import random
import pygame
from pygame.locals import *
from pong.Ball import *
from pong.Paddle import *

#initializing pygame
pygame.init()

#setting the FPS or number of Frames per Second
FPS = 60

#Setting the screen size
scr_size = (width,height) = (1280,800)
clock = pygame.time.Clock()

#Declaring various color values
bg = (0,5,35)
light_grey = (200,200,200)
amber = (205,190,0)
enemy_red = (200,5,0)
the ai paddle will try to chase the ball based on its coordinates
"""
def aimove(ai,ball):
    if ball.movement[0] > 0: #ensures that the ai moves only when the ball is directed towards it
        #the extra addition of ai.rect.height/5 ensures that the ai will miss the ball sometimes
        if ball.rect.bottom > ai.rect.bottom + ai.rect.height/5:
            ai.movement[1] = 8
        elif ball.rect.top < ai.rect.top - ai.rect.height/5:
            ai.movement[1] = -8
        else:
            ai.movement[1] = 0
    else:
#The main function of our program
def playGame():
    gameOver = False #Sets the initial state of the game
    paddle = Paddle(int(width/10),int(height/2),int(width/90),int(height/8),light_grey) #creating an object for the user's paddle
    ai = Paddle(int(width - width/10),int(height/2),int(width/90),int(height/8),enemy_red) #creating an object for the ai's paddle
    ball = Ball(int(width/2),int(height/2),12,amber,[6,6]) #creating an object for the ball

    while not gameOver: #running our game loop
        for event in pygame.event.get(): #checks for various events in pygame, like keypress, mouse movement, etc
                    paddle.movement[1] = -8  #Paddle moves upwards
                elif event.key == pygame.K_DOWN: #If user has pressed the down key
                    paddle.movement[1] = 8       #Paddle moves downwards
            if event.type == pygame.KEYUP:    #If the user lifts the key
                paddle.movement[1] = 0        #Paddle stops moving


    #Exiting the program by safely quitting pygame
    pygame.quit()
    quit()
