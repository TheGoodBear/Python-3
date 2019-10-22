# My third Python application
# Maze v1

# Imports of modules
# ------------------
import sys


# Variables (must be declared BEFORE using them)
# ---------

# Define variables for player data (LastName and FirstName)
LastName: str = ""
FirstName: str = ""
# Define variables for maze
MazeFilePath: str = "/Mazes"
MazeFileName: str = "Maze 1"
Maze = list()


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
if not LoadMazeFromFile(MazeFileName):
    sys.exit()

# 3) Game loop
