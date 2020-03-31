import pygame
from pygame.locals import *
from flappy_constants import *


def move_bird(playery, playerVelY):          
    player_height = GAME_SPRITES['player'].get_height()
    playery = playery + min(playerVelY, GROUNDY - playery - player_height)