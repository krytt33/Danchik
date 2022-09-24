k = int(input())
###
#if k % 300 == 0:
#    print('AHG' * (k // 300))
#elif k % 400 == 0:
#    print('ABIG' * (k // 400))
#elif k % 500 == 0:
#    print('ABILF' * (k // 500))

temp = 0
while True:
    temp += 300
    if k - temp == 0: