from .Price import Price
from .Topping import Topping


class Pizza:
    def __init__(self, name, toppings):
        # pridat druh testa, pridat druh zakaldu
        # moznost pridat extra topping
        self.__name = name
        self.__toppings = toppings
        self.__DOUGHT_PRICE = Price(4, 90)

    def get_name(self):
        return self.__name

    def get_price(self):
        result = self.__DOUGHT_PRICE.get_price()
        for t in self.__toppings:
            result += t.get_price().get_price()

        return result

    def __str__(self):
        topps = ""
        for t in self.__toppings:
            topps += t.get_name() + ", "
        # odstraneni posledni carky
        return f"""
{self.__name}              {self.get_price()}$
------------------
{topps}
"""

    def to_dict(self):
        return {
            "name": self.__name,
            "toppings": [t.to_dict() for t in self.__toppings]
        }

    @classmethod
    def from_dict(cls, pizza_dict):
        toppings = [Topping.from_dict(topping_dict) for topping_dict in pizza_dict['toppings']]
        return cls(pizza_dict['name'], toppings)
