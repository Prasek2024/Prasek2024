class Calculator:
    ans = 0
    @staticmethod
    def add( cls, a, b):
        return a + b

    @staticmethod
    def subtract( cls, a, b):
        return a - b

    @staticmethod
    def multiply( cls, a, b):
        return a * b

    @staticmethod
    def divide( cls, a, b):
        return a / b

    @classmethod
    def max( cls, a, b):
        return max(a, b)

    @classmethod
    def min( cls, a, b):
        return min(a, b)
    @classmethod
    def percentage( cls, a, b):
        return (a / b) * 100

    @classmethod
    def raise_to( cls, a, b):
        return a ** b

