# Password Generator

import random
import string

print("_______________________________________")
print("          PASSWORD GENERATOR           ")
print("_______________________________________\n")

while(True):
    try:
        length = int(input("Enter Password length (0 = Cancel): "))
        if length == 0 :
            print("\n_______________________________________")
            print("            THANKS FOR COMING!           ")
            print("\n_______________________________________")
            break
    except:
        print("Please! Enter only integer numbers.")
        exit()

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password: ", password)

    print("\n_______________________________________")