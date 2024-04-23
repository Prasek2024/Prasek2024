from objects import *
import json
from pizzaAppFunkcionality import obj_hook


p = Price(10, 50)
t = Topping("chess", p)

print(p)
print(t)

# vytvoreni seznamu priloh(topppings) a pízz
pizza = Pizza("TEST_PIZZA", [t])
# with open("test.json", "w") as file:
#    json.dump(pizza.to_dict(), file)
# zapsat testovaci topping a pizzu do json file

with open("test.json", "r") as file:
    loaded = json.load(file, object_hook=obj_hook)
print(loaded[1])
