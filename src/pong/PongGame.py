import sys, random, pygame
from pygame.locals import *
from pong.Ball import *
from pong.Paddle import *

#initializing pygame
pygame.init()

#setting the FPS or number of Frames per Second
FPS = 60

#Setting the screen size
scr_size = (width, height) = (1280, 800)
middleX = int(width/2)
middleY = int(height/2)

#creating a clock object from pygame.time.Clock class
clock = pygame.time.Clock()

#Declaring various color values
BG = (5, 35, 60)
WHITE = (255, 255, 255)
LIGHTGREY = (200, 200, 200)
AMBER = (255, 191, 0)
BLUE = (66, 133, 244)
HOVERBLUE = (36, 103, 214)
GREEN10 = (61, 220, 132)
GREEN = (0, 200, 0)
ORANGE = (240, 130, 0)
RED = (200, 30, 0)
ENEMYCOLOR = GREEN

"""
Creating our game screen by passing its screen size as the parameter, 
and setting its caption as 'Pong'
"""
screen = pygame.display.set_mode(scr_size)
pygame.display.set_caption('Pong')
click = False
gameOver = True

"""
A function used to display text on the screen
It takes in 4 parameters, i.e
text : the text which is to be printed. Has to be a string
fontsize : the fontsize of the text to be printed. Must be an integer
x, y : The x and y coordinates where we want our text to be printed
color : The color of the text. Its has to be in (R, G, B) format where R, G and B takes values from 0 to 255
"""
def displaytext(text, fontsize, x, y, color):
    font = pygame.font.SysFont('rockwell', fontsize, True)
    text = font.render(text, 1, color)
    textpos = text.get_rect(centerx=x, centery=y)
    screen.blit(text, textpos)

"""
A function which moves the ai's paddle
The concept behind this function is the same as that used in the real world, i.e
the ai paddle will try to chase the ball based on its coordinates
"""
def aimove(ai, ball, diff):
    if ball.movement[0] > 0: #ensures that the ai moves only when the ball is directed towards it
        #the extra addition of ai.rect.height/5 ensures that the ai will miss the ball sometimes
        if ball.rect.bottom > ai.rect.bottom + int(ai.rect.height/diff):
            ai.movement[1] = 6
        elif ball.rect.top < ai.rect.top - int(ai.rect.height/diff):
            ai.movement[1] = -6
        else:
            ai.movement[1] = 0
    else:
        ai.movement[1] = 0

def calculateScore(paddleScore, aiScore, maxScore):
    return int(((paddleScore * maxScore) - aiScore) * 17)

#The main function of our program
def mainGame(difficulty, maxScore):
    global gameOver
    if maxScore <= 0:
        maxScore = 5
    if difficulty <= 0:
        difficulty = 4
    if difficulty == 7:
        ENEMYCOLOR = ORANGE
    elif difficulty == 10:
        ENEMYCOLOR = RED
    else:
        ENEMYCOLOR = GREEN

    gameOver = False #Sets the initial state of the game
    paddle = Paddle(int(width/18), middleY, int(width/90), int(height/8), LIGHTGREY) #creating an object for the user's paddle
    ai = Paddle(int(width - width/18), middleY, int(width/90), int(height/8), ENEMYCOLOR) #creating an object for the ai's paddle
    ball = Ball(middleX, middleY, 25, AMBER, [6, 6]) #creating an object for the ball

    while not gameOver: #running our game loop
        for event in pygame.event.get(): #checks for various events in pygame, like keypress, mouse movement, etc
            if event.type == pygame.QUIT: #checks, if the user has clicked the close button
                quit()                    #quits the program

            if event.type == pygame.KEYDOWN: #checks whether a key has been pressed or not
                if event.key == pygame.K_UP: #If user has pressed the UP key
                    paddle.movement[1] = -8  #Paddle moves upwards
                elif event.key == pygame.K_DOWN: #If user has pressed the down key
                    paddle.movement[1] = 8       #Paddle moves downwards
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    pauseMenu(paddle.points, ai.points)
                if event.key == K_r:
                    ball.resetBall()
            if event.type == pygame.KEYUP:    #If the user lifts the key
                paddle.movement[1] = 0        #Paddle stops moving

        aimove(ai, ball, difficulty) #moves the ai's paddle

        screen.fill(BG) #fills the entire screen with BG color
        pygame.draw.aaline(screen, WHITE, (middleX, 0), (middleX, height))
        displaytext('PAUSE the game using the "ESC" key.', 20, 1075, 25, WHITE)


        #drawing user's paddle, ai's paddle and ball
        paddle.drawPaddle()
        ai.drawPaddle()
        ball.draw()

        #displaying the points scored by the user and ai
        displaytext(str(paddle.points), 40, middleX - 30, 30, WHITE)
        displaytext(str(ai.points), 40, middleX + 30, 30, WHITE)
        if (ai.points == maxScore):
            clock.tick(1)
            endGameMenu(0, paddle.points, ai.points, maxScore)
            gameOver = True
        if (paddle.points == maxScore):
            clock.tick(1)
            endGameMenu(1, paddle.points, ai.points, maxScore)
            gameOver = True

        """
        using pygame.sprite.collide_mask function to check for 'pixel perfect' collision
        between user's and ai's paddle with the ball
        The collision is based on the real world concept of perfectly elastic collisions.
        hence, whenever the ball strikes the paddle (placed vertically), the horizontal velocity is reversed, 
        while the vertical velocity is equal to the relative velocity of ball w.r.t the paddle.
        In order to add some randomness, some error is introduced to the relative velocity of the ball and the paddle, i.e
        The paddle's velocity is multiplied by a factor between 0.5 to 1 before calculating the relative velocity.
        """
        if pygame.sprite.collide_mask(paddle, ball):
            ball.movement[0] = -1*ball.movement[0]
            ball.movement[1] = ball.movement[1] - int(0.1*random.randrange(5, 10)*paddle.movement[1])
            if ball.movement[1] > ball.maxspeed:
                ball.movement[1] = ball.maxspeed
            if ball.movement[1] < -1*ball.maxspeed:
                ball.movement[1] = -1*ball.maxspeed

        if pygame.sprite.collide_mask(ai, ball):
            ball.movement[0] = -1*ball.movement[0]
            ball.movement[1] = ball.movement[1] - int(0.1*random.randrange(5, 10)*ai.movement[1])
            if ball.movement[1] > ball.maxspeed:
                ball.movement[1] = ball.maxspeed
            if ball.movement[1] < -1*ball.maxspeed:
                ball.movement[1] = -1*ball.maxspeed

        #checks whether user or ai scored a point and increments accordingly
        if ball.score == 1:
            ai.points += 1
            ball.score = 0
        elif ball.score == -1:
            paddle.points += 1
            ball.score = 0

        #updating the states of user's paddle, ai's paddle and ball
        paddle.movePaddle()
        ball.scoreGoal()
        ai.movePaddle()

        #updating the entire display"""
        pygame.display.update()

        #adding the time delay based on the number of 'Frames per Second'
        clock.tick(FPS)

    # #Exiting the program by safely quitting pygame
    # pygame.quit()
    # quit()

def pauseMenu(paddleScore, aiScore):
    global click, gameOver
    pause = True
    while pause:
        screen.fill(BG)
 
        mx, my = pygame.mouse.get_pos()
       
        displaytext('PAUSED', 80, middleX, 300, WHITE)
        displaytext((str(paddleScore) + ' - ' + str(aiScore)), 80, middleX, 200, WHITE)
        displaytext('TIP: If you feel like you are stuck, use the "R" key to RESET the BALL.', 20, middleX, height - 30, RED)


        #BEGIN selection of pause options
        resumeButton = pygame.Rect(middleX - 100, middleY - 25, 200, 50)
        resumeColor = BLUE
        mainMenuButton = pygame.Rect(middleX - 100, middleY + 50, 200, 50)
        mainMenuColor = BLUE
        launcherButton = pygame.Rect(middleX - 100, middleY + 125, 200, 50)
        launcherColor = BLUE
        if resumeButton.collidepoint((mx, my)):
            resumeColor = HOVERBLUE
            if click:
                # game()
                pause = False
        if mainMenuButton.collidepoint((mx, my)):
            mainMenuColor = HOVERBLUE
            if click:
                #options()
                screen.fill(BG)
                gameOver = True
                pause = False
        if launcherButton.collidepoint((mx, my)):
            launcherColor = HOVERBLUE
            if click:
                #options()
                # Launcher.displayLauncher
                print("Add return to launcher")
        pygame.draw.rect(screen, resumeColor, resumeButton)
        pygame.draw.rect(screen, mainMenuColor, mainMenuButton)
        pygame.draw.rect(screen, launcherColor, launcherButton)
        displaytext('Resume', 25, middleX, middleY, WHITE)
        displaytext('New Game', 25, middleX, middleY + 75, WHITE)
        displaytext('Quit Game', 25, middleX, middleY + 150, WHITE)
        #END selection of pause options

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
       
        pygame.display.update()
        clock.tick(60)

def endGameMenu(victor, paddleScore, aiScore, maxScore):
    global click
    endGame = True
    while endGame:
        screen.fill(BG)
        mx, my = pygame.mouse.get_pos()
        
        finalScore = calculateScore(paddleScore, aiScore, maxScore)
        if finalScore in [425, 1700, 3825]:
            displaytext('+*! PERFECT SCORE !*+', 30, middleX, 150, AMBER)
        if finalScore < 0:
            finalScore = int(maxScore/3)
            displaytext('THAT WAS TERRIBLE!' , 30, middleX, 150, ORANGE)
        if finalScore == 0:
            finalScore = maxScore

        if (victor == 0):
            displaytext('DEFEAT', 80, middleX, 200, RED)
        else:
            displaytext('YOU WIN!', 80, middleX, 200, GREEN10)
        displaytext(('FINAL SCORE: ' + str(finalScore)), 30, middleX, 275, WHITE)
        displaytext((str(paddleScore) + ' - ' + str(aiScore)), 90, middleX, 350, WHITE)

        #BEGIN selection of pause options
        saveScoreButton = pygame.Rect(middleX - 100, middleY + 25, 200, 50)
        saveScoreColor = BLUE
        mainMenuButton = pygame.Rect(middleX - 100, middleY + 100, 200, 50)
        mainMenuColor = BLUE
        launcherButton = pygame.Rect(middleX - 100, middleY + 175, 200, 50)
        launcherColor = BLUE
        if saveScoreButton.collidepoint((mx, my)):
            saveScoreColor = HOVERBLUE
            if click:
                # game()
                # Scoreboard.updateScore("Pong", calculateScore(paddleScore, aiScore))
                print("Add save score function but score is: " + str(finalScore))
        if mainMenuButton.collidepoint((mx, my)):
            mainMenuColor = HOVERBLUE
            if click:
                #options()
                screen.fill(BG)
                endGame = False
        if launcherButton.collidepoint((mx, my)):
            launcherColor = HOVERBLUE
            if click:
                #options()
                # Launcher.displayLauncher
                print("Add return to launcher")
        pygame.draw.rect(screen, saveScoreColor, saveScoreButton)
        pygame.draw.rect(screen, mainMenuColor, mainMenuButton)
        pygame.draw.rect(screen, launcherColor, launcherButton)
        displaytext('Save Score', 25, middleX, middleY + 50, WHITE)
        displaytext('New Game', 25, middleX, middleY + 125, WHITE)
        displaytext('Quit Game', 25, middleX, middleY + 200, WHITE)
        #END selection of pause options

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    endGame = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
       
        pygame.display.update()
        clock.tick(60)