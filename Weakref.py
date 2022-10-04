import gc
import weakref


class A:
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)


a = A(10)
d = weakref.WeakValueDictionary()
d["primary"] = a
print(d["primary"])
del a
gc.collect()

# d["primary"]
