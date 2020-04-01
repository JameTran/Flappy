import pygame
from pygame.locals import *
from flappy.flappy_constants import *


def update_bird(playery, playerVelY):          
    player_height = GAME_SPRITES['player'].get_height()
    playery = playery + min(playerVelY, GROUNDY - playery - player_height)
    return playery


def move_pipes(upper_pipes, lower_pipes, pipeVelX):
    for upperPipe , lowerPipe in zip(upper_pipes, lower_pipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX
