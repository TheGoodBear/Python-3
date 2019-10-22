# My first Python application

# Define variables for LastName and FirstName
LastName = ""
FirstName = ""

# Say Hello to user
print("Bonjour humain, veuillez vous identifier afin que je puisse interagir avec vous.")

# While LastName or FirstName are empty
while (LastName == "" or FirstName == ""):

    # Print a blank line
    print()

    # Ask for names if they are empty
    if (FirstName == ""):
        FirstName = input("Veuillez entrer votre prénom : ")
    if (LastName == ""):
        LastName = input("Veuillez entrer votre nom : ")

    # Check if names are empty
    if (LastName == "" and FirstName == ""):
        print("Le prénom et le nom entrés sont vides, veuillez recommencer.")
    elif (LastName == ""):
        print("Le nom entré est vide, veuillez compléter.")
    elif (FirstName == ""):
        print("Le prénom entré est vide, veuillez compléter.")

# Both names are not empty
# Say welcome
print()
print("Enchanté", FirstName, LastName, " je te souhaite une belle journée.")