def perform_operation(num1, num2, operation):
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
