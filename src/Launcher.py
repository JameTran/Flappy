# Launcher module of the program. This is the module that will be responsible for launching the mini-games
# By Mengxi (William) Lei
# Created 2020/02/11, Last Modified 2020/03/29

# Importation
import pygame
import thorpy
from maze import MazeGame
from pong import PlayPong
from flappy import playFlappy
import Scoreboard

# Class Definition
class Launcher:

    # Static Constants
    gameTitle = ["Maze", "Flappy", "Pong"]
    games = [MazeGame.MazeGame(), playFlappy, PlayPong]
    

    
#################################################################################################################################
    
    
    
    # Displaying the launcher
    @staticmethod
    def displayLauncher():

        # Declare Variables
        index = None                 #int
        game = None                  #String
        application = None           #Application(thorpy)
        buttons = [None, None, None] #Clickable(thorpy) Array
        scoreboardButton = None      #Clickable(thorpy)
        quitButton = None            #Clickable(thorpy)
        buttonGroup = None           #Group(thorpy)
        menu = None                  #Menu(thorpy)
        background = None            #Background(thorpy)
        painter = None               #Painters(thorpy)
        title = None                 #Text(thorpy)
        
        
        # Create GUI and set theme
        application = thorpy.Application(size=(1280,800), caption="Mini-Arcade")
        thorpy.theme.set_theme("human")
        
        # Create title
        title = thorpy.make_text("Mini-Arcade\n", 35, (0,0,0))

        # Create buttons
        painter = thorpy.painters.roundrect.RoundRect(size=(150,75),color=(102,204,255),radius=0.3)
        for index, game in enumerate(Launcher.gameTitle):
            buttons[index] = Launcher.createButton(game, index, painter)
        scoreboardButton = thorpy.Clickable("Scoreboard")
        scoreboardButton.user_func = Launcher.launchScoreboard
        scoreboardButton.set_painter(painter)
        scoreboardButton.finish()
        scoreboardButton.set_font_size(23)
        scoreboardButton.set_font_color_hover((57,197,187))
        quitButton = thorpy.Clickable("Exit")
        quitButton.user_func = thorpy.functions.quit_menu_func
        quitButton.set_painter(painter)
        quitButton.finish()
        quitButton.set_font_size(23)
        quitButton.set_font_color_hover((57,197,187))
        
        # Format the buttons
        buttonGroup = thorpy.make_group(buttons)

        # Set background
        background = thorpy.Background(color=(255,255,255),
                                       elements=[title, buttonGroup, scoreboardButton, quitButton])
        thorpy.store(background)

        # Create menu and display
        menu = thorpy.Menu(background)
        menu.play()

        # Exiting
        application.quit()



#################################################################################################################################



    # Launch the given game
    @staticmethod
    def launchGame(gameID):
        if gameID == 0:
            Launcher.games[gameID].on_execute()
        else:
            Launcher.games[gameID].playGame()
    
    
    
    # Launch the scoreboard
    @staticmethod
    def launchScoreboard():
        Scoreboard.Scoreboard.drawScoreboard("Launcher")
    
    
    
    # Create a buttton
    @staticmethod
    def createButton(title, index, painter):
        
        # Declare Variables
        button = None  #Clickable(thorpy)

        # Create button
        button = thorpy.Clickable(title)
        button.user_func = Launcher.launchGame
        button.user_params = {"gameID": index}
        button.set_painter(painter)
        button.finish()
        button.set_font_size(23)
        button.set_font_color_hover((57,197,187))
        
        # Return
        return button



#################################################################################################################################



# Main
if __name__ == "__main__":
    Scoreboard.Scoreboard.readData()
    Launcher.displayLauncher()