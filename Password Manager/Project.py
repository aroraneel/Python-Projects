# Import the random module to generate random characters
import random

# Import the string module to access letters, digits, and symbols
import string

# Create an empty dictionary to store website names and passwords
passwords = {}

# -------------------- Load Existing Passwords --------------------

# Try to read previously saved passwords from the file
try:
    with open("passwords.txt", "r") as file:

        # Read each line from the file
        for line in file:

            # Split the line into website and password using ":"
            website, pwd = line.strip().split(":")

            # Store the data in the dictionary
            passwords[website] = pwd

# If the file does not exist, ignore the error
except:
    pass

# -------------------- Password Generator Function --------------------

# Function to generate a random password
def generate_password():

    # Function to generate a random password
    chars = string.ascii_letters + string.digits + "!@#$%^&*()+[]"

    # Generate an 8-character random password
    password = ''.join(random.choice(chars) for _ in range(8))

    # Return the generated password
    return password

# -------------------- Main Program --------------------

# Run the program continuously until the user exits
while True:

    # Display the main menu
    print("\nPassword Manager")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")

    # Take the user's choice
    choice = input("Enter Your Choice: ")

    # -------------------- Save Password --------------------
    if choice == "1":

        # Ask the user for the website name
        website = input("Enter Website Name: ")

        # Ask the user for the password
        pwd = input("Enter Password: ")

        # Store the website and password in the dictionary
        passwords[website] = pwd

        # Save the password permanently in passwords.txt
        with open("passwords.txt", "a") as file:
            file.write(f"{website}:{pwd}\n")

        # Display success message
        print("Password Saved Successfully!")

    # -------------------- View Passwords --------------------
    elif choice == "2":

        # Check if there are any saved passwords
        if not passwords:
            print("No passwords saved yet.")

        else:
            # Display all saved websites and passwords
            for website, pwd in passwords.items():
                print(website, ":", pwd)

    # -------------------- Generate Password --------------------
    elif choice == "3":

        # Display a randomly generated password
        print("Generated Password:", generate_password())

    # -------------------- Exit Program --------------------
    elif choice == "4":

        # Display exit message
        print("Exitting Password Manager. Goodbye!")

        # Stop the program
        break

    # -------------------- Invalid Choice --------------------
    else:

        # Display an error message for an invalid menu option
        print("Invalid Choice. Please Try Again.")
