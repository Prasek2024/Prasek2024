

class WrongMonthError(Exception):
    def __init__(self, message='Wrong month!'):
        self.message = message
        super().__init__(self.message)


try:
   month = int(input("Zadejte mesic: "))
   if month not in range(1, 13):
       raise WrongMonthError

   if month in range(1, 13):
       if month in (12, 1, 2):
           print("Zima")
       elif month in (3, 4, 5):
           print("Jaro")
       elif month in (6, 7, 8):
           print("Leto")
       elif month in (9, 10, 11):
           print("Podzim")

except ValueError:
   print("Nezadal jsi cislo")

except WrongMonthError as e:
   print("Zadal jsi cislo mimo rozsah 1-12")
   print(e.message) #vpisujeme error z class WrongMonthError


