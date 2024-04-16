class MathFunctor:
    def __init__(self, operation):
        self.operation = operation

    def add(self, a, b):
        return a + b

    def __call__(self, a, b):
        if self.operation == "add":
            return self.add(a, b)
        elif self.operation == "subtract":
            return a - b
        elif self.operation == "multiply":
            return a * b
        elif self.operation == "divide":
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b


add_functor = MathFunctor("add")
subtract_functor = MathFunctor("subtract")
multiply_functor = MathFunctor("multiply")
divide_functor = MathFunctor("divide")

result1 = add_functor(5, 3)
result2 = subtract_functor(10, 4)
result3 = multiply_functor(7, 2)
result4 = divide_functor(12, 3)

print(result1)
print(result2)
print(result3)
print(result4)
print()

print(MathFunctor.mro()) # vypise mro (method resolution order) cestu k tridam
print(type(add_functor))
print(type(subtract_functor))
print()

t = [add_functor, subtract_functor, add_functor]
nums = [2, 4, 5]

num = 10
for i in range(3):
    num = t[i](num, nums[i])

print(num)