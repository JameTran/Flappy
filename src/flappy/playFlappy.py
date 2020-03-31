from menu import main_menu 
import pygame
from pygame.locals import *  # Basic pygame imports
from flappy_constants import *


def play_game():
    pygame.init()
    pygame.display.set_caption('Flappy Bird') 
    while True:
        main_menu()

play_game()