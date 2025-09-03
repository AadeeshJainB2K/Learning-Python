def get_numeric_input(prompt):
    """User se ek numeric value leta hai aur galat input ko handle karta hai."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation():
    """User se ek valid operation leta hai."""
    valid_operations = ["+", "-", "*", "/"]
    while True:
        op = input(f"Enter Operation ({', '.join(valid_operations)}): ")
        if op in valid_operations:
            return op
        else:
            print("Invalid Operation. Please choose from the allowed options.")

def main():
    """Calculator chalaane ke liye yeh main function hai."""
    first_number = get_numeric_input("Enter First Number: ")
    operation = get_operation()
    second_number = get_numeric_input("Enter Second Number: ")

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Error: Division by zero is not defined")
            return  # Function se bahar nikal jaa
        else:
            result = first_number / second_number

    print(f"Output is {result}")

if __name__ == "__main__":
    main()
