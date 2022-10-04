class MyClass:
    """A simple example class"""
    i = 12345

    def f(self) -> str:
        return "hello world"

    def __init__(self) -> None:
        self.data = []


x = MyClass()
print(x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

xf = x.f
print(xf())
