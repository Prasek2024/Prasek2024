

class Calculator:
    ans = 0
    @staticmethod
    def add( a, b):
        return a + b

    @staticmethod
    def subtract( a, b):
        return a - b

    @staticmethod
    def multiply( a, b):
        return a * b

    @staticmethod
    def divide( a, b):
        return a / b

    @classmethod
    def ans_add(cls, a):
        cls.ans += a
        return cls.ans

    @classmethod
    def clean_ans(cls):
        cls.ans = 0

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Calculator.factorial(n - 1)
    @staticmethod
    def avarage(a , b, c, d):
        return (a + b + c + d) / 2



