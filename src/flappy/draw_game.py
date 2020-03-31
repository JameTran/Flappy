from flappy.flappy_constants import *
import pygame
from pygame.locals import *


def draw_bird(x, y):
    SCREEN.blit(GAME_SPRITES['player'], (x, y))

def draw