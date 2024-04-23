from views import print_main_menu, print_bye, wrong_choice_message, load_pizza_list
from objects import Queue
from pizzaAppFunkcionality import create_new_order

def run_app():
    # TODO udelat v uvodu prihlaseni pro user a admin
    # TODO zalohovani a nacteni z pameti
    orders_queue = Queue(5)
    #TODO confing file pro cestu k datam
    pizza_list = load_pizza_list("resources/pizza_list.json")

    while True:
        # TODO pridat vlastni error alespon jeden
        print_main_menu()
        # TODO oŠetrit kontrolu vsupu
        user_choice = int(input("Zadej volbu: "))

        if user_choice == 1:
            create_new_order(orders_queue, pizza_list)

        elif user_choice == 2:
            get_order_state()

        elif user_choice == 3:
            update_order_state()

        elif user_choice == 4:
            print(orders_queue.show())

        elif user_choice == 0:
            # TODO ulozeni orders do pameti
            print_bye()
            exit()

        else:
            wrong_choice_message()

run_app()