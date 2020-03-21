import os
import pygame
import sys
import math
import random
from pygame.locals import *

"""
Just like the Paddle class, this is a Ball class which represents a real world ball
It is also initialized by taking in 5 parameters, i.e
x,y : x and y coordinates of where the ball is to be placed initially
size : the diameter of the ball
color : color of the ball in (R,G,B) format
movement : determines how much the ball will move initially (in pixels) in [x,y] direction.
           It is [0,0] by default.
"""
scr_size = (width, height) = (1280,800)
screen = pygame.display.set_mode((scr_size))

class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y,size,color,movement=[0,0]):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.movement = movement
        self.image = pygame.Surface((size,size),pygame.SRCALPHA,32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image,self.color,(int(self.rect.width/2),int(self.rect.height/2)),int(size/2))
        self.rect.centerx = x
        self.rect.centery = y
        self.maxspeed = 10
        self.score = 0

    def checkBounds(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width

    #This scoreGoal functions detemines how the ball will move
    def scoreGoal(self):
        if self.rect.top == 0 or self.rect.bottom == height: #reverses the vertical velocity on collision with top and bottom walls
            self.movement[1] = -1*self.movement[1]
        if self.rect.left == 0: #resets the ball's position and notes that the point is scored by the ai
            self.resetBall()
            self.score = 1

        if self.rect.right == width: #resets the position of the ball and notes that the point is scored by the user
            self.resetBall()
            self.score = -1

        self.rect = self.rect.move(self.movement)
        self.checkBounds()

    def resetBall(self):
        self.rect.centerx = width/2
        self.rect.centery = height/2
        self.movement = [random.randrange(-1,2,2)*6,random.randrange(-1,2,2)*6]

    def draw(self):
        pygame.draw.circle(self.image,self.color,(int(self.rect.width/2),int(self.rect.height/2)),int(self.size/2))
        screen.blit(self.image,self.rect)