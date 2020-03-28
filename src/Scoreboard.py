# Scoreboard module of the program. This is the module that will be responsible for launching the mini-games
# By Mengxi (William) Lei
# Created 2020/03/27, Last Modified 2020/03/28

# Importation
import pygame
import thorpy
import Launcher

# Class Definition
class Scoreboard:

    # Static Constants
    fileName = "scores"
    gameTitle = Launcher.gameTitle
    
    # Static Variables
    scores = []
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
        if (exitScreen < len(gameTitle)):
            Launcher.launchGame(exitScreen)
        else:
            Launcher.displayLauncher()



##################################################################################################################################



    # Read data from file
    @staticmethod
    def readData():
        
        # Declare variables
        file = None
        tempArray = None
        
        # Open file
        file = open(fileName, "r")
        
        # Read the data
        for game in gameTitle:
            tempArray = file.readline().split()
            scores.append([])
            for element in tempArray:
                scores[-1].append(int(element))
        
        # Close file
        file.close()



    # Write data to file
    @staticmethod
    def writeData():
        
        # Declare variables
        file = None
        tempString = None
        
        # Open file
        file = open(fileName, "w")
        
        # Write to file
        for game in scores:
            tempString = " ".join([str(element) for element in game])
            tempString += "\n"
            file.write(tempString)
        
        # Close file
        file.close()



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