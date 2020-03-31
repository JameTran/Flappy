import random  # For generating random numbers
import sys  # use sys.exit to close game
import pygame
from pygame.locals import *  # Basic pygame imports
import os
print(os.getcwd())


# Global Variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'sprites/bird.png'
BACKGROUND = 'sprites/background.png'
PIPE = 'sprites/pipe.png'


def main_menu():
    """
    Shows main_menu images on the screen
    """

    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on 'x' button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey ))    
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)


    


if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init()  # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('sprites/0.png').convert_alpha(),
        pygame.image.load('sprites/1.png').convert_alpha(),
        pygame.image.load('sprites/2.png').convert_alpha(),
        pygame.image.load('sprites/3.png').convert_alpha(),
        pygame.image.load('sprites/4.png').convert_alpha(),
        pygame.image.load('sprites/5.png').convert_alpha(),
        pygame.image.load('sprites/6.png').convert_alpha(),
        pygame.image.load('sprites/7.png').convert_alpha(),
        pygame.image.load('sprites/8.png').convert_alpha(),
        pygame.image.load('sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] = pygame.image.load('sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), pygame.image.load(PIPE).convert_alpha())
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('audio/wing.wav')

    
    while True:
        main_menu() # Shows welcome screen to the user until he presses a button


    

