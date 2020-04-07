import pygame
from pygame.locals import *
from flappy.flappy_constants import *

## @brief A function to update the position of the plahyer
#  @details This function updates the position of the bird based on the player's current y position and upwards velocity
#  @param  playery Current y position
#  @param  playerVelY Current Y velocity
def update_bird(playery, playerVelY):          
    player_height = GAME_SPRITES['player'].get_height()
    playery = playery + min(playerVelY, GROUNDY - playery - player_height)
    return playery

## @brief A function that moves the pipe pairs to the left on the screen
#  @details This function updates the x coordinates of all the current pipes shown on the screen, based on the pipe's leftwards velocity
#  @param pipeVelX Pipe's leftward velocity
def move_pipes(upper_pipes, lower_pipes, pipeVelX):
    for upperPipe , lowerPipe in zip(upper_pipes, lower_pipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX
