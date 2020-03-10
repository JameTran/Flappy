import pygame
from pygame.locals import *

wnLength = 1280 # window length
wnHeight = 800 # window height
offset = 100 # window starting offset

class Cell:
    def __init__(self, x, y, size, thickness):
        cLength = wnHeight // size
        self.walls = [(x, y, cLength + thickness, thickness), 
            (x, y + cLength, cLength + thickness, thickness), 
            (x, y, thickness, cLength + thickness), 
            (x + cLength, y, thickness, cLength + thickness)]

class Maze:
    def __init__(self, size):
        self.mazeSize = size
        self.maze = []
        self.cells = []
        self.mazeWalls = []
        self.thickness = 10

    def draw(self, display_surf):
        for x in range (offset, wnHeight + offset, wnHeight // self.mazeSize):
            for y in range (0, wnHeight, wnHeight // self.mazeSize):
                self.cells.append(Cell(x, y, self.mazeSize, self.thickness))


        for x in range (0, self.mazeSize * self.mazeSize):
            for v in self.cells[x].walls:
                self.mazeWalls.append(v)
                
        for x in range(0, self.mazeSize * self.mazeSize):
            for k in self.mazeWalls:
                pygame.draw.rect(display_surf, (255, 0, 0), pygame.Rect(k[0] + 40, k[1] + 40, k[2], k[3]))
