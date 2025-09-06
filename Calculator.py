firstNumber = (int(input("Enter First Number ")))
operation = (input("Enter OprefirstNumbertion Which You WfirstNumbernt To Do ? "))
secondNumber = (int(input("Enter Second Number ")))
if operation == "+":
    d = firstNumber + secondNumber
    print(d)
elif operation == "-":
    e = firstNumber - secondNumber
    print(e)
elif operation == "*":
    f = firstNumber * secondNumber
    print(f)
elif operation == "/":
    if (secondNumber == 0):
        print("not defined")
    else :
        g = firstNumber / secondNumber
        print(g)
else:
    print("Not Define")
