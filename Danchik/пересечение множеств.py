N, M = map(int, input().split())
lst_1 = set(map(int, input().split()))
lst_2 = set(map(int, input().split()))
result = lst_1 & lst_2
print(*sorted(result))