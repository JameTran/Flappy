import os
import pygame
import sys
import math
import random
from pygame.locals import *

scr_size = (width, height) = (1280,800)
screen = pygame.display.set_mode((scr_size))

"""
A paddle class which represents a real world Paddle.
The class is initialized by passing 5 parameters, i.e
x,y : the x and y coordinates of the paddle to determine its position
sizex,sizey : the width and height of the paddle which determines its size
color : the color of the paddle in (R,G,B) format
"""
class Paddle(pygame.sprite.Sprite):
    def __init__(self,x,y,sizex,sizey,color):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.color = color
        self.image = pygame.Surface((sizex,sizey),pygame.SRCALPHA,32)
        self.image = self.image.convert_alpha()
        pygame.draw.rect(self.image,self.color,(0,0,sizex,sizey))
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
        self.points = 0
        self.movement = [0,0]

    ## @brief A function which checks whether the paddle is going out of bounds and make corrections accordingly
    # 
    def checkBounds(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width

    ## @brief An update function which updates the state and position of the paddle
    # 
    def movePaddle(self):
        self.rect = self.rect.move(self.movement)
        self.checkBounds()

    #A draw function which draws our paddle onto the screen
    def drawPaddle(self):
        #pygame.draw.rect(self.image,self.color,(0,0,self.sizex,self.sizey))
        screen.blit(self.image,self.rect)