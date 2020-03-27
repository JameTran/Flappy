# Scoreboard module of the program. This is the module that will be responsible for launching the mini-games
# By Mengxi (William) Lei
# Created 2020/03/27, Last Modified 2020/03/27

# Importation
import pygame
import thorpy

# Class Definition
class Scoreboard:

    # Static Constants
    fileName = None
    gameTitle = ["Maze", "Flappy", "Pong"]
    
    # Static Variables
    scores = [[], [], []]
    displayGame = None
    exitScreen = None



##################################################################################################################################


    # Display the scoreboard
    @staticmethod
    def drawScoreboard(gameName):
        return
    


##################################################################################################################################


    
    # Change the game to be displayed
    @staticmethod
    def changeGame(gameID):
        return
    
    
    
    # Exit the scoreboard
    @staticmethod
    def exitScoreboard():
        return



##################################################################################################################################



    # Read data from file
    @staticmethod
    def readData():
        return



    # Write data to file
    @staticmethod
    def writeData():
        return



##################################################################################################################################



    # Return the highest score of the given game
    @staticmethod
    def highScore(game):
        for index, gameName in enumerate(Scoreboard.gameTitle):
            if game == gameName:
                return scores[index][0]
        return None
    
    
    
    # Update the scoreboard with the given score
    @staticmethod
    def updateScore(game, score):
    
        # Declare variables
        gameID = None
        scoreIndex = None
        tempScore = None
        length = None
        
        # Find the index of the game
        for index, gameName in enumerate(Scoreboard.gameTitle):
            if game == gameName:
                gameID = index
                break;
        if gameID is None:
            return
        
        # Find the index of the score
        scoreIndex = Scoreboard.findScoreLocation(Scoreboard.scores[gameID], score)
        if (scoreIndex < 0):
            return
            
        # Update the given list
        tempScore = score
        length = len(Scoreboard.scores[gameID])
        for index in range(scoreIndex, length):
            tempScore, Scoreboard.scores[gameID][index] = Scoreboard.scores[gameID][index], tempScore



##################################################################################################################################



    # Find the location of where the score fits
    @staticmethod
    def findScoreLocation(scoreList, score):
        for index, value in enumerate(scoreList):
            if score > value:
                return index
        return -1