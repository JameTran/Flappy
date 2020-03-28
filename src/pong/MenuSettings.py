# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from PongGame import playGame
 #initializing pygame
pygame.init()

#setting the FPS or number of Frames per Second
FPS = 70

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
BG = (5, 45, 60)
BLUE = (66, 133, 244)
HOVERBLUE = (36, 103, 214)
GREEN = (61, 220, 132)
HOVERGREEN = (31, 190, 102)
AMBER = (255, 191, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
bg = (0,5,35)
light_grey = (200,200,200)
enemy_red = (200,5,0)

screen = pygame.display.set_mode(scr_size)
pygame.display.set_caption('Main Menu')
numOfPlayers = -1
difficulty = 1

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

def changeNumberOfPlayers(x):
    global displayPlayers, numOfPlayers
    numOfPlayers = x
    displayPlayers = ('Number of Players: ' + str(x))

def changeDifficulty(x):
    global displayDifficulty, difficulty
    difficulty = x
    if (x == 1): level = 'EASY'
    elif (x == 2): level = 'HARD'    
    elif (x == 3): level = 'INSANE'
    else: level = ''
    displayDifficulty = ('Difficulty: ' + str(level))

def startGameAnimation():
    screen.fill(BG)
    displaytext('WELCOME TO PONG', 100, middleX, middleY, WHITE)
    pygame.display.update()
    clock.tick(0.5)


click = False
displayPlayers = 'Select the number of players'
displayDifficulty = 'Select difficulty'
coverDifficulty = pygame.Rect(middleX - 200, middleY + 150, 800, 90)

def main_menu():
    while True:
 
        screen.fill(BG)
 
        mx, my = pygame.mouse.get_pos()
        displaytext('Press "ESC" to exit the game', 20, middleX, height-30, light_grey)

        #BEGIN selection of difficulty
        easyButton = pygame.Rect(middleX - 125, middleY + 55, 50, 50)
        ecolor = BLUE
        medButton = pygame.Rect(middleX - 25, middleY + 55, 50, 50)
        mcolor = BLUE
        hardButton = pygame.Rect(middleX + 75, middleY + 55, 50, 50)
        hcolor = BLUE
        if easyButton.collidepoint((mx, my)):
            ecolor = HOVERBLUE
            if click:
                # game()
                changeDifficulty(1)
        if medButton.collidepoint((mx, my)):
            mcolor = HOVERBLUE
            if click:
                #options()
                changeDifficulty(2)
        if hardButton.collidepoint((mx, my)):
            hcolor = HOVERBLUE
            if click:
                #options()
                changeDifficulty(3)
        pygame.draw.rect(screen, ecolor, easyButton)
        pygame.draw.rect(screen, mcolor, medButton)
        pygame.draw.rect(screen, hcolor, hardButton)
        displaytext('UwU', 18, middleX - 100, middleY + 80, WHITE)
        displaytext('O-O', 18, middleX, middleY + 80, WHITE)
        displaytext('X_X', 18, middleX + 100, middleY + 80, WHITE)
        displaytext(displayDifficulty, 20, middleX, middleY + 30, WHITE)
        #END selection of difficulty

        #BEGIN start button
        startButton = pygame.Rect(middleX - 110, middleY + 160, 220, 80)
        startColor = GREEN
        beginColor = WHITE
        if numOfPlayers < 0:
            startColor = BG
            beginColor = BG
        if startButton.collidepoint((mx, my)):
            startColor = HOVERGREEN
            if click:
                startGameAnimation()
                playGame()
        pygame.draw.rect(screen, startColor, startButton)
        displaytext('BEGIN', 50, middleX, middleY + 200, beginColor)
        #END start button
        
        # BEGIN selection of players buttons
        onePButton = pygame.Rect(middleX - 75, middleY - 75, 50, 50)
        p1color = BLUE
        twoPButton = pygame.Rect(middleX + 25, middleY - 75, 50, 50)
        p2color = BLUE
        if onePButton.collidepoint((mx, my)):
            p1color = HOVERBLUE
            if click:
                # game()
                coverDifficulty.x = 1280
                changeNumberOfPlayers(1)
        if twoPButton.collidepoint((mx, my)):
            p2color = HOVERBLUE
            if click:
                #options()
                coverDifficulty.x = middleX - 200
                changeNumberOfPlayers(2)
        pygame.draw.rect(screen, p1color, onePButton)
        pygame.draw.rect(screen, p2color, twoPButton)
        pygame.draw.rect(screen, BG, coverDifficulty)
        displaytext('I', 30, middleX - 50, middleY - 50, WHITE)
        displaytext('II', 30, middleX + 50, middleY - 50, WHITE)
        displaytext(displayPlayers, 20, middleX, middleY - 100, WHITE)
        # END selection of players

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
 
def game():
    running = True
    while running:
        screen.fill(BG)
       
        displaytext('game', 30, 100, 20, WHITE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        clock.tick(60)
 
def options():
    running = True
    while running:
        screen.fill(BG)
 
        displaytext('options', 30, 20, 20, WHITE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        clock.tick(60)
 
main_menu()