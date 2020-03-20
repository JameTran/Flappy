# Launcher module of the program. This is the module that will be responsible for launching the mini-games
# By Mengxi (William) Lei
# Created 2020/02/11, Last Modified 2020/02/11



##################################################################################################################################


if __name__ == "__main__":

    # Declare Variables
    games = ["Maze", "Flappy", "Pong"]
    index = None
    game = None
    userInput = None

    # Main loop
    while True:
        print("Please enter the number representing the option you wish to select:")
        for index, game in enumerate(games):
            print("\t" + str(index+1) + ": " + game)
        print("\t0: Exit")
        print("\n")
        userInput = input()
        print("\n")
        if userInput == "0":
            print("Exiting")
            break
        elif userInput == "1":
            print("Running Maze")
        elif userInput == "2":
            print("Running Flappy")
        elif userInput == "3":
            print("Running Pong")
        else:
            print("\n")
            print("Invalid number, please enter a valid number.")
        print("\n\n")