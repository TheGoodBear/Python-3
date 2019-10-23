# My third Python application
# Maze v1

# Imports of modules
# ------------------
import sys


# Variables (must be declared BEFORE using them)
# ---------

# Variables for player data (LastName and FirstName)
LastName: str = ""
FirstName: str = ""
# Variables for maze and objects
MazeFilePath: str = "/Mazes"
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
        Get player data (First and Last names)

        :return: an error if appropriate
            - "" if no error
            - "LF" if LastName and FirstName are empty
            - "L" if only LastName is empty
            - "F" if only FirstName is empty
        :rtype: string
    """

    # Use global variables (defined at beginning of file)
    global LastName
    global FirstName

    # Ask for names if they are empty
    if (FirstName == ""):
        FirstName = input("Veuillez entrer votre prénom : ")
    if (LastName == ""):
        LastName = input("Veuillez entrer votre nom : ")

    # Check if names are empty
    if (LastName == "" and FirstName == ""):
        return "LF"
    elif (LastName == ""):
        return "L"
    elif (FirstName == ""):
        return "F"


def ShowPlayerDataResult(ErrorMessage: str):
    """ 
        Show player data result
            - Welcome if all data is valid
            - Error message if not

        :param arg1: An error message if any
        :type arg1: string
    """

    # Check for an error message
    if (ErrorMessage == "LF"):
        # Missing both names
        print("Le prénom et le nom entrés sont vides, veuillez recommencer.")
    elif (ErrorMessage == "L"):
        # Missing LastName
        print("Le nom entré est vide, veuillez compléter.")
    elif (ErrorMessage == "F"):
        # Missing FirstName
        print("Le prénom entré est vide, veuillez compléter.")
    else:
        # Both names are not empty
        # Say welcome
        print()
        print(
            "Enchanté {0} {1}, j'espère que tu vas bien t'amuser." 
            .format(FirstName, LastName))


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
        with open(MazeFilePath + "/" + FileName, "r") as MyFile:
            for Line in MyFile:
                # Define temporary list to store evry character in a line
                LineCharacters = list()
                # For each Character in Line
                for Character in Line:
                    # Store Character in LineCharacters list
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
    for Y in Maze:
        # For each character (X) in line
        for X in Maze[Y]:
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
print("Bonjour humain, veuillez vous identifier afin que je puisse interagir avec vous.")

# While LastName or FirstName are empty
while (LastName == "" or FirstName == ""):

    # Print a blank line
    print()

    # Ask for names if they are empty
    # and check if an error occurs
    DataError = GetPlayerData()

    # Show result 
    ShowPlayerDataResult(DataError)

# 2) Initialize Maze

# Load maze from text file to memory 2 dimensions list
if not LoadMazeFromFile(MazeFileName):
    sys.exit()

# Draw maze on screen
DrawMazeOnScreen()

# Put objects in random positions

# 3) Game loop

# Variable for end of game
EndOfGame: bool = False

# Do this code until end of game is triggered
while not EndOfGame:

    # Wait for a player action
    PlayerAction: str = WaitForPlayerAction()

    # Do action
    pass