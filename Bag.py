class Bag:
    def __init__(self) -> None:
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


bag = Bag()
bag.addtwice(123)
print(bag.data)
