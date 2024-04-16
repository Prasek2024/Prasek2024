class Price:
    def __init__(self, integer, fraction):
        self.__integer = integer
        self.__fraction = fraction

    def get_price(self):
        return self.__integer + self.__fraction / 100

    def __str__(self):
        return f"{self.__integer}.{self.__fraction}"



