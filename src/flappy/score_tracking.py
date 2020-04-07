import pygame
import sys
from pygame.locals import *
from flappy.flappy_constants import *

def get_score(playerx, upperPipes, score):
    playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
    for pipe in upperPipes:
        pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
        if pipeMidPos <= playerMidPos < pipeMidPos + 4:
            score += 1
            GAME_SOUNDS['point'].play()
            return score
        else:
            return score