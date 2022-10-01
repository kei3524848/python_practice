from cmath import pi
from itertools import count


squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[2:]) # slice
print(squares + [36, 49, 64, 72, 81, 100])
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)
print(len(letters))
letters[2:5] = ["C", "D", "E"]
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
a = ["a", "b", "c"]
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

print("part 5")
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count("x"))
a.insert(2, -1)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
print(a.pop())
print(a)

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)

from collections import deque
queue = deque(["Eric", "Jhon", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

print("#" * 10)
squares.clear()
squares = list(map(lambda x: x**2, range(10)))
print(squares)

print("#" * 10)
squares.clear()
squares = [x ** 2 for x in range(10)]
print(squares)

inclusion = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(inclusion)

vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])
print([x for x in vec if 0 <= x])
print([abs(x) for x in vec])
freshfruit = [" banana", " loganberry ", "passion fruit "]
print([weapon.strip() for weapon in freshfruit])
print([(x, x**2) for x in range(6)])
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

print("#" * 10)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])
print(list(zip(*matrix)))

print("#" * 10)
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

