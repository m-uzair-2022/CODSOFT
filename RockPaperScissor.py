# Rock Paper Scissors Game
# User plays against the computer using CLI

import random

print("_______________________________________")
print("       Rock Paper Scissors Game        ")
print("_______________________________________")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

# Main game loop
while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Exit game and display final score
    if choice == '4':
        print("\nFinal Score:")
        print("You      :", user_score)
        print("Computer :", computer_score)
        print("_______________________________________")
        print("        Thanks for Playing!           ")
        print("_______________________________________")
        break

    # Validate input
    if choice not in ['1', '2', '3']:
        print("Invalid choice! Please select 1 to 4.")
        continue

    user_choice = choices[int(choice) - 1]
    computer_choice = random.choice(choices)

    print("\nYou chose     :", user_choice)
    print("Computer chose:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: Computer Wins!")
        computer_score += 1
