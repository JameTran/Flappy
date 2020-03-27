import pygame
from maze import Maze
from maze import Player
from pygame.locals import *

size = 25

class MazeGame:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.wnSize = 1280, 800
        self.maze = Maze.Maze(size)
        self.player = Player.Player(size, self.maze.allRect)

    def on_init(self):
        pygame.init()
        self.font1 = pygame.font.SysFont("couriernew", 25, True)
        self._display_surf = pygame.display.set_mode(self.wnSize)
        pygame.display.set_caption('Maze')
        self._running = True

    def on_event(self, event):
        if (event.type == pygame.QUIT):
            self._running = False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                self._running = False

    def on_loop(self): 
        pass

    def on_render(self): 
        self._display_surf.fill((255, 255, 255))
        self.maze.draw(self._display_surf)
        pygame.draw.rect(self._display_surf, (0, 255, 0), self.player.goal)
        pygame.draw.rect(self._display_surf, (255, 100, 0), self.player.rect)
        pygame.display.flip()

    def on_cleanup(self): 
        pygame.quit()

    def on_execute(self):
        if (self.on_init() == False):
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                    self.on_event(event)
            
            while (self.player.isWon == False and self._running):
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
    
                if (keyPress[K_ESCAPE]):
                    self._running = False

                self.on_loop()
                self.on_render()    

            if (self.player.isWon == True):
                self._display_surf.fill((255, 255, 255))
                victoryText = self.font1.render("CONGRATULATIONS! You completed the maze!", True, (0, 0, 0))
                self._display_surf.blit(victoryText, (630 - (victoryText.get_width() // 2), 400 - (victoryText.get_height() // 2)))
            pygame.display.flip()

            
        self.on_cleanup()


if __name__ == "__main__" :
    Maze = MazeGame()
    Maze.on_execute()