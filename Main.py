# My third Python application
# Maze v1

# Imports of modules
# ------------------
import sys


# Variables (must be declared BEFORE using them)
# ---------

# Variables for player data
PlayerName: str = ""
# Variables for maze and objects
MazeFilePath: str = "Mazes/"
MazeFileName: str = "Maze 1"
Maze = list()
ObjectsInMaze = ["Statue de Dragon", "Statue de Poisson", "Statue d'Oiseau", "Statue de Buffle", "Miroir", "Clé dorée", "Clé argentée", "Bouteille"]
# Variables for player character
PlayerY: int = 0
PlayerX: int = 0


# Methods (must be declared BEFORE using them)
# -------

def GetPlayerData() -> str:
    """ 
        Get player data

        :return: player name
        :rtype: string
    """

    # Ask for names if they are empty
    Name = input("\nMerci d'entrer ton nom : ")

    # Return Name
    return Name


def SayWelcome():
    """ 
        Say Welcome to player
    """

    print(
        "Enchanté {0}, j'espère que tu vas bien t'amuser." 
        .format(PlayerName))


def LoadMazeFromFile(FileName: str) -> bool:
    """ 
        Load maze from text file and store it into a 2 dimensional list

        :param arg1: The name of the file
        :type arg1: string

        :return: 
            - True if no error
            - False if an error occured
        :rtype: boolean
    """

    # Use global Maze variable
    global MazeFilePath
    global Maze

    # try/exception block, 
    try:
        # Open file (and automaticlly close it when finished)
        with open(MazeFilePath + FileName, "r") as MyFile:
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
        return True
    except OSError:
        print("Le labyrinthe demandé n'a pas été trouvé !")
        return False


def PutMazeObjectsAtRandomPositions():
    """ 
        Put all objects from dictionary at random positions in maze

        :param arg1: The name of the file
        :type arg1: string

        :return: 
            - True if no error
            - False if an error occured
        :rtype: boolean
    """
    
    pass


def DrawMazeOnScreen():
    """ 
        Draw maze in console
    """

    # Use global Maze variable
    global Maze

    # Prints a blank line
    print()

    # For each line (Y) in Maze
    for Y, Line in enumerate(Maze):
        # For each character (X) in line
        for X, Column in enumerate(Maze[Y]):
            # Print current maze element at Y, X without jumping a line
            print(Maze[Y][X], end="")
        # Jump a line for new Y
        print()


def WaitForPlayerAction() -> str:
    """ 
        Wait player to make an action

        :return: 
            - The name of the action if the action
        :rtype: string
    """
    
    # Print a blank line
    print()

    # Ask for player input until it is valid
    while True:
        PlayerInput = input("Entrez une action à effectuer -> se déplacer vers le (H)aut, le (B)as, la (G)auche ou la (D)roite : ")

        # Check if this is a valid action
        if (PlayerInput.upper == "H"):
            return "MoveUp"
        elif (PlayerInput.upper == "B"):
            return "MoveBottom"
        elif (PlayerInput.upper == "G"):
            return "MoveLeft"
        elif (PlayerInput.upper == "D"):
            return "MoveRight"
        else:
            print("Cette action n'est pas reconnue.")


# Application
# -----------

# 1) Splash screen and get player data

# Say Hello to user
print("Bonjour humain, merci de t'identifier afin que je puisse interagir avec toi.")

# While player name is empty
while (PlayerName == ""):

    # Ask for name
    PlayerName = GetPlayerData()

# Say welcome
SayWelcome()


# 2) Initialize Maze

# Load maze from text file to memory 2 dimensions list
if not LoadMazeFromFile(MazeFileName):
    sys.exit()

# Draw maze on screen
DrawMazeOnScreen()

# Put objects in random positions

# Say good luck
print("\nTu es représenté par ☺ et tu dois sortir du labyrinthe, bonne chance.\n")

# 3) Game loop

# Variable for end of game
EndOfGame: bool = False

# Do this code until end of game is triggered
while not EndOfGame:

    # Wait for a player action
    PlayerAction: str = WaitForPlayerAction()

    # Do action
    pass