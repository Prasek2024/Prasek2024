
from .Price import Price

class Pizza:
    def __init__(self, name, toppings):
        self.__name = name
        self.__toppings = toppings
        self__DOUGHT_PRICE = Price(4, 90)

    def get_name(self):
        return self.__name
    def get_price(self):
        result = self__DOUGHT_PRICE.get_price()
        for t in self.__toppings:
            result += t.get_price().get_price()
        return result

    def __str__(self):
        topps = ""
        for t in self.__toppings:
            topps += t.get_name() + ", "
        return f"""
{self.__name}          {self.get_price()}$
---------------------
{topps}
"""
