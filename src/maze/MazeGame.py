import pygame
import time
from datetime import datetime
from maze import Maze
from maze import Player
from pygame.locals import *
import Scoreboard


## @brief Class that represents the maze game
class MazeGame:
    
    ## @brief Constructor for the maze game
    # @param None
    # @return None
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.wnSize = 1280, 800
        self.currState = "menu"
        self.maze = Maze.Maze()
        self.player = Player.Player()
        self.mode = ""
        self.completionTime, self.startTime, self.totalPauseTime, self.pauseTime, self.pauseStartTime = 0, 0, 0, 0, 0

    ## @brief On initialization, initializes the fonts, display window and the running variable
    # @param None
    # @return None
    def on_init(self):
        pygame.init()
        self.titleFont = pygame.font.SysFont("couriernew", 130, True)
        self.headingFont = pygame.font.SysFont("couriernew", 80, True)
        self.buttonFont = pygame.font.SysFont("couriernew", 35, True)
        self.typeFont = pygame.font.SysFont("couriernew", 25, True)
        self._display_surf = pygame.display.set_mode(self.wnSize)
        pygame.display.set_caption('Maze')
        self._running = True

    ## @brief On the quit event, you can close the game
    # @param event: represents the apsecific event
    # @return None
    def on_event(self, event):
        if (event.type == pygame.QUIT):
            self._running = False

    ## @brief A function used for rendering fonts to a specific surface
    # @param text: the message to be rendered
    # @param font: the style/size of font to be rendered
    # @return a tuple representing the rendered font and a rectangle
    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    ## @brief  Creates a button with text centered and conducts an action upon click
    # @param msg: the text for the button
    # @param x: the x coordinate for the button
    # @param y: the y coordinate for the button
    # @param w: the width for the buttom
    # @param h: the height of the button
    # @param ic: the inactive colour of the button
    # @param ac: the active colour of the button
    # @param state: the current state of the game
    def button(self, msg, x, y, w, h, ic, ac, state=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self._display_surf, ac, (x, y, w, h))
            if click[0] == 1 and state != None:
                self.currState = state
                time.sleep(0.2)

                if (state == "easyMaze"):
                    self.maze.setMaze(15)
                    self.player.setPlayer(self.maze.size, self.maze.allRect)
                    self.startTime = time.time()
                    self.pauseTime, self.pauseStarTime = 0, 0
                    self.mode = "easy"
                    self.currState = "maze"
                elif (state == "mediumMaze"):
                    self.maze.setMaze(25)
                    self.player.setPlayer(self.maze.size, self.maze.allRect)
                    self.startTime = time.time()
                    self.pauseTime, self.pauseStarTime = 0, 0
                    self.mode = "medium"
                    self.currState = "maze"
                elif (state == "hardMaze"):
                    self.maze.setMaze(30)
                    self.player.setPlayer(self.maze.size, self.maze.allRect)
                    self.startTime = time.time()
                    self.pauseTime, self.pauseStarTime = 0, 0
                    self.mode = "hard"
                    self.currState = "maze"
        else:
            pygame.draw.rect(self._display_surf, ic,(x,y,w,h))

        textSurf, textRect = self.text_objects(msg, self.buttonFont)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        self._display_surf.blit(textSurf, textRect)   

    ## @brief Draws the menu screen when the game is in the menu state
    # @param None
    # @return None
    def menuScreen(self): 
        self._display_surf.fill((255, 255, 255))
        titleText = self.titleFont.render("M A Z E", True, (0, 0, 0))
        self._display_surf.blit(titleText, (640 - (titleText.get_width() // 2), 100))
        self.button("PLAY", 490, 300, 300, 100, (230, 230, 230), (200, 200, 200), "difficulty")
        self.button("HOW TO PLAY", 490, 450, 300, 100, (230, 230, 230), (200, 200, 200), "howto")
        self.button("HOME", 490, 600, 140, 100, (230, 230, 230), (200, 200, 200), "launcher")
        self.button("QUIT", 650, 600, 140, 100, (230, 230, 230), (200, 200, 200), "done")
        pygame.display.flip()
        
    ## @brief Draws the difficulty screen when the game is in the difficulty state
    # @param None
    # @return None
    def difficultyScreen(self):
        self._display_surf.fill((255, 255, 255))
        headingText = self.headingFont.render("SELECT DIFFICULTY", True, (0, 0, 0))
        self._display_surf.blit(headingText, (640 - (headingText.get_width() // 2), 100))
        self.button("EASY", 490, 300, 300, 100, (230, 230, 230), (200, 200, 200), "easyMaze")
        self.button("MEDIUM", 490, 450, 300, 100, (230, 230, 230), (200, 200, 200), "mediumMaze")
        self.button("HARD", 490, 600, 300, 100, (230, 230, 230), (200, 200, 200), "hardMaze")
        pygame.display.flip()
    
    ## @brief Draws the how to play screen when the game is in the howto state
    # @param None
    # @return None
    def howtoScreen(self):
        self._display_surf.fill((255, 255, 255))

        headingText = self.headingFont.render("How to Play", True, (0, 0, 0))
        howtoplay1 = self.typeFont.render("The goal of the game is to get to the green square as fast as possible.", True, (0, 0, 0))
        howtoplay2 = self.typeFont.render("To move you can use the 'W', 'A', 'S', 'D' keys or the arrow keys.", True, (0, 0, 0))
        howtoplay3 = self.typeFont.render("Press 'Esc' or 'P' to pause the game or return to the main menu.", True, (0, 0, 0))
        howtoplay4 = self.typeFont.render("You can return to the launcher using the main menu.", True, (0, 0, 0))

        self._display_surf.blit(headingText, (640 - (headingText.get_width() // 2), 100))
        self._display_surf.blit(howtoplay1, (640 - (howtoplay1.get_width() // 2), 300))
        self._display_surf.blit(howtoplay2, (640 - (howtoplay2.get_width() // 2), 350))
        self._display_surf.blit(howtoplay3, (640 - (howtoplay3.get_width() // 2), 400))
        self._display_surf.blit(howtoplay4, (640 - (howtoplay4.get_width() // 2), 450))
        self.button("BACK", 540, 650, 200, 50, (230, 230, 230), (200, 200, 200), "menu")
        pygame.display.flip()
    
    ## @brief Draws the pause screen when the game is in the pause state
    # @param None
    # @return None
    def pauseScreen(self):
        self.pauseStartTime = time.time()
        self._display_surf.fill((255, 255, 255))
        headingText = self.headingFont.render("GAME PAUSED", True, (0, 0, 0))
        self._display_surf.blit(headingText, (640 - (headingText.get_width() // 2), 100))
        self.button("RESUME", 490, 300, 300, 100, (230, 230, 230), (200, 200, 200), "resume")
        self.button("MENU", 490, 450, 300, 100, (230, 230, 230), (200, 200, 200), "menu")
        pygame.display.flip()
        self.pauseTime += time.time() - self.pauseStartTime

    ## @brief Renders the maze, player and the goal
    # @param None
    # @return None
    def renderMaze(self): 
        self._display_surf.fill((255, 255, 255))
        self.maze.draw(self._display_surf)
        pygame.draw.rect(self._display_surf, (0, 255, 0), self.player.goal)
        pygame.draw.rect(self._display_surf, (255, 100, 0), self.player.rect)
        timeText = self.buttonFont.render(str(round((time.time() - self.startTime - self.pauseTime), 2)), True, (0, 0, 0))
        self._display_surf.blit(timeText, (10, 10))
        pygame.display.flip()
    
    ## @brief Draws the victory screen and outputs the highscore and elapsed time
    # @param None
    # @return None
    def victoryScreen(self):
        self._display_surf.fill((255, 255, 255))
        victoryText1 = self.titleFont.render("VICTORY", True, (0, 0,0))
        victoryText2 = self.buttonFont.render("Highest Score: ", True, (0, 0, 0))
        victoryText3 = self.buttonFont.render("Your Score: ", True, (0, 0, 0))
        highscoreText = self.buttonFont.render(str(Scoreboard.Scoreboard.highScore("Maze")), True, (0, 0, 0))
        timeText = self.buttonFont.render(str(MazeGame.tupleToScore((self.mode, self.completionTime))), True, (0, 0, 0))
        self._display_surf.blit(victoryText1, (640 - (victoryText1.get_width() // 2), 100))
        self._display_surf.blit(victoryText2, (640 - (victoryText2.get_width() // 2), 300))
        self._display_surf.blit(highscoreText, (640 - (timeText.get_width() // 2), 350))
        self._display_surf.blit(victoryText3, (640 - (victoryText3.get_width() // 2), 450))
        self._display_surf.blit(timeText, (640 - (timeText.get_width() // 2), 500))
        self.button("MENU", 540, 650, 200, 50, (230, 230, 230), (200, 200, 200), "menu")
        pygame.display.flip()

    ## @brief When called, closes the game
    # @param None
    # @return None
    def on_cleanup(self): 
        pygame.quit()

    ## @brief Controls the game during execution, including it's current state, player movement, completion and returning to the launcher
    # @param None
    # @return None
    def on_execute(self):
        if (self.on_init() == False):
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                    self.on_event(event)
            if (self.currState == "launcher"):
                import Launcher
                Launcher.Launcher.displayLauncher()
            while ((self.currState == "menu") and self._running):
                for event in pygame.event.get():
                    self.on_event(event)
                self.menuScreen()
            while ((self.currState == "difficulty") and self._running):
                for event in pygame.event.get():
                    self.on_event(event)
                self.difficultyScreen()
            while ((self.currState == "howto") and self._running):
                for event in pygame.event.get():
                    self.on_event(event)
                self.howtoScreen()
            while ((self.currState == "done") and self._running):
                self._running = False
            while (((self.currState == "maze") or self.currState == "resume") and self._running):
                for event in pygame.event.get():
                    self.on_event(event)
                pygame.event.pump()
                keyPress = pygame.key.get_pressed()
                # Move the player if an arrow key is pressed
                if (keyPress[K_LEFT] or keyPress[K_a]):
                    self.player.move(-1, 0)

                if (keyPress[K_RIGHT] or keyPress[K_d]):
                    self.player.move(1, 0)

                if (keyPress[K_UP] or keyPress[K_w]):
                    self.player.move(0, -1)

                if (keyPress[K_DOWN] or keyPress[K_s]):
                    self.player.move(0, 1)

                if (keyPress[K_ESCAPE] or keyPress[K_p]):
                    self.currState = "pause"
                    while (self.currState == "pause"):
                        for event in pygame.event.get():
                            self.on_event(event)
                        self.pauseScreen()
                
                if (self.player.isWon == True):
                    self.completionTime = time.time() - self.startTime - self.pauseTime
                    self.currState = "victory"
                    Scoreboard.Scoreboard.updateScore("Maze", MazeGame.tupleToScore((self.mode, self.completionTime))) # Updating the scoreboard
                self.renderMaze()  
            while ((self.currState == "victory") and self._running):
                for event in pygame.event.get():
                    self.on_event(event)
                self.victoryScreen()


        self.on_cleanup()

    ## @brief Transform from tuple to score
    ## @param tuple: represents the difficulty, as a string, and the time, as a float
    ## return an integer representing the score calcualted by difficulty
    @staticmethod
    def tupleToScore(tuple):
        defaultScore = 100
        defaultTime = [20, 60, 180]
        if tuple[0] == "easy":
            return (defaultScore + defaultTime[0] - int(tuple[1]))
        elif tuple[0] == "medium":
            return (defaultScore + defaultTime[1] - int(tuple[1]))
        elif tuple[0] == "hard":
            return (defaultScore + defaultTime[2] - int(tuple[1]))
        else:
            return 0
    
if __name__ == "__main__" :
    Maze = MazeGame()
    Maze.on_execute()