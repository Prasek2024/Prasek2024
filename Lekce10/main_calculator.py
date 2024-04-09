from calculator import Calculator




a = Calculator.add(3, 6)
print(a, "vysledek add metody")




b = Calculator.ans_add(8)
c = Calculator.ans_add(4)
print(c, "soucet druhých statickych metod ans , drzi vysledek ")

print(Calculator.clean_ans(), " - vynulovani vysledku")

d = Calculator.factorial(5)
print(d, " - vysledek factorial metody")

e = Calculator.avarage(4, 8, 10,12)
print(e, " - vysledek avarage metody")

