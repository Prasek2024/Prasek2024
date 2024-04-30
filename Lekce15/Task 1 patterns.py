class DisplayStrategy:
    def action(self, data):
        pass


class PrintStrategy(DisplayStrategy):
    def action(self, data):
        print(data)


class FileStrategy(DisplayStrategy):
    def action(self, data):
        print(f"data to file {data}")


class DataClass:
    def __init__(self, data):
        self.data = data
        self.strategy = FileStrategy()

    def display(self):
        self.strategy.action(self.data)

    def set_strategy(self,strategy):
        self.strategy = strategy


d = DataClass("DATA1")

d.display()
d.set_strategy(PrintStrategy())
d.display()