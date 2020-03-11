import random

## @brief The class creates a Cell object
# # @param None
class Cell(object):

    ## @brief Cell constructor accepts 2 parameters
    # @param id: an integer specifying which the id of the cell
    # @param gridLength: an integer specifying the dimensions of the maze
    def __init__ (self, id: int, gridLength: int):
        self.id = id 
        self.gridLength = gridLength
        self.isVisited = False
        self.cellWalls = []
        self.adjCells = []
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
            self.cellWalls.append(topWall)
       	if (bottomWall < self.gridLength ** 2): # checks if cell is in the bottom row
            self.cellWalls.append(bottomWall)
        if ((leftWall // self.gridLength) == (self.id // self.gridLength)):
            self.cellWalls.append(leftWall)
        if ((rightWall // self.gridLength) == (self.id // self.gridLength)):
            self.cellWalls.append(rightWall) 

testCell = Cell(0, 10)
print(random.choice(testCell.cellWalls))