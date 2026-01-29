# Password Generator 

import random
import string

print("_______________________________________")
print("          PASSWORD GENERATOR           ")
print("_______________________________________\n")

try:
    length = int(input("Enter Password length: "))
except:
    print("Please! Enter only float numbers.")
    exit()

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password: ", password)

print("\n_______________________________________")