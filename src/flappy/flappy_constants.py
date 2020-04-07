import pygame
from pygame.locals import *

## A collection of global constants that are global to all flappy modules
pygame.init()
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((1280, 800))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'flappy/sprites/bird.png'
BACKGROUND = 'flappy/sprites/background.png'
PIPE = 'flappy/sprites/pipe.png'
WHITE = (255, 255, 255)
FPSCLOCK = pygame.time.Clock()

## Constants are loaded from the directories on the computer into pygame interpretable objects
GAME_SPRITES['numbers'] = ( 
    pygame.image.load('flappy/sprites/0.png').convert_alpha(),
    pygame.image.load('flappy/sprites/1.png').convert_alpha(),
    pygame.image.load('flappy/sprites/2.png').convert_alpha(),
    pygame.image.load('flappy/sprites/3.png').convert_alpha(),
    pygame.image.load('flappy/sprites/4.png').convert_alpha(),
    pygame.image.load('flappy/sprites/5.png').convert_alpha(),
    pygame.image.load('flappy/sprites/6.png').convert_alpha(),
    pygame.image.load('flappy/sprites/7.png').convert_alpha(),
    pygame.image.load('flappy/sprites/8.png').convert_alpha(),
    pygame.image.load('flappy/sprites/9.png').convert_alpha(),
)


GAME_SPRITES['base'] = pygame.image.load('flappy/sprites/base.png').convert_alpha()
GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), pygame.image.load(PIPE).convert_alpha())
GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
GAME_SPRITES['start'] = pygame.image.load('flappy/sprites/start.png')
GAME_SPRITES['main_menu'] = pygame.image.load('flappy/sprites/main_menu.png')
GAME_SPRITES['end'] = pygame.image.load('flappy/sprites/end.png')


GAME_SOUNDS['die'] = pygame.mixer.Sound('flappy/audio/die.wav')
GAME_SOUNDS['hit'] = pygame.mixer.Sound('flappy/audio/hit.wav')
GAME_SOUNDS['point'] = pygame.mixer.Sound('flappy/audio/point.wav')
GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('flappy/audio/swoosh.wav')
GAME_SOUNDS['wing'] = pygame.mixer.Sound('flappy/audio/wing.wav')