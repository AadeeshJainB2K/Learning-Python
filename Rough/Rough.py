try:
    firstNumber = float(input("Enter First Number: "))
except ValueError:
    print("Invalid input for the first number. Please enter a numeric value.")
    exit()

Operation = input("Enter Operation (+, -, *, /): ")

try:
    secondNumber = float(input("Enter Second Number: "))
except ValueError:
    print("Invalid input for the second number. Please enter a numeric value.")
    exit()

if Operation == "+":
    print("Output is", firstNumber + secondNumber)

elif Operation == "-":
    print("Output is", firstNumber - secondNumber)

elif Operation == "*":
    print("Output is", firstNumber * secondNumber)

elif Operation == "/":
    if secondNumber == 0:
        print("Error: Division by zero is not possible.")
    else:
        print("Output is", firstNumber / secondNumber)
else:
    print("Invalid Operation")
