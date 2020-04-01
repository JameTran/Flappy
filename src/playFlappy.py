from flappy.menu import main_menu 
from flappy.flappy_game import main_game
import pygame
from pygame.locals import *  # Basic pygame imports
from flappy.flappy_constants import *


def play_game():
    pygame.init()
    pygame.display.set_caption('Flappy Bird') 
    while True:
        main_menu()
        main_game()

#play_game()
