import random

## @brief The class creates a Cell object
class Cell(object):

    ## @brief Cell constructor
    # @param id: an integer specifying which the id of the cell
    # @param gridLength: an integer specifying the dimensions of the maze
    # @return None
    def __init__ (self, id: int, gridLength: int):
        self.id = id 
        self.gridLength = gridLength
        self.isVisited = False
        self.walls = []
        self.genWalls()
    
    ## @brief Identifies the walls of the current cell and appends it to the cellWalls
    # @param No arguments
    # @return None
    def genWalls (self):
        topWall = self.id - self.gridLength
        bottomWall = self.id + self.gridLength
        leftWall = self.id - 1
        rightWall = self.id + 1
        
        if (topWall >= 0): # checks if cell is in the top row
            self.walls.append((self.id, topWall))
       	if (bottomWall < self.gridLength ** 2): # checks if cell is in the bottom row
            self.walls.append((self.id, bottomWall))
        if ((leftWall // self.gridLength) == (self.id // self.gridLength)):
            self.walls.append((self.id,leftWall))
        if ((rightWall // self.gridLength) == (self.id // self.gridLength)):
            self.walls.append((self.id,rightWall))
