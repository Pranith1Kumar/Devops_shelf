def calculator():
    print("Welcome to the Calculator!")
    print("Options: 1-Add 2-Subtract 3-Multiply 4-Divide")
    try:
        choice = int(input("Enter choice: "))
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == 1:
                print(f"Result: {num1 + num2}")
            elif choice == 2:
                print(f"Result: {num1 - num2}")
            elif choice == 3:
                print(f"Result: {num1 * num2}")
            elif choice == 4:
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Division by zero is not allowed!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter valid inputs.")

if __name__ == "__main__":
    calculator()
