import pygame
from pygame.locals import *

pygame.init()
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'sprites/bird.png'
BACKGROUND = 'sprites/background.png'
PIPE = 'sprites/pipe.png'

FPSCLOCK = pygame.time.Clock()
GAME_SPRITES['numbers'] = ( 
    pygame.image.load('sprites/0.png').convert_alpha(),
    pygame.image.load('sprites/1.png').convert_alpha(),
    pygame.image.load('sprites/2.png').convert_alpha(),
    pygame.image.load('sprites/3.png').convert_alpha(),
    pygame.image.load('sprites/4.png').convert_alpha(),
    pygame.image.load('sprites/5.png').convert_alpha(),
    pygame.image.load('sprites/6.png').convert_alpha(),
    pygame.image.load('sprites/7.png').convert_alpha(),
    pygame.image.load('sprites/8.png').convert_alpha(),
    pygame.image.load('sprites/9.png').convert_alpha(),
)

GAME_SPRITES['message'] = pygame.image.load('sprites/message.png').convert_alpha()
GAME_SPRITES['base'] = pygame.image.load('sprites/base.png').convert_alpha()
GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), pygame.image.load(PIPE).convert_alpha())
GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

# Game sounds
GAME_SOUNDS['die'] = pygame.mixer.Sound('audio/die.wav')
GAME_SOUNDS['hit'] = pygame.mixer.Sound('audio/hit.wav')
GAME_SOUNDS['point'] = pygame.mixer.Sound('audio/point.wav')
GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('audio/swoosh.wav')
GAME_SOUNDS['wing'] = pygame.mixer.Sound('audio/wing.wav')