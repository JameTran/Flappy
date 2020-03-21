import sys
import random
import pygame
from pygame.locals import *
from Ball import *
from Paddle import *

#initializing pygame
pygame.init()

#setting the FPS or number of Frames per Second
FPS = 60

#Setting the screen size
scr_size = (width,height) = (1280,800)

#creating a clock object from pygame.time.Clock class
clock = pygame.time.Clock()

#Declaring various color values
bg = (0,5,35)
light_grey = (200,200,200)
amber = (205,190,0)
enemy_red = (200,5,0)

"""
Creating our game screen by passing its screen size as the parameter,
and setting its caption as 'Pong'
"""
screen = pygame.display.set_mode(scr_size)
pygame.display.set_caption('Pong')

"""
A function used to display text on the screen
It takes in 4 parameters, i.e
text : the text which is to be printed. Has to be a string
fontsize : the fontsize of the text to be printed. Must be an integer
x,y : The x and y coordinates where we want our text to be printed
color : The color of the text. Its has to be in (R,G,B) format where R, G and B takes values from 0 to 255
"""
def displaytext(text,fontsize,x,y,color):
    font = pygame.font.SysFont('rockwell', fontsize, True)
    text = font.render(text, 1, color)
    textpos = text.get_rect(centerx=x, centery=y)
    screen.blit(text, textpos)

"""
A function which moves the ai's paddle
The concept behind this function is the same as that used in the real world,i.e
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
        ai.movement[1] = 0


#The main function of our program
def playGame():
    gameOver = False #Sets the initial state of the game
    paddle = Paddle(int(width/10),int(height/2),int(width/90),int(height/8),light_grey) #creating an object for the user's paddle
    ai = Paddle(int(width - width/10),int(height/2),int(width/90),int(height/8),enemy_red) #creating an object for the ai's paddle
    ball = Ball(int(width/2),int(height/2),12,amber,[6,6]) #creating an object for the ball

    while not gameOver: #running our game loop
        for event in pygame.event.get(): #checks for various events in pygame, like keypress, mouse movement, etc
            if event.type == pygame.QUIT: #checks, if the user has clicked the close button
                quit()                    #quits the program

            if event.type == pygame.KEYDOWN: #checks whether a key has been pressed or not
                if event.key == pygame.K_UP: #If user has pressed the UP key
                    paddle.movement[1] = -8  #Paddle moves upwards
                elif event.key == pygame.K_DOWN: #If user has pressed the down key
                    paddle.movement[1] = 8       #Paddle moves downwards
            if event.type == pygame.KEYUP:    #If the user lifts the key
                paddle.movement[1] = 0        #Paddle stops moving

        aimove(ai,ball) #moves the ai's paddle

        screen.fill(bg) #fills the entire screen with bg color

        #welcomeScreen() #presents the introductory screen

        #drawing user's paddle, ai's paddle and ball
        paddle.drawPaddle()
        ai.drawPaddle()
        ball.draw()

        #displaying the points scored by the user and ai
        displaytext(str(paddle.points),20,width/8,25,(255,255,255))
        displaytext(str(ai.points),20,width - width/8,25,(255,255,255))

        """
        using pygame.sprite.collide_mask function to check for 'pixel perfect' collision
        between user's and ai's paddle with the ball
        The collision is based on the real world concept of perfectly elastic collisions.
        hence, whenever the ball strikes the paddle (placed vertically), the horizontal velocity is reversed,
        while the vertical velocity is equal to the relative velocity of ball w.r.t the paddle.
        In order to add some randomness, some error is introduced to the relative velocity of the ball and the paddle, i.e
        The paddle's velocity is multiplied by a factor between 0.5 to 1 before calculating the relative velocity.
        """
        if pygame.sprite.collide_mask(paddle,ball):
            ball.movement[0] = -1*ball.movement[0]
            ball.movement[1] = ball.movement[1] - int(0.1*random.randrange(5,10)*paddle.movement[1])
            if ball.movement[1] > ball.maxspeed:
                ball.movement[1] = ball.maxspeed
            if ball.movement[1] < -1*ball.maxspeed:
                ball.movement[1] = -1*ball.maxspeed

        if pygame.sprite.collide_mask(ai,ball):
            ball.movement[0] = -1*ball.movement[0]
            ball.movement[1] = ball.movement[1] - int(0.1*random.randrange(5,10)*ai.movement[1])
            if ball.movement[1] > ball.maxspeed:
                ball.movement[1] = ball.maxspeed
            if ball.movement[1] < -1*ball.maxspeed:
                ball.movement[1] = -1*ball.maxspeed

        #checks whether user or ai scored a point and increments accordingly
        if ball.score == 1:
            ai.points += 1
            ball.score = 0
        elif ball.score == -1:
            paddle.points += 1
            ball.score = 0

        #updating the states of user's paddle, ai's paddle and ball
        paddle.movePaddle()
        ball.scoreGoal()
        ai.movePaddle()

        #updating the entire display"""
        pygame.display.update()

        #adding the time delay based on the number of 'Frames per Second'
        clock.tick(FPS)

    #Exiting the program by safely quitting pygame
    pygame.quit()
    quit()
