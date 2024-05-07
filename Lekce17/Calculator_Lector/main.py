from Calculator import Calculator
from ConsoleView import Console

def menu_controller(strategy):
    a = Console.input_number()
    b = Console.input_number()
    try:
        result = strategy(a, b)
        Console.print_result(result)
    except ValueError:
        Console.message_wrong_input()

def run():
    c = Calculator()

    choice = -1
    while choice != 0:
        Console.print_menu()
        choice = Console.input_choice(4)

        if choice == 1:
            menu_controller(c.add)

        elif choice == 2:
            menu_controller(c.subtract)

        elif choice == 3:
            menu_controller(c.multiply)

        elif choice == 4:
            menu_controller(c.divide)

        else:
            Console.message_wrong_input()

run()
