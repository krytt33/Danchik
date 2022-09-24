a = int(input())
b = int(input())
a, b = min(a, b), max(a, b)
if a * 3 == b:
    print(a ** 2, a ** 2,a ** 2)
else:
    print(a ** 2, (b - a) ** 2, (b - a) ** 2)