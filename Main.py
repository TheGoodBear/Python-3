# Maze v1

# Variables (must be declared BEFORE using them)
# ---------

# Variables for player data
PlayerName: str = ""
PlayerImage: str = "☻" # alt+2
# Variables for maze and objects
MazeFilePath: str = "Mazes/"
MazeFileName: str = "Maze 1"
Maze = list()
# Variables for player character
PlayerX: int = 0
PlayerY: int = 0


# Methods (must be declared BEFORE using them)
# -------

def ApplicationStart():
    """ 
        Initialize application and show initial message
    """

    print("\nBonjour humain, merci de t'identifier afin que je puisse interagir avec toi.")


def GetPlayerData() -> str:
    """ 
        Get player data

        :return: Player name
        :rtype: string
    """

    Name: str = ""

    # While player name is empty
    while (Name == ""):
        # Ask for name
        Name = input("\nMerci d'entrer ton nom : ")

    # Return Name
    return Name


def SayWelcome():
    """ 
        Say Welcome to player
    """

    print(
        "\nEnchanté {0}, j'espère que tu vas bien t'amuser." 
        .format(PlayerName))


def StartGame():
    """ 
        Give rules to player
    """

    print(
        "\nTon objectif est de sortir du labyrinthe." + 
        "\nTu es représenté par {0}, à chaque tour tu peux effectuer l'une des actions suivantes :".format(PlayerImage) + 
        "\nTe déplacer vers le (H)aut, le (B)as, la (G)auche, la (D)roite ou (Q)uitter le jeu (et perdre...)" + 
        "\nBonne chance.")


def LoadMazeFromFile(FileName: str):
    """ 
        Load maze from text file and store it into a 2 dimensional list

        :param arg1: The name of the file
        :type arg1: string
    """

    # Use global Maze variable
    global Maze

    # Open file (and automatically close it when finished)
    with open(MazeFilePath + FileName + ".maz", "r") as MyFile:
        for Line in MyFile:
            # Define temporary list to store evry character in a line
            LineCharacters = list()
            # For each Character in Line
            for Character in Line:
                # Store Character in LineCharacters list (except new line \n)
                if (Character != "\n"):
                    LineCharacters.append(Character)
            # Store LineCharacters list in Maze list (2 dimensional list)
            Maze.append(LineCharacters)


def DrawMazeOnScreen():
    """ 
        Draw maze in console
        Including player
    """

    # Prints a blank line
    print()

    # For each line (Y) in Maze
    for Line in Maze:
        # For each character (X) in line
        for Column in Line:
            # Print current maze element at Y, X without jumping a line
            print(Column, end="")
        # Jump a line for new Y
        print()
    

def PlacePlayerInMaze(
    PlayerNewX: int = 0,
    PlayerNewY: int = 0):
    """ 
        Place player in maze

        :param arg1: The new X position of player
        :type arg1: integer
        :param arg2: The new Y position of player
        :type arg2: integer
    """

    # Use global variables
    global Maze, PlayerX, PlayerY

    # Variables for maze coordinates
    X: int = 0
    Y: int = 0

    # Check if player is not already in the maze (coordinates set to 0)
    if (PlayerX == 0 and PlayerY == 0):
        # In that case put him at the entrance
        # find it by browsing maze list
        for Line in Maze:
            # New line, set X coordinate to 0
            X = 0
            for Character in Line:
                # If position contains entrance (E)
                if (Maze[Y][X] == "E"):
                    # Save coordinates for player
                    PlayerX = X
                    PlayerY = Y
                    # Replace entrance with player
                    Maze[Y][X] = PlayerImage
                    # Exit loops (and method)
                    return
                # Increment X coordinate
                X += 1
            # Increment Y coordinate
            Y += 1

    else:
        # Player is already in maze
        # replace actual player position with an empty space
        Maze[PlayerY][PlayerX] = " "
        # and place player to new position
        Maze[PlayerNewY][PlayerNewX] = PlayerImage


def WaitForPlayerAction() -> str:
    """ 
        Wait player to make an action

        :return: The name of the action if the action is valid
        :rtype: string
    """

    # Ask for player input until it is valid
    while True:
        PlayerInput = input("\nQuelle est ta prochaine action ? ")

        # Check if this is a valid action
        # show a message saying what player is doing
        # and return action name if valid
        if (PlayerInput.upper() == "H"):
            print("Tu te déplaces vers le haut...")
            return "MoveUp"
        elif (PlayerInput.upper() == "B"):
            print("Tu te déplaces vers le bas...")
            return "MoveDown"
        elif (PlayerInput.upper() == "G"):
            print("Tu te déplaces vers la gauche...")
            return "MoveLeft"
        elif (PlayerInput.upper() == "D"):
            print("Tu te déplaces vers la droite...")
            return "MoveRight"
        elif (PlayerInput.upper() == "Q"):
            print("Tu choisis de quitter le labyrinthe, tu as perdu !\n")
            return "QuitGame"
        else:
            print("Cette action n'est pas reconnue.")


def ExecutePlayerAction(PlayerAction: str) -> bool:
    """ 
        Execute player action and returns new position

        :param arg1: The action
        :type arg1: string

        :return: If this is the end of the game
        :rtype: boolean
    """

    # Use global variables
    global PlayerX, PlayerY

    # Variables for new player coordinates
    PlayerNewX: int = PlayerX
    PlayerNewY: int = PlayerY

    # Calculate player new coordinates
    if (PlayerAction == "MoveUp"):
        PlayerNewY -= 1
    elif (PlayerAction == "MoveDown"):
        PlayerNewY += 1
    elif (PlayerAction == "MoveLeft"):
        PlayerNewX -= 1
    elif (PlayerAction == "MoveRight"):
        PlayerNewX += 1
    elif (PlayerAction == "QuitGame"):
        # If action is QuitGame the return game end
        return True


    # Check if new coordinates are valid (into maze limits and no obstacle)
    # or if exit is reached
    if (PlayerNewX<0 or 
        PlayerNewX>len(Maze[0]) or 
        PlayerNewY<0 or 
        PlayerNewY>len(Maze)):
        # If player is out of maze limits
        print("Tu es en dehors des limites, tu ne peux pas aller par là !")
        # and redraw maze with new player position
        DrawMazeOnScreen()
        return False
    elif (Maze[PlayerNewY][PlayerNewX] == "*"):
        # If there is an obstacle, say it
        print("Oups un mur, tu ne peux pas bouger !")
        # and redraw maze with new player position
        DrawMazeOnScreen()
        return False
    elif (Maze[PlayerNewY][PlayerNewX] == "X"):
        # If exit is reached
        # replace player in maze
        PlacePlayerInMaze(PlayerNewX,PlayerNewY)
        # assign new coordinates to player
        PlayerX = PlayerNewX
        PlayerY = PlayerNewY
        # redraw maze with new player position
        DrawMazeOnScreen()
        # say victory
        print("\nOuiiii, bravo {0}, tu as trouvé la sortie !\n".format(PlayerName))
        # and return game end
        return True
    else:
        # If nothing special
        # replace player in maze
        PlacePlayerInMaze(PlayerNewX,PlayerNewY)
        # assign new coordinates to player
        PlayerX = PlayerNewX
        PlayerY = PlayerNewY
        # and redraw maze with new player position
        DrawMazeOnScreen()
        return False


# Application
# -----------

# 1) Show initial message and get player data

# Application start
ApplicationStart()

# Ask for name
PlayerName = GetPlayerData()

# Say welcome
SayWelcome()


# 2) Initialize Maze

# Load maze from text file to memory 2 dimensions list
LoadMazeFromFile(MazeFileName)

# Place player in maze
PlacePlayerInMaze()

# Draw maze on screen
DrawMazeOnScreen()

# Put objects in random positions

# Start game
StartGame()


# 3) Game loop

# Variable for end of game
EndOfGame: bool = False

# Do this code until end of game is triggered
while not EndOfGame:

    # Wait for a player action
    PlayerAction: str = WaitForPlayerAction()

    # Do action
    EndOfGame = ExecutePlayerAction(PlayerAction)
