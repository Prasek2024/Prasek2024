class Console:

    @staticmethod
    def print_menu():
        print("""
        -------MENU----
        [1] scitani
        [2] odecitani
        [3] nasobeni
        [4] deleni
        [0] konec
        """)

    @staticmethod
    def message_wrong_input():
        print("Zadal si zly vstup")

    @staticmethod
    def input_choice(num):
        choice = -1
        while not choice in range(num+1):
            choice = input("zadej tvou volbu: ")

            try:
                choice = int(choice)
            except ValueError:
                Console.message_wrong_input()
                choice = -1

        return choice

    @staticmethod
    def input_number():
        num = ""
        while type(num) != type(0):
            num = input("zadej čislo: ")

            try:
                num = int(num)
            except ValueError:
                Console.message_wrong_input()
                num = ""

        return num

    @staticmethod
    def print_result(result):
        print(f"tvoj vysledek je {result}")