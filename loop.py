words = ["cat", "window", "defenstrate"]
for w in words:
    print(w, len(w))
print("########")
for w in words[:]:
    if 6 < len(w):
        words.insert(0, w)
print(words)

print("########")
for i in range(5):
    print(i)

print("########")
for i in range(5, 10):
    print(i)

print("########")
for i in range(0, 10, 3): # targeting increment amount
    print(i)

print("########")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x,  '*', n//x)
            break
    else:
        print(n, "is a prime number")

print("########")
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

knigths = {"gallahad": "the pure", "robin": "the braze"}
for k, v in knigths.items():
    print(k, v)

for i, v in enumerate(["tic", "tax", "toe"]):
    print(i, v)

questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}.".format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)
    
basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
for f in sorted(basket):
    print(f)
    
import math
raw_data = [56.2, float("NaN"), 51.7, 52.5, float("NaN"), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)