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
    gameTitle = ["Maze", "Flappy", "Pong"]
    
    # Static Variables
    scores = []
    displayGame = None
    exitScreen = None



#################################################################################################################################



    # Display the scoreboard
    @staticmethod
    def drawScoreboard(gameName):
        
        # Declare variables
        notFound = True
        
        # Set value of displayGame and exitScreen
        for index, game in enumerate(Scoreboard.gameTitle):
            if gameName == game:
                Scoreboard.displayGame = index
                Scoreboard.exitScreen = index
                notFound = False
                break
        if notFound:
            Scoreboard.displayGame = 0
            Scoreboard.exitScreen = len(Scoreboard.gameTitle)
        
        # Draw and display the scoreboard
        Scoreboard.drawBoard()
    
    
    
    # Draw the scoreboard
    @staticmethod
    def drawBoard():
        
        # Declare variables
        application = None           #Application(thorpy)
        title = None                 #Text(thorpy)
        buttons = [None, None, None] #Clickable/Element(thorpy) Array
        quitButton = None            #Clickable(thorpy)
        painter1 = None              #Painters(thorpy)
        painter2 = None              #Painters(thorpy)
        buttonGroup = None           #Group(thorpy)
        menu = None                  #Menu(thorpy)
        background = None            #Background(thorpy)
        
        # Create GUI and set theme
        application = thorpy.Application(size=(1280,800), caption="Mini-Arcade")
        thorpy.theme.set_theme("human")
        
        # Create title
        title = thorpy.make_text("Scoreboard\n", 35, (0,0,0))
        
        # Create buttons
        painter1 = thorpy.painters.roundrect.RoundRect(size=(100,50),color=(102,204,255),radius=0.3)
        painter2 = thorpy.painters.roundrect.RoundRect(size=(100,50),color=(57,197,187),radius=0.3)
        for index, game in enumerate(Scoreboard.gameTitle):
            buttons[index] = Scoreboard.createButton(game, index, painter1, painter2)
        quitButton = thorpy.Clickable("Return")
        quitButton.user_func = Scoreboard.exitScoreboard
        quitButton.set_painter(painter1)
        quitButton.finish()
        quitButton.set_font_size(17)
        quitButton.set_font_color_hover((57,197,187))
        
        # Format the buttons
        buttonGroup = thorpy.make_group(buttons)

        # Set background
        background = thorpy.Background(color=(255,255,255), elements=[title, buttonGroup, quitButton])
        thorpy.store(background)

        # Create menu and display
        menu = thorpy.Menu(background)
        menu.play()

        # Exiting
        application.quit()
    


#################################################################################################################################


    
    # Change the game to be displayed
    @staticmethod
    def changeGame(gameID):
        displayGame = gameID
        Scoreboard.drawBoard()
    
    
    
    # Exit the scoreboard
    @staticmethod
    def exitScoreboard():
        if (Scoreboard.exitScreen < len(Scoreboard.gameTitle) and Scoreboard.exitScreen > -1):
            Launcher.launchGame(Scoreboard.exitScreen)
        else:
            Launcher.displayLauncher()



#################################################################################################################################



    # Read data from file
    @staticmethod
    def readData():
        
        # Declare variables
        file = None
        tempArray = None
        
        # Open file
        file = open(Scoreboard.fileName, "r")
        
        # Read the data
        for game in Scoreboard.gameTitle:
            tempArray = file.readline().split()
            Scoreboard.scores.append([])
            for element in tempArray:
                Scoreboard.scores[-1].append(int(element))
        
        # Close file
        file.close()



    # Write data to file
    @staticmethod
    def writeData():
        
        # Declare variables
        file = None
        tempString = None
        
        # Open file
        file = open(Scoreboard.fileName, "w")
        
        # Write to file
        for game in Scoreboard.scores:
            tempString = " ".join([str(element) for element in game])
            tempString += "\n"
            file.write(tempString)
        
        # Close file
        file.close()



#################################################################################################################################



    # Return the highest score of the given game
    @staticmethod
    def highScore(game):
        for index, gameName in enumerate(Scoreboard.gameTitle):
            if game == gameName:
                return Scoreboard.scores[index][0]
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
        
        # Update file after updating high score
        Scoreboard.writeData()



#################################################################################################################################



    # Create a buttton
    @staticmethod
    def createButton(title, index, painter1, painter2):
        
        # Declare Variables
        button = None  #Clickable(thorpy)

        # Create button
        if index != Scoreboard.displayGame: # Clickable Button
            button = thorpy.Clickable(title)
            button.user_func = Scoreboard.changeGame
            button.user_params = {"gameID": index}
            button.set_painter(painter1)
            button.finish()
            button.set_font_size(17)
            button.set_font_color_hover((57,197,187))
        else: # Non-clickable Button
            button = thorpy.Element(title)
            button.set_painter(painter2)
            button.finish()
            button.set_font_size(17)
        
        # Return
        return button
    
    
    
    # Find the location of where the score fits
    @staticmethod
    def findScoreLocation(scoreList, score):
        for index, value in enumerate(scoreList):
            if score > value:
                return index
        return -1