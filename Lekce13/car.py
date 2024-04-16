from vehicle import Vehicle
import json

class Car(Vehicle):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def turn(self, direction):
        print(f"odbacim do {direction}")

    def __str__(self):
        return f"name: {self.name}, color: {self.color}"

    def to_json(self):
        # Use the __dict__ attribute to access the instance attributes
        # Then use the json.dumps() function to convert the dictionary
        return self.__dict__