# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from PongGame import *
 #initializing pygame
pygame.init()

#setting the FPS or number of Frames per Second
FPS = 60

#Setting the screen size
scr_size = (width,height) = (1280,800)
middleX = int(width/2)
middleY = int(height/2)


#creating a clock object from pygame.time.Clock class
clock = pygame.time.Clock()


#Defining the beginning speed of the ball
ball = pygame.Rect(582,460, 104, 104)
#ball2 = pygame.Rect(518, 152, 104, 104)
ball_speed_x = 8
ball_speed_y = 5


#Declaring various color values
BG = (5, 35, 60)
BLUE = (66, 133, 244)
HOVERBLUE = (36, 103, 214)
GREEN10 = (61, 220, 132)
HOVERGREEN10 = (31, 190, 102)
GREEN = (0, 200, 0)
HOVERGREEN = (0, 170, 0)
ORANGE = (240, 130, 0)
HOVERORANGE = (210, 100, 0)
RED = (200, 30, 0)
HOVERRED = (170, 0, 0)
AMBER = (255, 191, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(scr_size)
pygame.display.set_caption('Main Menu')
finalScore = -1
diff = 1

def displaytext(text,fontsize,x,y,color):
    font = pygame.font.SysFont('rockwell', fontsize, True)
    text = font.render(text, 1, color)
    textpos = text.get_rect(centerx=x, centery=y)
    screen.blit(text, textpos)

def ball_animation():
    global ball_speed_x, ball_speed_y

    # Moves the ball by one multiple of the ball speed
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Keeps the ball in the boundaries
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_speed_x *= -1

def changeFinalScore(x):
    global displayFinalScore, finalScore
    finalScore = x
    displayFinalScore = ('Play up to: ' + str(x))

def changeDifficulty(x):
    global displayDifficulty, diff
    diff = x
    if (x == 4): level = 'EASY'
    elif (x == 6): level = 'HARD'    
    elif (x == 8): level = 'INSANE'
    else: level = ''
    displayDifficulty = ('Difficulty: ' + str(level))

def startGameAnimation():
    screen.fill(BG)
    fadeR = 5
    fadeG = 35
    fadeB = 60
    timer = 20
    while timer > 0:
        screen.fill((fadeR, fadeG, fadeB))
        fadeR = fadeR - int(5/20)
        fadeG = fadeG - int(35/20)
        fadeB = fadeB - int(60/20)
        timer -= 1
        pygame.display.update()
        clock.tick(8)
    displaytext('Welcome TO PONG', 100, middleX, middleY, WHITE)
    pygame.display.update()
    clock.tick(0.7)


click = False
displayFinalScore = 'Select the maximum score'
displayDifficulty = 'Select difficulty'
coverDifficulty = pygame.Rect(middleX - 200, middleY + 150, 800, 90)

def main_menu():
    while True:
 
        screen.fill(BG)
 
        mx, my = pygame.mouse.get_pos()
        displaytext('Press "ESC" to exit the game', 20, middleX, height-30, WHITE)

        #BEGIN selection of difficulty
        easyButton = pygame.Rect(middleX - 125, middleY - 75, 50, 50)
        ecolor = GREEN
        medButton = pygame.Rect(middleX - 25, middleY - 75, 50, 50)
        mcolor = ORANGE
        hardButton = pygame.Rect(middleX + 75, middleY - 75, 50, 50)
        hcolor = RED
        if easyButton.collidepoint((mx, my)):
            ecolor = HOVERGREEN
            if click:
                # game()
                changeDifficulty(4)
        if medButton.collidepoint((mx, my)):
            mcolor = HOVERORANGE
            if click:
                #options()
                changeDifficulty(6)
        if hardButton.collidepoint((mx, my)):
            hcolor = HOVERRED
            if click:
                #options()
                changeDifficulty(8)
        pygame.draw.rect(screen, ecolor, easyButton)
        pygame.draw.rect(screen, mcolor, medButton)
        pygame.draw.rect(screen, hcolor, hardButton)
        displaytext('!', 18, middleX - 100, middleY - 50, WHITE)
        displaytext('!!', 18, middleX, middleY - 50, WHITE)
        displaytext('!!!', 18, middleX + 100, middleY - 50, WHITE)
        displaytext(displayDifficulty, 20, middleX, middleY - 100, WHITE)
        #END selection of difficulty

        #BEGIN start button
        startButton = pygame.Rect(middleX - 125, middleY + 160, 250, 80)
        startColor = BG
        beginColor = BG
        if finalScore > 0:
            startColor = GREEN10
            beginColor = WHITE
            coverDifficulty.x = 1280
        if startButton.collidepoint((mx, my)):
            startColor = HOVERGREEN10
            if click:
                startGameAnimation()
                playGame(diff, finalScore)
        pygame.draw.rect(screen, startColor, startButton)
        displaytext('BEGIN', 50, middleX, middleY + 200, beginColor)
        #END start button
        pygame.draw.rect(screen, BG, coverDifficulty)
        
        #BEGIN selection of final score
        sevenButton = pygame.Rect(middleX - 125, middleY + 50, 50, 50)
        color7 = BLUE
        elevenButton = pygame.Rect(middleX - 25, middleY + 50, 50, 50)
        color11 = BLUE
        fifteenButton = pygame.Rect(middleX + 75, middleY + 50, 50, 50)
        color15 = BLUE
        if sevenButton.collidepoint((mx, my)):
            color7 = HOVERBLUE
            if click:
                # game()
                changeFinalScore(7)
        if elevenButton.collidepoint((mx, my)):
            color11 = HOVERBLUE
            if click:
                #options()
                changeFinalScore(11)
        if fifteenButton.collidepoint((mx, my)):
            color15 = HOVERBLUE
            if click:
                #options()
                changeFinalScore(15)
        pygame.draw.rect(screen, color7, sevenButton)
        pygame.draw.rect(screen, color11, elevenButton)
        pygame.draw.rect(screen, color15, fifteenButton)
        displaytext('7', 20, middleX - 100, middleY + 75, WHITE)
        displaytext('11', 20, middleX, middleY + 75, WHITE)
        displaytext('15', 20, middleX + 100, middleY + 75, WHITE)
        displaytext(displayFinalScore, 20, middleX, middleY + 25, WHITE)
        #END selection of final score

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        if (ball.x > 518):
            ball_animation()

        pygame.draw.ellipse(screen, AMBER, ball)
        displaytext("P   NG", 150, middleX, 200, AMBER)
 
        pygame.display.update()
        clock.tick(70)
 