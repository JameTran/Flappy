import pygame
import time
from datetime import datetime
#import Maze 
#import Player
from maze import Maze
from maze import Player
from pygame.locals import *

class MazeGame:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.wnSize = 1280, 800
        self.currState = "menu"
        self.maze = Maze.Maze()
        self.player = Player.Player()
        self.completionTime, self.startTime, self.pauseTime = 0, 0, 0

    def on_init(self):
        pygame.init()
        self.titleFont = pygame.font.SysFont("couriernew", 130, True)
        self.headingFont = pygame.font.SysFont("couriernew", 80, True)
        self.buttonFont = pygame.font.SysFont("couriernew", 35, True)
        self.typeFont = pygame.font.SysFont("couriernew", 25, True)
        self._display_surf = pygame.display.set_mode(self.wnSize)
        pygame.display.set_caption('Maze')
        self._running = True

    def on_event(self, event):
        if (event.type == pygame.QUIT):
            self._running = False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                self._running = False

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac, state=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self._display_surf, ac,(x,y,w,h))
            if click[0] == 1 and state != None:
                self.currState = state
                time.sleep(0.1)

                if (state == "easyMaze"):
                    self.maze.setMaze(15)
                    self.player.setPlayer(self.maze.size, self.maze.allRect)
                    self.startTime = time.time()
                    self.currState = "maze"
                elif (state == "mediumMaze"):
                    self.maze.setMaze(25)
                    self.player.setPlayer(self.maze.size, self.maze.allRect)
                    self.startTime = time.time()
                    self.currState = "maze"
                elif (state == "hardMaze"):
                    self.maze.setMaze(30)
                    self.player.setPlayer(self.maze.size, self.maze.allRect)
                    self.startTime = time.time()
                    self.currState = "maze"
        else:
            pygame.draw.rect(self._display_surf, ic,(x,y,w,h))

        textSurf, textRect = self.text_objects(msg, self.buttonFont)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        self._display_surf.blit(textSurf, textRect)   

    def menuScreen(self): 
        self._display_surf.fill((255, 255, 255))
        titleText = self.titleFont.render("M A Z E", True, (0, 0, 0))
        self._display_surf.blit(titleText, (640 - (titleText.get_width() // 2), 100))
        self.button("PLAY", 490, 300, 300, 100, (230, 230, 230), (200, 200, 200), "difficulty")
        self.button("HOW TO PLAY", 490, 450, 300, 100, (230, 230, 230), (200, 200, 200), "howto")
        self.button("HOME", 490, 600, 140, 100, (230, 230, 230), (200, 200, 200), None)
        self.button("QUIT", 650, 600, 140, 100, (230, 230, 230), (200, 200, 200), "done")
        pygame.display.flip()
        

    def difficultyScreen(self):
        self._display_surf.fill((255, 255, 255))
        headingText = self.headingFont.render("SELECT DIFFICULTY", True, (0, 0, 0))
        self._display_surf.blit(headingText, (640 - (headingText.get_width() // 2), 100))
        self.button("EASY", 490, 300, 300, 100, (230, 230, 230), (200, 200, 200), "easyMaze")
        self.button("MEDIUM", 490, 450, 300, 100, (230, 230, 230), (200, 200, 200), "mediumMaze")
        self.button("HARD", 490, 600, 300, 100, (230, 230, 230), (200, 200, 200), "hardMaze")
        pygame.display.flip()
    
    def howtoScreen(self):
        self._display_surf.fill((255, 255, 255))

        headingText = self.headingFont.render("How to Play", True, (0, 0, 0))
        howtoplay1 = self.typeFont.render("The goal of the game is to get to the green square as fast as possible.", True, (0, 0, 0))
        howtoplay2 = self.typeFont.render("To move you can use the 'W', 'A', 'S', 'D' keys or the arrow keys.", True, (0, 0, 0))
        howtoplay3 = self.typeFont.render("Press 'Esc' to pause the game or return to the main menu.", True, (0, 0, 0))
        howtoplay4 = self.typeFont.render("You can return to the launcher using the main menu.", True, (0, 0, 0))

        self._display_surf.blit(headingText, (640 - (headingText.get_width() // 2), 100))
        self._display_surf.blit(howtoplay1, (640 - (howtoplay1.get_width() // 2), 300))
        self._display_surf.blit(howtoplay2, (640 - (howtoplay2.get_width() // 2), 350))
        self._display_surf.blit(howtoplay3, (640 - (howtoplay3.get_width() // 2), 400))
        self._display_surf.blit(howtoplay4, (640 - (howtoplay4.get_width() // 2), 450))
        self.button("BACK", 540, 650, 200, 50, (230, 230, 230), (200, 200, 200), "menu")
        pygame.display.flip()
    
    def renderMaze(self): 
        self._display_surf.fill((255, 255, 255))
        self.maze.draw(self._display_surf)
        pygame.draw.rect(self._display_surf, (0, 255, 0), self.player.goal)
        pygame.draw.rect(self._display_surf, (255, 100, 0), self.player.rect)
        timeText = self.buttonFont.render(str(round((time.time() - self.startTime), 2)), True, (0, 0, 0))
        self._display_surf.blit(timeText, (10, 10))
        pygame.display.flip()
    
    def victoryScreen(self):
        self._display_surf.fill((255, 255, 255))
        victoryText1 = self.titleFont.render("VICTORY", True, (0, 0,0))
        victoryText2 = self.buttonFont.render("Fastest Time: ", True, (0, 0, 0))
        victoryText3 = self.buttonFont.render("Completion Time: ", True, (0, 0, 0))
        timeText = self.buttonFont.render(str(round(self.completionTime, 2)), True, (0, 0, 0))
        self._display_surf.blit(victoryText1, (640 - (victoryText1.get_width() // 2), 100))
        self._display_surf.blit(victoryText2, (640 - (victoryText2.get_width() // 2), 300))
        self._display_surf.blit(timeText, (640 - (timeText.get_width() // 2), 350))
        self._display_surf.blit(victoryText3, (640 - (victoryText3.get_width() // 2), 450))
        self._display_surf.blit(timeText, (640 - (timeText.get_width() // 2), 500))
        self.button("MENU", 540, 650, 200, 50, (230, 230, 230), (200, 200, 200), "menu")
        pygame.display.flip()

    def on_cleanup(self): 
        pygame.quit()

    def on_execute(self):
        if (self.on_init() == False):
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                    self.on_event(event)
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
            while ((self.currState == "maze") and self._running):
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
                
                if (self.player.isWon == True):
                    self.completionTime = time.time() - self.startTime
                    self.currState = "victory"
                self.renderMaze()  
            while ((self.currState == "victory") and self._running):
                for event in pygame.event.get():
                    self.on_event(event)
                self.victoryScreen()


        self.on_cleanup()


if __name__ == "__main__" :
    Maze = MazeGame()
    Maze.on_execute()