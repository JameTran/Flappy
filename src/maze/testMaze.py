import pytest
import Cell
import Player

def testCellCreation():
    testCell = Cell.Cell(0, 5) # Creates the first cell with a maze of size 5 x 5
    assert isinstance(testCell, Cell.Cell)

def testCellWalls():
    testCell = Cell.Cell(0, 5)
    assert testCell.walls == [(0, 5), (0, 1)]

def testCellNumWalls():
    testCell = Cell.Cell(6, 5)
    assert len(testCell.walls) == 4

def testCellVisited():
    testCell = Cell.Cell(0, 5)
    assert testCell.isVisited == False

def testPlayerCreation():
    testPlayer = Player.Player()
    testPlayer.setPlayer(5, [1, 2, 3])
    assert isinstance(testPlayer, Player.Player)
