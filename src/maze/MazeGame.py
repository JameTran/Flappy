import pygame
import genMaze
from pygame.locals import *

black = (0, 0, 0)
red = (255, 0, 0)

class MazeGame:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.wnSize = genMaze.wnLength, genMaze.wnHeight
        self.maze = genMaze.Maze(10)
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.wnSize, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.NOFRAME)
        pygame.display.set_caption('Maze')
        self._running = True

    def on_event(self, event):
        if (event.type == pygame.QUIT):
            self._running = False

    def on_loop(self): 
        pass

    def on_render(self): 
        self._display_surf.fill(black)
        self.maze.draw(self._display_surf)
        pygame.display.flip()

    def on_cleanup(self): 
        pygame.quit()

    def on_execute(self):
        if (self.on_init() == False):
            self._running = False
 
        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[KEYDOWN]):
                self._running = False
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__" :
    Maze = MazeGame()
    Maze.on_execute()