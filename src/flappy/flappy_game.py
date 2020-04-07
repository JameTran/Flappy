import pygame
import sys
from pygame.locals import *
from flappy.flappy_constants import *
from flappy.player_movement import *
from flappy.draw_game import *
from flappy.score_tracking import *
import random
import Scoreboard
import time


def main_game():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1
    playerFlapAccv = -8  # velocity while flapping
    playerFlapped = False  # It is true only when the bird is flapping


    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
    ]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                import Launcher
                Launcher.Launcher.displayLauncher()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True 
                    GAME_SOUNDS['wing'].play()
        
        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY
        
        if playerFlapped:
            playerFlapped = False
        
        playery = update_bird(playery, playerVelY)

        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            print('{}{}'.format("Your score is: ", score))
            # save score to scoreboard
            Scoreboard.Scoreboard.updateScore("Flappy", score)
            while True:
                pygame.draw.rect(SCREEN, WHITE, [0,0,1280,800])
                draw_back_ground()
                pygame.draw.rect(SCREEN, WHITE, [280,0,991,800])
                draw_pipes(upperPipes, lowerPipes)
                draw_bird(playerx, playery)
                draw_ground()
                draw_menuScore(score)
                pygame.draw.rect(SCREEN, WHITE, [280,0,991,800])
                pygame.draw.rect(SCREEN, WHITE, [0,512,991,289])
                SCREEN.blit(GAME_SPRITES['end'], (0, 0))
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        import Launcher
                        Launcher.Launcher.displayLauncher()
                    if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                        return
                pygame.display.update()
                FPSCLOCK.tick(FPS)
                    

        score = get_score(playerx, upperPipes, score)
        # move pipes to the left
        move_pipes(upperPipes, lowerPipes, pipeVelX)

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            remove_pipes(upperPipes, lowerPipes)

        ## DRAW BACKGROUND FIRST
        pygame.draw.rect(SCREEN, WHITE, [0,0,1280,800])
        draw_back_ground()
        pygame.draw.rect(SCREEN, WHITE, [280,0,991,800])
        draw_pipes(upperPipes, lowerPipes)
        draw_bird(playerx, playery)
        draw_ground()
        pygame.draw.rect(SCREEN, WHITE, [0,512,991,289])
        pygame.draw.rect(SCREEN, WHITE, [280,0,991,800])
        pygame.draw.rect(SCREEN, WHITE, [0,512,991,289])
        draw_score(score)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> GROUNDY - 25  or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    return False

def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe

 

        
