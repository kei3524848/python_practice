class Dog:
    kind = "canine"

    def __init__(self, name) -> None:
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("ころがる")
e.add_trick("死んだふり")

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
print(d.tricks)
print(e.tricks)
