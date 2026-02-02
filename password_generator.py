# Password Generator Application
# Generates a strong random password based on user-defined length

import random
import string

print("_______________________________________")
print("          PASSWORD GENERATOR           ")
print("_______________________________________\n")

# Main loop for password generation
while True:
    try:
        length = int(input("Enter Password length (0 = Cancel): "))
        if length == 0:
            print("\n_______________________________________")
            print("            THANKS FOR COMING!          ")
            print("\n_______________________________________")
            break
    except:
        print("Please! Enter only integer numbers.")
        exit()

    # Character set for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""  # Variable to store generated password

    # Generate password using random choices
    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)
    print("\n_______________________________________")
