from calc_funcionality import Calculator

class Calculator_menu:
 while True:
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
     print("Result: ", Calculator.add(num1, num2))
    elif choice == '2':
     print("Result: ", Calculator.subtract(num1, num2))
    elif choice == '3':
     print("Result: ", Calculator.multiply(num1, num2))
    elif choice == '4':
     print("Result: ", Calculator.divide(num1, num2))
    else:
        print("Invalid choice. Please enter a valid option.")


