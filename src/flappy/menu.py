import pygame
import sys
from pygame.locals import *  # Basic pygame imports
from flappy.flappy_constants import *
from flappy.flappy_game import main_game


def main_menu():
     
    """
    Shows main_menu images on the screen
    """

    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT/2)
    #messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    #messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on 'x' button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                import Launcher
                Launcher.Launcher.displayLauncher()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                pygame.draw.rect(SCREEN, WHITE, [0,0,1280,800])
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                #SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey ))    
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                pygame.draw.rect(SCREEN, WHITE, [280,0,991,800])
                pygame.draw.rect(SCREEN, WHITE, [0,512,991,289])
                pygame.display.update()
                FPSCLOCK.tick(FPS)
        
