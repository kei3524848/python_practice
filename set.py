basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)
print("orange" in basket)
print("crabgrass" in basket)
a = set("abracadabra")
b = set("alacazam")
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
print({x for x in "abracadabra" if x not in "abc"})
