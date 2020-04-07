from flappy.flappy_constants import *
import pygame
from pygame.locals import *

## @brief A function to draw the player on to the screen
def draw_bird(x, y):
    SCREEN.blit(GAME_SPRITES['player'], (x, y))

## @brief A function to draw the ground on to the screen
def draw_ground():
    SCREEN.blit(GAME_SPRITES['base'], (0, GROUNDY))

## @brief A function to draw the background on to the screen
def draw_back_ground():
    SCREEN.blit(GAME_SPRITES['background'], (0, 0))

## @brief A function to draw the pipes on to the screen
#  @param upper_pipes The list of all upper pipes currently in the game
#  @param lower_pipe The list of all lower pipes currently in the game
def draw_pipes(upper_pipes, lower_pipes):
    for upper_pipe, lower_pipe in zip(upper_pipes, lower_pipes):
        SCREEN.blit(GAME_SPRITES['pipe'][0], (upper_pipe['x'], upper_pipe['y']))
        SCREEN.blit(GAME_SPRITES['pipe'][1], (lower_pipe['x'], lower_pipe['y']))

## @brief A function to draw the score on to the screen
#  @details Recieives the score, and draws the number sprites on to the screen with an offset between the sprites to ensure readability
def draw_score(score):
    myDigits = [int(x) for x in list(str(score))]
    width = 0
    for digit in myDigits:
        width += GAME_SPRITES['numbers'][digit].get_width()
    Xoffset = (SCREENWIDTH - width)/2

    for digit in myDigits:
        SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
        Xoffset += GAME_SPRITES['numbers'][digit].get_width()

## @brief A function to remove pipes from the game
#  @details When the pipes move to the leftmost, this function removes them from the game
#  @param upper_pipes The list of all upper pipes currently in the game
#  @param lower_pipe The list of all lower pipes currently in the game
def remove_pipes(upper_pipes, lower_pipes):
    upper_pipes.pop(0)
    lower_pipes.pop(0)

## @brief A function to draw the score on to the screen
#  @details Recieives the score, and draws the number sprites on to the screen with an offset between the sprites to ensure readability at the end of the game. The difference between this function and the other draw_score function is that these numbers are drawn lower, in order to fit into the end game screen
def draw_menuScore(score):
    myDigits = [int(x) for x in list(str(score))]
    width = 0
    for digit in myDigits:
        width += GAME_SPRITES['numbers'][digit].get_width()
    Xoffset = (SCREENWIDTH - width)/2

    for digit in myDigits:
        SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.4))
        Xoffset += GAME_SPRITES['numbers'][digit].get_width()
