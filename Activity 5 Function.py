def divide(a, b):
    """Returns the result of a / b if b is not zero, otherwise returns None."""
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

def exponentiate(a, b):
    """Returns a raised to the power of b."""
    return a ** b

def remainder(a, b):
    """Returns the remainder of a divided by b if b is not zero, otherwise returns None."""
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a % b

def summation(a, b):
    """Returns the summation from a to b if b > a, otherwise returns None."""
    if b <= a:
        print("Error: The second number must be greater than the first number.")
        return None
    sequence = " + ".join(str(i) for i in range(a, b + 1))
    total = sum(range(a, b + 1))
    return f"{sequence} = {total}"

def get_integer(prompt):
    """Gets a valid integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer.")

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == "Q":
            print("Exiting program. Goodbye!")
            break

        if choice in ["D", "E", "R", "F"]:
            num1 = get_integer("Enter first number: ")
            num2 = get_integer("Enter second number: ")

            if choice == "D" or choice == "R":
                while num2 == 0:
                    print("Error: The second number must not be zero.")
                    num2 = get_integer("Enter a nonzero second number: ")

            if choice == "F":
                while num2 <= num1:
                    print("Error: The second number must be greater than the first number.")
                    num2 = get_integer("Enter a valid second number: ")

            if choice == "D":
                result = divide(num1, num2)
            elif choice == "E":
                result = exponentiate(num1, num2)
            elif choice == "R":
                result = remainder(num1, num2)
            elif choice == "F":
                result = summation(num1, num2)

            if result is not None:
                print("Result:", result)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
