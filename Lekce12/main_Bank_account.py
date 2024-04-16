from Lekce12.Bank_account import *

b = BankAccount(100)
b2 = BankAccount(200)
s = SavingsAccount(b, 50)

print(b)
print(s)

b.deposit(100)
s.deposit(200)



print(b)
print(s)

print(b.counter)
print(b2.counter)

b2.add.counter(66)
print(b.get.counter())
print(b2.get.counter())

b.counter = 22

