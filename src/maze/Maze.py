import pygame
from pygame.locals import *
import random
import math
from maze import Cell

## @brief This class creates the Maze object
class Maze(object):

    ## @brief Constructor for the Maze class
    # @param None
    # @return: None
    def __init__ (self):
        self.size = 0 # the dimension of one side of the maze
        self.cells = []
        self.startingCell = None
        self.endingCell = None
        self.mazeWalls = []
        self.allRect = []

    ## @brief A callable function that initializes the maze
    # @param size: an integer representing a dimension of the maze
    # @return None
    def setMaze(self, size):
        self.size = size # the dimension of one side of the maze
        self.cells = [Cell.Cell(i, size) for i in range (size ** 2)]
        self.startingCell = self.cells[0]
        self.endingCell = self.cells[size ** 2 - 1]
        self.mazeWalls = []
        self.allRect = []
        self.genMaze()

    ## @brief Determines if the cells given have been visited
    # @param id: a tuple of ids, each representing a cell
    # @return the cell that has not been visited
    def checkVisited(self, id):
        if (self.cells[id[0]].isVisited == False):
            self.cells[id[0]].isVisited = True
            return self.cells[id[0]]
        else:    
            self.cells[id[1]].isVisited = True
            return self.cells[id[1]]
        
    ## @brief Generates the maze using prim's algorithm and stores the remaining walls in mazeWalls
    # @param None
    # @return None
    def genMaze (self):
        # Generates maze walls
        for i in range (self.size ** 2):
            for j in (self.cells[i].walls):
                if ((j[1], j[0]) not in self.mazeWalls):
                    self.mazeWalls.append(j)
        # Initialize starting position
        self.startingCell.isVisited = True  
        wallList = [self.startingCell.walls[0], self.startingCell.walls[1]]

        while (len(wallList) > 0):
            currWall = random.choice(wallList)
            if (currWall[0] > currWall[1]): currWall = (currWall[1], currWall[0])
            if (self.cells[currWall[0]].isVisited != self.cells[currWall[1]].isVisited):
                currCell = self.checkVisited(currWall)
                self.mazeWalls.remove(currWall)
                for i in (currCell.walls):
                    if (i != currWall and ((i[1], i[0]) != currWall)):
                        if (i[0] > i[1]): wallList.append((i[1], i[0]))
                        else: wallList.append(i)
            wallList.remove((currWall))
        self.transformWalls()

    ## @brief Transforms the walls from prim's algorithm into tuples that represent the pygame rectangle command
    # @param None
    # @return None
    def transformWalls(self):
        l = 700 / self.size # wall length
        vo = 40 # vertical offset
        ho = (1280 - 700) // 2  # hortizontal offset
        if (self.size == 15): 
            t = 10 # wall thickness
        elif (self.size == 25): 
            t = 8 
        elif (self.size == 30):
            t = 6
    
        rect = pygame.Rect(ho, vo, 700 + t, t)
        self.allRect.append(rect)

        rect = pygame.Rect(ho, self.size * l + vo, 700 + t, t)
        self.allRect.append(rect)

        rect = pygame.Rect(ho, vo, t, 700)
        self.allRect.append(rect)

        rect = pygame.Rect(700 + ho, vo, t, 700)
        self.allRect.append(rect)

        for i in self.mazeWalls: # Draw walls
            if (i[1] - i[0] == 1): # Right wall
                rect = pygame.Rect(i[1] % self.size * l + ho, i[1] // self.size * l + vo, t, l + t)
                self.allRect.append(rect)
            elif ((i[1] - i[0]) == self.size): # Bottom wall
                rect = pygame.Rect(i[0] % self.size * l + ho, i[1] // self.size * l + vo, l + t, t)
                self.allRect.append(rect)
  
    ## @brief Draws the maze given the mazeWalls from the transform
    # @param display_surf: the output window from the MazeGame
    # @return None
    def draw(self, display_surf):
        for i in self.allRect: # Draw walls
            pygame.draw.rect(display_surf, (0, 0, 0), i)
            

