def perform_operation(num1, num2, operation):
    if operation not in (add, subtract, multiply, divide):
        print('something went Wrong!')
    match operation:
        case 'add':
            print(f"The result is {num1 + num2}")
        case 'subtract':
            print(f"The result is {num1 - num2}")
        case 'multiply':
            print(f"The result is {num1 * num2}")
        case 'divide':
            if num2 != 0:
                print(f"The result is {num1 / num2}")
            elif num2 == 0:
                print("Cannot divide by zero.")
                return


perform_operation()
