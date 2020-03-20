# Launcher module of the program. This is the module that will be responsible for launching the mini-games
# By Mengxi (William) Lei
# Created 2020/02/11, Last Modified 2020/02/11

# Importation
import pygame
from maze import MazeGame

# Class Definition
class Launcher :

    #Static Variables
    Maze = MazeGame.MazeGame()
    
    
##################################################################################################################################
    
    
    
    # Displaying the launcher
    @staticmethod
    def displayLauncher():
        # Declare Variables
        gameTitle = ["Maze", "Flappy", "Pong"]
        games = [Launcher.Maze, "Flappy", "Pong"]
        index = None
        game = None
        userInput = None

        # Main loop
        while True:
            print("Please enter the number representing the option you wish to select:")
            for index, game in enumerate(gameTitle):
                print("\t" + str(index+1) + ": " + game)
            print("\t0: Exit\n")
            userInput = input()
            if userInput == "0":
                print("\nExiting\n\n")
                break
            elif userInput >= 1 and userInput <=3:
                print("\nRunning " + gameTitle[userInput-1] + "\n\n")
            else:
                print("\n\nInvalid number, please enter a valid number.\n\n")



##################################################################################################################################



# Main
if __name__ == "__main__":
    Launcher.displayLauncher()