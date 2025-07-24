def perform_operation():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input(
        "Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operation not in ('+', '-', '*', '/'):
        print('something went Wrong!')
    match operation:
        case '+':
            print(f"The result is {num1 + num2}")
        case '-':
            print(f"The result is {num1 - num2}")
        case '*':
            print(f"The result is {num1 * num2}")
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(f"The result is {num1 / num2}")


perform_operation()
