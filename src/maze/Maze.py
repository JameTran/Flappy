import random
import Cell

## @brief This class creates the Maze object
# @param None
class Maze(object):

    def __init__ (self, size):
        self.size = size # the dimension of one side of the maze
        self.cells = [Cell(i, size) for i in range (size ** 2)]
        self.startingCell = self.cells[0]
        self.endingCell = self.cells[size ** 2 - 1]

    def createNeighbours(self, cell1: Cell, cell2: Cell):
        pass

    def checkAdjacent(self):
        pass

    def genMaze (self):
        
        visited = [self.startingNode.id]
        self.startingCell.isVisited = True
        

        while (len(cells)):
            randWall = random.choice(visited)
            self.cells[randWall].isVisited = True
            

