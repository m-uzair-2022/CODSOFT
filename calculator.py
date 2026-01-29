# Simple Calculator 
print("_______________________________________")
print("           Simple Calculator           ")
print("_______________________________________\n")

print("What you want to perform?")
print("1. Addition (+)      : ")
print("2. Subtraction (-)   : ")
print("3. Multiplication (*): ")
print("4. Division (/)      : ")
print("5. Modulus (%)       : ")
print("6. Exit.               ")

while(True):
    choice = input("Enter You Choice:    ")
    if choice == '6':
        print("_______________________________________")
        print("      Thank You! Have a Good Day.      ")
        print("_______________________________________")
        break
    try:
        firstNumber = float(input("Enter First Number: "))
        SecondNumber = float(input("Enter Second Number: "))
    except:
        print("Please! Enter only float numbers.")
        continue
    if choice == '1':
        print("Result : ", firstNumber + SecondNumber)
    elif choice == '2':
        print("Result : ", firstNumber - SecondNumber)
    elif choice == '3':
        print("Result : ", firstNumber * SecondNumber)
    elif choice == '4':
        if SecondNumber != 0:
            print("Result : ", firstNumber / SecondNumber)
        else :
            print("Error: Result = not Defined")
    elif choice == '5':
        print("Result : ", firstNumber % SecondNumber)
    else :
        print("Please! Enter a choice from given index.")