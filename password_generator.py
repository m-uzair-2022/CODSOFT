# Password Generator - CodSoft Internship Task 3

import random
import string

print("_______________________________________")
print("          PASSWORD GENERATOR           ")
print("_______________________________________\n")

length = int(input("Enter Password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password: ", password)

print("\n_______________________________________")