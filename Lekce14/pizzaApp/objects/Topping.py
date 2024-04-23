class Topping:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def to_dict(self):
        return {
            "name": self.__name,
            "price": self.__price.to_dict()
        }
    # pridat moznost zdrazeni