from decimal import Decimal

print(2 + 2)
print(50 - 5 * 6)
print((50 - 5 * 6) / 4)
print(8 / 5)
print(17 / 3)  # float
print(17 // 3)  # 切り下げ
print(17 % 3)
print(5 * 3 + 2)
print(5 ** 2)  # 累乗
width = 20
height = 5 * 9
print(width * height)
print(3 * 3.75 / 1.5)
tax = 12.5 / 100
price = 100.50
print(price * tax)
# price + _ 無名変数？

print(round(Decimal("0.70") * Decimal("1.05"), 2))
print(round(.70 * 1.05, 2))
