import pygame
import random
import time

pygame.init()
# all fonts used

class cell:
    def __init__(self,up,down,left,right):
        self.visited = False
        self.walls = [up,down,left,right]


class labyrinth:
    # generates the maze
    def __init__(self):
        self.maze_walls = []
        self.cells = []

        size = 10
        wnHeight = 700
        wallLength = wnHeight // size
        thickness = 10

        
        # creates all cell within the maze
        for x in range(100, wnHeight + 100, wallLength):
            for y in range(0,wnHeight, wallLength):
                self.cells.append(cell((x, y, 80, 10), (x, y + 70, 80, 10), (x, y, 10, 80), (x + 70, y, 10, 80)))

        # generates maze using prim's algorithm
        for x in range (0, size * size):
            for v in self.cells[x].walls:
                self.maze_walls.append(v)
        #print(self.cells[398].walls)

        self.cells[0].visited = True

        # for x in range(100, wnHeight + wallLength + 100, wallLength):
        #     for y in range(0,wnHeight + wallLength + 100, wallLength):
        #         self.maze_walls.append((x, y, thickness, thickness))

    # draws the maze
    def draw(self):
        for k in self.maze_walls:
            pygame.draw.rect(screen, color, pygame.Rect(k[0] + 40,k[1] + 40, k[2], k[3]))


running = True
while running:
    screen = pygame.display.set_mode((1280, 800), pygame.HWSURFACE)
    color = (0, 128, 255) # color of the walls
    x = 55
    y = 55
    maze = labyrinth()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                running = False

            # draws the screen
            maze.draw()
            pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(x,y,10,10))

        pygame.display.flip()