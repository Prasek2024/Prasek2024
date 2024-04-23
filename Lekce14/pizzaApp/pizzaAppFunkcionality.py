from views import (print_pizza_menu,
                   create_order_message)
from objects import Order, Pizza, Topping, Price
import json
from typing import Any


def create_new_order(orders_queue, pizza_list):
    print_pizza_menu()
    # TODO pridat moznost objednat vice polozek na jednou (split)
    user_pizza = int(input("Zadej volbu: "))
    user_address = input("Zadej adresu: ")
    user_order = Order(address=user_address, meal=[pizza_list[user_pizza-1]])
    orders_queue.enqueue(user_order)
    create_order_message(user_order)

#TODO states -> enums


def get_order_state():
    pass


def update_order_state():
    pass