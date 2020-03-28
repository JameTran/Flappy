# Launcher module of the program. This is the module that will be responsible for launching the mini-games
# By Mengxi (William) Lei
# Created 2020/02/11, Last Modified 2020/03/28

# Importation
import pygame
import thorpy
from maze import MazeGame
from pong import PongGame
import Scoreboard

# Class Definition
class Launcher:

    # Static Constants
    gameTitle = ["Maze", "Flappy", "Pong"]
    games = [MazeGame.MazeGame(), None, PongGame]
    

    
##################################################################################################################################
    
    
    
    # Displaying the launcher
    @staticmethod
    def displayLauncher():

        # Declare Variables
        index = None                 #int
        game = None                  #string
        application = None           #Application(thorpy)
        buttons = [None, None, None] #Clickable(thorpy) Array
        quitButtons = None           #Clickable(thorpy)
        buttonGroup = None           #Group(thorpy)
        menu = None                  #Menu(thorpy)
        
        # Create GUI and set theme
        application = thorpy.Application(size=(1280,800), caption="Mini-Games")
        thorpy.theme.set_theme("human")

        # Create buttons
        for index, game in enumerate(Launcher.gameTitle):
            buttons[index] = thorpy.Clickable(game)
            buttons[index].user_func = Launcher.launchGame
            buttons[index].user_params = {"game": index}
            buttons[index].set_size((100, 50))
            buttons[index].set_main_color((102,204,255))
        quitButtons = thorpy.Clickable("Exit")
        quitButtons.user_func = thorpy.functions.quit_menu_func
        
        # Format the buttons
        buttonGroup = thorpy.make_group(buttons)

        # Set background
        background = thorpy.Background(color=(255,255,255), elements=[buttonGroup, quitButtons])
        thorpy.store(background)

        # Create menu and display
        menu = thorpy.Menu(background)
        menu.play()

        # Exiting
        application.quit()



##################################################################################################################################



    # Launch the given game
    @staticmethod
    def launchGame(gameID):
        if gameID == 0:
            Launcher.games[gameID].on_execute()
        elif gameID == 1:
            print("\nRunning " + Launcher.gameTitle[gameID] + "\n\n")
        else:
            Launcher.games[gameID].playGame()



##################################################################################################################################



# Main
if __name__ == "__main__":
    Launcher.displayLauncher()