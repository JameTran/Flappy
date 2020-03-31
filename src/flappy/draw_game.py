from flappy.flappy_constants import *
import pygame
from pygame.locals import *


def draw_bird(x, y):
    SCREEN.blit(GAME_SPRITES['player'], (x, y))


def draw_ground():
    SCREEN.blit(GAME_SPRITES['base'], (0, GROUNDY))


def draw_back_ground():
    SCREEN.blit(GAME_SPRITES['background'], (0, 0))


def draw_pipes(upper_pipes, lower_pipes):
    for upper_pipe, lower_pipe in zip(upper_pipes, lower_pipes):
        SCREEN.blit(GAME_SPRITES['pipe'][0], (upper_pipe['x'], upper_pipe['y']))
        SCREEN.blit(GAME_SPRITES['pipe'][1], (lower_pipe['x'], lower_pipe['y']))


def draw_score(score):
    myDigits = [int(x) for x in list(str(score))]
    width = 0
    for digit in myDigits:
        width += GAME_SPRITES['numbers'][digit].get_width()
    Xoffset = (SCREENWIDTH - width)/2

    for digit in myDigits:
        SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
        Xoffset += GAME_SPRITES['numbers'][digit].get_width()


def remove_pipes(upper_pipes, lower_pipes):
    upper_pipes.pop(0)
    lower_pipes.pop(0)
