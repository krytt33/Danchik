s, p= map(int, input().split())
for x in range(1, 1000):
    y = s - x
    if x * y == p:
        print(x, y)
        break

