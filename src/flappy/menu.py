import pygame
import sys
from pygame.locals import *  # Basic pygame imports
from flappy.flappy_constants import *
from flappy.flappy_game import main_game
from flappy.draw_game import *
import time

## @brief This function displays the main menu
#  @details This function is an infinite while loop that displays the main menu sprites. Upon starting the game or closing the application, the loop breaks
def main_menu():
    while True:
        for event in pygame.event.get():
            # if user clicks on 'x' button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                import Launcher
                Launcher.Launcher.displayLauncher()

            # If the user presses space or up key, start the game for them
            elif event.type ==KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                t_end = time.time() + 5
                while time.time() < t_end:
                    pygame.draw.rect(SCREEN, WHITE, [0,0,1280,800])
                    draw_back_ground()
                    SCREEN.blit(GAME_SPRITES['start'], (0, 0))  
                    draw_bird(int(SCREENWIDTH/5), int(SCREENWIDTH/2))
                    draw_ground()
                    pygame.draw.rect(SCREEN, WHITE, [280,0,991,800])
                    pygame.draw.rect(SCREEN, WHITE, [0,512,991,289])
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)
                return
            else:
                pygame.draw.rect(SCREEN, WHITE, [0,0,1280,800])
                SCREEN.blit(GAME_SPRITES['main_menu'], (0, 0))  
                pygame.draw.rect(SCREEN, WHITE, [280,0,991,800])
                pygame.draw.rect(SCREEN, WHITE, [0,512,991,289])
                pygame.display.update()
                FPSCLOCK.tick(FPS)
        
