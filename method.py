from cgi import test
from ssl import VERIFY_X509_PARTIAL_CHAIN
from venv import create


def fib(n):
    """nまでのフィボナッチ級数を表示する"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()

fib(2000)
f = fib
f(200)

print("#########")
def createFibList(n):
    """nまでのフィボナッチ級数からなるリストを返す"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f100 = createFibList(100)
print(f100)

print("#########")
def ask_ok(prompt, retries=4, complaint="Yes or no, please!"):
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError("非協力的ユーザー")
        print(complaint)

# ask_ok("Do you really want to quit?")
# ask_ok("OK to overwrite the file?", 2)
# ask_ok("OK to overwrite the file?", 2, "Come on, only yes or no!")
print("#########")
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print("#########")
def parrot(voltage, state="a stiff", action="voom", type="Norweign Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumgae, the", type)
    print("-- It's", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=100000, action="VOOOOOM")
parrot(action="VOOOOM", voltage=1000000)
parrot("a million", "benefit of life", "jump")
parrot("a thousand", state="pushing up the daisies")

print("#########")
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese shop Sketch")

print("#" * 10)
args=[3, 6]
l = list(range(*args))
print(l)

print("#" * 10)
d = {"voltage": "four million",
     "state": "bleedin' demised",
     "action" : "V",
     "type" : "wild"}
parrot(**d)

print("#" * 10)
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(1))

print("#" * 10)
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

print("#" * 10)
def f(ham: str, eggs: str = "eggs") -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + " and " + eggs

print(f("spam"))