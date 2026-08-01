# Import the random module.
# It is used to randomly select characters.
import random

# Import the string module.
# It provides ready-made collections of letters,
# numbers, and special characters.
import string

# Take the desired password length from the user.
length = int(input("Password Length: "))

# Create a collection of characters that can be
# used in the password.
# It includes:
# - Uppercase and lowercase letters
# - Numbers
# - Special characters
chars = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

# Generate a random password.
# random.choice() selects one random character
# from the character collection.
# The loop repeats until the required password
# length is reached.
password = "".join(
    random.choice(chars)
    for _ in range(length)
)

# Display a heading.
print("\nGenerated Password:")

# Display the generated password.
print(password)