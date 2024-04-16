#problematika scoppes... pokud vytvorim existuje v zanoreni a nizsi funkci.

def counter():
   number = 0

   def incrementer():
       nonlocal number #viditelnost vlastnich promennych o uroven vyse
       number += 1
       return number

   return incrementer


c = counter()
print(c) # <function counter.<locals>.incrementer at 0x0000016C447DF240>
print(c())
print(c())


def print_Hello():
    print("Hello")
    return "return"

pozdrav = print_Hello() #pozdrav je funkce se zavorkou se provede vsechno
pozdrav2 = print_Hello

print(pozdrav)
print(pozdrav2) #pozdrav2 je funkce bez zavorky ukaze cestu k funkci - <function print_Hello at 0x0000016C447DF240>

pozdrav2() # pozdrav2 je funkce bez zavorky uzije predeslo ulozenou fuknci ...jako alias
print_Hello()





