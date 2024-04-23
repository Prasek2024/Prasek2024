# from pizzaAppFunkcionality import obj_hook
import json
from objects import Pizza, Topping, Price
from typing import Any


def print_main_menu():
    print("""
-------------MAIN MENU-----------
[1] - Nova objednavka
[2] - Zjistit stav objednavky
[3] - vybavyt posledni objednavku
[0] - Ukončit aplikaci
    """)


def load_pizza_list(file_name):
    with open(file_name, "r") as file:
        loaded = json.load(file, object_hook=obj_hook)

    return loaded


def obj_hook(adict: dict[Any, Any]):
    if adict.get("integer") is not None:
        return Price(adict["integer"], adict["fraction"])

    if adict.get("price") is not None:
        return Topping(adict["name"], adict["price"])

    if adict.get("toppings") is not None:
        return Pizza(adict["name"], adict["toppings"])

    return adict


def print_pizza_menu():
    pizza = ""
    pizza_list = load_pizza_list("resources/pizza_list.json")
    print(pizza_list)
    for num in range(len(pizza_list)):
        pizza += f"\n{num + 1}\n" + str(pizza_list[num])

    print(f"""
--------- PIZZA MENU ----------
    {pizza}

    """)


def print_bye():
    print("Naschledanou.")


def input_address():
    address = input("zadej adresu pro duručeni: ")
    return address


def create_order_message(order):
    print("Objednavka vytvorena")
    print("info o objednavce")


def wrong_choice_message():
    print("Zadal si zlou volbu.")
