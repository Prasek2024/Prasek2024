# Importing 'pickle' module, used for object serialization and deserialization.
import pickle
from car import Car

# Creating a list of numbers.
numbers = [1, 2, 3, 4, 5]
c = Car("audi", "black")

print("prvni car: ", c)
# Serializing the list to a bytes object.
serialized_data = pickle.dumps(c)

# Printing the serialized data.
print(f"Serialized data:\n{serialized_data}\n")

# Deserializing the bytes back into a list.
deserialized_data = pickle.loads(serialized_data)

# Printing the deserialized data.
print(f"Deserialized data:\n{deserialized_data}\n")