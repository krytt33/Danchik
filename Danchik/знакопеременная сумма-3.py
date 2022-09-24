n = int(input())
x = list(int, input().split())
totals = []
znak = 1
total = 0
for num in x:
    total += znak * num
    znak *= -1
    totals.append(total)
count = int(input())
for i in range(count):
    b, e = list(int, input().split())
    if b == 1:
        print(totals[e - 1])
    elif b % 2 == 0:
        print(totals[b - 2] - totals[e - 1])
    else:
        print(totals[e - 1] - totals[b - 2])