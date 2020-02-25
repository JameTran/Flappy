import os
import pygame
os.environ['SDL_AUDIODRIVER'] = 'dsp'
pygame.init()

class maze:
    def__init__(self):
        self.M = 10
        self.N = 10