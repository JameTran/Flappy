#### Program Breakdown

```python
class Cell:
    def __init__ (self, id: int, gridLength: int):
        self.id = id # [0 .. gridLength], [gridLength + 1 .. gridLength * 2]
        self.gridLength = gridLength
        self.isVisited = False
        self.cellWalls = []
        self.genWalls()
    
    def genWalls (self) # generates the walls of the cell and appends it to the list of cellWalls
        

```

```python
class Maze:
    def __init__ (self):
        
       
    def blankMaze(self) # generates a maze with all walls
        
```

```python
def PrimAlg
```

```python
class App:
    
```





#### Prim's Algorithm

1. Start with a grid full of walls

2. Pick a cell, mark is as part of the maze. Add the walls of the cell to the wall list

   ```python
   startingCell = (Cell.id == 0)
   ```

3. While there are walls in the list

   1. Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
      1. Make the wall a passage and mark the unvisited cell as part of the maze
      2. Add the neighbouring walls of the cell to the wall list
   2. Remove the wall from the list

```python
startingPoint = cell[0]

choose random wall
check if adjacent cell is visited
if not remove wall from list and mark cell as visited
else break

choose random wall 

```



#### Types of Modules

Behaviour hiding may hide input formats, screen formats, and text messages

Software decision hiding may hide internal data structures and algorithms

Hardware hiding may hide the hardware machine or the "virtual machine" provided by the operating system and

utilities



#### Maze Modules

Software Decision Hiding:

* Maze Generator
* Score Tracking ( Maze )

Behaviour Hiding:

* Draw Game ( Maze )
* Player Movement ( Maze )
* Main Menu & Settings ( Maze )

#### Pong Modules

Software Decision Hiding:

* Ball Trajectory
* Score Tracking ( Pong )

Behaviour Hiding:

* Draw Game ( Pong )
* Player Movement ( Pong )
* Main Menu & Settings ( Pong )