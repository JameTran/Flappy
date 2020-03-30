import pygame
from pygame.locals import *

## @brief Represents the Player class
class Player:
 
    ## @brief Constructor for the player class
    # @param None
    # @return None
    def __init__(self):
        self.size = 0
        self.walls = []
        self.isWon = False
    
    ## @brief A callable function to set the player based on the size and walls
    # @param size: an integer representing the size of the maze
    # @param walls: a list of tuples representing the walls of the maze for collision purposes
    # @return None
    def setPlayer(self, size, walls):
        self.size = size
        self.playerPos()
        self.goalPos()
        self.walls = walls
        self.isWon = False

    ## @brief Sets the player position based on the maze size
    # @param None
    # @return None
    def playerPos(self):
        if (self.size == 15): self.rect = pygame.Rect(310, 60, 20, 20)
        elif (self.size == 25): self.rect = pygame.Rect(302, 54, 12, 12)
        elif (self.size == 30): self.rect = pygame.Rect(300, 51, 10, 10)

    ## @brief Sets the goal position based on the maze size
    # @param None
    # @return None
    def goalPos(self):
        if (self.size == 15): self.goal = pygame.Rect(958, 708, 20, 20)
        elif (self.size == 25): self.goal = pygame.Rect(973, 724, 12, 12)
        elif (self.size == 30): self.goal = pygame.Rect(975, 726, 10, 10)
    
    ## @brief Controls player movement
    # @param dx: a float representing the player's x position
    # @param dy: a float representing the player's y position
    # @return None
    def move(self, dx, dy):    
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0.0:
            self.move_single_axis(dx, 0)
        if dy != 0.0:
            self.move_single_axis(0, dy)
    
    ## @brief Determiens if a player's movement results in a collision with a maze wall
    # @param dx: a float representing the player's x position
    # @param dy: a float representing the player's y position
    # @return None
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in self.walls:
            if self.rect.colliderect(wall):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.bottom
        
        if self.rect.colliderect(self.goal): self.isWon = True
