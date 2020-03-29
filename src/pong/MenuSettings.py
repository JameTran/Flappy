import pygame, sys
from pygame.locals import *
from pong.PongGame import *
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
diff = 0

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
    elif (x == 7): level = 'HARD'    
    elif (x == 10): level = 'INSANE'
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
        displaytext('TIP: If you feel like you are stuck, use the "R" key to RESET the BALL.', 20, middleX, height - 120, RED)
        displaytext('Use the "UP"/"DOWN" arrow keys to move your PADDLE.', 20, middleX, height - 90, WHITE)
        displaytext('Get the BALL  past your opponent to score.', 20, middleX, height - 60, WHITE)
        displaytext('Press "ESC" to PAUSE the game.', 20, middleX, height-30, WHITE)
        timer -= 1
        pygame.display.update()
        clock.tick(8)
    displaytext('Welcome TO PONG', 100, middleX, middleY, WHITE)
    pygame.display.update()
    clock.tick(0.7)


click = False
displayFinalScore = 'Select the maximum score'
displayDifficulty = 'Select difficulty'
coverStart = pygame.Rect(0, 0, 1280, 800)

def main_menu():
    while True:
 
        screen.fill(BG)
 
        mx, my = pygame.mouse.get_pos()
        displaytext('Use the UP / DOWN arrow keys to move your PADDLE.', 20, middleX, height - 90, WHITE)
        displaytext('Get the BALL  past your opponent to score.', 20, middleX, height - 60, WHITE)
        displaytext('Press "ESC" to return to the launcher.', 20, middleX, height-30, WHITE)

        #BEGIN show scoreboard button
        scoresButton = pygame.Rect(middleX - 60, 75, 120, 50)
        scoresColor = WHITE
        if scoresButton.collidepoint((mx, my)):
            scoresColor = (200, 200, 200)
            if click:
                # Scoreboard.drawScoreboard()
                print("Add display scoreboard")
        pygame.draw.rect(screen, scoresColor, scoresButton)
        displaytext('Scoreboard', 18, middleX, 100, BLACK)
        #END show scoreboard button

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
                changeDifficulty(7)
        if hardButton.collidepoint((mx, my)):
            hcolor = HOVERRED
            if click:
                #options()
                changeDifficulty(10)
        pygame.draw.ellipse(screen, ecolor, easyButton)
        pygame.draw.ellipse(screen, mcolor, medButton)
        pygame.draw.ellipse(screen, hcolor, hardButton)
        displaytext('!', 20, middleX - 100, middleY - 50, WHITE)
        displaytext('!!', 20, middleX, middleY - 50, WHITE)
        displaytext('!!!', 20, middleX + 100, middleY - 50, WHITE)
        displaytext(displayDifficulty, 25, middleX, 300, WHITE)
        #END selection of difficulty

        #BEGIN start button
        startButton = pygame.Rect(middleX - 125, middleY + 160, 250, 80)
        startColor = BG
        beginColor = BG
        if finalScore > 0 and diff > 0:
            startColor = GREEN10
            beginColor = WHITE
        if startButton.collidepoint((mx, my)):
            if finalScore > 0 and diff > 0:
                startColor = HOVERGREEN10
            if click:
                startGameAnimation()
                playGame(diff, finalScore)
        pygame.draw.rect(screen, startColor, startButton)
        displaytext('BEGIN', 50, middleX, middleY + 200, beginColor)
        #END start button
        
        #BEGIN selection of final score
        fiveButton = pygame.Rect(middleX - 125, middleY + 50, 50, 50)
        color5 = BLUE
        tenButton = pygame.Rect(middleX - 25, middleY + 50, 50, 50)
        color10 = BLUE
        fifteenButton = pygame.Rect(middleX + 75, middleY + 50, 50, 50)
        color15 = BLUE
        if fiveButton.collidepoint((mx, my)):
            color5 = HOVERBLUE
            if click:
                # game()
                changeFinalScore(5)
        if tenButton.collidepoint((mx, my)):
            color10 = HOVERBLUE
            if click:
                #options()
                changeFinalScore(10)
        if fifteenButton.collidepoint((mx, my)):
            color15 = HOVERBLUE
            if click:
                #options()
                changeFinalScore(15)
        pygame.draw.ellipse(screen, color5, fiveButton)
        pygame.draw.ellipse(screen, color10, tenButton)
        pygame.draw.ellipse(screen, color15, fifteenButton)
        displaytext('5', 20, middleX - 100, middleY + 75, WHITE)
        displaytext('10', 20, middleX, middleY + 75, WHITE)
        displaytext('15', 20, middleX + 100, middleY + 75, WHITE)
        displaytext(displayFinalScore, 25, middleX, middleY + 25, WHITE)
        #END selection of final score
        pygame.draw.rect(screen, BG, coverStart)

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
        if (ball.x <= 518):
            coverStart.x = 1280

        pygame.draw.ellipse(screen, AMBER, ball)
        displaytext("P   NG", 150, middleX, 200, AMBER)
 
        pygame.display.update()
        clock.tick(70)