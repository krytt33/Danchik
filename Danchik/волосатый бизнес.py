n = int(input())
prise = list(map(int, input().split()))
length = 1
total = 0
for i in range(n):
    if prise[i] == max(prise[i:]):
        total += length * prise[i]
        length = 1
    else:
        length += 1
print(total)