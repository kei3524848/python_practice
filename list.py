import bisect
from array import array
from cmath import pi
from collections import deque
from heapq import heapify, heappop, heappush

# from itertools import count
# from math import pi

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[2:])  # slice
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

arr = array("H", [4000, 10, 700, 22222])
print(sum(arr))
print(arr[1:3])

d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

scores = [(100, "perl"), (200, "tcl"), (400, "lua"), (500, "python")]
bisect.insort(scores, (300, "ruby"))
print(scores)


data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
print([heappop(data) for i in range(3)])
